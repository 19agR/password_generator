# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\python_work\PyQt\password_generator\password_generator.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(664, 217)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 217))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 217))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setContentsMargins(10, -1, 20, 0)
        self.verticalLayout_1.setSpacing(8)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.formLayout_1 = QtWidgets.QFormLayout()
        self.formLayout_1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_1.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_1.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout_1.setObjectName("formLayout_1")
        self.label_length = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_length.sizePolicy().hasHeightForWidth())
        self.label_length.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_length.setFont(font)
        self.label_length.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_length.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_length.setObjectName("label_length")
        self.formLayout_1.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_length)
        self.spinBox_length = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_length.sizePolicy().hasHeightForWidth())
        self.spinBox_length.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_length.setFont(font)
        self.spinBox_length.setProperty("showGroupSeparator", False)
        self.spinBox_length.setSuffix("")
        self.spinBox_length.setMinimum(3)
        self.spinBox_length.setMaximum(30)
        self.spinBox_length.setProperty("value", 10)
        self.spinBox_length.setDisplayIntegerBase(10)
        self.spinBox_length.setObjectName("spinBox_length")
        self.formLayout_1.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_length)
        self.verticalLayout_1.addLayout(self.formLayout_1)
        self.button_generate = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_generate.sizePolicy().hasHeightForWidth())
        self.button_generate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_generate.setFont(font)
        self.button_generate.setObjectName("button_generate")
        self.verticalLayout_1.addWidget(self.button_generate, 0, QtCore.Qt.AlignHCenter)
        self.label_your_password = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_your_password.sizePolicy().hasHeightForWidth())
        self.label_your_password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_your_password.setFont(font)
        self.label_your_password.setObjectName("label_your_password")
        self.verticalLayout_1.addWidget(self.label_your_password, 0, QtCore.Qt.AlignLeft)
        self.line_password = QtWidgets.QLineEdit(self.centralwidget)
        self.line_password.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_password.sizePolicy().hasHeightForWidth())
        self.line_password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line_password.setFont(font)
        self.line_password.setInputMask("")
        self.line_password.setText("")
        self.line_password.setMaxLength(30)
        self.line_password.setFrame(True)
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_password.setDragEnabled(False)
        self.line_password.setReadOnly(False)
        self.line_password.setClearButtonEnabled(True)
        self.line_password.setObjectName("line_password")
        self.verticalLayout_1.addWidget(self.line_password)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_1.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_1)
        self.dividing_line_1 = QtWidgets.QFrame(self.centralwidget)
        self.dividing_line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.dividing_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dividing_line_1.setObjectName("dividing_line_1")
        self.horizontalLayout.addWidget(self.dividing_line_1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(20, -1, 10, 10)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_head_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_head_2.setFont(font)
        self.label_head_2.setObjectName("label_head_2")
        self.verticalLayout_2.addWidget(self.label_head_2, 0, QtCore.Qt.AlignHCenter)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_key = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_key.setFont(font)
        self.label_key.setObjectName("label_key")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_key)
        self.line_key = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line_key.setFont(font)
        self.line_key.setClearButtonEnabled(True)
        self.line_key.setObjectName("line_key")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_key)
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_password)
        self.line_password_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line_password_2.setFont(font)
        self.line_password_2.setStyleSheet("")
        self.line_password_2.setClearButtonEnabled(True)
        self.line_password_2.setObjectName("line_password_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_password_2)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radio_button_to_db = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_button_to_db.setFont(font)
        self.radio_button_to_db.setChecked(True)
        self.radio_button_to_db.setObjectName("radio_button_to_db")
        self.horizontalLayout_3.addWidget(self.radio_button_to_db, 0, QtCore.Qt.AlignHCenter)
        self.radio_button_from_db = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_button_from_db.setFont(font)
        self.radio_button_from_db.setChecked(False)
        self.radio_button_from_db.setObjectName("radio_button_from_db")
        self.horizontalLayout_3.addWidget(self.radio_button_from_db, 0, QtCore.Qt.AlignHCenter)
        self.radio_button_del = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_button_del.setFont(font)
        self.radio_button_del.setObjectName("radio_button_del")
        self.horizontalLayout_3.addWidget(self.radio_button_del, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_complete = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_complete.sizePolicy().hasHeightForWidth())
        self.button_complete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_complete.setFont(font)
        self.button_complete.setObjectName("button_complete")
        self.horizontalLayout_2.addWidget(self.button_complete)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.dividing_line_2 = QtWidgets.QFrame(self.centralwidget)
        self.dividing_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.dividing_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dividing_line_2.setObjectName("dividing_line_2")
        self.verticalLayout_2.addWidget(self.dividing_line_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_del_all_passwords = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_del_all_passwords.sizePolicy().hasHeightForWidth())
        self.button_del_all_passwords.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_del_all_passwords.setFont(font)
        self.button_del_all_passwords.setObjectName("button_del_all_passwords")
        self.horizontalLayout_5.addWidget(self.button_del_all_passwords)
        self.button_take_all_passwords = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_take_all_passwords.sizePolicy().hasHeightForWidth())
        self.button_take_all_passwords.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_take_all_passwords.setFont(font)
        self.button_take_all_passwords.setObjectName("button_take_all_passwords")
        self.horizontalLayout_5.addWidget(self.button_take_all_passwords)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password generator"))
        self.label_length.setText(_translate("MainWindow", "?????????? ????????????:"))
        self.button_generate.setText(_translate("MainWindow", "?????????????????????????? ????????????"))
        self.label_your_password.setText(_translate("MainWindow", "?????? ????????????:"))
        self.label_head_2.setText(_translate("MainWindow", "???????????? ?? ???? ?????????? ??????????????"))
        self.label_key.setText(_translate("MainWindow", "????????/????????:"))
        self.label_password.setText(_translate("MainWindow", "????????????:"))
        self.radio_button_to_db.setText(_translate("MainWindow", "??????????????"))
        self.radio_button_from_db.setText(_translate("MainWindow", "????????????????"))
        self.radio_button_del.setText(_translate("MainWindow", "??????????????"))
        self.button_complete.setText(_translate("MainWindow", "??????????????????"))
        self.button_del_all_passwords.setText(_translate("MainWindow", "?????????????? ?????? ????????????"))
        self.button_take_all_passwords.setText(_translate("MainWindow", "???????????????? ?????? ????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
