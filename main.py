import select
import sys
import addEvent
import editEvent

from GUI import Ui_Dialog
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtGui, QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)

import pickle

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# ToDo -------------------------------------------------------------


mainWindow = None
selectedEvent = ['gfs', 'Work', '17.05.2022', '00:00:00']
ogModel = None
hidden = []

def fuckGarbageColletor(selecteevent):
    return selecteevent

# Co to jest?
class QtWidgets:
    pass


# To coś jest do tworzenia label-ów dynamicznie.
class ExampleLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("Example")
        self.setGeometry(100, 100, 100, 100)
        self.show()


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


class Event:
    # W konstruktorach klas i deklaracji funkcji można dawać domyślne parametry.
    # Brakowało mi tego w Javie.
    # Są one używane, jeśli do konstruktora lub funkcji zostanie przekazany pusty parametr.
    def __init__(self, hour, minutes, day, month, year, alert=0, text="", category="General"):
        self.day = day
        self.hour = hour
        self.minutes = minutes
        self.month = month
        self.text = text
        self.category = category
        self.alert = alert
        self.year = year

        # To może być głupie, zastanowię się potem.
        # Widzę potencjalny NullPointerException.
        # Dobra to jest głupie, nie rób tak nigdy.
        if self.alert != 0:
            self.alert = alert

    # Metoda sprawdza, czy parametry dwóch obiektów są takie same.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


# Główne okno
class Window(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.firstAddCats()
        self.loadEvents()

    ####################################################################################################################
    ####################################################################################################################

    #Zabijcie mnie bruh
    def onChanged2(self, text):
        global hidden
        ogModel2 = self.listView.model()
        for index in range(ogModel2.rowCount()):
            try:
                expression = (ogModel2.data(ogModel2.index(index, 0)).split()[0])
            except:
                continue
            #expression = str(expression)
            if (expression.startswith(self.lineEdit.text()) == False):
                hidden.append(ogModel2.data(ogModel2.index(index, 0)).split())
                ogModel2.removeRow(index)
        for x in hidden:
            if x[0].startswith(self.lineEdit.text()):
                hidden.remove(x)
                self.displayEvent()

        self.saveEvents()

    def on_clicked(self, index):
        self.listView.setCurrentIndex(index)
        item = self.listView.currentIndex()
        itemdata = item.data()
        splitted = itemdata.split("\t")
        for x in splitted:
            if x == "":
                splitted.remove(x)

        splitted[0] = splitted[0][2:]

        #Wooow ale to głupie
        selectedEvent.clear()
        for x in splitted:
            selectedEvent.append(x)

        dialog = editEvent(self)
        dialog.exec()

    # Dodawanie kategorii z CatDatabase do SelectCatBox-a na przy otwarciu okna.
    def firstAddCats(self):
        for x in CatDatabase:
            self.SelectCatBox.addItem(x.name)

    # Element z SelectCatBox jest usuwany z SelectCatBox-a i z CatDatabase.
    def removeCats(self):

        try:
            # O dziwo jak to wkleję bezpośrednio, to nie działa, jak powinno. Nie porządkować!
            toRem = self.SelectCatBox.itemText(self.SelectCatBox.currentIndex())

            # Jeszcze sobie wybierzemy nazwę/nazwy kategorii, których nie usuwamy.
            # General na pewno.
            if toRem == general.name:
                print("Nie można usunąć kategorii " + toRem)
            else:
                self.SelectCatBox.removeItem(self.SelectCatBox.currentIndex())

            for x in CatDatabase:
                if x.name == toRem:
                    if x.name == general.name:
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

        # Ważne, żeby po usunięciu kategorii zniknęły jej Eventy z ViewList-y.
        self.displayEvent()

    ####################################################################################################################
    ####################################################################################################################

    # Pod te funkcje podpięte są przyciski.

    # Dodawanie kategorii.
    def execAdd(self):
        # Trzeba zdekodować.
        text = self.textEditCat.toPlainText()

        # ToDo --------------------------------------------------------
        # Co to jest?
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
    def execRem(self):
        self.removeCats()
#
    #Zapisywanie kategorii (i ich eventów)
    def saveEvents(self):
        with open('config.dictionary', 'wb') as configfile:
            toSave = []
            for x in CatDatabase:
                toSave.append(x)

            pickle.dump((toSave), configfile)

    def loadEvents(self):
        try:
            pass
        except:
            pass

    # Otwiera okienko z dodawaniem eventów.
    def open(self):
        # Tak można łatwo sprawdzić, czy lista jest pusta.
        # Przydatna rzecz.
        if not CatDatabase:
            print("Brak kategorii")

        else:
            dialog = AddEvent(self)
            dialog.exec()

        # IDEA:
        # Przyjmujemy string z SelectCatBox-a z nazwą aktualnie wybranej kategorii.
        # Szukamy tej kategorii w CatDataBase po nazwie i do specjalnie nowo stworzonej tablicy wrzucamy jej eventy.
        # Wypisujemy eventy do ListView.

    # Wyświetla wydarzenia z wybranej kategorii.
    def displayEvent(self, toLoad=[]):

        if (len(toLoad) == 0):
            toLoad = CatDatabase

        # Ustawianie viewList z poziomu okna Window.
        # To ma tu być, bo wtedy dynamicznie zmieniają się wydarzenia w zależności od kategorii.
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)

        # Nagłówek i uzupełnianie viewList.
        row = self.listView.model()
        # label = QtGui.QStandardItem("Treść\t\tKategoria\tData\t\t\tGodzina")
        # row.appendRow(label)

        actCat = self.SelectCatBox.itemText(self.SelectCatBox.currentIndex())

        for x in CatDatabase:
            if x.name == self.SelectCatBox.itemText(self.SelectCatBox.currentIndex()):
                actCat = self.SelectCatBox.itemText(self.SelectCatBox.currentIndex())

        dispEvents = []

        # Wypisuje nazwę kategorii przy zmianie kategorii w SelectCatBox.
        # print(actCat)

        for x in CatDatabase:
            if x.name == actCat:
                dispEvents = x.heldEvents

        for e in dispEvents:
            if e.text.startswith(self.lineEdit.text()):
                item = QtGui.QStandardItem("  " + e.text + "\t\t" + e.category + "\t\t"
                                           + str(e.day).zfill(2) + "." + str(e.month).zfill(2) + "." + str(e.year).zfill(2)
                                           + "\t\t" + str(e.hour).zfill(2) + ":" + str(e.minutes).zfill(2) + ":00")
                row.appendRow(item)

        #self.listView.setCurrentIndex(self.entry.indexFromItem(item))


    ####################################################################################################################
    ####################################################################################################################

    # ToDO - To ma coś robić, zmieniać i wyświetlać eventy na przykład
    # Na razie wyświetla istniejące kategorie.
    # Nie używane jak na razie.
    def onChanged(self):
        print(CatDatabase)
        print(self.SelectCatBox.itemText(self.SelectCatBox.currentIndex()))

    # Może kiedyś tego użyjemy.
    def addLabel(self):
        self.widget = ExampleLabel(self)

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
                                 self.calendarEd.selectedDate().day(), self.calendarEd.selectedDate().month(),
                                 self.calendarEd.selectedDate().year(), 0, self.lineDesc.text(), cat.name)

                try:
                    # Mogą być te same nazwy. To od użytkownika zależy.
                    """
                    if newEvent.__eq__(general.heldEvents[-1]) is True:
                         print("Takie wydarzenie już istnieje")
                    """
                    # Zawsze dodajemy do generala i/albo innej kategorii.
                    # General ma mieć wszystkie wydarzenia
                    if cat.name != general.name:
                        cat.eventToCat(newEvent)
                        general.eventToCat(newEvent)
                        print("Dodano wydarzenie " + self.lineDesc.text() + " do kategorii " + cat.name)
                        print("Dodano wydarzenie " + self.lineDesc.text() + " do kategorii " + general.name)
                        self.lineDesc.clear()
                    else:
                        cat.eventToCat(newEvent)
                        print("Dodano wydarzenie " + self.lineDesc.text() + " do kategorii " + cat.name)
                        self.lineDesc.clear()

                # Jeśli kategoria jest pusta:
                except:
                    if not cat.heldEvents:
                        if cat.name != general.name:
                            cat.eventToCat(newEvent)
                            general.eventToCat(newEvent)
                            print("Dodano wydarzenie " + self.lineDesc.text() + " do kategorii " + cat.name)
                            print("Dodano wydarzenie " + self.lineDesc.text() + " do kategorii " + general.name)
                            self.lineDesc.clear()
                        else:
                            cat.eventToCat(newEvent)
                            print("Dodano wydarzenie " + self.lineDesc.text() + " do kategorii " + cat.name)
                            self.lineDesc.clear()
                    else:
                        raise TypeError


        # Wyświetlanie wydarzeń po zamknięciu okna przyciskiem OK.
        # Fajnie jakby zadziałało.
        mainWindow.displayEvent()




# Loading i ładowanie głównego okna programu
class GUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("GUI.ui", self)


class editEvent(QDialog, editEvent.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.label_4.hide()
        self.remindComb.hide()

        for x in CatDatabase:
            self.catCombo.addItem(x.name)

        self.setupik()


    def setupik(self):
        self.lineDesc.setText(selectedEvent[0])
        self.calendarEd.setSelectedDate(QDate(int(selectedEvent[2][6:]), int(selectedEvent[2][0:1]), int(selectedEvent[2][3:4])))
        time = selectedEvent[3].split(":")
        self.timeEditComb.setTime(QTime(int(time[0]), int(time[1]), int(time[2])))

        #Wyszukiwanie obecnej kategorii
        i = 0
        for x in CatDatabase:
            if x.name == selectedEvent[1]:
                self.catCombo.setCurrentIndex(i)
            i += 1

    def execRemBox(self):
        if self.label_4.isHidden():
            self.label_4.show()
            self.remindComb.show()
        else:
            self.label_4.hide()
            self.remindComb.hide()

    def accept(self):
        category = self.catCombo.itemText(self.catCombo.currentIndex())

        #Pętla do szukania eventów do nadpisania
        for x in CatDatabase:
            for y in x.heldEvents:
                if selectedEvent[0] == y.text:
                    x.heldEvents.remove(y)

        for cat in CatDatabase:
            if category == cat.name:

                # Nie wiem jak dynamicznie tworzyć obiekty, HELP!
                # def __init__(self, hour, day, month, alert=0, desc='', category="General"):
                # ToDo - ogarnąć alert przy dodawaniu eventów jak już ogarniemy zawiadamianie.
                # ToDo - ogarnąć ten konstruktor, bo brakuje mu przekazanych parametrów.

                newEvent = Event(self.timeEditComb.time().hour(), self.timeEditComb.time().minute(),
                                 self.calendarEd.selectedDate().day(), self.calendarEd.selectedDate().month(),
                                 self.calendarEd.selectedDate().year(), 0, self.lineDesc.text(), cat.name)

                try:

                    # Mogą być te same nazwy. To od użytkownika zależy.
                    """
                    if newEvent.__eq__(general.heldEvents[-1]) is True:
                         print("Takie wydarzenie już istnieje")
                    """
                    # Zawsze dodajemy do generala i/albo innej kategorii.
                    # General ma mieć wszystkie wydarzenia
                    if cat.name != general.name:
                        cat.eventToCat(newEvent)
                        general.eventToCat(newEvent)
                        print("Edytowano wydarzenie " + self.lineDesc.text() + " w kategorii " + cat.name)
                        print("Edytowano wydarzenie " + self.lineDesc.text() + " w kategorii " + general.name)
                        self.lineDesc.clear()
                    else:
                        cat.eventToCat(newEvent)
                        print("Edytowano wydarzenie " + self.lineDesc.text() + " w kategorii " + cat.name)
                        self.lineDesc.clear()

                # Jeśli kategoria jest pusta:
                except:
                    if not cat.heldEvents:
                        if cat.name != general.name:
                            cat.eventToCat(newEvent)
                            general.eventToCat(newEvent)
                            print("Edytowano wydarzenie " + self.lineDesc.text() + " w kategorii " + cat.name)
                            print("Edytowano wydarzenie " + self.lineDesc.text() + " w kategorii " + general.name)
                            self.lineDesc.clear()
                        else:
                            cat.eventToCat(newEvent)
                            print("Edytowano wydarzenie " + self.lineDesc.text() + " w kategorii " + cat.name)
                            self.lineDesc.clear()
                    else:
                        raise TypeError

                mainWindow.displayEvent()
                #ładne zamykanie okienka :3
                self.reject()



# Standardowe wejście do skryptu Pythona.
# Nie musi istnieć, ale w dużych projektach wiele porządkuje.
# Jak go nie ma, to interpreter jedzie po otwartym pliku od góry na dół.
# Odpowiednik main z java + ładnie wygląda i wiadomo gdzie zacząć.
if __name__ == "__main__":
    general = Category("General")
    work = Category("Work")
    Ludwin = Category("Loudwin")


    CatDatabase = [general, work, Ludwin]
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    mainWindow = win
    sys.exit(app.exec())
