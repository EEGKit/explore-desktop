"""Settings module"""
import logging
import os
from copy import deepcopy

import yaml
from exploredesktop.modules.dialogs import ConvertBinDialog
from PySide6.QtCore import (
    QAbstractTableModel,
    QEvent,
    QModelIndex,
    QSettings,
    Qt,
    Slot
)
from PySide6.QtGui import QBrush
from PySide6.QtWidgets import (
    QComboBox,
    QFileDialog,
    QHeaderView,
    QItemDelegate,
    QMessageBox,
    QStyledItemDelegate
)


from exploredesktop.modules.app_settings import (  # isort: skip
    ConnectionStatus,
    DataAttributes,
    ExGModes
)
from exploredesktop.modules import (  # isort: skip
    Messages,
    Settings,
    BaseModel
)
from exploredesktop.modules.utils import display_msg, wait_cursor, ELECTRODES_10_20  # isort: skip


logger = logging.getLogger("explorepy." + __name__)


class SettingsFrameView(BaseModel):
    """_summary_
    """

    def __init__(self, ui, filters) -> None:
        super().__init__()
        self.ui = ui
        self.filters = filters
        self.setup_frame()

        self.ui.table_settings.setModel(ConfigTableModel([]))
        self.setup_tableview()

        # Setup signal connections
        self.signals.dataSettingsChanged.connect(self.disable_apply)

    @Slot()
    def disable_apply(self, index: QModelIndex) -> None:
        """Disable apply button based on the names of the channels

        Args:
            index (QModelIndex): index of the item changed
        """
        # Only relevant for Name column, return if item changed is another one
        if index.column() != 2:
            return

        # Default values
        enable = True
        tooltip = ""

        custom_names = self.ui.table_settings.model().get_list_names()
        custom_names_alnum = ["".join(e for e in name if e.isalnum()).strip() for name in custom_names]

        # Check for names containing only special characters
        if "" in custom_names_alnum:
            enable = False
            tooltip = "Channel names cannot contain only special characters"

        # Check for repeated names
        if len(custom_names) != len(set(custom_names)):
            enable = False
            tooltip = "Channel names must be unique"

        # Disable button and set tooltip
        self.ui.btn_apply_settings.setEnabled(enable)
        # TODO? add tooltip to cells
        self.ui.btn_apply_settings.setToolTip(tooltip)

    def setup_tableview(self) -> None:
        """Configure settings table
        """
        # Add delegates
        self.ui.table_settings.setItemDelegateForColumn(1, CheckBoxDelegate(None))
        self.ui.table_settings.setItemDelegate(_ConfigItemDelegate())

        # Resize to fill all horizontal space
        self.ui.table_settings.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_settings.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_settings.verticalHeader().setVisible(False)

        # Stylesheet
        self.ui.table_settings.setAlternatingRowColors(True)
        self.ui.table_settings.horizontalHeader().setStyleSheet("""
        QHeaderView::section {
            border-bottom: 1px solid black;
            border-right: 0px;
            border-top: 0px;
        }""")

        self.ui.table_settings.setStyleSheet("""
        border: none;""")

        # Remove button to select all
        self.ui.table_settings.setCornerButtonEnabled(False)

        # Hide signal type column
        self.ui.table_settings.setColumnHidden(3, True)

    def setup_frame(self) -> None:
        """Initialize dropdowns and checkboxes
        """
        self.ui.value_sampling_rate.addItems([str(int(sr)) for sr in Settings.SAMPLING_RATES])
        # TODO uncomment later if implemented
        # self.ui.dropdown_signal_type.addItems(ExGModes.all_values())
        # self.ui.cb_multitype_signal.setChecked(False)
        # self.ui.dropdown_signal_type.setHidden(False)

        # Hide multitype signal dropdown and checkbox
        # self.ui.cb_multitype_signal.setHidden(True)
        # self.ui.dropdown_signal_type.setHidden(True)
        # self.ui.cb_1020.setHidden(True)

    def setup_ui_connections(self) -> None:
        """Connect ui widgets to corresponding slot
        """
        self.ui.value_sampling_rate.currentTextChanged.connect(self.display_sr_warning)

        self.ui.btn_reset_settings.clicked.connect(self.reset_settings)
        self.ui.btn_format_memory.clicked.connect(self.format_memory)
        self.ui.btn_apply_settings.clicked.connect(self.change_settings)
        # TODO uncomment when implemented
        # self.ui.btn_calibrate.setHidden(True)

        # TODO uncomment later when implemented
        # self.ui.cb_multitype_signal.stateChanged.connect(self.multisignal_clicked)
        # self.ui.dropdown_signal_type.currentTextChanged.connect(self.signal_type_changed)
        # self.ui.cb_1020.stateChanged.connect(self.enable_10_20)

    def setup_settings_frame(self) -> None:
        """Setup the settings frame
        """
        # Set device name
        self.ui.label_explore_name.setText(self.explorer.device_name)

        # Set active channels
        data = deepcopy(self.explorer.chan_dict_list)
        self.ui.table_settings.setModel(ConfigTableModel(data))
        self.ui.table_settings.viewport().update()

        # Set sampling rate
        s_rate = int(self.explorer.sampling_rate)
        self.ui.value_sampling_rate.setCurrentText(str(s_rate))

    ###
    # Button slots
    ###
    @Slot()
    def reset_settings(self) -> None:
        """
        Display a popup asking for confirmation.
        If yes, the settinngs are set to default.
        """
        reset = False

        response = display_msg(msg_text=Messages.RESET_SETTINGS_QUESTION, popup_type="question")

        if response == QMessageBox.StandardButton.No:
            return reset

        with wait_cursor():
            reset = self.explorer.reset_soft()
            self.explorer.disconnect()
            self.signals.connectionStatus.emit(ConnectionStatus.DISCONNECTED)
            self.signals.pageChange.emit("btn_bt")

        if reset:
            self.explorer.disconnect()
            self.signals.connectionStatus.emit(ConnectionStatus.DISCONNECTED)

        else:
            msg = (
                "There was an error while resetting the settings."
                "\nPlease make sure the bluetooth connection is stable and try again."
            )
            display_msg(msg)

    @Slot()
    def format_memory(self) -> None:
        """
        Display a popup asking for confirmation.
        If yes, memory is formatted.
        """

        response = display_msg(msg_text=Messages.FORMAT_MEM_QUESTION, popup_type="question")

        if response != QMessageBox.StandardButton.Yes:
            return

        with wait_cursor():
            result = self.explorer.format_memory()

        if result:
            display_msg(msg_text="Memory formatted", popup_type="info")
        else:
            msg = (
                "There was an error while formatting the memory."
                "\nPlease make sure the bluetooth connection is stable and try again."
            )
            display_msg(msg)

    @Slot()
    def change_settings(self) -> None:
        """
        Apply changes in device settings
        """
        with wait_cursor():
            self._remove_filters()

            changed_chan = self.change_active_channels()
            changed_sr = self.change_sampling_rate()
            changed_chan_names = self.change_channel_names()

            # Reset exg data and reapply filters
            self.signals.updateDataAttributes.emit([DataAttributes.DATA])
            if self.filters.current_filters is not None:
                self.filters.apply_filters()

        if changed_sr or changed_chan or changed_chan_names:
            self._display_new_settings()
            self.signals.restartPlot.emit()
            self.signals.displayDefaultImp.emit()

    def _display_new_settings(self) -> None:
        """Display popup with new sampling rate and active channels
        """
        chan_dict = self.explorer.get_chan_dict_list()
        act_chan = ", ".join([
            f'{one_chan_dict["input"]} ({one_chan_dict["name"]})'
            for one_chan_dict in chan_dict if one_chan_dict["enable"]])
        msg = (
            "Device settings have been changed:"
            f"\nSampling Rate: {self.explorer.sampling_rate}"
            f"\nActive Channels: {act_chan}"
        )
        display_msg(msg_text=msg, popup_type="info")

    def _remove_filters(self) -> None:
        """Remove filters"""
        if self.filters.current_filters is not None:
            self.signals.updateDataAttributes.emit([DataAttributes.BASELINE])
            self.explorer.stream_processor.remove_filters()

    ###
    # Change settings functions
    ###
    def change_channel_names(self) -> bool:
        """Read table and change the channel names

        Returns:
            bool: _description_
        """
        changed = False
        chan_names_table = self.ui.table_settings.model().get_list_names()

        if chan_names_table != self.explorer.active_chan_list(custom_name=True):
            changed = True
            self.explorer.set_chan_dict_list(self.ui.table_settings.model().chan_data)
            self.explorer.settings.set_chan_names(self.ui.table_settings.model().get_list_names())
        return changed

    def change_active_channels(self) -> bool:
        """
        Read selected checkboxes and set the channel mask of the device

        Returns:
            bool: whether sampling rate has changed
        """

        changed = False

        active_chan = self.get_active_chan_ui()
        active_chan_int = [int(i) for i in active_chan]
        # verify at least one channel is selected
        n_active = sum(active_chan_int)
        if n_active == 0:
            display_msg(Messages.SELECT_1_CHAN)
            return

        if (active_chan_int != self.explorer.chan_mask):
            # TODO decide how we handle (de)activation of channels for 4, 8 chan
            changed = True
            # mask = "".join(active_chan)
            # changed = self.explorer.set_channels(mask)
            # self.explorer.chan_mask = self.ui.table_settings.model().get_chan_mask()
            mask = self.ui.table_settings.model().get_chan_mask()
            self.explorer.set_chan_mask(mask)
            self.explorer.set_chan_dict_list(self.ui.table_settings.model().chan_data)
            self.update_modules()

        return changed

    def update_modules(self) -> None:
        """Update modules dependent on number of active channels"""
        self.signals.updateDataAttributes.emit([DataAttributes.OFFSETS, DataAttributes.BASELINE])
        self.signals.displayDefaultImp.emit()

    def get_active_chan_ui(self) -> list:
        """Get active channels from UI settings table checkboxes

        Returns:
            list[str]: binary list indicating whether channel is active
        """
        active_chan = [str(one_chan_dict["enable"]) for one_chan_dict in self.ui.table_settings.model().chan_data]
        # active_chan = list(reversed(active_chan))
        return active_chan

    def change_sampling_rate(self) -> bool:
        """Change the sampling rate

        Returns:
            bool: whether sampling rate has changed
        """

        current_sr = int(self.explorer.sampling_rate)
        new_sr = int(self.ui.value_sampling_rate.currentText())
        changed = False

        if int(current_sr) != new_sr:
            if self.filters.current_filters is not None:
                self.filters.check_filters_sr(new_sr)

            logger.info("Old Sampling rate: %s", self.explorer.sampling_rate)
            changed = self.explorer.set_sampling_rate(sampling_rate=new_sr)
            logger.info("New Sampling rate: %s", self.explorer.sampling_rate)

        return changed

    def check_settings_saved(self) -> bool:
        """Check if the settings in UI are the same as in explore, i.e. all settings have been saved

        Returns:
            bool: whether settings have been saved
        """
        saved = True
        if not self.explorer.is_connected:
            return saved
        current_sr = int(self.explorer.sampling_rate)
        ui_sr = int(self.ui.value_sampling_rate.currentText())

        current_chan_names = self.explorer.active_chan_list(custom_name=True)
        ui_chan_names = self.ui.table_settings.model().get_list_names()

        # TODO uncomment when adc mask is implemented
        # current_active_chan = self.explorer.stream_processor.device_info['adc_mask']
        current_active_chan = self.explorer.chan_mask
        ui_active_chan = [int(i) for i in self.get_active_chan_ui()]

        if (
            current_sr != ui_sr
        ) or (
            current_chan_names != ui_chan_names
        ) or (current_active_chan != ui_active_chan):
            saved = False
        return saved

    ###
    # Vis feedback slots
    ###
    @Slot()
    def display_sr_warning(self) -> None:
        """Display warning for 1000 Hz sampling rate
        """
        if int(self.ui.value_sampling_rate.currentText()) == 1000:
            self.ui.lbl_sr_warning.show()
        else:
            self.ui.lbl_sr_warning.hide()

    def enable_settings(self, enable=True) -> None:
        """Disable or enable device settings widgets

        Args:
            enable (bool, optional): True will enable, False will disable. Defaults to True.
        """

        enabled = True
        s_rate_stylesheet = ""
        # TODO decide which stylesheet to use
        # stylesheet = ""
        tooltip_apply_settings = ""
        tooltip_reset_settings = ""
        tooltip_format_mem = ""

        if enable is False:
            enabled = False
            s_rate_stylesheet = "color: gray;\nborder-color: gray;"
            # stylesheet = Stylesheets.DISABLED_BTN_STYLESHEET
            tooltip_apply_settings = Messages.DISABLED_SETTINGS
            tooltip_reset_settings = Messages.DISABLED_RESET
            tooltip_format_mem = Messages.DISABLED_FORMAT_MEM

        self.ui.value_sampling_rate.setEnabled(enabled)
        self.ui.value_sampling_rate.setStyleSheet(s_rate_stylesheet)

        self.ui.btn_apply_settings.setEnabled(enabled)
        # self.ui.btn_apply_settings.setStyleSheet(stylesheet)
        self.ui.btn_apply_settings.setToolTip(tooltip_apply_settings)

        self.ui.btn_reset_settings.setEnabled(enabled)
        # self.ui.btn_reset_settings.setStyleSheet(stylesheet)
        self.ui.btn_reset_settings.setToolTip(tooltip_reset_settings)

        self.ui.btn_format_memory.setEnabled(enabled)
        # self.ui.btn_format_memory.setStyleSheet(stylesheet)
        self.ui.btn_format_memory.setToolTip(tooltip_format_mem)

        self.ui.label_warning_disabled.setHidden(enabled)

    def multisignal_clicked(self) -> None:
        """Allow/Block selection of multiple signal types
        """
        multitype = self.ui.cb_multitype_signal.isChecked()

        self.ui.dropdown_signal_type.setHidden(multitype)
        self.ui.table_settings.model().change_column_edit("type", multitype)
        self.ui.table_settings.viewport().update()

    def signal_type_changed(self) -> None:
        """Change all signal type values based on dropdown value
        """
        if self.ui.dropdown_signal_type.currentText() == ExGModes.EEG.value:
            new_value = ExGModes.EEG.value
        else:
            new_value = ExGModes.ECG.value

        for ch_dict in self.ui.table_settings.model().chan_data:
            ch_dict["type"] = new_value
        self.ui.table_settings.viewport().update()

    def enable_10_20(self) -> None:
        """Enable combobox for 10/20 notation
        """
        if self.ui.cb_1020.isChecked():
            self.ui.table_settings.model().change_column_editor("name", "combobox")
        else:
            self.ui.table_settings.model().change_column_editor("name", "default")

        self.ui.table_settings.viewport().update()

    # TODO create a class for menubar and move there
    def export_settings(self):
        """
        Open a dialog to select folder to be saved
        """
        settings = QSettings("Mentalab", "ExploreDesktop")
        path = settings.value("last_settings_save_folder")
        if not path:
            path = os.path.expanduser("~")

        dialog = QFileDialog()
        file_path = dialog.getSaveFileName(
            None,
            "Save As",
            os.path.join(path, "untitled.yaml"),
            "YAML (*.yaml)")

        file_path = file_path[0]

        if path != os.path.dirname(file_path):
            settings.setValue("last_settings_save_folder", os.path.dirname(file_path))

        settings_to_export = self.explorer.settings.settings_dict.copy()
        del settings_to_export["adc_mask"]
        del settings_to_export["firmware_version"]
        del settings_to_export["mac_address"]

        with open(file_path, 'w+') as fp:
            yaml.safe_dump(settings_to_export, fp, default_flow_style=False)
            fp.close()

    def import_settings(self):
        """Import settings
        """
        settings_dict = self._read_settings_file()

        if not self._verify_settings(settings_dict):
            return

        new_dict_list = [
            {
                'input': f'ch{idx + 1}', 'enable': val[0],
                'name': val[1], 'type': 'EEG'}
            for idx, val in enumerate(zip(settings_dict['software_mask'], settings_dict['channel_name']))]
        self.ui.table_settings.setModel(ConfigTableModel(new_dict_list))
        self.ui.value_sampling_rate.setCurrentText(str(int(settings_dict['sampling_rate'])))
        self.change_settings()
        self.explorer.chan_dict_list = new_dict_list

    def _verify_settings(self, settings_dict: dict) -> bool:
        """Check if imported settings can be applied to connected device

        Args:
            settings_dict (dict): dictionary of imported settings

        Returns:
            bool: whether imported settings are ok
        """
        settings_ok = True
        if len(settings_dict['software_mask']) == self.explorer.device_chan:
            return settings_ok

        extra = len(settings_dict['software_mask']) - self.explorer.device_chan
        if extra > 0:
            blurb = "The file selected has too many channels for the current device"
        elif extra < 0:
            blurb = "The file selected is missing some channels"
        display_msg(blurb, title="Invalid file")
        settings_ok = False

        return settings_ok

    def _read_settings_file(self) -> dict:
        """Open settings yaml file

        Returns:
            dict: dictionary with imported settings
        """
        settings = QSettings("Mentalab", "ExploreDesktop")
        path = settings.value("last_settings_import_folder")
        if not path:
            path = os.path.expanduser("~")

        dialog = QFileDialog()
        file_path = dialog.getOpenFileName(
            None,
            "Import",
            path,
            "YAML (*.yaml)")

        file_path = file_path[0]

        if path != os.path.dirname(file_path):
            settings.setValue("last_settings_import_folder", os.path.dirname(file_path))

        stream = open(file_path, 'r')
        settings_dict = yaml.load(stream, Loader=yaml.SafeLoader)
        return settings_dict

    def convert_bin(self) -> None:
        """Convert BIN file to csv/bdf
        """
        dialog = ConvertBinDialog()
        data = dialog.exec()
        print(data)
        self.explorer.convert_bin(
            bin_file=data['bin_path'],
            out_dir=data['dst_folder'],
            file_type=data['file_type'],
            out_dir_is_full=True
        )
        display_msg("Conversion finished", popup_type="info")


class CheckBoxDelegate(QItemDelegate):
    """
    A delegate that places a fully functioning QCheckBox cell of the column to which it's applied.
    """
    def __init__(self, parent):
        QItemDelegate.__init__(self, parent)

    # pylint: disable=invalid-name
    def createEditor(self, parent, option, index):
        """
        Important, otherwise an editor is created if the user clicks in this cell.
        """
        return None

    def paint(self, painter, option, index):
        """
        Paint a checkbox without the label.
        """
        self.drawCheck(painter, option, option.rect, Qt.Unchecked if int(index.data()) == 0 else Qt.Checked)

    # pylint: disable=invalid-name
    def editorEvent(self, event, model, option, index):
        """
        Change the data in the model and the state of the checkbox
        if the user presses the left mousebutton and this cell is editable. Otherwise do nothing.
        """
        if not int(index.flags() & Qt.ItemIsEditable) > 0:
            return False

        if event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
            # Change the checkbox-state
            self.setModelData(None, model, index)
            return True

        return False

    # pylint: disable=invalid-name
    def setModelData(self, editor, model, index):
        """
        Set new data in the model
        """
        model.setData(index, 1 if int(index.data()) == 0 else 0, Qt.EditRole)


class _ConfigItemDelegate(QStyledItemDelegate):
    ''' Combobox item editor
    '''

    # pylint: disable=invalid-name
    def createEditor(self, parent, option, index):
        """
        Create dropdown editor
        """
        if index.model().editorType(index.column()) == 'combobox':
            combobox = QComboBox(parent)
            combobox.addItems(index.model().comboBoxList(index.column()))
            combobox.setEditable(False)
            return combobox

        if index.model().editorType(index.column()) == 'checkbox':
            return None

        return QStyledItemDelegate.createEditor(self, parent, option, index)

    # pylint: disable=invalid-name
    def setEditorData(self, editor, index):
        """Set editor data
        """
        if index.model().columns[index.column()]['editor'] == 'combobox':
            text = index.model().data(index, Qt.DisplayRole)
            i = editor.findText(text)
            if i == -1:
                i = 0
            editor.setCurrentIndex(i)
        QStyledItemDelegate.setEditorData(self, editor, index)

    # pylint: disable=invalid-name
    def setModelData(self, editor, model, index):
        """Set data in the model
        """
        if model.columns[index.column()]['editor'] == 'combobox':
            model.setData(index, editor.currentText(), Qt.EditRole)
            # model.reset()
        QStyledItemDelegate.setModelData(self, editor, model, index)


class ConfigTableModel(QAbstractTableModel, BaseModel):
    """Table Model for configuration Table View
    """
    def __init__(self, data):
        """_summary_

        Args:
            data (_type_): _description_
        """
        super(ConfigTableModel, self).__init__()
        self.chan_data = data

        # column description
        self.columns = [
            {'property': 'input', 'header': 'Channel', 'edit': False, 'editor': 'default'},
            {'property': 'enable', 'header': 'Enable', 'edit': True, 'editor': 'checkbox'},
            {'property': 'name', 'header': 'Name', 'edit': True, 'editor': 'default'},
            {'property': 'type', 'header': 'Type', 'edit': False, 'editor': 'combobox'},
        ]

    def change_column_edit(self, col_name: str, new_val: bool) -> None:
        """Change edit field of a column to make it (un)editable

        Args:
            col_name (str): name of the property to change
            new_val (bool): whether column is editable
        """
        next(item for item in self.columns if item["property"] == col_name)["edit"] = new_val

    def change_column_editor(self, col_name: str, new_val: str) -> None:
        """Change editor flag of a column
        Args:
            col_name (str): name of the property to change
            new_val (bool): editor type
        """
        next(item for item in self.columns if item["property"] == col_name)["editor"] = new_val

    def data(self, index, role):
        """Abstract method from QAbstactTableModel to get data
        """
        value = self._getitem(index.row(), index.column())

        if (role == Qt.DisplayRole) or (role == Qt.EditRole):
            return value

        if role == Qt.BackgroundRole:
            if index.column() == 2 and (
                "".join(
                    e for e in value if e.isalnum()).strip() == "" or self.get_list_names().count(value) > 1):
                return QBrush("#fa5c62")

        if role == Qt.TextAlignmentRole:
            return Qt.AlignHCenter

    def get_list_names(self) -> list:
        """Return list of custom names
        """
        return [d["name"] for d in self.chan_data if d["enable"]]

    def get_chan_mask(self) -> list:
        """Return channel mask as list"""
        return [d["enable"] for d in self.chan_data]

    # pylint: disable=invalid-name
    def rowCount(self, index) -> int:
        """Return number of rows
        """
        return len(self.chan_data)

    # pylint: disable=invalid-name
    def columnCount(self, index) -> int:
        """Return number of columns
        """
        if self.chan_data:
            return len(self.chan_data[0])
        return len(self.columns)

    # pylint: disable=invalid-name
    def headerData(self, col, orientation, role):
        """Abstract method from QAbstactTableModel to get the column header
        """
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.columns[col]['header']

    def comboBoxList(self, column: int) -> list:
        """Get list of items for comboboxes

        Args:
            column (int): column number

        Returns:
            list: list of combobox items
        """
        if column >= len(self.columns):
            return None
        if self.columns[column]['property'] == 'type':
            return ExGModes.all_values()
        if self.columns[column]['property'] == 'name':
            return ELECTRODES_10_20

    def editorType(self, column: int) -> str:
        """Get the columns editor type from column description

        Args:
            column (int): column number

        Returns:
            str: editor type
        """
        if column >= len(self.columns):
            return None
        return str(self.columns[column]['editor'])

    def flags(self, index):
        """Abstract method from QAbstactTableModel
        """
        if not index.isValid():
            return Qt.ItemIsEnabled
        if not self.columns[index.column()]['edit']:
            return Qt.NoItemFlags
        if self.columns[index.column()]['header'] == "Enable":
            n_active = sum(item["enable"] for item in self.chan_data)
            if n_active == 1:
                ch_active = next(item for item in self.chan_data if item["enable"] == 1)["input"]
                row_active = int(ch_active.replace("ch", "")) - 1
                if index.column() == 1 and index.row() == row_active:
                    return Qt.NoItemFlags

        return QAbstractTableModel.flags(self, index) | Qt.ItemIsEditable

    def _setitem(self, row: int, column: int, value: str) -> bool:
        """Set property item based on table row and column

        Args:
            row (int): row number
            column (int): column number
            value (str): value to set

        Returns:
            bool: True if property value was set, False if not
        """
        if (row >= len(self.chan_data)) or (column >= len(self.columns)):
            return False
        # get channel properties
        property = self.chan_data[row]
        # get property name from column description
        property_name = self.columns[column]['property']
        # set channel property
        if property_name == 'enable':
            property["enable"] = value
            return True

        if property_name == 'name':
            n = value
            if "".join(n.split()) == "":
                return False
            property["name"] = value
            return True

        if property_name == 'type':
            n = value
            property["type"] = value
            return True

        return False

    def _getitem(self, row: int, column: int) -> str:
        """Get property item based on table row and column

        Args:
            row (int): row number
            column (int): column number

        Returns:
            str: property value
        """
        if (row >= len(self.chan_data)) or (column >= len(self.columns)):
            return None

        # get channel properties
        property = self.chan_data[row]
        # get property name from column description
        property_name = self.columns[column]['property']
        # get property value
        if property_name in ['input', 'enable', 'name', 'type']:
            d = str(property[property_name])
        else:
            d = None
        return d

    # pylint: disable=invalid-name
    def setData(self, index, value, role):
        """Abstract method from QAbstactTableModel to set cell data based on role
        """
        if index.isValid():
            if role == Qt.EditRole:
                if not self._setitem(index.row(), index.column(), value):
                    return False
                self.signals.dataSettingsChanged.emit(index)
                return True
            elif role == Qt.CheckStateRole:
                if not self._setitem(index.row(), index.column(), Qt.QVariant(value == Qt.Checked)):
                    return False
                return True
        return False
