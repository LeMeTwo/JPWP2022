import sys
import time

from GUI import Ui_Dialog
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)


class Window(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.count = 1

    # elf.connectSignalsSlots()
    # def connectSignalsSlots(self):
    # self.action_Exit.triggered.connect(self.close)
    # self.action_Find_Replace.triggered.connect(self.GUI)
    # self.action_About.triggered.connect(self.about)

    def accept(self):
        print("Działą")

    def reject(self):
        print("(nie) Działa")

    def onButtonClick(self):
        self.progressBarGit.setValue(self.count)
        try:
            if ((int(self.lineEdit7Shit.text())) >= 0 and (self.count < 100)):
                self.count += int(self.lineEdit7Shit.text())
                self.progressBarGit.setValue(int(self.count))
            else:
                if ((int(self.lineEdit7Shit.text())) <= -1 and (self.progressBarGit.value() <= 100)):
                    while self.count <= 100:
                        self.count += 1
                        time.sleep(0.01)
                        self.progressBarGit.setValue(self.count)
                        print("Dziauua")
                else:
                    if (self.count > 100):
                        self.count = (self.progressBarGit.value())
                    else:
                        self.count = 4
                    self.progressBarGit.setValue(self.count)
            print(self.count)
        except:
            print("Error")

    def onButtonClick2(self):
        print("bruh")

    def findAndReplace(self):
        dialog = GUI(self)
        dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )


class GUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("GUI.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
