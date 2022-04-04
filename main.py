import sys

from PyQt5.QtGui import QIcon
from PyQt5.uic.properties import QtGui

import addEvent

CatDatabas = ["General", "Work"]

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)


# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from PyQt5.uic import loadUi

from GUI import Ui_Dialog

class Category:
    def __init__(self):
        pass


class Month:
    def __init__(self):
        pass


class Day:
    def __init__(self):
        pass


class Hour:
    def __init__(self):
        pass


class Event:
    def __init__(self, hour, day, month, alert=0, desc='', category="General"):
        self.day = day
        self.hour = hour
        self.month = month
        self.desc = desc
        self.category = category


        if self.alert != 0:
            self.alert = alert

class Window(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.addCats()

    def addCats(self):
        for x in CatDatabas:
            self.SelectCatBox.addItem(x)

    def execRem(self):
        self.removeCats()

    def removeCats(self):
        try:
            #O dziwo jak to wkleję bezpośrednio to nie działa jak powinno
            toRem = self.SelectCatBox.itemText(self.SelectCatBox.currentIndex())
            self.SelectCatBox.removeItem(self.SelectCatBox.currentIndex())
            CatDatabas.remove(toRem)
        except:
            print("Nie ma czego usuwać")
            self.setWindowIcon(QIcon('resources/TrollfaceProblem.jpg'))
            self.listView.setStyleSheet("background-image : url(resources/TrollfaceProblem.jpg);")

    #ToDO - To ma coś robić
    def onChanged(self):
        print(CatDatabas)

        print(self.SelectCatBox.itemText(self.SelectCatBox.currentIndex()))

    def execAdd(self):
        text = self.textEditCat.toPlainText()

        try:

            if(text == None or text == ""):
                raise TypeError

            elif(text not in CatDatabas):
                self.SelectCatBox.addItem(text)
                CatDatabas.append(text)
                self.textEditCat.clear()

            else:
                print("Proszę wpisać unikalną nazwę kategorii")


        except(TypeError):
            print("Proszę wpisać nazwę kategori")

    def open(self):
        if not (CatDatabas):
            print("Brak kategorii")

        else:
            dialog = AddEvent(self)
            dialog.exec()

class GUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("GUI.ui", self)

class AddEvent(QDialog, addEvent.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.label_6.hide()
        self.remindComb.hide()

        for x in CatDatabas:
            self.catCombo.addItem(x)



    def execRem(self):
        if(self.label_6.isHidden()):
            self.label_6.show()
            self.remindComb.show()
        else:
            self.label_6.hide()
            self.remindComb.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
