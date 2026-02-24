import sys

from PySide6 import QtWidgets, QtGui, QtCore
from pages import MainWindow

def loadStyle():
    with open("style.qss", "r", encoding="UTF-8") as f:
        return f.read()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(loadStyle())
    app.setWindowIcon(QtGui.QIcon("logo.png"))
    app.setApplicationName("Лаб. 3. Вариант 4. Вишняков П.С.")

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())