import sys
import addEvent

from GUI import Ui_Dialog
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtGui
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Category:
    # Podstawowy konstruktor w Pythonie.
    def __init__(self, name):
        # Python jest językiem dynamicznie typowanym, ale można wcześniej deklarować zmienne i ich typy.
        # Pomaga w osiąganiu abstrakcji i przejrzystości kodu.
        # Gettery są tu niepotrzebne. Klasy prywatne tworzy się przy użyciu _Internal.
        self.heldEvents = []
        self.name = name

    def eventToCat(self, toAdd):
        self.heldEvents.append(toAdd)


# ToDO - może być niepotrzebne, najprawdopodobniej jest
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
    # W konstruktorach klas i deklaracji funkcji można dawać domyślne parametry.
    # Brakowało mi tego w Javie.
    # Są one używane, jeśli do konstruktora lub funkcji zostanie przekazany pusty parametr.
    def __init__(self, hour, minutes, day, month, alert=0, desc="", category="General"):
        self.day = day
        self.hour = hour
        self.minutes = minutes
        self.month = month
        self.desc = desc
        self.category = category
        self.alert = alert

        # To może być głupie, zastanowię się potem.
        # Widzę potencjalny NullPointerException.
        # Dobra to jest głupie, nie rób tak nigdy.
        if self.alert != 0:
            self.alert = alert

    # Metoda sprawdza, czy parametry dwóch obiektów są takie same.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Window(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.addCats()

    def addCats(self):
        for x in CatDatabase:
            self.SelectCatBox.addItem(x.name)

    def execRem(self):
        self.removeCats()

    def removeCats(self):
        try:
            # O dziwo jak to wkleję bezpośrednio, to nie działa, jak powinno. Nie porządkować!
            toRem = self.SelectCatBox.itemText(self.SelectCatBox.currentIndex())
            self.SelectCatBox.removeItem(self.SelectCatBox.currentIndex())
            for x in CatDatabase:
                if x.name is toRem:
                    CatDatabase.remove(x)
                    break

            if not CatDatabase:
                # Ogarnij tutaj jak się wyświetla grafiki na przykładzie.
                print("Nie ma czego usuwać")
                self.setWindowIcon(QIcon('resources/Troll-faceProblem.jpg'))
                self.listView.setStyleSheet("background-image : url(resources/Troll-faceProblem.jpg);")

        except:
            print("Nie ma czego usuwać")
            self.setWindowIcon(QIcon('resources/Troll-faceProblem.jpg'))
            self.listView.setStyleSheet("background-image : url(resources/Troll-faceProblem.jpg);")

    # ToDO - To ma coś robić, zmieniać i wyświetlać eventy na przykład
    # Na razie wyświetla istniejące kategorie.
    def onChanged(self):
        print(CatDatabase)
        print(self.SelectCatBox.itemText(self.SelectCatBox.currentIndex()))

    # Dodawanie kategorii.
    def execAdd(self):
        # Trzeba zdekodować.
        text = self.textEditCat.toPlainText()

        try:

            if text is None or text == "":
                raise TypeError

            elif text not in CatDatabase:
                self.SelectCatBox.addItem(text)
                CatDatabase.append(Category(text))
                self.textEditCat.clear()

            else:
                print("Proszę wpisać unikalną nazwę kategorii")


        except(TypeError):
            print("Proszę wpisać nazwę kategorii")

    # Otwiera okienko z dodawaniem eventów.
    def open(self):
        # Tak można łatwo sprawdzić, czy lista jest pusta.
        # Przydatna rzecz.
        if not CatDatabase:
            print("Brak kategorii")

        else:
            dialog = AddEvent(self)
            dialog.exec()


# Loading i ładowanie głównego okna programu
class GUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("GUI.ui", self)


# Loading i otwieranie widget-ów.
class AddEvent(QDialog, addEvent.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        #self.label_6.hide()
        #self.remindComb.hide()

        # Dodaje kategorie do combobox-ów.
        for x in CatDatabase:
            self.catCombo.addItem(x.name)

    # Funkcja otwiera funkcje do przypomnień po zaznaczeniu przycisku.
    # Zauważ, że istnieje już taka funkcja, ale w innej klasie.
    def execRem(self):
        if self.label_6.isHidden():
            self.label_6.show()
            self.remindComb.show()
        else:
            self.label_6.hide()
            self.remindComb.hide()

    def accept(self):
        category = self.catCombo.itemText(self.catCombo.currentIndex())
        for x in CatDatabase:
            if category == x.name:
                # Nie wiem jak dynamicznie tworzyć obiekty, HELP!

                # def __init__(self, hour, day, month, alert=0, desc='', category="General"):

                # ToDO ogarnąć alert przy dodawaniu eventów jak już ogarniemy zawiadamianie
                newEvent = Event(self.timeEditComb.time().hour(), self.timeEditComb.time().minute(),
                                 self.calendarEd.monthShown(), 0, self.lineDesc.text(), x.name)

                try:
                    if newEvent.__eq__(x.heldEvents[-1]) is True:
                        print("Takie wydarzenie już istnieje.")
                    else:
                        x.eventToCat(newEvent)

                # A co jeśli kategoria jest pusta?
                except:
                    if not x.heldEvents:
                        x.eventToCat(newEvent)
                    else:
                        raise TypeError


# Standardowe wejście do skryptu Pythona.
# Nie musi istnieć, ale w dużych projektach wiele porządkuje.
# Jak go nie ma, to interpreter jedzie po otwartym pliku od góry na dół.
# Odpowiednik main z java + ładnie wygląda i wiadomo gdzie zacząć.
if __name__ == "__main__":
    # CatDatabase = ["General", "Work"]
    general = Category("General")
    work = Category("Work")
    CatDatabase = [general, work]
    app = QApplication(sys.argv)
    win = Window()
    # win = AddEvent()
    win.show()
    sys.exit(app.exec())
