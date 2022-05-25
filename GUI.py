# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        Dialog.setMinimumSize(QtCore.QSize(700, 500))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Dialog.setWindowOpacity(1.0)
        Dialog.setStyleSheet("background-color: rgb(0,0,0)")
        self.Widget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Widget.sizePolicy().hasHeightForWidth())
        self.Widget.setSizePolicy(sizePolicy)
        self.Widget.setMinimumSize(QtCore.QSize(700, 500))
        self.Widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Widget.setStyleSheet("background-color: rgb(0,0,0)")
        self.Widget.setObjectName("Widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Widget)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(200, 30))
        self.label_2.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(112, 182, 252);\n"
"color: rgb(252,252,252);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.SelectCatBox = QtWidgets.QComboBox(self.Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelectCatBox.sizePolicy().hasHeightForWidth())
        self.SelectCatBox.setSizePolicy(sizePolicy)
        self.SelectCatBox.setMinimumSize(QtCore.QSize(200, 30))
        self.SelectCatBox.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.SelectCatBox.setFont(font)
        self.SelectCatBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SelectCatBox.setAutoFillBackground(False)
        self.SelectCatBox.setStyleSheet("background-color:rgb(26, 72, 170);\n"
"color: rgb(252,252,252);")
        self.SelectCatBox.setEditable(False)
        self.SelectCatBox.setCurrentText("")
        self.SelectCatBox.setObjectName("SelectCatBox")
        self.verticalLayout.addWidget(self.SelectCatBox)
        self.label = QtWidgets.QLabel(self.Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(200, 30))
        self.label.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(112, 182, 252);\n"
"color: rgb(252,252,252);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEditCat = QtWidgets.QTextEdit(self.Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditCat.sizePolicy().hasHeightForWidth())
        self.textEditCat.setSizePolicy(sizePolicy)
        self.textEditCat.setMinimumSize(QtCore.QSize(200, 30))
        self.textEditCat.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textEditCat.setFont(font)
        self.textEditCat.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.textEditCat.setStyleSheet("background-color:rgb(26, 72, 170);\n"
"color: rgb(252,252,252);")
        self.textEditCat.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEditCat.setObjectName("textEditCat")
        self.verticalLayout.addWidget(self.textEditCat)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushAddCat = QtWidgets.QPushButton(self.Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushAddCat.sizePolicy().hasHeightForWidth())
        self.pushAddCat.setSizePolicy(sizePolicy)
        self.pushAddCat.setMinimumSize(QtCore.QSize(120, 40))
        self.pushAddCat.setMaximumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushAddCat.setFont(font)
        self.pushAddCat.setStyleSheet("background-color:rgb(26, 72, 170);\n"
"color: rgb(252,252,252);")
        self.pushAddCat.setObjectName("pushAddCat")
        self.horizontalLayout.addWidget(self.pushAddCat)
        self.pushRemoveCat = QtWidgets.QPushButton(self.Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushRemoveCat.sizePolicy().hasHeightForWidth())
        self.pushRemoveCat.setSizePolicy(sizePolicy)
        self.pushRemoveCat.setMinimumSize(QtCore.QSize(120, 40))
        self.pushRemoveCat.setMaximumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushRemoveCat.setFont(font)
        self.pushRemoveCat.setStyleSheet("background-color:rgb(26, 72, 170);\n"
"color: rgb(252,252,252);")
        self.pushRemoveCat.setObjectName("pushRemoveCat")
        self.horizontalLayout.addWidget(self.pushRemoveCat)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 660, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(200, 30))
        self.label_3.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.label_3.setStyleSheet("background-color: rgb(112, 182, 252);\n"
"color: rgb(252,252,252);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.textBrowser = QtWidgets.QTextBrowser(self.Widget)
        self.textBrowser.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(200, 30))
        self.textBrowser.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textBrowser.setStyleSheet("background-color:rgb(26, 72, 170);\n"
"color: rgb(252,252,252);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.lineEdit = QtWidgets.QLineEdit(self.Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(26, 72, 170);\n"
"color: rgb(252,252,252);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.listView = QtWidgets.QListView(self.Widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.listView.setFont(font)
        self.listView.setStyleSheet("background-image : url(resources/Space.jpg);\n"
"color: rgb(252,252,252)")
        self.listView.setObjectName("listView")
        self.horizontalLayout_2.addWidget(self.listView)
        Dialog.setCentralWidget(self.Widget)
        self.menubar = QtWidgets.QMenuBar(Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        Dialog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")
        Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        self.pushRemoveCat.clicked.connect(Dialog.execRem) # type: ignore
        self.pushAddCat.clicked.connect(Dialog.execAdd) # type: ignore
        self.pushButton.pressed.connect(Dialog.open) # type: ignore
        self.SelectCatBox.currentIndexChanged['QString'].connect(Dialog.displayEvent) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.listView.clicked[QtCore.QModelIndex].connect(self.on_clicked)
        self.lineEdit.textChanged.connect(self.onChanged2)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ToDoList"))
        self.label_2.setText(_translate("Dialog", "Kategoria"))
        self.label.setText(_translate("Dialog", "Nowa Kategoria"))
        self.pushAddCat.setText(_translate("Dialog", "Dodaj kategorię"))
        self.pushRemoveCat.setText(_translate("Dialog", "Usuń kategorię"))
        self.label_3.setText(_translate("Dialog", "Szukaj wydarzenia"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">lol</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">kek</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Dodaj Wydarzenie"))

