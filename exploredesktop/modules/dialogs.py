import os
import re
from abc import abstractmethod
from typing import Union

import numpy as np
from PySide6.QtCore import (
    QRegularExpression,
    QSettings
)
from PySide6.QtGui import (
    QCloseEvent,
    QIcon,
    QRegularExpressionValidator
)
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFileDialog
)


from exploredesktop.modules.app_settings import (  # isort: skip
    FileTypes,
    GUISettings,
    Messages,
    QSettingsKeys,
    Settings
)
from exploredesktop.modules.utils import (  # isort: skip
    verify_filters,
    get_path_settings
)
from exploredesktop.modules.ui import (  # isort: skip
    Ui_PlotDialog,
    Ui_RecordingDialog,
    Ui_BinDialog
)

par_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
ICON_PATH = os.path.join(par_dir, "MentalabLogo.ico")


class CustomDialog(QDialog):
    """Base class for custom pop-up dialogs

    Args:
       QDialog (Pyside6.QtWidgets.QDialog): pyside widget
    """

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.close = False

    # pylint: disable=invalid-name
    def closeEvent(self, arg__1: QCloseEvent) -> None:
        """Rewrite close event

        Args:
            arg__1 (PySide6.QtGui.QCloseEvent): pyside close event
        """
        self.close = True
        return super().closeEvent(arg__1)

    def reject(self) -> None:
        """Rewrite reject event, i.e. clicking on cancel
        """
        self.close = True
        return super().reject()

    @abstractmethod
    def get_data(self):
        """Abstract function to be implemented in child classes

        Raises:
            NotImplementedError: method has to be override in child class
        """
        raise NotImplementedError("Must override get_data method")

    def exec(self) -> Union[bool, dict]:
        """Rewrite exec method

        Returns:
            Union[bool, dict]: False if dialog was closed or canceled. Otherwise dictionary with data from pop-up
        """
        super().exec()

        if self.close:
            return False

        data = self.get_data()
        return data


class PathInputDialog(CustomDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.file_type = FileTypes.CSV.value

    def validate_filepath(self) -> None:
        """Validate selected path by checking if it already exists and warning the user
        """
        file_path = self.get_file_path()
        if os.path.isfile(file_path):
            self._display_warning_file_exists()
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        else:
            self._hide_warning()
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)

    @abstractmethod
    def get_file_path(self):
        raise NotImplementedError

    def file_extension(self) -> str:
        """Return file extension selected

        Returns:
            str: file extension (edf or csv)
        """
        if self.ui.rdbtn_edf.isChecked():
            self.file_type = FileTypes.BDF.value
        else:
            self.file_type = FileTypes.CSV.value

        return self.file_type

    def _display_warning_file_exists(self) -> None:
        """Display warning for file already exists"""
        self.ui.warning_label.setText(Messages.FILE_EXISTS)
        self.ui.warning_label.setHidden(False)

    def _hide_warning(self) -> None:
        """Hide warning from dialog
        """
        self.ui.warning_label.setHidden(True)

    def _display_warning_char(self) -> None:
        """Display warning for special characters in file name"""
        self.ui.warning_label.setText(Messages.SPECIAL_CHAR_WARNING)
        self.ui.input_file_name.setStyleSheet("border: 1px solid rgb(217, 0, 0)")
        self.ui.warning_label.setHidden(False)


class RecordingDialog(PathInputDialog):
    """Dialog Recording Settings pop up

    Args:
        QDialog (Pyside6.QtWidgets.QDialog): pyside widget
    """

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_RecordingDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Recording Settings")

        self.recording_time = int(self.ui.spinBox_recording_time.value())
        self.file_type = FileTypes.CSV.value
        self.recording_path = ""

        self.ui.btn_browse.clicked.connect(self.save_dir_name)
        self.ui.input_file_name.textChanged.connect(self.validate_filename)

        self.ui.rdbtn_csv.toggled.connect(self.validate_filepath)
        self.ui.rdbtn_edf.toggled.connect(self.validate_filepath)
        self.ui.input_filepath.textChanged.connect(self.validate_filepath)
        self.ui.input_file_name.textChanged.connect(self.validate_filepath)

        self.set_default_ui_values()

    def set_default_ui_values(self) -> None:
        """Set up default values for GUI elements
        """
        self.ui.spinBox_recording_time.setMaximum(10000000)
        self.ui.spinBox_recording_time.setValue(3600)
        self.ui.rdbtn_csv.setChecked(True)
        self.ui.warning_label.setHidden(True)

    def get_file_path(self) -> str:
        """Join directory and file name to obtain file path

        Returns:
            str: file path
        """
        file_dir = self._get_file_dir()
        file_name = self._get_file_name()

        file_path = os.path.join(file_dir, file_name)
        return file_path

    def _get_file_name(self) -> str:
        """Returns file name. If empty it returns the placeholder text
        """
        input_name = self.ui.input_file_name.text()
        placeholder_name = self.ui.input_filepath.placeholderText()
        file_name = input_name if input_name != "" else placeholder_name
        file_name += "_ExG." + self.file_extension()
        return file_name

    def _get_file_dir(self) -> str:
        """Returns file directory. If empty it returns the placeholder text
        """
        input_dir = self.ui.input_filepath.text()
        placeholder_dir = self.ui.input_filepath.placeholderText()
        file_dir = input_dir if input_dir != "" else placeholder_dir
        return file_dir

    def save_dir_name(self) -> None:
        """
        Open a dialog to select file name to be saved
        """
        key = QSettingsKeys.RECORD_FOLDER
        settings = QSettings("Mentalab", "ExploreDesktop")
        path = get_path_settings(settings, key)

        dialog = QFileDialog()
        file_path = dialog.getExistingDirectory(
            self,
            "Choose Directory",
            path,
            QFileDialog.ShowDirsOnly)

        self.recording_path = file_path
        self.ui.input_filepath.setText(self.recording_path)
        if path != self.recording_path:
            settings.setValue(key, self.recording_path)

    def validate_filename(self, text: str) -> None:
        """Validate input file name by removing special characters and warning the user

        Args:
            text (str): file name input by the user
        """
        if any(char in text for char in GUISettings.RESERVED_CHARS):
            self.remove_special_chars(text)
            self._display_warning_char()
        else:
            self._hide_warning()

    def remove_special_chars(self, text: str) -> None:
        """Remove special characters from input file name

        Args:
            text (str): input file name
        """
        new_text = re.sub(GUISettings.RESERVED_CHARS, "", text)
        self.ui.input_file_name.setText(new_text)

    def _display_warning_file_exists(self) -> None:
        self.ui.input_file_name.setStyleSheet("border: 1px solid rgb(217, 0, 0)")
        super()._display_warning_file_exists()

    def _hide_warning(self) -> None:
        self.ui.input_file_name.setStyleSheet("")
        super()._hide_warning()

    def get_data(self) -> dict:
        """Get dialog data

        Returns:
            dict: dictionary with dialog data
        """
        data = {
            "file_name": self.ui.input_file_name.text(),
            "file_path": self.ui.input_filepath.text(),
            "duration": int(self.ui.spinBox_recording_time.value()),
            "file_type": self.file_extension()
        }
        return data


class FiltersDialog(CustomDialog):
    """Dialog Filters Pop-upa

    Args:
        QDialog (Pyside6.QtWidgets.QDialog): pyside widget
    """

    def __init__(self, sr, current_filters, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_PlotDialog()
        self.s_rate = float(sr)
        self.current_filters = current_filters

        self.ui.setupUi(self)
        self.setWindowTitle("Visualization Settings")

        self.ui.lbl_warning.hide()
        self.ui.cb_offset.setToolTip(Messages.OFFSET_EXPLANATION)

        self.set_filter_values()
        self.display_current_values()
        self.add_validators()

        # Verify input without output message when typing
        self.ui.value_lowcutoff.textChanged.connect(self.verify_input)
        self.ui.value_highcutoff.textChanged.connect(self.verify_input)

        # Verify input without output message when typing
        self.ui.value_lowcutoff.textChanged.connect(self.verify_input)
        self.ui.value_highcutoff.textChanged.connect(self.verify_input)

    def set_filter_values(self) -> None:
        """Set values from current filters to attributes
        """
        if self.current_filters is None:  # default values
            self._set_default_values()
        else:
            self._set_current_values()

        if self.high_cutoff == "None":
            self.high_cutoff = ""
        if self.low_cutoff == "None":
            self.low_cutoff = ""

    def _set_current_values(self) -> None:
        """Set filter current values"""
        self.offset = self.current_filters["offset"]
        self.notch = str(self.current_filters["notch"])
        self.low_cutoff = str(self.current_filters["low_cutoff"])
        self.high_cutoff = str(self.current_filters["high_cutoff"])

    def _set_default_values(self) -> None:
        """Set filter default values"""
        self.offset = True
        self.notch = "50"
        self.low_cutoff = "1" if self.s_rate < 1000 else "2"
        self.high_cutoff = "30"

    def display_current_values(self) -> None:
        """Add filter values to UI
        """
        # Add options to notch combobox
        self.ui.value_notch.addItems(["", "50", "60"])

        # Display current values
        self.ui.value_notch.setCurrentText(self.notch)
        self.ui.value_highcutoff.setText(self.high_cutoff)
        self.ui.value_lowcutoff.setText(self.low_cutoff)
        self.ui.cb_offset.setChecked(self.offset)

    def add_validators(self) -> None:
        """Add validator to text boxes to only accept doubles
        """
        # Set validators (only accept doubles)
        regex = QRegularExpression(r"([0-9]+\.?[0-9]|\.[0-9])")
        self.ui.value_highcutoff.setValidator(QRegularExpressionValidator(regex))
        self.ui.value_lowcutoff.setValidator(QRegularExpressionValidator(regex))

    def verify_input(self) -> None:
        """Verify frequencies are not above/below the threshold
        """

        hc_freq = "" if self.ui.value_highcutoff.text() in [None, 'None', ''] else self.ui.value_highcutoff.text()
        lc_freq = "" if self.ui.value_lowcutoff.text() in [None, 'None', ''] else self.ui.value_lowcutoff.text()

        hc_stylesheet = ""
        lc_stylesheet = ""
        lbl_txt = ""

        if hc_freq in ["."] or lc_freq in ["."]:
            return

        filter_ok = verify_filters((lc_freq, hc_freq), self.s_rate)

        hc_stylesheet, lc_stylesheet, lbl_txt = self.get_le_stylesheets(filter_ok)

        self._apply_le_stylesheets(lc_stylesheet, hc_stylesheet, lbl_txt)
        enable = False not in filter_ok.values()
        self._enable_ok_button(enable)

    def get_le_stylesheets(self, filter_ok: dict) -> Union[str, str, str]:
        """Get stylesheets for UI lineedits

        Args:
            filter_ok (dict): dictionary containing whether filters are corrects

        Returns:
            Union[str, str, str]: stylesheet for line edit and warning text to display
        """
        hc_stylesheet, lc_stylesheet, lbl_txt = "", "", ""
        hc_freq_warning, lc_freq_warning, bp_freq_warning = self._get_warning_msg()

        if filter_ok['lc_freq'] is False:
            lbl_txt = lc_freq_warning
            hc_stylesheet = ""
            lc_stylesheet = "border: 1px solid rgb(217, 0, 0)"

        elif filter_ok['hc_freq'] is False:
            lbl_txt = hc_freq_warning
            hc_stylesheet = "border: 1px solid rgb(217, 0, 0)"
            lc_stylesheet = ""

        elif filter_ok['bp_valid'] is False:
            lbl_txt = bp_freq_warning
            hc_stylesheet = "border: 1px solid rgb(217, 0, 0)"
            lc_stylesheet = "border: 1px solid rgb(217, 0, 0)"

        return hc_stylesheet, lc_stylesheet, lbl_txt

    def _get_warning_msg(self) -> Union[str, str, str]:
        """Generate warning message with appropiate frequencies

        Returns:
            Union[str, str, str]: warning messages for high cutoff, lowcutoff and bandpass
        """
        nyq_freq = self.s_rate / 2.
        max_hc_freq = nyq_freq - 1
        min_lc_freq = Settings.MIN_LC_WEIGHT * nyq_freq

        hc_freq_warning = (
            "High cutoff frequency cannot be larger than or equal to the nyquist frequency."
            f"The maximum high cutoff frequency is {np.ceil(max_hc_freq*10)/10} Hz!"
        )

        lc_freq_warning = (
            "Transient band for low cutoff frequency is too narrow."
            f"The minimum low cutoff frequency is {np.ceil(min_lc_freq*10)/10} Hz!"
        )

        bp_freq_warning = ("High cutoff frequency must be larger than low cutoff frequency.")
        return hc_freq_warning, lc_freq_warning, bp_freq_warning

    def _apply_le_stylesheets(self, lc_stylesheet: str, hc_stylesheet: str, lbl_txt: str) -> None:
        """Apply stylesheets to lineedit widgets and display warning text

        Args:
            lc_stylesheet (str): stylesheet for low cutoff frequency lineedit
            hc_stylesheet (str): stylesheet for low cutoff frequency lineedit
            lbl_txt (str): warning text
        """
        self.ui.value_highcutoff.setStyleSheet(hc_stylesheet)
        self.ui.value_lowcutoff.setStyleSheet(lc_stylesheet)
        self.ui.lbl_warning.setText(lbl_txt)
        if lbl_txt != "":
            self.ui.lbl_warning.setHidden(False)
        else:
            self.ui.lbl_warning.setHidden(True)

    def _enable_ok_button(self, enable: bool) -> None:
        """Enable OK button while filter value changes

        Args:
            enable (bool): whether to enable
        """
        self.ui.value_lowcutoff.textChanged.connect(
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enable))
        self.ui.value_highcutoff.textChanged.connect(
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enable))

    def get_data(self) -> dict:
        """Get filter data from dialog

        Returns:
            dict: dictionary containing filter values
        """
        data = {
            "offset":
                self.ui.cb_offset.isChecked(),
            "notch":
                None if self.ui.value_notch.currentText() == "" else int(self.ui.value_notch.currentText()),
            "low_cutoff":
                None if self.ui.value_lowcutoff.text() in [None, 'None', ""] else float(self.ui.value_lowcutoff.text()),
            "high_cutoff":
                None if self.ui.value_highcutoff.text() in [
                    None, 'None', ""] else float(self.ui.value_highcutoff.text())
        }
        return data


class ConvertBinDialog(PathInputDialog):
    """Dialog Convert BIN File pop up

    Args:
        QDialog (Pyside6.QtWidgets.QDialog): pyside widget
    """

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_BinDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Convert .BIN")

        self.file_type = FileTypes.CSV.value
        self.bin_path = ""
        self.dst_folder = ""

        self.ui.btn_browse_bin.clicked.connect(self.get_bin_path)
        self.ui.btn_browse_dest_folder.clicked.connect(self.get_dst_folder)

        self.ui.rdbtn_csv.toggled.connect(self.validate_filepath)
        self.ui.rdbtn_edf.toggled.connect(self.validate_filepath)
        self.ui.input_filepath.textChanged.connect(self.validate_filepath)
        self.ui.input_filepath.textChanged.connect(self.validate_input_file)
        self.ui.input_filepath.textChanged.connect(self.check_not_empty)
        self.ui.input_dest_folder.textChanged.connect(self.validate_filepath)
        self.ui.input_dest_folder.textChanged.connect(self.check_not_empty)

        self.set_default_ui_values()

    def set_default_ui_values(self) -> None:
        """Set up default values for GUI elements
        """
        self.ui.rdbtn_csv.setChecked(True)
        self.ui.warning_label.setHidden(True)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

    def get_bin_path(self) -> None:
        """
        Open a dialog to select file name to be saved
        """
        key = QSettingsKeys.BIN_FOLDER.value
        settings = QSettings("Mentalab", "ExploreDesktop")
        path = get_path_settings(settings, key)

        dialog = QFileDialog()
        file_path = dialog.getOpenFileName(
            self,
            "Select .BIN file",
            path,
            "BIN (*.BIN)")

        self.bin_path = file_path[0]
        self.ui.input_filepath.setText(self.bin_path)
        if path != self.bin_path:
            settings.setValue(key, os.path.dirname(self.bin_path))

    def get_dst_folder(self) -> None:
        """
        Open a dialog to select file name to be saved
        """
        key = QSettingsKeys.BIN_EXPORT.value
        settings = QSettings("Mentalab", "ExploreDesktop")
        path = get_path_settings(settings, key)

        dialog = QFileDialog()
        file_path = dialog.getExistingDirectory(
            self,
            "Select Destination Directory",
            path,
            QFileDialog.ShowDirsOnly)

        self.dst_folder = file_path
        self.ui.input_dest_folder.setText(self.dst_folder)
        if path != self.dst_folder:
            settings.setValue(key, self.dst_folder)

    def get_file_path(self) -> str:
        """Get full path to the file to save

        Returns:
            str: file path
        """
        file_dir = self.ui.input_dest_folder.text()
        file_name = os.path.basename(self.ui.input_filepath.text()).replace(".BIN", "_ExG." + self.file_extension())
        return os.path.join(file_dir, file_name)

    def _display_warning_file_exists(self) -> None:
        self.ui.input_dest_folder.setStyleSheet("border: 1px solid rgb(217, 0, 0)")
        super()._display_warning_file_exists()

    def _hide_warning(self) -> None:
        self.ui.input_dest_folder.setStyleSheet("")
        super()._hide_warning()

    def validate_input_file(self) -> None:
        file = self.ui.input_filepath.text()
        if file.replace(" ", "") != "" and not file.endswith(".BIN"):
            self._display_warning_notBin()
        else:
            self.ui.input_filepath.setStyleSheet("")
            self.ui.warning_label.setText("")

    def _display_warning_notBin(self) -> None:
        self.ui.input_filepath.setStyleSheet("border: 1px solid rgb(217, 0, 0)")
        self.ui.warning_label.setText("File must be .BIN")

    def check_not_empty(self) -> None:
        folder_field = self.ui.input_dest_folder.text().replace(" ", "")
        input_file_field = self.ui.input_filepath.text().replace(" ", "")
        if (folder_field == "" or input_file_field == ""):
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        else:
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)

    def get_data(self) -> dict:
        """Get dialog data

        Returns:
            dict: dictionary with dialog data
        """
        data = {
            "bin_path": self.ui.input_filepath.text(),
            "dst_folder": self.ui.input_dest_folder.text(),
            "file_type": self.file_extension()
        }
        return data


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dial = ConvertBinDialog()
    data = dial.exec()
    print(data)
