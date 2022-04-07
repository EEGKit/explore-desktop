from email.errors import MessageParseError
import logging

import numpy as np
from exploredesktop.modules import (
    AppFunctions,
    Settings
)
from exploredesktop.modules.app_settings import Messages, Stylesheets
from exploredesktop.modules.bt_functions import DISABLED_STYLESHEET
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QCheckBox,
    QMessageBox
)



logger = logging.getLogger("explorepy." + __name__)


class ConfigFunctions(AppFunctions):
    """[summary]

    Args:
        AppFunctions ([type]): [description]
    """
    def __init__(self, ui, explorer, vis_functions):
        super().__init__(ui, explorer)
        self.vis_functions = vis_functions

    @Slot()
    def one_chan_selected(self):
        """
        Make sure at least one checkbox is selected.
        If only one checkbox is left it will be disabled so status cannot change. A tooltip will be added.
        """
        cbs = {ch_wdgt: ch_wdgt.isChecked() for ch_wdgt in self.ui.frame_cb_channels.findChildren(QCheckBox)}
        if sum(cbs.values()) == 1:
            unchecked_cb = list(cbs.keys())[list(cbs.values()).index(True)]
            unchecked_cb.setEnabled(False)
            unchecked_cb.setToolTip(Messages.SELECT_1_CHAN)

        else:
            for ch_wdgt in self.ui.frame_cb_channels.findChildren(QCheckBox):
                ch_wdgt.setEnabled(True)
                ch_wdgt.setToolTip("")

    @Slot()
    def format_memory(self):
        r"""
        Display a popup asking for confirmation.
        If yes, memory is formatted.
        """

        response = self.display_msg(msg_text=Messages.FORMAT_MEM_QUESTION, type="question")

        if response == QMessageBox.StandardButton.Yes:
            with self.wait_cursor():
                self.explorer.format_memory()
            self.display_msg(msg_text="Memory formatted", type="info")
        else:
            return

    @Slot()
    def calibrate_orn(self):
        r"""
        Calibrate the orientation
        """
        lbl = self.ui.ft_label_device_3.text()
        response = self.display_msg(msg_text=Messages.CALIBRATE_ORN_QUESTION, type="question")

        if response == QMessageBox.StandardButton.Yes:
            # QMessageBox.information(self, "", "Calibrating...\nPlease move and rotate the device")
            self.ui.ft_label_device_3.setText("Calibrating ORN ... ")
            self.ui.ft_label_device_3.repaint()
            with self.wait_cursor():
                self.explorer.calibrate_orn(do_overwrite=True)
            self.ui.ft_label_device_3.setText(lbl)
            self.ui.ft_label_device_3.repaint()
            self.display_msg(msg_text="Calibration Complete", title="Done", type="info")
        else:
            return

    @Slot()
    def reset_settings(self):
        """
        Display a popup asking for confirmation.
        If yes, the settinngs are set to default.
        """
        reset = False

        response = self.display_msg(msg_text=Messages.RESET_SETTINGS_QUESTION, type="question")

        if response == QMessageBox.StandardButton.Yes:
            with self.wait_cursor():
                self.explorer.reset_soft()
            reset = True
        return reset

    def display_sr_warning(self):
        """Display warning for 1000 Hz sampling rate
        """
        if int(self.ui.value_sampling_rate.currentText()) == 1000:
            self.ui.lbl_sr_warning.show()
        else:
            self.ui.lbl_sr_warning.hide()

    def change_sampling_rate(self):
        """Change the sampling rate

        Returns:
            bool: whether sampling rate has changed
        """

        sr = self.explorer.stream_processor.device_info['sampling_rate']
        str_value = self.ui.value_sampling_rate.currentText()
        value = int(str_value)
        changed = False

        if int(sr) != value:
            if self.plotting_filters is not None:
                self.check_filters_new_sr()

            logger.info("Old Sampling rate: %s", self.explorer.stream_processor.device_info['sampling_rate'])
            self.explorer.set_sampling_rate(sampling_rate=value)
            logger.info("New Sampling rate: %s", self.explorer.stream_processor.device_info['sampling_rate'])
            changed = True

        return changed

    def change_active_channels(self):
        """
        Read selected checkboxes and set the channel mask of the device

        Returns:
            bool: whether sampling rate has changed
        """

        active_chan = []
        changed = False

        for w in self.ui.frame_cb_channels.findChildren(QCheckBox):
            status = str(1) if w.isChecked() else str(0)
            active_chan.append(status)

        active_chan = list(reversed(active_chan))
        active_chan_int = [int(i) for i in active_chan]
        n_active = sum(active_chan_int)
        if n_active == 0:
            self.display_msg(Messages.SELECT_1_CHAN)
            return

        if active_chan_int != self.explorer.stream_processor.device_info['adc_mask']:

            mask = "".join(active_chan)
            int_mask = int(mask, 2)
            try:
                self.explorer.set_channels(int_mask)
            except TypeError:
                self.explorer.set_channels(mask)

            n_chan = self.explorer.stream_processor.device_info['adc_mask']
            n_chan = list(reversed(n_chan))

            self.chan_dict = dict(zip([c.lower() for c in Settings.CHAN_LIST], n_chan))
            AppFunctions.chan_dict = self.chan_dict

            self.vis_functions.offsets = np.arange(1, n_chan.count(1) + 1)[:, np.newaxis].astype(float)
            self.vis_functions._baseline_corrector["baseline"] = None
            self.init_imp()
            changed = True

        return changed

    @Slot()
    def change_settings(self):
        """
        Apply changes in device settings
        """

        stream_processor = self.explorer.stream_processor

        with self.wait_cursor():
            if self.plotting_filters is not None:
                self.vis_functions._baseline_corrector["baseline"] = None
                self.explorer.stream_processor.remove_filters()

            changed_chan = self.change_active_channels()
            changed_sr = self.change_sampling_rate()
            self.reset_exg_plot_data()

            if self.plotting_filters is not None:
                self.apply_filters()

        if changed_sr or changed_chan:
            act_chan = ", ".join([ch for ch in self.chan_dict if self.chan_dict[ch] == 1])
            msg = (
                "Device settings have been changed:"
                f"\nSampling Rate: {int(stream_processor.device_info['sampling_rate'])}"
                f"\nActive Channels: {act_chan}"
            )
            self.display_msg(msg_text=msg, type="info")

        self.vis_functions.init_plots()

    def check_filters_new_sr(self):
        """Check whether current filters are compatible with new sampling rate.
        If not, update plotting_filters
        """
        if self.plotting_filters is None:
            return

        r_value = "" if self.plotting_filters["highpass"] in [None, 'None'] else self.plotting_filters["highpass"]
        l_value = "" if self.plotting_filters["lowpass"] in [None, 'None'] else self.plotting_filters["lowpass"]

        str_value = self.ui.value_sampling_rate.currentText()
        sr = int(str_value)

        nyq_freq = sr / 2.

        max_hc_freq = round(nyq_freq - 1, 1)
        min_lc_freq = round(0.0035 * nyq_freq, 1)

        warning = ""

        hc_freq_warning = (
            "High cutoff frequency cannot be larger than or equal to the nyquist frequency.\n"
            f"The high cutoff frequency has changed to {max_hc_freq:.1f} Hz!"
        )

        lc_freq_warning = (
            "Transient band for low cutoff frequency was too narrow.\n"
            f"The low cutoff frequency has changed {min_lc_freq:.1f} Hz!"
        )

        if (l_value != "") and (float(l_value) / nyq_freq <= 0.0035):
            warning += lc_freq_warning
            self.plotting_filters["lowpass"] = min_lc_freq

        if (r_value != "") and (float(r_value) >= nyq_freq):
            warning += hc_freq_warning
            self.plotting_filters["highpass"] = max_hc_freq

        if warning != "":
            self.display_msg(msg_text=warning, type="info")

    def enable_settings(self, enable=True) -> None:
        """Disable or enable device settings widgets

        Args:
            enable (bool, optional): True will enable, False will disable. Defaults to True.
        """

        enabled = True
        s_rate_stylesheet = ""
        stylesheet = ""
        tooltip_apply_settings = ""
        tooltip_reset_settings = ""
        tooltip_format_mem = ""

        if enable is False:
            enabled = False
            s_rate_stylesheet = "color: gray;\nborder-color: gray;"
            stylesheet = Stylesheets.DISABLED_BTN_STYLESHEET
            tooltip_apply_settings = Messages.DISABLED_SETTINGS
            tooltip_reset_settings = Messages.DISABLED_RESET
            tooltip_format_mem = Messages.DISABLED_FORMAT_MEM

        for wdgt in self.ui.frame_cb_channels.findChildren(QCheckBox):
            wdgt.setEnabled(enabled)

        self.ui.value_sampling_rate.setEnabled(enabled)
        self.ui.value_sampling_rate.setStyleSheet(s_rate_stylesheet)

        self.ui.btn_apply_settings.setEnabled(enabled)
        self.ui.btn_apply_settings.setStyleSheet(stylesheet)
        self.ui.btn_apply_settings.setToolTip(tooltip_apply_settings)

        self.ui.btn_reset_settings.setEnabled(enabled)
        self.ui.btn_reset_settings.setStyleSheet(stylesheet)
        self.ui.btn_reset_settings.setToolTip(tooltip_reset_settings)

        self.ui.btn_format_memory.setEnabled(enabled)
        self.ui.btn_format_memory.setStyleSheet(stylesheet)
        self.ui.btn_format_memory.setToolTip(tooltip_format_mem)

        self.ui.label_warning_disabled.setHidden(enabled)
