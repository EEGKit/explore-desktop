"""ExG visualization module"""
import logging

import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import Slot, QTimer

from explorepy.tools import HeartRateEstimator

from exploredesktop.modules.app_settings import (  # isort:skip
    DataAttributes,
    Messages,
    Settings,
    Stylesheets
)
from exploredesktop.modules.base_data_module import (  # isort:skip
    BasePlots,
    DataContainer
)
from exploredesktop.modules.tools import display_msg   # isort:skip


logger = logging.getLogger("explorepy." + __name__)


class ExGData(DataContainer):
    """_summary_"""
    def __init__(self, filters) -> None:
        super().__init__()

        self.filters = filters

        self._baseline = None
        self.offsets = np.array([])
        self.y_unit = Settings.DEFAULT_SCALE
        self.y_string = '1 mV'
        self.last_t = 0

        self.packet_count = 0
        self.t_bt_drop = None
        self.bt_drop_warning_displayed = False

        self.rr_estimator = None
        self.r_peak = {'t': [], 'r_peak': [], 'points': []}
        self.r_peak_replot = {'t': [], 'r_peak': [], 'points': []}
        self.rr_warning_displayed = False

        self.signals.updateDataAttributes.connect(self.update_attributes)

    def reset_vars(self):
        self._baseline = None
        self.offsets = np.array([])
        self.y_unit = Settings.DEFAULT_SCALE
        self.y_string = '1 mV'
        self.last_t = 0

        self.packet_count = 0
        self.t_bt_drop = None
        self.bt_drop_warning_displayed = False

        self.rr_estimator = None
        self.r_peak = {'t': [], 'r_peak': [], 'points': []}
        self.r_peak_replot = {'t': [], 'r_peak': [], 'points': []}
        self.rr_warning_displayed = False

        DataContainer.vis_time_offset = None
        self.pointer = 0

    def new_t_axis(self, signal=None):
        signal = self.signals.tAxisEXGChanged
        return super().new_t_axis(signal)

    def update_pointer(self, data, signal=None):
        signal = self.signals.tRangeEXGChanged
        return super().update_pointer(data, signal)

    def on_wrap(self, signal):
        super().on_wrap(signal)
        self.remove_r_peak()
        self.add_r_peaks_replot()

    @Slot(list)
    def update_attributes(self, attributes: list):
        """_summary_

        Args:
            attribute (str): _description_
        """
        n_chan = self.explorer.n_active_chan
        active_chan = self.explorer.active_chan_list
        if DataAttributes.OFFSETS in attributes:
            self.offsets = np.arange(1, n_chan + 1)[:, np.newaxis].astype(float)
        if DataAttributes.BASELINE in attributes:
            self._baseline = None
        if DataAttributes.DATA in attributes:
            points = self.plot_points()
            self.plot_data = {ch: np.array([np.NaN] * points) for ch in active_chan}
            self.t_plot_data = np.array([np.NaN] * points)
        if DataAttributes.POINTER in attributes:
            self.pointer = 0

    def handle_disconnection(self, timestamp: list):
        """Handle disconnection errors

        Args:
            timestamp (list): list of timestamps
        """
        if self.vis_time_offset is None or timestamp[0] > self.vis_time_offset:
            return
        self.reset_vars()
        self.signals.updateDataAttributes.emit([DataAttributes.DATA])
        self.signals.tRangeEXGChanged.emit(0)

    def handle_bt_drop(self, data: dict, sec_th: int = 10):
        """Handle bluetooth drop

        Args:
            data (dict): exg data
            sec_th (int): threshold of seconds to display the warning again. Defaults to 10
        """
        t_point = data['t'][0]
        if t_point < 0:
            return
        elif t_point < self.last_t and self.bt_drop_warning_displayed is False:
            print(f"Bt drop:\n{t_point=}\n{self.last_t=}\n")
            self.bt_drop_warning_displayed = True
            self.t_bt_drop = t_point
            self.signals.btDrop.emit(True)

        elif (self.t_bt_drop is not None) and (t_point > self.last_t) and \
                (t_point - self.t_bt_drop > sec_th) and self.bt_drop_warning_displayed is True:
            self.bt_drop_warning_displayed = False

    def callback(self, packet):
        """_summary_"""
        chan_list = self.explorer.active_chan_list
        exg_fs = self.explorer.sampling_rate
        timestamp, exg = packet.get_data(exg_fs)

        # self.handle_disconnection(timestamp)
        # From timestamp to seconds
        if DataContainer.vis_time_offset is None:
            DataContainer.vis_time_offset = timestamp[0]

        time_vector = timestamp - DataContainer.vis_time_offset

        # Downsampling
        if Settings.DOWNSAMPLING:
            time_vector, exg = self.downsampling(time_vector, exg, exg_fs)

        # Baseline Correction
        if self.filters.current_filters is not None and self.filters.current_filters['offset']:
            exg = self.baseline_correction(exg)

        # ValueError thrown when changing the channels. Can be ignored
        try:
            exg = self.update_unit(exg)
        except ValueError as error:
            logger.warning("ValueError: %s", str(error))

        data = dict(zip(chan_list, exg))
        data['t'] = time_vector

        self.insert_new_data(data)
        self.update_pointer(data)
        self.new_t_axis()
        self.handle_bt_drop(data)

        self.last_t = data['t'][-1]
        self.packet_count += 1

        try:
            self.signals.exgChanged.emit([self.t_plot_data, self.plot_data])
        except RuntimeError as error:
            logger.warning("RuntimeError: %s", str(error))

    def downsampling(self, time_vector, exg, exg_fs):
        """Downsample"""
        # Correct packet for 4 chan device
        if len(time_vector) == 33 and self.decide_drop(exg_fs):
            exg = exg[:, 1:]
            time_vector = time_vector[1:]

        # Downsample
        exg = exg[:, ::int(exg_fs / Settings.EXG_VIS_SRATE)]
        time_vector = time_vector[::int(exg_fs / Settings.EXG_VIS_SRATE)]
        return time_vector, exg

    def decide_drop(self, exg_fs: int) -> bool:
        """Decide whether to drop a data point from the packet based on the sampling rate

        Args:
            exg_fs (int): sampling rate

        Returns:
            bool: whether to drop a data point
        """
        drop = True
        if exg_fs == 1000 and self.packet_count % 8 == 0:
            drop = False
        elif exg_fs == 500 and self.packet_count % 4 == 0:
            drop = False
        elif exg_fs == 250 and self.packet_count % 2 == 0:
            drop = False
        return drop

    def baseline_correction(self, exg):
        """baseline correction"""
        samples_avg = exg.mean(axis=1)

        if self._baseline is None:
            self._baseline = samples_avg
        else:
            try:
                self._baseline = self._baseline - (
                    (self._baseline - samples_avg) / Settings.BASELINE_MA_LENGTH * exg.shape[1]
                )
            except ValueError:
                self._baseline = samples_avg

        exg = exg - self._baseline[:, np.newaxis]

        return exg

    def update_unit(self, exg):
        """_summary_

        Args:
            exg (_type_): _description_

        Returns:
            _type_: _description_
        """
        exg = self.offsets + exg / self.y_unit
        return exg

    def change_timescale(self):
        super().change_timescale()
        self.signals.tRangeEXGChanged.emit(self.last_t)
        self.signals.updateDataAttributes.emit([DataAttributes.POINTER, DataAttributes.DATA])

    @Slot(str)
    def change_scale(self, new_val: str):
        """
        Change y-axis scale in ExG plot
        """
        old = Settings.SCALE_MENU[self.y_string]
        new = Settings.SCALE_MENU[new_val]
        logger.debug("ExG scale has been changed from %s to %s", self.y_string, new_val)

        old_unit = 10 ** (-old)
        new_unit = 10 ** (-new)

        self.y_string = new_val
        self.y_unit = new_unit

        chan_list = self.explorer.active_chan_list
        for chan, value in self.plot_data.items():
            if chan in chan_list:
                temp_offset = self.offsets[chan_list.index(chan)]
                self.plot_data[chan] = (value - temp_offset) * (old_unit / new_unit) + temp_offset
        # TODO
        # # Rescale r_peaks
        # # Remove old rpeaks
        # # Plot rescaled rpeaks

        # # Rescale replotted rpeaks
        # # Remove old replotted rpeaks
        # # Plot rescaled rpeaks
        self.signals.updateYAxis.emit()

    def add_r_peaks(self):
        peaks_time, peaks_val = self._obtain_r_peaks()

        if peaks_time:
            for i, pk_time in enumerate(peaks_time):
                if pk_time not in self.r_peak['t']:
                    self.r_peak['t'].append(pk_time)
                    self.r_peak['r_peak'].append(peaks_val[i])

    def _obtain_r_peaks(self):
        first_chan = list(self.plot_data.keys())[0]

        if self.rr_estimator is None:
            try:
                self.rr_estimator = HeartRateEstimator(fs=self.explorer.sampling_rate)
            except TypeError:
                print(f"TypeError - {self.explorer.sampling_rate=}")
        sr = Settings.EXG_VIS_SRATE if Settings.DOWNSAMPLING else self.explorer.sampling_rate
        i = self.pointer - (2 * sr)
        i = i if i >= 0 else 0
        f = self.pointer if i + self.pointer >= (2 * sr) else (2 * sr)
        # f = self.exg_pointer
        ecg_data = (np.array(self.plot_data[first_chan])[i:f] - self.offsets[0]) * self.y_unit
        time_vector = np.array(self.t_plot_data)[i:f]

        # Check if the peak2peak value is bigger than threshold
        if (np.ptp(ecg_data) < Settings.V_TH[0]) or (np.ptp(ecg_data) > Settings.V_TH[1]):
            msg = 'P2P value larger or less than threshold. Cannot compute heart rate!'
            logger.warning(msg)
            return None, None

        try:
            peaks_time, peaks_val = self.rr_estimator.estimate(ecg_data, time_vector)
        except IndexError:
            return None, None
        peaks_val = (np.array(peaks_val) / self.y_unit) + self.offsets[0]

        return peaks_time, peaks_val

    def add_r_peaks_replot(self):
        for i, pk_time in enumerate(self.r_peak['t']):
            if pk_time > self.last_t:
                return
            new_t = self.r_peak['t'][i] + self.timescale
            if new_t not in self.r_peak_replot['t']:
                self.r_peak_replot['t'].append(new_t)
                self.r_peak_replot['r_peak'].append(self.r_peak['r_peak'][i])

    def remove_r_peak(self, replot=False):
        if replot:
            peaks_dict = self.r_peak_replot
        else:
            peaks_dict = self.r_peak

        to_remove = []
        for idx_t in range(len(peaks_dict['t'])):
            if peaks_dict['t'][idx_t] < self.last_t:
                try:
                    to_remove.append([peaks_dict[key][idx_t] for key in peaks_dict.keys()])
                except IndexError:
                    print(f"\n{replot=}")
                    print(f"{idx_t=}")
                    for key in peaks_dict.keys():
                        print("len: ", len(peaks_dict[key]))
                        print(peaks_dict[key])
                    # input("press enter to continue\n\n")

        points_to_remove = [point[2] for point in to_remove]
        for point in to_remove:
            peaks_dict['t'].remove(point[0])
            peaks_dict['r_peak'].remove(point[1])
            peaks_dict['points'].remove(point[2])
            to_remove.remove(point)

        self.signals.rrPeakRemove.emit(points_to_remove)
        return peaks_dict, to_remove


class ExGPlot(BasePlots):
    """_summary_
    """
    def __init__(self, ui, filters) -> None:
        super().__init__(ui)
        self.model = ExGData(filters)

        self.lines = [None]

        self.plots_list = [self.ui.plot_exg]

        self.timer = QTimer()

    def setup_ui_connections(self):
        super().setup_ui_connections()
        self.ui.value_timeScale.currentTextChanged.connect(self.model.change_timescale)
        self.ui.value_yAxis.currentTextChanged.connect(self.model.change_scale)
        self.ui.value_signal.currentTextChanged.connect(self.change_signal_mode)

    def reset_vars(self):
        """Reset variables"""
        self.lines = [None]
        self.plots_list = [self.ui.plot_exg]
        self.bt_drop_warning_displayed = False

        self.model.reset_vars()

    def init_plot(self):
        plot_wdgt = self.ui.plot_exg

        n_chan = self.model.explorer.n_active_chan
        timescale = self.time_scale

        if self.ui.plot_orn.getItem(0, 0) is not None:
            plot_wdgt.clear()
            self.lines = [None]

        # Set Background color
        plot_wdgt.setBackground(Stylesheets.PLOT_BACKGROUND)

        # Disable zoom
        plot_wdgt.setMouseEnabled(x=False, y=False)

        # Add chan ticks to y axis
        # Left axis
        plot_wdgt.setLabel('left', 'Voltage')
        self.add_left_axis_ticks()
        plot_wdgt.getAxis('left').setWidth(60)
        plot_wdgt.getAxis('left').setPen(color=(255, 255, 255, 50))
        plot_wdgt.getAxis('left').setGrid(50)

        # Right axis
        plot_wdgt.showAxis('right')
        plot_wdgt.getAxis('right').linkToView(plot_wdgt.getViewBox())
        self.add_right_axis_ticks()
        plot_wdgt.getAxis('right').setGrid(200)

        # Add range of time axis
        plot_wdgt.setRange(yRange=(-0.5, n_chan + 1), xRange=(0, int(timescale)), padding=0.01)
        plot_wdgt.setLabel('bottom', 'time (s)')

        all_curves_list = [
            pg.PlotCurveItem(pen=Stylesheets.EXG_LINE_COLOR) for i in range(self.model.explorer.device_chan)]
        self.active_curves_list = self.add_active_curves(all_curves_list, plot_wdgt)

    def add_right_axis_ticks(self):
        """
        Add upper and lower lines delimiting the channels in exg plot
        """
        active_chan = self.model.explorer.active_chan_list

        ticks_right = [(idx + 1.5, '') for idx, _ in enumerate(active_chan)]
        ticks_right += [(0.5, '')]

        self.ui.plot_exg.getAxis('right').setTicks([ticks_right])

    def add_left_axis_ticks(self):
        """
        Add central lines and channel name ticks in exg plot
        """
        active_chan = self.model.explorer.active_chan_list

        ticks = [
            (idx + 1, f'{ch}\n' + '(\u00B1' + f'{self.model.y_string})') for idx, ch in enumerate(active_chan)]
        self.ui.plot_exg.getAxis('left').setTicks([ticks])

    @Slot(dict)
    def swipe_plot(self, data):
        t_vector, plot_data = data

        # TODO: if wrap handle - check if there is a way to to it without model access
        # if self.model.pointer >= len(self.model.t_plot_data):
        #     self.model.signals.mkrReplot.emit(self.model.t_plot_data[0])
        # 1. check id_th (check if necessary)
        # 3. Remove rr peaks and replot in new axis
        if self.ui.value_signal.currentText() == Settings.MODE_LIST[1]:
            # self.remove_old_item()
            self.plot_r_peaks(replot=True)

        # position line
        self._add_pos_line(t_vector)

        # connection vector
        connection = self._connection_vector(len(t_vector))

        # Paint curves
        for curve, chan in zip(self.active_curves_list, self.model.explorer.active_chan_list):
            try:
                curve.setData(t_vector, plot_data[chan], connect=connection)
            except KeyError:
                pass

        # remove reploted markers
        self.model.signals.mkrRemove.emit(self.model.last_t)
        # TODO:
        # remove reploted r_peaks
        self.model.remove_r_peak(replot=True)

    @Slot(bool)
    def display_bt_drop(self, bt_drop: bool):
        """Display bluetooth drop warning

        Args:
            bt_drop (bool): whether there is a bluetooth drop
        """
        if bt_drop:
            title = "Unstable Bluetooth connection"
            display_msg(msg_text=Messages.BT_DROP, title=title, popup_type="info")

    def plot_r_peaks(self, replot=False):
        if replot:
            # self.model.add_r_peaks_replot()
            r_peak_dict = self.model.r_peak_replot
            color = (200, 0, 0, 200)
        else:
            r_peak_dict = self.model.r_peak
            color = (200, 0, 0)

        # if not in ECG mode or no peaks in dict, return
        if self.ui.value_signal.currentText() == 'EEG' or len(r_peak_dict['t']) == 0:
            return

        for i in range(len(r_peak_dict['t'])):
            try:
                r_peak_dict['points'][i]
                return
            except IndexError:
                point = self.ui.plot_exg.plot(
                    [r_peak_dict['t'][i]],
                    [r_peak_dict['r_peak'][i]],
                    pen=None,
                    symbolBrush=color,
                    symbol='o',
                    symbolSize=8)

                r_peak_dict['points'].append(point)

    @Slot(str)
    def change_signal_mode(self, new_mode):
        """
        Log mode change (EEG or ECG)
        """
        logger.debug("ExG mode has been changed to %s", new_mode)
        if new_mode == Settings.MODE_LIST[1]:
            print("In ECG mode")
            if self.timer.isActive():
                return
            self.timer.setInterval(2000)
            self.timer.timeout.connect(self.model.add_r_peaks)
            self.timer.timeout.connect(self.plot_r_peaks)
            self.timer.start()

        elif new_mode == Settings.MODE_LIST[0]:
            print("In EEG mode")
            if self.timer.isActive:
                self.timer.stop()

    @Slot(list)
    def remove_old_r_peak(self, to_remove):
        plt_widget = self.plots_list[0]
        for point in to_remove:
            plt_widget.removeItem(point)
        # if replot:
        #     peaks_dict = self.model.r_peak_replot
        # else:
        #     peaks_dict = self.model.r_peak

        # to_remove = []
        # for idx_t in range(len(peaks_dict['t'])):
        #     if peaks_dict['t'][idx_t] < self.model.last_t:
        #         for plt_wdgt in self.plots_list:
        #             plt_wdgt.removeItem(peaks_dict['points'][idx_t])
        #             to_remove.append([peaks_dict[key][idx_t] for key in peaks_dict.keys()])

        # if to_remove:
        #     self.model.signals.rrPeakRemove.emit(to_remove)
        # return to_remove
