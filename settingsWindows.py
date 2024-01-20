import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from game import game
from settings import *
from map_creation import *


def middle_graphics_fun():
    con__ = sqlite3.connect(f"save\\settings.db")
    cur__ = con.cursor()
    cur__.execute(f"""UPDATE graphics SET num_reys = {str(151)}""")
    con__.commit()
    con__.close()


def hight_graphics_fun():
    con__ = sqlite3.connect(f"save\\settings.db")
    cur__ = con.cursor()
    cur__.execute(f"""UPDATE graphics SET num_reys = {str(301)}""")
    con__.commit()
    con__.close()


def low_graphics_fun():
    con__ = sqlite3.connect(f"save\\settings.db")
    cur__ = con.cursor()
    cur__.execute(f"""UPDATE graphics SET num_reys = {str(75)}""")
    con__.commit()
    con__.close()


class Settings(QMainWindow):
    def __init__(self):
        super(Settings, self).__init__()
        uic.loadUi('ui\\settingsgame.ui', self)

        self.pixmap = QPixmap('images\\set.png')
        self.pixmap = self.pixmap.scaled(self.label_4.size(), Qt.KeepAspectRatioByExpanding)
        self.label_4.setPixmap(self.pixmap)
        self.label_4.adjustSize()
        self.low_graphics.clicked.connect(low_graphics_fun)
        self.middle_graphics.clicked.connect(middle_graphics_fun)
        self.hight_graphics.clicked.connect(hight_graphics_fun)

    def save_settings(self):
        pass


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui\\maingame.ui', self)

        self.settings = Settings()
        self.settings.pushButton.clicked.connect(self.closeSettings)

        self.pixmap = QPixmap('images\\img.png')
        self.pixmap = self.pixmap.scaled(self.label.size(), Qt.KeepAspectRatioByExpanding)
        self.label.setPixmap(self.pixmap)
        self.label.adjustSize()

        self.pushButton_4.clicked.connect(self.open_settings)
        self.pushButton_2.clicked.connect(self.open_new_game)
        self.pushButton.clicked.connect(self.open_game)
        self.pushButton_3.clicked.connect(makemap)
        self.pushButton_5.clicked.connect(self.mygame)

    def closeSettings(self):
        self.settings.save_settings()
        self.settings.close()
        self.show()

    def open_settings(self):
        self.settings.show()
        self.close()

    def open_game(self):
        # self.close()
        try:
            game()
        except Exception as exc:
            print(exc)

    def open_new_game(self):
        # self.close()
        try:
            game(True)
        except Exception as exc:
            print(exc)

    def mygame(self):
        try:
            game(True, True)
        except Exception as exc:
            print(exc)
