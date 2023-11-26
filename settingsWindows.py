import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Settings(QMainWindow):
    def __init__(self):
        super(Settings, self).__init__()
        uic.loadUi('settingsgame.ui', self)

        self.pixmap = QPixmap('set.png')
        self.pixmap = self.pixmap.scaled(self.label_4.size(), Qt.KeepAspectRatioByExpanding)
        self.label_4.setPixmap(self.pixmap)
        self.label_4.adjustSize()

    def save_settings(self):
        volume_music = self.horizontalSlider.value()
        volume_game = self.horizontalSlider_2.value()

        conn = sqlite3.connect('settings.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS settings (volume_music, volume_game)")
        cursor.execute("SELECT COUNT(*) FROM settings")
        row_count = cursor.fetchone()[0]
        if row_count == 0:
            cursor.execute("INSERT INTO settings (volume_music, volume_game) VALUES (?, ?)",
                           (volume_music, volume_game))
        cursor.execute("UPDATE settings SET volume_music = ?, volume_game = ?", (volume_music, volume_game))
        conn.commit()
        conn.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('maingame.ui', self)

        self.settings = Settings()
        self.settings.pushButton.clicked.connect(self.closeSettings)

        self.pixmap = QPixmap('img.png')
        self.pixmap = self.pixmap.scaled(self.label.size(), Qt.KeepAspectRatioByExpanding)
        self.label.setPixmap(self.pixmap)
        self.label.adjustSize()

        self.pushButton_4.clicked.connect(self.open_settings)

    def closeSettings(self):
        self.settings.save_settings()
        self.settings.close()
        self.show()

    def open_settings(self):
        try:
            conn = sqlite3.connect('settings.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM settings")
            result = cursor.fetchone()
            if result is None:
                volume_music = 70
                volume_game = 80
                cursor.execute("INSERT INTO settings (volume_music, volume_game) VALUES (?, ?)",
                               (volume_music, volume_game))
            else:
                volume_music, volume_game = result
            conn.close()
        except Exception:
            volume_music = 70
            volume_game = 80

        self.settings.horizontalSlider.setValue(volume_music)
        self.settings.horizontalSlider_2.setValue(volume_game)

        self.settings.show()
        self.close()
