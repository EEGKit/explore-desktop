# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window_redisign_menubar.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollBar,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

from pyqtgraph import (GraphicsLayoutWidget, PlotWidget)
from exploredesktop import app_resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1116, 691)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionCSV_data = QAction(MainWindow)
        self.actionCSV_data.setObjectName(u"actionCSV_data")
        self.actionEDF_data = QAction(MainWindow)
        self.actionEDF_data.setObjectName(u"actionEDF_data")
        self.actionBIN_data = QAction(MainWindow)
        self.actionBIN_data.setObjectName(u"actionBIN_data")
        self.actionMetadata_import = QAction(MainWindow)
        self.actionMetadata_import.setObjectName(u"actionMetadata_import")
        self.actionMetadata_export = QAction(MainWindow)
        self.actionMetadata_export.setObjectName(u"actionMetadata_export")
        self.actionConvert = QAction(MainWindow)
        self.actionConvert.setObjectName(u"actionConvert")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionLast_Session_Settings = QAction(MainWindow)
        self.actionLast_Session_Settings.setObjectName(u"actionLast_Session_Settings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(140, 0))
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"	border-top: 1px solid rgb(173, 173, 173)\n"
"}\n"
"\n"
"QWidget{\n"
"	font:11pt;\n"
"}\n"
"\n"
"QFrame{\n"
"	border:none;\n"
"}\n"
"\n"
"#main_header{\n"
"	border:none;\n"
"	border-bottom: 1px solid rgb(95, 197, 201);\n"
"}\n"
"\n"
"#main_header .QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"#main_footer{\n"
"	border:none;\n"
"	border-top: 1px solid rgb(95, 197, 201);\n"
"}\n"
"\n"
"/*#page_home .QPushButton{\n"
"	border:none\n"
"}\n"
"*/\n"
"#btn_bt_2{\n"
"	border:none\n"
"}\n"
"\n"
"#btn_settings_2{\n"
"	border:none\n"
"}\n"
"\n"
"#btn_plots_2{\n"
"	border:none\n"
"}\n"
"\n"
"\n"
"#btn_impedance_2{\n"
"	border:none\n"
"}\n"
"\n"
"#btn_integration_2{\n"
"	border:none\n"
"}\n"
"\n"
"\n"
"#value_heartRate{\n"
"	border: 1px solid\n"
"}\n"
"\n"
"#label_recording_time{\n"
"	border: 1px solid\n"
"}\n"
"\n"
"#list_devices{\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"\n"
"/*LEFT SIDE MENU*/\n"
"#left_side_menu {\n"
"	border:none;\n"
"	border-right: 1px solid rgb(95, 197, 201);\n"
"}\n"
"#toggle_left_"
                        "menu{\n"
"	border:none;\n"
"}\n"
"\n"
"#btns_left_menu{\n"
"	border:none;\n"
"}\n"
"\n"
"#left_side_menu .QPushButton{\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}\n"
"\n"
"\n"
"/*TITLES FONT*/\n"
"\n"
"QLabel#integration_title{\n"
"	font: 20pt;\n"
"}\n"
"\n"
"QLabel#home_title{\n"
"	font: 20pt;\n"
"}\n"
"\n"
"QLabel#impedance_title{\n"
"	font: 20pt;\n"
"}\n"
"\n"
"QLabel#settings_title{\n"
"	font: 20pt;\n"
"}\n"
"\n"
"QLabel#bt_title{\n"
"	font: 20pt;\n"
"}\n"
"QTabBar::tab{\n"
"	height: 25px}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setMinimumSize(QSize(0, 50))
        self.main_body.setStyleSheet(u"")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.main_body)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMinimumSize(QSize(60, 0))
        self.left_side_menu.setMaximumSize(QSize(60, 16777215))
        self.left_side_menu.setStyleSheet(u"")
        self.left_side_menu.setFrameShape(QFrame.StyledPanel)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.toggle_left_menu = QFrame(self.left_side_menu)
        self.toggle_left_menu.setObjectName(u"toggle_left_menu")
        self.toggle_left_menu.setStyleSheet(u"")
        self.toggle_left_menu.setFrameShape(QFrame.StyledPanel)
        self.toggle_left_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.toggle_left_menu)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.btn_left_menu_toggle = QPushButton(self.toggle_left_menu)
        self.btn_left_menu_toggle.setObjectName(u"btn_left_menu_toggle")
        self.btn_left_menu_toggle.setMinimumSize(QSize(0, 45))
        self.btn_left_menu_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_left_menu_toggle.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-hamburger-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_left_menu_toggle.setIcon(icon)

        self.horizontalLayout_67.addWidget(self.btn_left_menu_toggle)


        self.verticalLayout_29.addWidget(self.toggle_left_menu, 0, Qt.AlignTop)

        self.btns_left_menu = QFrame(self.left_side_menu)
        self.btns_left_menu.setObjectName(u"btns_left_menu")
        self.btns_left_menu.setStyleSheet(u"")
        self.btns_left_menu.setFrameShape(QFrame.StyledPanel)
        self.btns_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.btns_left_menu)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.btns_left_menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon1)

        self.verticalLayout_30.addWidget(self.btn_home)

        self.btn_bt = QPushButton(self.btns_left_menu)
        self.btn_bt.setObjectName(u"btn_bt")
        self.btn_bt.setMinimumSize(QSize(0, 45))
        self.btn_bt.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_bt.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-bluetooth.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_bt.setIcon(icon2)

        self.verticalLayout_30.addWidget(self.btn_bt)

        self.btn_settings = QPushButton(self.btns_left_menu)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(0, 45))
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon3)

        self.verticalLayout_30.addWidget(self.btn_settings)

        self.btn_plots = QPushButton(self.btns_left_menu)
        self.btn_plots.setObjectName(u"btn_plots")
        self.btn_plots.setMinimumSize(QSize(0, 45))
        self.btn_plots.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plots.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/cil-chart-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_plots.setIcon(icon4)

        self.verticalLayout_30.addWidget(self.btn_plots)

        self.btn_impedance = QPushButton(self.btns_left_menu)
        self.btn_impedance.setObjectName(u"btn_impedance")
        self.btn_impedance.setMinimumSize(QSize(0, 45))
        self.btn_impedance.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_impedance.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/cil-speedometer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_impedance.setIcon(icon5)

        self.verticalLayout_30.addWidget(self.btn_impedance)

        self.btn_integration = QPushButton(self.btns_left_menu)
        self.btn_integration.setObjectName(u"btn_integration")
        self.btn_integration.setMinimumSize(QSize(0, 45))
        self.btn_integration.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_integration.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/cil-share-boxed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_integration.setIcon(icon6)

        self.verticalLayout_30.addWidget(self.btn_integration)


        self.verticalLayout_29.addWidget(self.btns_left_menu, 0, Qt.AlignTop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.left_side_menu)

        self.center_main_items = QFrame(self.main_body)
        self.center_main_items.setObjectName(u"center_main_items")
        self.center_main_items.setStyleSheet(u"")
        self.center_main_items.setFrameShape(QFrame.WinPanel)
        self.center_main_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.center_main_items)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.center_main_items)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet(u"f")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_7 = QVBoxLayout(self.page_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)

        self.frame_home_title = QFrame(self.page_home)
        self.frame_home_title.setObjectName(u"frame_home_title")
        self.frame_home_title.setMaximumSize(QSize(16777215, 50))
        self.frame_home_title.setStyleSheet(u"")
        self.frame_home_title.setFrameShape(QFrame.StyledPanel)
        self.frame_home_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_home_title)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.home_title = QLabel(self.frame_home_title)
        self.home_title.setObjectName(u"home_title")
        self.home_title.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.home_title.setFont(font)
        self.home_title.setStyleSheet(u"")
        self.home_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.home_title)


        self.verticalLayout_7.addWidget(self.frame_home_title)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setStyleSheet(u"")
        self.label.setMargin(15)

        self.verticalLayout_7.addWidget(self.label)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_bt_2 = QPushButton(self.page_home)
        self.btn_bt_2.setObjectName(u"btn_bt_2")
        self.btn_bt_2.setEnabled(False)
        self.btn_bt_2.setMinimumSize(QSize(0, 45))
        self.btn_bt_2.setMaximumSize(QSize(60, 16777215))
        self.btn_bt_2.setCursor(QCursor(Qt.ArrowCursor))
        self.btn_bt_2.setStyleSheet(u"")
        self.btn_bt_2.setIcon(icon2)
        self.btn_bt_2.setFlat(False)

        self.horizontalLayout_12.addWidget(self.btn_bt_2)

        self.label_18 = QLabel(self.page_home)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_12.addWidget(self.label_18)


        self.verticalLayout_18.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_settings_2 = QPushButton(self.page_home)
        self.btn_settings_2.setObjectName(u"btn_settings_2")
        self.btn_settings_2.setEnabled(False)
        self.btn_settings_2.setMinimumSize(QSize(0, 45))
        self.btn_settings_2.setMaximumSize(QSize(60, 16777215))
        self.btn_settings_2.setCursor(QCursor(Qt.ArrowCursor))
        self.btn_settings_2.setStyleSheet(u"")
        self.btn_settings_2.setIcon(icon3)
        self.btn_settings_2.setFlat(False)

        self.horizontalLayout_15.addWidget(self.btn_settings_2)

        self.label_17 = QLabel(self.page_home)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_15.addWidget(self.label_17)


        self.verticalLayout_18.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.btn_plots_2 = QPushButton(self.page_home)
        self.btn_plots_2.setObjectName(u"btn_plots_2")
        self.btn_plots_2.setEnabled(False)
        self.btn_plots_2.setMinimumSize(QSize(60, 45))
        self.btn_plots_2.setMaximumSize(QSize(60, 16777215))
        self.btn_plots_2.setCursor(QCursor(Qt.ArrowCursor))
        self.btn_plots_2.setStyleSheet(u"")
        self.btn_plots_2.setIcon(icon4)
        self.btn_plots_2.setFlat(False)

        self.horizontalLayout_41.addWidget(self.btn_plots_2)

        self.label_14 = QLabel(self.page_home)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_41.addWidget(self.label_14)


        self.verticalLayout_18.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.btn_impedance_2 = QPushButton(self.page_home)
        self.btn_impedance_2.setObjectName(u"btn_impedance_2")
        self.btn_impedance_2.setEnabled(False)
        self.btn_impedance_2.setMinimumSize(QSize(0, 45))
        self.btn_impedance_2.setMaximumSize(QSize(60, 16777215))
        self.btn_impedance_2.setCursor(QCursor(Qt.ArrowCursor))
        self.btn_impedance_2.setStyleSheet(u"")
        self.btn_impedance_2.setIcon(icon5)
        self.btn_impedance_2.setFlat(False)

        self.horizontalLayout_42.addWidget(self.btn_impedance_2)

        self.label_9 = QLabel(self.page_home)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_42.addWidget(self.label_9)


        self.verticalLayout_18.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_integration_2 = QPushButton(self.page_home)
        self.btn_integration_2.setObjectName(u"btn_integration_2")
        self.btn_integration_2.setEnabled(False)
        self.btn_integration_2.setMinimumSize(QSize(0, 45))
        self.btn_integration_2.setMaximumSize(QSize(60, 16777215))
        self.btn_integration_2.setCursor(QCursor(Qt.ArrowCursor))
        self.btn_integration_2.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/cil-share-boxed.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icons/icons/cil-share-boxed.png", QSize(), QIcon.Disabled, QIcon.On)
        self.btn_integration_2.setIcon(icon7)
        self.btn_integration_2.setFlat(False)

        self.horizontalLayout_10.addWidget(self.btn_integration_2)

        self.label_8 = QLabel(self.page_home)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8, 0, Qt.AlignVCenter)


        self.verticalLayout_18.addLayout(self.horizontalLayout_10)


        self.verticalLayout_7.addLayout(self.verticalLayout_18)

        self.label_4 = QLabel(self.page_home)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setStyleSheet(u"")
        self.label_4.setMargin(15)

        self.verticalLayout_7.addWidget(self.label_4)

        self.cb_permission = QCheckBox(self.page_home)
        self.cb_permission.setObjectName(u"cb_permission")
        self.cb_permission.setChecked(True)

        self.verticalLayout_7.addWidget(self.cb_permission)

        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setStyleSheet(u"")
        self.label_6.setMargin(15)

        self.verticalLayout_7.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.le_import_edf = QLineEdit(self.page_home)
        self.le_import_edf.setObjectName(u"le_import_edf")

        self.horizontalLayout_8.addWidget(self.le_import_edf)

        self.horizontalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_14)

        self.btn_import_edf = QPushButton(self.page_home)
        self.btn_import_edf.setObjectName(u"btn_import_edf")
        self.btn_import_edf.setMinimumSize(QSize(100, 35))
        self.btn_import_edf.setMaximumSize(QSize(100, 30))
        self.btn_import_edf.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.btn_import_edf)

        self.horizontalSpacer_15 = QSpacerItem(59, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_15)

        self.btn_generate_bdf = QPushButton(self.page_home)
        self.btn_generate_bdf.setObjectName(u"btn_generate_bdf")
        self.btn_generate_bdf.setMinimumSize(QSize(100, 35))

        self.horizontalLayout_8.addWidget(self.btn_generate_bdf)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_16)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.page_home)
        self.page_integration = QWidget()
        self.page_integration.setObjectName(u"page_integration")
        self.verticalLayout_12 = QVBoxLayout(self.page_integration)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_12.addItem(self.verticalSpacer_8)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_9)

        self.frame_integration_title = QFrame(self.page_integration)
        self.frame_integration_title.setObjectName(u"frame_integration_title")
        self.frame_integration_title.setMaximumSize(QSize(16777215, 50))
        self.frame_integration_title.setStyleSheet(u"")
        self.frame_integration_title.setFrameShape(QFrame.StyledPanel)
        self.frame_integration_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_integration_title)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.integration_title = QLabel(self.frame_integration_title)
        self.integration_title.setObjectName(u"integration_title")
        self.integration_title.setMinimumSize(QSize(0, 0))
        self.integration_title.setFont(font)
        self.integration_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.integration_title)


        self.verticalLayout_12.addWidget(self.frame_integration_title)

        self.frame_integration = QFrame(self.page_integration)
        self.frame_integration.setObjectName(u"frame_integration")
        self.frame_integration.setStyleSheet(u"")
        self.frame_integration.setFrameShape(QFrame.StyledPanel)
        self.frame_integration.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_integration)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_36.addItem(self.verticalSpacer_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_integration)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        self.label_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_11 = QLabel(self.frame_integration)
        self.label_11.setObjectName(u"label_11")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_11.setFont(font2)
        self.label_11.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_11)

        self.empty_frame_5 = QFrame(self.frame_integration)
        self.empty_frame_5.setObjectName(u"empty_frame_5")
        self.empty_frame_5.setFrameShape(QFrame.StyledPanel)
        self.empty_frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.empty_frame_5)

        self.cb_lsl_duration = QCheckBox(self.frame_integration)
        self.cb_lsl_duration.setObjectName(u"cb_lsl_duration")

        self.verticalLayout_3.addWidget(self.cb_lsl_duration)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_lsl_duration = QLabel(self.frame_integration)
        self.label_lsl_duration.setObjectName(u"label_lsl_duration")
        self.label_lsl_duration.setEnabled(False)

        self.horizontalLayout_13.addWidget(self.label_lsl_duration)

        self.lsl_duration_value = QSpinBox(self.frame_integration)
        self.lsl_duration_value.setObjectName(u"lsl_duration_value")
        self.lsl_duration_value.setEnabled(False)
        self.lsl_duration_value.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_13.addWidget(self.lsl_duration_value)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.btn_push_lsl = QPushButton(self.frame_integration)
        self.btn_push_lsl.setObjectName(u"btn_push_lsl")
        self.btn_push_lsl.setMinimumSize(QSize(100, 35))
        self.btn_push_lsl.setMaximumSize(QSize(100, 30))
        self.btn_push_lsl.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_push_lsl, 0, Qt.AlignHCenter)


        self.verticalLayout_36.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 300, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_36.addItem(self.verticalSpacer)


        self.verticalLayout_12.addWidget(self.frame_integration)

        self.stackedWidget.addWidget(self.page_integration)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.page_settings.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.page_settings)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_10)

        self.frame_settings_title = QFrame(self.page_settings)
        self.frame_settings_title.setObjectName(u"frame_settings_title")
        self.frame_settings_title.setMaximumSize(QSize(16777215, 50))
        self.frame_settings_title.setStyleSheet(u"")
        self.frame_settings_title.setFrameShape(QFrame.StyledPanel)
        self.frame_settings_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_settings_title)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.settings_title = QLabel(self.frame_settings_title)
        self.settings_title.setObjectName(u"settings_title")
        self.settings_title.setMinimumSize(QSize(0, 0))
        self.settings_title.setSizeIncrement(QSize(0, 0))
        self.settings_title.setFont(font)
        self.settings_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.settings_title)


        self.verticalLayout_8.addWidget(self.frame_settings_title)

        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_11)

        self.frame_settings = QFrame(self.page_settings)
        self.frame_settings.setObjectName(u"frame_settings")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_settings.sizePolicy().hasHeightForWidth())
        self.frame_settings.setSizePolicy(sizePolicy1)
        self.frame_settings.setStyleSheet(u"")
        self.frame_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_settings.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_device = QFrame(self.frame_settings)
        self.frame_device.setObjectName(u"frame_device")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_device.sizePolicy().hasHeightForWidth())
        self.frame_device.setSizePolicy(sizePolicy2)
        self.frame_device.setMinimumSize(QSize(0, 0))
        self.frame_device.setMaximumSize(QSize(650, 16777215))
        self.frame_device.setStyleSheet(u"")
        self.frame_device.setFrameShape(QFrame.StyledPanel)
        self.frame_device.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_device)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(60, -1, 60, -1)
        self.label_explore_name = QLabel(self.frame_device)
        self.label_explore_name.setObjectName(u"label_explore_name")
        sizePolicy.setHeightForWidth(self.label_explore_name.sizePolicy().hasHeightForWidth())
        self.label_explore_name.setSizePolicy(sizePolicy)
        self.label_explore_name.setMinimumSize(QSize(0, 0))
        self.label_explore_name.setMaximumSize(QSize(16777215, 75))
        self.label_explore_name.setStyleSheet(u"")
        self.label_explore_name.setAlignment(Qt.AlignCenter)
        self.label_explore_name.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_explore_name)

        self.label_warning_disabled = QLabel(self.frame_device)
        self.label_warning_disabled.setObjectName(u"label_warning_disabled")
        self.label_warning_disabled.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_warning_disabled)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_20)

        self.table_settings = QTableView(self.frame_device)
        self.table_settings.setObjectName(u"table_settings")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.table_settings.sizePolicy().hasHeightForWidth())
        self.table_settings.setSizePolicy(sizePolicy3)
        self.table_settings.setStyleSheet(u"")
        self.table_settings.setAlternatingRowColors(True)
        self.table_settings.setCornerButtonEnabled(False)
        self.table_settings.horizontalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_2.addWidget(self.table_settings)

        self.spacer_frame = QFrame(self.frame_device)
        self.spacer_frame.setObjectName(u"spacer_frame")
        self.spacer_frame.setMinimumSize(QSize(0, 30))
        self.spacer_frame.setFrameShape(QFrame.StyledPanel)
        self.spacer_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.spacer_frame)

        self.frame_samplingrate = QFrame(self.frame_device)
        self.frame_samplingrate.setObjectName(u"frame_samplingrate")
        self.frame_samplingrate.setStyleSheet(u"")
        self.frame_samplingrate.setFrameShape(QFrame.StyledPanel)
        self.frame_samplingrate.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_samplingrate)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_samping_rate = QLabel(self.frame_samplingrate)
        self.label_samping_rate.setObjectName(u"label_samping_rate")
        self.label_samping_rate.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.label_samping_rate)

        self.value_sampling_rate = QComboBox(self.frame_samplingrate)
        self.value_sampling_rate.setObjectName(u"value_sampling_rate")
        self.value_sampling_rate.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.value_sampling_rate)


        self.verticalLayout_2.addWidget(self.frame_samplingrate)

        self.lbl_sr_warning = QLabel(self.frame_device)
        self.lbl_sr_warning.setObjectName(u"lbl_sr_warning")
        sizePolicy.setHeightForWidth(self.lbl_sr_warning.sizePolicy().hasHeightForWidth())
        self.lbl_sr_warning.setSizePolicy(sizePolicy)
        self.lbl_sr_warning.setMaximumSize(QSize(16777215, 100))
        self.lbl_sr_warning.setStyleSheet(u"color: red;\n"
"font: 11pt;")
        self.lbl_sr_warning.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lbl_sr_warning)

        self.btn_apply_settings = QPushButton(self.frame_device)
        self.btn_apply_settings.setObjectName(u"btn_apply_settings")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_apply_settings.sizePolicy().hasHeightForWidth())
        self.btn_apply_settings.setSizePolicy(sizePolicy4)
        self.btn_apply_settings.setMinimumSize(QSize(160, 35))
        self.btn_apply_settings.setMaximumSize(QSize(160, 30))
        self.btn_apply_settings.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btn_apply_settings, 0, Qt.AlignHCenter)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_16)

        self.frame_device_buttons = QFrame(self.frame_device)
        self.frame_device_buttons.setObjectName(u"frame_device_buttons")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(35)
        sizePolicy5.setHeightForWidth(self.frame_device_buttons.sizePolicy().hasHeightForWidth())
        self.frame_device_buttons.setSizePolicy(sizePolicy5)
        self.frame_device_buttons.setStyleSheet(u"")
        self.frame_device_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_device_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_device_buttons)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_format_memory = QPushButton(self.frame_device_buttons)
        self.btn_format_memory.setObjectName(u"btn_format_memory")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_format_memory.sizePolicy().hasHeightForWidth())
        self.btn_format_memory.setSizePolicy(sizePolicy6)
        self.btn_format_memory.setMinimumSize(QSize(160, 35))
        self.btn_format_memory.setMaximumSize(QSize(160, 30))
        self.btn_format_memory.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_format_memory)

        self.btn_reset_settings = QPushButton(self.frame_device_buttons)
        self.btn_reset_settings.setObjectName(u"btn_reset_settings")
        sizePolicy6.setHeightForWidth(self.btn_reset_settings.sizePolicy().hasHeightForWidth())
        self.btn_reset_settings.setSizePolicy(sizePolicy6)
        self.btn_reset_settings.setMinimumSize(QSize(160, 35))
        self.btn_reset_settings.setMaximumSize(QSize(160, 30))
        self.btn_reset_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reset_settings.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.btn_reset_settings)

        self.btn_calibrate = QPushButton(self.frame_device_buttons)
        self.btn_calibrate.setObjectName(u"btn_calibrate")
        sizePolicy6.setHeightForWidth(self.btn_calibrate.sizePolicy().hasHeightForWidth())
        self.btn_calibrate.setSizePolicy(sizePolicy6)
        self.btn_calibrate.setMinimumSize(QSize(160, 35))
        self.btn_calibrate.setMaximumSize(QSize(160, 30))
        self.btn_calibrate.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_calibrate)


        self.verticalLayout_2.addWidget(self.frame_device_buttons)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_19)


        self.gridLayout.addWidget(self.frame_device, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_settings)

        self.stackedWidget.addWidget(self.page_settings)
        self.page_plotsNoWidget = QWidget()
        self.page_plotsNoWidget.setObjectName(u"page_plotsNoWidget")
        self.page_plotsNoWidget.setStyleSheet(u"")
        self.verticalLayout_21 = QVBoxLayout(self.page_plotsNoWidget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.btn_record = QPushButton(self.page_plotsNoWidget)
        self.btn_record.setObjectName(u"btn_record")
        self.btn_record.setMinimumSize(QSize(100, 30))
        self.btn_record.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/cil-media-record.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_record.setIcon(icon8)
        self.btn_record.setIconSize(QSize(18, 18))

        self.horizontalLayout_33.addWidget(self.btn_record)

        self.label_recording_time = QLabel(self.page_plotsNoWidget)
        self.label_recording_time.setObjectName(u"label_recording_time")
        self.label_recording_time.setMinimumSize(QSize(100, 0))
        self.label_recording_time.setMaximumSize(QSize(150, 30))
        self.label_recording_time.setStyleSheet(u"")
        self.label_recording_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_recording_time)


        self.horizontalLayout_32.addLayout(self.horizontalLayout_33)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_12)

        self.label_yAxis = QLabel(self.page_plotsNoWidget)
        self.label_yAxis.setObjectName(u"label_yAxis")
        self.label_yAxis.setFont(font2)
        self.label_yAxis.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.label_yAxis)

        self.value_yAxis = QComboBox(self.page_plotsNoWidget)
        self.value_yAxis.setObjectName(u"value_yAxis")
        self.value_yAxis.setMinimumSize(QSize(85, 0))
        self.value_yAxis.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_32.addWidget(self.value_yAxis)

        self.label_timeScale = QLabel(self.page_plotsNoWidget)
        self.label_timeScale.setObjectName(u"label_timeScale")
        self.label_timeScale.setFont(font2)
        self.label_timeScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.label_timeScale)

        self.value_timeScale = QComboBox(self.page_plotsNoWidget)
        self.value_timeScale.setObjectName(u"value_timeScale")
        self.value_timeScale.setMinimumSize(QSize(85, 0))
        self.value_timeScale.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_32.addWidget(self.value_timeScale)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.value_event_code = QLineEdit(self.page_plotsNoWidget)
        self.value_event_code.setObjectName(u"value_event_code")
        self.value_event_code.setMaximumSize(QSize(85, 30))
        self.value_event_code.setFont(font2)
        self.value_event_code.setStyleSheet(u"font: 11pt ")

        self.horizontalLayout_34.addWidget(self.value_event_code)

        self.btn_marker = QPushButton(self.page_plotsNoWidget)
        self.btn_marker.setObjectName(u"btn_marker")
        self.btn_marker.setMinimumSize(QSize(80, 30))
        self.btn_marker.setMaximumSize(QSize(80, 16777215))
        self.btn_marker.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_marker.setStyleSheet(u"")

        self.horizontalLayout_34.addWidget(self.btn_marker)


        self.horizontalLayout_32.addLayout(self.horizontalLayout_34)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_6)

        self.btn_plot_filters = QPushButton(self.page_plotsNoWidget)
        self.btn_plot_filters.setObjectName(u"btn_plot_filters")
        self.btn_plot_filters.setMinimumSize(QSize(100, 30))
        self.btn_plot_filters.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/cil-options.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_plot_filters.setIcon(icon9)
        self.btn_plot_filters.setIconSize(QSize(16, 12))

        self.horizontalLayout_32.addWidget(self.btn_plot_filters)


        self.verticalLayout_21.addLayout(self.horizontalLayout_32)

        self.tabWidget = QTabWidget(self.page_plotsNoWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.exg = QWidget()
        self.exg.setObjectName(u"exg")
        self.horizontalLayout_21 = QHBoxLayout(self.exg)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.plot_exg = PlotWidget(self.exg)
        self.plot_exg.setObjectName(u"plot_exg")

        self.horizontalLayout_21.addWidget(self.plot_exg)

        self.verticalScrollBar = QScrollBar(self.exg)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.horizontalLayout_21.addWidget(self.verticalScrollBar)

        self.tabWidget.addTab(self.exg, "")
        self.orn = QWidget()
        self.orn.setObjectName(u"orn")
        self.horizontalLayout_22 = QHBoxLayout(self.orn)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.plot_orn = GraphicsLayoutWidget(self.orn)
        self.plot_orn.setObjectName(u"plot_orn")

        self.horizontalLayout_22.addWidget(self.plot_orn)

        self.tabWidget.addTab(self.orn, "")
        self.fft = QWidget()
        self.fft.setObjectName(u"fft")
        self.horizontalLayout_23 = QHBoxLayout(self.fft)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.plot_fft = PlotWidget(self.fft)
        self.plot_fft.setObjectName(u"plot_fft")

        self.horizontalLayout_23.addWidget(self.plot_fft)

        self.tabWidget.addTab(self.fft, "")

        self.verticalLayout_21.addWidget(self.tabWidget)

        self.label_7 = QLabel(self.page_plotsNoWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7.setOpenExternalLinks(True)

        self.verticalLayout_21.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.page_plotsNoWidget)
        self.page_plotsRecorded = QWidget()
        self.page_plotsRecorded.setObjectName(u"page_plotsRecorded")
        self.page_plotsRecorded.setStyleSheet(u"")
        self.verticalLayout_25 = QVBoxLayout(self.page_plotsRecorded)
        self.verticalLayout_25.setSpacing(6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_signal_rec = QLabel(self.page_plotsRecorded)
        self.label_signal_rec.setObjectName(u"label_signal_rec")
        self.label_signal_rec.setFont(font2)
        self.label_signal_rec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_signal_rec)

        self.value_signal_rec = QComboBox(self.page_plotsRecorded)
        self.value_signal_rec.setObjectName(u"value_signal_rec")
        self.value_signal_rec.setMinimumSize(QSize(85, 0))
        self.value_signal_rec.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_36.addWidget(self.value_signal_rec)

        self.label_yAxis_rec = QLabel(self.page_plotsRecorded)
        self.label_yAxis_rec.setObjectName(u"label_yAxis_rec")
        self.label_yAxis_rec.setFont(font2)
        self.label_yAxis_rec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_yAxis_rec)

        self.value_yAxis_rec = QComboBox(self.page_plotsRecorded)
        self.value_yAxis_rec.setObjectName(u"value_yAxis_rec")
        self.value_yAxis_rec.setMinimumSize(QSize(85, 0))
        self.value_yAxis_rec.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_36.addWidget(self.value_yAxis_rec)

        self.label_timeScale_rec = QLabel(self.page_plotsRecorded)
        self.label_timeScale_rec.setObjectName(u"label_timeScale_rec")
        self.label_timeScale_rec.setFont(font2)
        self.label_timeScale_rec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_timeScale_rec)

        self.value_timeScale_rec = QComboBox(self.page_plotsRecorded)
        self.value_timeScale_rec.setObjectName(u"value_timeScale_rec")
        self.value_timeScale_rec.setMinimumSize(QSize(85, 0))
        self.value_timeScale_rec.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_36.addWidget(self.value_timeScale_rec)

        self.label_heartRate_rec = QLabel(self.page_plotsRecorded)
        self.label_heartRate_rec.setObjectName(u"label_heartRate_rec")
        self.label_heartRate_rec.setFont(font2)
        self.label_heartRate_rec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_heartRate_rec)

        self.value_heartRate_rec = QLabel(self.page_plotsRecorded)
        self.value_heartRate_rec.setObjectName(u"value_heartRate_rec")
        self.value_heartRate_rec.setMaximumSize(QSize(16777215, 25))
        self.value_heartRate_rec.setStyleSheet(u"")
        self.value_heartRate_rec.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.value_heartRate_rec)

        self.btn_stream_rec = QPushButton(self.page_plotsRecorded)
        self.btn_stream_rec.setObjectName(u"btn_stream_rec")
        self.btn_stream_rec.setMinimumSize(QSize(150, 30))
        self.btn_stream_rec.setMaximumSize(QSize(16777215, 16777215))
        self.btn_stream_rec.setFont(font2)
        self.btn_stream_rec.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stream_rec.setStyleSheet(u"")

        self.horizontalLayout_36.addWidget(self.btn_stream_rec)


        self.verticalLayout_25.addLayout(self.horizontalLayout_36)

        self.cb_swipping_rec = QCheckBox(self.page_plotsRecorded)
        self.cb_swipping_rec.setObjectName(u"cb_swipping_rec")

        self.verticalLayout_25.addWidget(self.cb_swipping_rec)

        self.tabWidget_rec = QTabWidget(self.page_plotsRecorded)
        self.tabWidget_rec.setObjectName(u"tabWidget_rec")
        self.tabWidget_rec.setStyleSheet(u"")
        self.exg_rec = QWidget()
        self.exg_rec.setObjectName(u"exg_rec")
        self.horizontalLayout_24 = QHBoxLayout(self.exg_rec)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.plot_exg_rec = GraphicsLayoutWidget(self.exg_rec)
        self.plot_exg_rec.setObjectName(u"plot_exg_rec")

        self.horizontalLayout_24.addWidget(self.plot_exg_rec)

        self.tabWidget_rec.addTab(self.exg_rec, "")
        self.orn_rec = QWidget()
        self.orn_rec.setObjectName(u"orn_rec")
        self.horizontalLayout_30 = QHBoxLayout(self.orn_rec)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.plot_orn_rec = GraphicsLayoutWidget(self.orn_rec)
        self.plot_orn_rec.setObjectName(u"plot_orn_rec")

        self.horizontalLayout_30.addWidget(self.plot_orn_rec)

        self.tabWidget_rec.addTab(self.orn_rec, "")
        self.fft_rec = QWidget()
        self.fft_rec.setObjectName(u"fft_rec")
        self.horizontalLayout_40 = QHBoxLayout(self.fft_rec)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.plot_fft_rec = PlotWidget(self.fft_rec)
        self.plot_fft_rec.setObjectName(u"plot_fft_rec")

        self.horizontalLayout_40.addWidget(self.plot_fft_rec)

        self.tabWidget_rec.addTab(self.fft_rec, "")

        self.verticalLayout_25.addWidget(self.tabWidget_rec)

        self.label_3 = QLabel(self.page_plotsRecorded)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3.setOpenExternalLinks(True)

        self.verticalLayout_25.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page_plotsRecorded)
        self.page_impedance = QWidget()
        self.page_impedance.setObjectName(u"page_impedance")
        self.page_impedance.setStyleSheet(u"QFrame[accessibleName=\"color_frame\"] {\n"
"border: 2px solid rgb(145, 145, 145);\n"
"border-radius: 30px;\n"
"background-color: rgb(169, 169, 169)\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.page_impedance)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacer_13)

        self.frame_impedance_title = QFrame(self.page_impedance)
        self.frame_impedance_title.setObjectName(u"frame_impedance_title")
        self.frame_impedance_title.setMaximumSize(QSize(16777215, 50))
        self.frame_impedance_title.setStyleSheet(u"")
        self.frame_impedance_title.setFrameShape(QFrame.StyledPanel)
        self.frame_impedance_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_impedance_title)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.impedance_title = QLabel(self.frame_impedance_title)
        self.impedance_title.setObjectName(u"impedance_title")
        self.impedance_title.setMinimumSize(QSize(0, 0))
        self.impedance_title.setFont(font)
        self.impedance_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.impedance_title)


        self.verticalLayout_16.addWidget(self.frame_impedance_title)

        self.verticalSpacer_12 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_16.addItem(self.verticalSpacer_12)

        self.imp_graph_layout = GraphicsLayoutWidget(self.page_impedance)
        self.imp_graph_layout.setObjectName(u"imp_graph_layout")

        self.verticalLayout_16.addWidget(self.imp_graph_layout)

        self.verticalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_16.addItem(self.verticalSpacer_15)

        self.imp_mode = QComboBox(self.page_impedance)
        self.imp_mode.setObjectName(u"imp_mode")
        self.imp_mode.setMinimumSize(QSize(200, 0))
        self.imp_mode.setMaximumSize(QSize(200, 16777215))
        self.imp_mode.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.imp_mode, 0, Qt.AlignHCenter)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.btn_imp_meas = QPushButton(self.page_impedance)
        self.btn_imp_meas.setObjectName(u"btn_imp_meas")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_imp_meas.sizePolicy().hasHeightForWidth())
        self.btn_imp_meas.setSizePolicy(sizePolicy7)
        self.btn_imp_meas.setMinimumSize(QSize(160, 35))
        self.btn_imp_meas.setMaximumSize(QSize(200, 16777215))
        self.btn_imp_meas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_imp_meas.setToolTipDuration(-1)

        self.horizontalLayout_11.addWidget(self.btn_imp_meas, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.imp_meas_info = QPushButton(self.page_impedance)
        self.imp_meas_info.setObjectName(u"imp_meas_info")
        self.imp_meas_info.setMaximumSize(QSize(20, 20))
        self.imp_meas_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.imp_meas_info.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"color: #FFF;")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/pngfind.com-png-circle-1194554.png", QSize(), QIcon.Normal, QIcon.Off)
        self.imp_meas_info.setIcon(icon10)
        self.imp_meas_info.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.imp_meas_info, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)


        self.verticalLayout_16.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_17 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_16.addItem(self.verticalSpacer_17)

        self.stackedWidget.addWidget(self.page_impedance)
        self.page_bt = QWidget()
        self.page_bt.setObjectName(u"page_bt")
        self.page_bt.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.page_bt)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_14)

        self.frame_bt_title = QFrame(self.page_bt)
        self.frame_bt_title.setObjectName(u"frame_bt_title")
        self.frame_bt_title.setMaximumSize(QSize(16777215, 50))
        self.frame_bt_title.setStyleSheet(u"")
        self.frame_bt_title.setFrameShape(QFrame.StyledPanel)
        self.frame_bt_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_bt_title)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.bt_title = QLabel(self.frame_bt_title)
        self.bt_title.setObjectName(u"bt_title")
        self.bt_title.setMinimumSize(QSize(0, 0))
        self.bt_title.setFont(font)
        self.bt_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.bt_title)


        self.verticalLayout_17.addWidget(self.frame_bt_title)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(250, -1, 250, -1)
        self.label_10 = QLabel(self.page_bt)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"")
        self.label_10.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_10)

        self.lbl_wdws_warning = QLabel(self.page_bt)
        self.lbl_wdws_warning.setObjectName(u"lbl_wdws_warning")
        self.lbl_wdws_warning.setStyleSheet(u"color: red;")
        self.lbl_wdws_warning.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.lbl_wdws_warning, 0, Qt.AlignHCenter)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.list_devices = QListWidget(self.page_bt)
        self.list_devices.setObjectName(u"list_devices")
        self.list_devices.setMaximumSize(QSize(300, 200))
        self.list_devices.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.list_devices.setStyleSheet(u"")
        self.list_devices.setWordWrap(True)

        self.horizontalLayout_9.addWidget(self.list_devices)

        self.frame_btns_scan_connect = QFrame(self.page_bt)
        self.frame_btns_scan_connect.setObjectName(u"frame_btns_scan_connect")
        self.frame_btns_scan_connect.setMaximumSize(QSize(150, 100))
        self.frame_btns_scan_connect.setStyleSheet(u"")
        self.frame_btns_scan_connect.setFrameShape(QFrame.StyledPanel)
        self.frame_btns_scan_connect.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_btns_scan_connect)
        self.verticalLayout_38.setSpacing(10)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.btn_scan = QPushButton(self.frame_btns_scan_connect)
        self.btn_scan.setObjectName(u"btn_scan")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.btn_scan.sizePolicy().hasHeightForWidth())
        self.btn_scan.setSizePolicy(sizePolicy8)
        self.btn_scan.setMinimumSize(QSize(140, 35))
        self.btn_scan.setMaximumSize(QSize(140, 30))
        self.btn_scan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_scan.setStyleSheet(u"")
        self.btn_scan.setFlat(False)

        self.verticalLayout_38.addWidget(self.btn_scan)

        self.btn_connect = QPushButton(self.frame_btns_scan_connect)
        self.btn_connect.setObjectName(u"btn_connect")
        sizePolicy.setHeightForWidth(self.btn_connect.sizePolicy().hasHeightForWidth())
        self.btn_connect.setSizePolicy(sizePolicy)
        self.btn_connect.setMinimumSize(QSize(140, 35))
        self.btn_connect.setMaximumSize(QSize(140, 30))
        self.btn_connect.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_38.addWidget(self.btn_connect)


        self.horizontalLayout_9.addWidget(self.frame_btns_scan_connect)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.frame_8 = QFrame(self.page_bt)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy4.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy4)
        self.frame_8.setMinimumSize(QSize(500, 30))
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 50, 0)
        self.label_15 = QLabel(self.frame_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.label_15)

        self.dev_name_input = QLineEdit(self.frame_8)
        self.dev_name_input.setObjectName(u"dev_name_input")
        self.dev_name_input.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.dev_name_input)


        self.verticalLayout_6.addWidget(self.frame_8, 0, Qt.AlignHCenter)

        self.verticalSpacer_18 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_18)


        self.verticalLayout_17.addLayout(self.verticalLayout_6)

        self.stackedWidget.addWidget(self.page_bt)
        self.page__testing = QWidget()
        self.page__testing.setObjectName(u"page__testing")
        self.label_5 = QLabel(self.page__testing)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 30, 701, 51))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color:#fff")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.table_settings_3 = QTableView(self.page__testing)
        self.table_settings_3.setObjectName(u"table_settings_3")
        self.table_settings_3.setGeometry(QRect(115, 181, 441, 281))
        self.table_settings_3.setStyleSheet(u"border: 1px solid rgb(0,0,0)")
        self.cb_1020_3 = QCheckBox(self.page__testing)
        self.cb_1020_3.setObjectName(u"cb_1020_3")
        self.cb_1020_3.setGeometry(QRect(130, 110, 131, 22))
        self.btn_apply_settings_2 = QPushButton(self.page__testing)
        self.btn_apply_settings_2.setObjectName(u"btn_apply_settings_2")
        self.btn_apply_settings_2.setGeometry(QRect(680, 270, 80, 24))
        self.layoutWidget = QWidget(self.page__testing)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 150, 229, 32))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cb_multitype_signal_3 = QCheckBox(self.layoutWidget)
        self.cb_multitype_signal_3.setObjectName(u"cb_multitype_signal_3")

        self.horizontalLayout_2.addWidget(self.cb_multitype_signal_3)

        self.dropdown_signal_type_3 = QComboBox(self.layoutWidget)
        self.dropdown_signal_type_3.setObjectName(u"dropdown_signal_type_3")

        self.horizontalLayout_2.addWidget(self.dropdown_signal_type_3)

        self.stackedWidget.addWidget(self.page__testing)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        self.main_footer = QFrame(self.center_main_items)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMinimumSize(QSize(0, 30))
        self.main_footer.setMaximumSize(QSize(16777215, 40))
        self.main_footer.setStyleSheet(u"")
        self.main_footer.setFrameShape(QFrame.StyledPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.main_footer)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(10, 6, 0, 6)
        self.ft_label_device_3 = QLabel(self.main_footer)
        self.ft_label_device_3.setObjectName(u"ft_label_device_3")
        self.ft_label_device_3.setFont(font2)
        self.ft_label_device_3.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.ft_label_device_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)

        self.ft_label_firmware = QLabel(self.main_footer)
        self.ft_label_firmware.setObjectName(u"ft_label_firmware")

        self.horizontalLayout_14.addWidget(self.ft_label_firmware)

        self.ft_label_firmware_value = QLabel(self.main_footer)
        self.ft_label_firmware_value.setObjectName(u"ft_label_firmware_value")

        self.horizontalLayout_14.addWidget(self.ft_label_firmware_value, 0, Qt.AlignLeft)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")

        self.horizontalLayout_14.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(6)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.ft_label_battery = QLabel(self.main_footer)
        self.ft_label_battery.setObjectName(u"ft_label_battery")
        self.ft_label_battery.setStyleSheet(u"")

        self.horizontalLayout_26.addWidget(self.ft_label_battery, 0, Qt.AlignHCenter)

        self.ft_label_battery_value = QLabel(self.main_footer)
        self.ft_label_battery_value.setObjectName(u"ft_label_battery_value")
        self.ft_label_battery_value.setStyleSheet(u"")

        self.horizontalLayout_26.addWidget(self.ft_label_battery_value)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_26)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.ft_label_temp = QLabel(self.main_footer)
        self.ft_label_temp.setObjectName(u"ft_label_temp")
        self.ft_label_temp.setMaximumSize(QSize(10000, 100000))
        self.ft_label_temp.setStyleSheet(u"")
        self.ft_label_temp.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.ft_label_temp)

        self.ft_label_temp_value = QLabel(self.main_footer)
        self.ft_label_temp_value.setObjectName(u"ft_label_temp_value")

        self.horizontalLayout_27.addWidget(self.ft_label_temp_value)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_27)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_4)

        self.ft_label_version = QLabel(self.main_footer)
        self.ft_label_version.setObjectName(u"ft_label_version")
        self.ft_label_version.setStyleSheet(u"")
        self.ft_label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.ft_label_version)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addWidget(self.main_footer)


        self.horizontalLayout.addWidget(self.center_main_items)


        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1116, 21))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuImport = QMenu(self.menuFile)
        self.menuImport.setObjectName(u"menuImport")
        self.menuExport = QMenu(self.menuFile)
        self.menuExport.setObjectName(u"menuExport")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.menuImport.menuAction())
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addAction(self.actionConvert)
        self.menuFile.addAction(self.actionExit)
        self.menuImport.addAction(self.actionCSV_data)
        self.menuImport.addAction(self.actionEDF_data)
        self.menuImport.addAction(self.actionBIN_data)
        self.menuImport.addAction(self.actionMetadata_import)
        self.menuImport.addAction(self.actionLast_Session_Settings)
        self.menuExport.addAction(self.actionMetadata_export)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_rec.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionCSV_data.setText(QCoreApplication.translate("MainWindow", u"CSV data", None))
        self.actionEDF_data.setText(QCoreApplication.translate("MainWindow", u"EDF data", None))
        self.actionBIN_data.setText(QCoreApplication.translate("MainWindow", u"BIN data", None))
        self.actionMetadata_import.setText(QCoreApplication.translate("MainWindow", u"Device Settings", None))
        self.actionMetadata_export.setText(QCoreApplication.translate("MainWindow", u"Device Settings", None))
        self.actionConvert.setText(QCoreApplication.translate("MainWindow", u"Convert BIN", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionLast_Session_Settings.setText(QCoreApplication.translate("MainWindow", u"Last Session Settings", None))
        self.btn_left_menu_toggle.setText(QCoreApplication.translate("MainWindow", u"        Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"        Home", None))
        self.btn_bt.setText(QCoreApplication.translate("MainWindow", u"        Connect", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"        Settings", None))
        self.btn_plots.setText(QCoreApplication.translate("MainWindow", u"        Visualization", None))
        self.btn_impedance.setText(QCoreApplication.translate("MainWindow", u"        Impedance", None))
        self.btn_integration.setText(QCoreApplication.translate("MainWindow", u"        Integration", None))
        self.home_title.setText(QCoreApplication.translate("MainWindow", u"Welcome to Mentalab's ExploreDesktop", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">HOW TO</span></p></body></html>", None))
        self.btn_bt_2.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Connect and disconnect from your device ", None))
        self.btn_settings_2.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Change Explore's settings", None))
        self.btn_plots_2.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Filter and visualize the ExG signal, its spectral analysis and the orientation data", None))
        self.btn_impedance_2.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Measure and visualize the channel's impedance", None))
        self.btn_integration_2.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Integrate with other platforms", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">DATA SHARING PERMISSION</span></p></body></html>", None))
        self.cb_permission.setText(QCoreApplication.translate("MainWindow", u"Automatically send error logs to Mentalab", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">EXPORT EEGLAB DATASET</span></p></body></html>", None))
        self.le_import_edf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path/to/file", None))
        self.btn_import_edf.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.btn_generate_bdf.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.integration_title.setText(QCoreApplication.translate("MainWindow", u"Integration", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Push to LSL</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Stream data from other software such as OpenVibe or other programming languages. </p><p>It will create three LSL streams for ExG, Orientation and markers. </p></body></html>", None))
        self.cb_lsl_duration.setText(QCoreApplication.translate("MainWindow", u"Set duration (the default stream duration is 3600 seconds.)", None))
        self.label_lsl_duration.setText(QCoreApplication.translate("MainWindow", u"Duration (s):", None))
        self.btn_push_lsl.setText(QCoreApplication.translate("MainWindow", u"Push", None))
        self.settings_title.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_explore_name.setText(QCoreApplication.translate("MainWindow", u"Explore_XXXXX", None))
        self.label_warning_disabled.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-style:italic;\">Changing the settings during recording and LSL streaming is not possible</span></p></body></html>", None))
        self.label_samping_rate.setText(QCoreApplication.translate("MainWindow", u"Sampling Rate", None))
        self.lbl_sr_warning.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Please note that 1000 Hz sampling rate is in beta phase</p></body></html>", None))
        self.btn_apply_settings.setText(QCoreApplication.translate("MainWindow", u"Apply changes", None))
        self.btn_format_memory.setText(QCoreApplication.translate("MainWindow", u"Format Memory", None))
        self.btn_reset_settings.setText(QCoreApplication.translate("MainWindow", u"Reset Settings", None))
        self.btn_calibrate.setText(QCoreApplication.translate("MainWindow", u"Calibrate ORN", None))
        self.btn_record.setText(QCoreApplication.translate("MainWindow", u" Record", None))
        self.label_recording_time.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_yAxis.setText(QCoreApplication.translate("MainWindow", u"Y-axis Scale", None))
        self.label_timeScale.setText(QCoreApplication.translate("MainWindow", u"Time window", None))
        self.value_event_code.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Event Code", None))
        self.btn_marker.setText(QCoreApplication.translate("MainWindow", u" Set Marker", None))
        self.btn_plot_filters.setText(QCoreApplication.translate("MainWindow", u"Filters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.exg), QCoreApplication.translate("MainWindow", u"  ExG  ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.orn), QCoreApplication.translate("MainWindow", u"  Orientation  ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fft), QCoreApplication.translate("MainWindow", u"  FFT  ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"mentalab.com\"><span style=\" text-decoration: underline; color:#0069d9;\">Back to recorded data visualization</span></a></p></body></html>", None))
        self.label_signal_rec.setText(QCoreApplication.translate("MainWindow", u"Signal", None))
        self.label_yAxis_rec.setText(QCoreApplication.translate("MainWindow", u"Y-axis Scale", None))
        self.label_timeScale_rec.setText(QCoreApplication.translate("MainWindow", u"Time window", None))
        self.label_heartRate_rec.setText(QCoreApplication.translate("MainWindow", u"Heart Rate (bpm)", None))
        self.value_heartRate_rec.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.btn_stream_rec.setText(QCoreApplication.translate("MainWindow", u"Start Visualization", None))
        self.cb_swipping_rec.setText(QCoreApplication.translate("MainWindow", u"Moving window", None))
        self.tabWidget_rec.setTabText(self.tabWidget_rec.indexOf(self.exg_rec), QCoreApplication.translate("MainWindow", u"  ExG  ", None))
        self.tabWidget_rec.setTabText(self.tabWidget_rec.indexOf(self.orn_rec), QCoreApplication.translate("MainWindow", u"  Orientation  ", None))
        self.tabWidget_rec.setTabText(self.tabWidget_rec.indexOf(self.fft_rec), QCoreApplication.translate("MainWindow", u"  FFT  ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"mentalab.com\"><span style=\" text-decoration: underline; color:#0069d9;\">Back to RT visualization</span></a></p></body></html>", None))
        self.impedance_title.setText(QCoreApplication.translate("MainWindow", u"Impedance Measurement", None))
#if QT_CONFIG(tooltip)
        self.btn_imp_meas.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_imp_meas.setText(QCoreApplication.translate("MainWindow", u"Measure Impedances", None))
        self.imp_meas_info.setText("")
        self.bt_title.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Press the button on your device to turn it on.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Scan the paired devices or directly input the name of your device.</span></p></body></html>", None))
        self.lbl_wdws_warning.setText("")
        self.btn_scan.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Device Name: ", None))
        self.dev_name_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Explore_XXXX or XXXX", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TESTING IMP", None))
        self.cb_1020_3.setText(QCoreApplication.translate("MainWindow", u"Use 10 - 20", None))
        self.btn_apply_settings_2.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.cb_multitype_signal_3.setText(QCoreApplication.translate("MainWindow", u"Multi Type signal", None))
        self.ft_label_device_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Not connected</span></p></body></html>", None))
        self.ft_label_firmware.setText(QCoreApplication.translate("MainWindow", u"Firmware Version  ", None))
        self.ft_label_firmware_value.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.ft_label_battery.setText(QCoreApplication.translate("MainWindow", u"Battery ", None))
        self.ft_label_battery_value.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.ft_label_temp.setText(QCoreApplication.translate("MainWindow", u"Device Temperature", None))
        self.ft_label_temp_value.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.ft_label_version.setText(QCoreApplication.translate("MainWindow", u"v0.1", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuImport.setTitle(QCoreApplication.translate("MainWindow", u"Import", None))
        self.menuExport.setTitle(QCoreApplication.translate("MainWindow", u"Export", None))
    # retranslateUi

