# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_convert_bin.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(460, 285)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_step2 = QLabel(Dialog)
        self.lbl_step2.setObjectName(u"lbl_step2")

        self.verticalLayout.addWidget(self.lbl_step2)

        self.layout_folder_browse = QHBoxLayout()
        self.layout_folder_browse.setObjectName(u"layout_folder_browse")
        self.input_filepath = QLineEdit(Dialog)
        self.input_filepath.setObjectName(u"input_filepath")

        self.layout_folder_browse.addWidget(self.input_filepath)

        self.btn_browse_bin = QPushButton(Dialog)
        self.btn_browse_bin.setObjectName(u"btn_browse_bin")

        self.layout_folder_browse.addWidget(self.btn_browse_bin)


        self.verticalLayout.addLayout(self.layout_folder_browse)

        self.layout_file_format = QHBoxLayout()
        self.layout_file_format.setObjectName(u"layout_file_format")
        self.lbl_step1_2 = QLabel(Dialog)
        self.lbl_step1_2.setObjectName(u"lbl_step1_2")

        self.layout_file_format.addWidget(self.lbl_step1_2)

        self.rdbtn_csv = QRadioButton(Dialog)
        self.rdbtn_csv.setObjectName(u"rdbtn_csv")

        self.layout_file_format.addWidget(self.rdbtn_csv)

        self.rdbtn_edf = QRadioButton(Dialog)
        self.rdbtn_edf.setObjectName(u"rdbtn_edf")

        self.layout_file_format.addWidget(self.rdbtn_edf)


        self.verticalLayout.addLayout(self.layout_file_format)

        self.lbl_step2_2 = QLabel(Dialog)
        self.lbl_step2_2.setObjectName(u"lbl_step2_2")

        self.verticalLayout.addWidget(self.lbl_step2_2)

        self.layout_folder_browse_2 = QHBoxLayout()
        self.layout_folder_browse_2.setObjectName(u"layout_folder_browse_2")
        self.input_dest_folder = QLineEdit(Dialog)
        self.input_dest_folder.setObjectName(u"input_dest_folder")

        self.layout_folder_browse_2.addWidget(self.input_dest_folder)

        self.btn_browse_dest_folder = QPushButton(Dialog)
        self.btn_browse_dest_folder.setObjectName(u"btn_browse_dest_folder")

        self.layout_folder_browse_2.addWidget(self.btn_browse_dest_folder)


        self.verticalLayout.addLayout(self.layout_folder_browse_2)

        self.warning_label = QLabel(Dialog)
        self.warning_label.setObjectName(u"warning_label")
        self.warning_label.setMinimumSize(QSize(0, 0))
        self.warning_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.warning_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(54, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_step2.setText(QCoreApplication.translate("Dialog", u"1. Select the file to convert:", None))
        self.btn_browse_bin.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.lbl_step1_2.setText(QCoreApplication.translate("Dialog", u"2. Select the output file format :     ", None))
        self.rdbtn_csv.setText(QCoreApplication.translate("Dialog", u"csv", None))
        self.rdbtn_edf.setText(QCoreApplication.translate("Dialog", u"bdf", None))
        self.lbl_step2_2.setText(QCoreApplication.translate("Dialog", u"3. Select the folder to export the file:", None))
        self.btn_browse_dest_folder.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.warning_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" color:#d90000;\">A file name can't contain any of the following characters:</span></p><p align=\"center\"><span style=\" color:#d90000;\">| \\ ? * &lt; &quot; : &gt; + [ ] / '</span></p></body></html>", None))
    # retranslateUi

