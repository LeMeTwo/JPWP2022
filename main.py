import select
import sys
import addEvent

from GUI import Ui_Dialog
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtGui, QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


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


# ToDo -------------------------------------------------------------
""""
# To gówno jest do tworzenia label-ów dynamicznie.
class ExampleLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("KEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEK")
        self.setGeometry(100, 100, 100, 100)
        self.show()
        """
# ToDo ---------------------------------------------------------------


# Listy / Kategorie
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


# Główne okno
class Window(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.firstAddCats()

        # ToDo --------------------------------------------------------
        """
        # Ustawianie viewList.
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        """
        # ToDo --------------------------------------------------------

    ####################################################################################################################
    ####################################################################################################################

    # ToDo ------------------------------------------------------------
    """
    def addLabel(self):
        self.widget = ExampleLabel(self)
        """
    # ToDo ------------------------------------------------------------

    ####################################################################################################################
    ####################################################################################################################

    # Dodawanie kategorii z CatDatabase do SelectCatBox-a na przy otwarciu okna.
    # Do czego to służy?
    def firstAddCats(self):
        for x in CatDatabase:
            self.SelectCatBox.addItem(x.name)

    # Element z SelectCatBox jest usuwany z SelectCatBox-a i z CatDatabase.
    def removeCats(self):

        # ToDo ---------------------------------------------------------
        """
        # Wstawianie elementów to viewList
        entries = ['one', 'two', 'three']

        for i in entries:
            item = QtGui.QStandardItem(i)
            a = self.listView.model()
            a.appendRow(item)
            """
        # ToDo ---------------------------------------------------------

        try:
            # O dziwo jak to wkleję bezpośrednio, to nie działa, jak powinno. Nie porządkować!
            toRem = self.SelectCatBox.itemText(self.SelectCatBox.currentIndex())

            # Jeszcze sobie wybierzemy nazwę/nazwy kategorii, których nie usuwamy.
            # General na pewno.
            if toRem == "General":
                print("Nie można usunąć kategorii " + toRem)
            else:
                self.SelectCatBox.removeItem(self.SelectCatBox.currentIndex())

            for x in CatDatabase:
                if x.name == toRem:
                    if x.name == "General":
                        break
                        # print ("Nie można usunąć kategorii " + x.name)
                    else:
                        CatDatabase.remove(x)
                        print("Usunięto kategorię " + x.name)
                        break

        except:
            print("Nie ma czego usuwać")
            self.setWindowIcon(QIcon('resources/Troll-faceProblem.jpg'))
            self.listView.setStyleSheet("background-image : url(resources/Troll-faceProblem.jpg);")

    ####################################################################################################################
    ####################################################################################################################

    # Dodawanie kategorii.
    # Element z textEditCat trafia do SelectCatBox-a i na koniec CatDataBase.
    def execAdd(self):
        # Trzeba zdekodować.
        text = self.textEditCat.toPlainText()

        # ToDo --------------------------------------------------------
        # self.addblock()
        # ToDo --------------------------------------------------------

        # Sprawdza, czy taka kategoria już istnieje.
        isCat = False
        for x in CatDatabase:
            if text == x.name:
                isCat = True

        try:
            if text is None or text == "":
                raise TypeError

            elif not isCat:
                self.SelectCatBox.addItem(text)
                CatDatabase.append(Category(text))
                self.textEditCat.clear()
                print("Dodano kategorię o nazwie " + text)

            else:
                self.textEditCat.clear()
                print("Istnieje już kategoria o nazwie " + text)

        except(TypeError):
            print("Proszę wpisać nazwę kategorii")

    # Usuwanie kategorii.
    # Powtórzenie funkcji removeCats.
    def execRem(self):
        self.removeCats()

    ####################################################################################################################
    ####################################################################################################################

    # ToDO - To ma coś robić, zmieniać i wyświetlać eventy na przykład
    # Na razie wyświetla istniejące kategorie.
    # Nie używane jak na razie.
    def onChanged(self):
        print(CatDatabase)
        print(self.SelectCatBox.itemText(self.SelectCatBox.currentIndex()))

    # Otwiera okienko z dodawaniem eventów.
    def open(self):
        # Tak można łatwo sprawdzić, czy lista jest pusta.
        # Przydatna rzecz.
        if not CatDatabase:
            print("Brak kategorii")

        else:
            dialog = AddEvent(self)
            dialog.exec()

    ####################################################################################################################
    ####################################################################################################################


# Loading i otwieranie widget-ów.
class AddEvent(QDialog, addEvent.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.label_4.hide()
        self.remindComb.hide()

        # Dodaje kategorie do combobox-a w oknie dodawania wydarzeń.
        for x in CatDatabase:
            self.catCombo.addItem(x.name)

    # Funkcja otwiera funkcje do przypomnień po zaznaczeniu przycisku.
    # Zauważ, że istnieje już taka funkcja, ale w innej klasie.
    def execRemBox(self):
        if self.label_4.isHidden():
            self.label_4.show()
            self.remindComb.show()
        else:
            self.label_4.hide()
            self.remindComb.hide()

    def accept(self):
        category = self.catCombo.itemText(self.catCombo.currentIndex())
        for cat in CatDatabase:
            if category == cat.name:

                # Nie wiem jak dynamicznie tworzyć obiekty, HELP!
                # def __init__(self, hour, day, month, alert=0, desc='', category="General"):
                # ToDo - ogarnąć alert przy dodawaniu eventów jak już ogarniemy zawiadamianie.
                # ToDo - ogarnąć ten konstruktor, bo brakuje mu przekazanych parametrów.

                newEvent = Event(self.timeEditComb.time().hour(), self.timeEditComb.time().minute(),
                                 self.calendarEd.monthShown(), 0, self.lineDesc.text(), cat.name)

                try:
                    if newEvent.__eq__(cat.heldEvents[-1]) is True:
                        print("Takie wydarzenie już istnieje")
                    else:
                        cat.eventToCat(newEvent)
                        print("Dodano wydarzenie " + self.lineDesc.text() + " do kategorii " + cat.name)

                # Jeśli kategoria jest pusta:
                except:
                    if not cat.heldEvents:
                        cat.eventToCat(newEvent)
                        print("Dodano wydarzenie " + self.lineDesc.text() + " do kategorii " + cat.name)
                    else:
                        raise TypeError


# Loading i ładowanie głównego okna programu
class GUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("GUI.ui", self)


# ToDo -------------------------------------------------------------
"""
class QtWidgets:
    pass
    """
# ToDo -------------------------------------------------------------


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
