import sys

from PySide6 import QtWidgets, QtGui, QtCore
from pages import MainWindow

# загрузка стилей
def loadStyle():
    with open("style.qss", "r", encoding="UTF-8") as f:
        return f.read()


if __name__ == "__main__":
    # запуск потока приложения
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(loadStyle())
    app.setWindowIcon(QtGui.QIcon("images/logo.png"))
    app.setApplicationName("Лаб. 6. Вариант 4. Вишняков П.С. ИВТ-11")

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())