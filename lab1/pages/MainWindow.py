from PySide6 import QtWidgets, QtGui, QtCore
from pages.HelloPage import HelloPage
from pages.CalculatorPage import CalculatorPage

class MainWindow(QtWidgets.QWidget):
    """
    Основное окно приложения
    """
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 600)

        # основной макет
        self.centralLayout = QtWidgets.QStackedLayout(self)

        # приветственное окно
        self.helloPage = HelloPage(self)
        self.helloPage.nextPage.connect(self.nextPage)

        # окно с заданием
        self.calcPage = CalculatorPage(self)

        # добавление в макет
        self.centralLayout.addWidget(self.helloPage)
        self.centralLayout.addWidget(self.calcPage)

    # переход на следующую страницу
    def nextPage(self):
        self.centralLayout.setCurrentIndex(self.centralLayout.currentIndex() + 1)