# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEvent.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(1000, 600))
        Dialog.setMaximumSize(QtCore.QSize(1000, 600))
        Dialog.setWindowOpacity(0.9)
        Dialog.setStyleSheet("background-color: rgb(252,252,252)")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(150, 40))
        self.label.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(252,252,252)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineDesc = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineDesc.sizePolicy().hasHeightForWidth())
        self.lineDesc.setSizePolicy(sizePolicy)
        self.lineDesc.setMinimumSize(QtCore.QSize(200, 40))
        self.lineDesc.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineDesc.setFont(font)
        self.lineDesc.setStyleSheet("background-color: rgb(252,252,252)")
        self.lineDesc.setDragEnabled(False)
        self.lineDesc.setObjectName("lineDesc")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineDesc)
        self.label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(150, 40))
        self.label_2.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(252,252,252)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.catCombo = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catCombo.sizePolicy().hasHeightForWidth())
        self.catCombo.setSizePolicy(sizePolicy)
        self.catCombo.setMinimumSize(QtCore.QSize(200, 40))
        self.catCombo.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.catCombo.setFont(font)
        self.catCombo.setStyleSheet("background-color: rgb(252,252,252)")
        self.catCombo.setFrame(True)
        self.catCombo.setObjectName("catCombo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.catCombo)
        spacerItem = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.label_3 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(150, 40))
        self.label_3.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(252,252,252)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.ifRemindBox = QtWidgets.QCheckBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ifRemindBox.sizePolicy().hasHeightForWidth())
        self.ifRemindBox.setSizePolicy(sizePolicy)
        self.ifRemindBox.setMinimumSize(QtCore.QSize(105, 40))
        self.ifRemindBox.setMaximumSize(QtCore.QSize(105, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ifRemindBox.setFont(font)
        self.ifRemindBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ifRemindBox.setText("")
        self.ifRemindBox.setObjectName("ifRemindBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ifRemindBox)
        self.label_4 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(150, 40))
        self.label_4.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(252,252,252)")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.remindComb = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remindComb.sizePolicy().hasHeightForWidth())
        self.remindComb.setSizePolicy(sizePolicy)
        self.remindComb.setMinimumSize(QtCore.QSize(200, 40))
        self.remindComb.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.remindComb.setFont(font)
        self.remindComb.setStyleSheet("background-image : url(resources/hulicki.jpg)")
        self.remindComb.setFrame(True)
        self.remindComb.setObjectName("remindComb")
        self.remindComb.addItem("")
        self.remindComb.addItem("")
        self.remindComb.addItem("")
        self.remindComb.addItem("")
        self.remindComb.addItem("")
        self.remindComb.addItem("")
        self.remindComb.addItem("")
        self.remindComb.addItem("")
        self.remindComb.addItem("")
        self.remindComb.addItem("")
        self.remindComb.addItem("")
        self.remindComb.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.remindComb)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.horizontalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.formLayout_2.setItem(0, QtWidgets.QFormLayout.SpanningRole, spacerItem2)
        self.label_5 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(150, 40))
        self.label_5.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(252,252,252)")
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.calendarEd = QtWidgets.QCalendarWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarEd.sizePolicy().hasHeightForWidth())
        self.calendarEd.setSizePolicy(sizePolicy)
        self.calendarEd.setMinimumSize(QtCore.QSize(400, 300))
        self.calendarEd.setMaximumSize(QtCore.QSize(400, 300))
        self.calendarEd.setStyleSheet("background-color: rgb(252,252,252)")
        self.calendarEd.setMinimumDate(QtCore.QDate(2001, 9, 11))
        self.calendarEd.setMaximumDate(QtCore.QDate(2101, 9, 11))
        self.calendarEd.setObjectName("calendarEd")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.calendarEd)
        spacerItem3 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.formLayout_2.setItem(2, QtWidgets.QFormLayout.SpanningRole, spacerItem3)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setMinimumSize(QtCore.QSize(150, 40))
        self.label_6.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(252,252,252)")
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.timeEditComb = QtWidgets.QTimeEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEditComb.sizePolicy().hasHeightForWidth())
        self.timeEditComb.setSizePolicy(sizePolicy)
        self.timeEditComb.setMinimumSize(QtCore.QSize(70, 40))
        self.timeEditComb.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.timeEditComb.setFont(font)
        self.timeEditComb.setStyleSheet("background-color: rgb(252,252,252)")
        self.timeEditComb.setObjectName("timeEditComb")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.timeEditComb)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.formLayout_2.setItem(4, QtWidgets.QFormLayout.SpanningRole, spacerItem4)
        self.okcanButtons = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okcanButtons.sizePolicy().hasHeightForWidth())
        self.okcanButtons.setSizePolicy(sizePolicy)
        self.okcanButtons.setMinimumSize(QtCore.QSize(200, 30))
        self.okcanButtons.setMaximumSize(QtCore.QSize(500, 30))
        self.okcanButtons.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.okcanButtons.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.okcanButtons.setStyleSheet("background-color: rgb(252,252,252)")
        self.okcanButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okcanButtons.setObjectName("okcanButtons")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.okcanButtons)
        self.horizontalLayout.addLayout(self.formLayout_2)

        self.retranslateUi(Dialog)
        self.okcanButtons.accepted.connect(Dialog.accept)
        self.okcanButtons.rejected.connect(Dialog.reject)
        self.ifRemindBox.toggled['bool'].connect(Dialog.exec)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dodaj wydarzenie"))
        self.label.setText(_translate("Dialog", "Opis"))
        self.label_2.setText(_translate("Dialog", "Kategoria"))
        self.label_3.setText(_translate("Dialog", "Przypomnienie"))
        self.label_4.setText(_translate("Dialog", "Kiedy przypomnieć"))
        self.remindComb.setItemText(0, _translate("Dialog", "Godzinę przed"))
        self.remindComb.setItemText(1, _translate("Dialog", "3 godziny przed"))
        self.remindComb.setItemText(2, _translate("Dialog", "5 godzin przed"))
        self.remindComb.setItemText(3, _translate("Dialog", "12 godzin przed"))
        self.remindComb.setItemText(4, _translate("Dialog", "Dzień przed"))
        self.remindComb.setItemText(5, _translate("Dialog", "Dwa dni przed"))
        self.remindComb.setItemText(6, _translate("Dialog", "Tydzień przed"))
        self.remindComb.setItemText(7, _translate("Dialog", "2 tygodnie przed"))
        self.remindComb.setItemText(8, _translate("Dialog", "Miesiąc przed"))
        self.remindComb.setItemText(9, _translate("Dialog", "Kwartał przed"))
        self.remindComb.setItemText(10, _translate("Dialog", "Pół roku przed"))
        self.remindComb.setItemText(11, _translate("Dialog", "Rok przed"))
        self.label_5.setText(_translate("Dialog", "Wybierz dzień"))
        self.label_6.setText(_translate("Dialog", "Wybierz godzinę"))
