import sys
from PyQt5.QtWidgets import QApplication
from settingsWindows import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
