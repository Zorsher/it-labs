from PySide6 import QtWidgets, QtGui, QtCore
from pages.HelloPage import HelloPage
from pages.LevelOnePage import LevelOnePage
from pages.LevelTwoPage import LevelTwoPage

class MainWindow(QtWidgets.QWidget):
    """
    Основное окно приложения
    """
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        # основной макет
        self.centralLayout = QtWidgets.QVBoxLayout(self)

        self.stackedLayout = QtWidgets.QStackedLayout()

        # приветственное окно
        self.helloPage = HelloPage(self)

        # окна с заданиями
        self.levelOnePage = LevelOnePage(self)
        self.levelTwoPage = LevelTwoPage(self)

        self.stackedLayout.addWidget(self.helloPage)
        self.stackedLayout.addWidget(self.levelOnePage)
        self.stackedLayout.addWidget(self.levelTwoPage)

        # кнопки для навигации
        self.buttonsLayout = QtWidgets.QHBoxLayout()

        self.previousButton = QtWidgets.QPushButton("Назад")
        self.previousButton.clicked.connect(self.previousPage)
        self.previousButton.setObjectName("red")
        self.previousButton.hide()

        self.nextButton = QtWidgets.QPushButton("Вперёд")
        self.nextButton.setObjectName("green")
        self.nextButton.clicked.connect(self.nextPage)

        self.buttonsLayout.addWidget(self.previousButton)
        self.buttonsLayout.addWidget(self.nextButton)

        self.centralLayout.addLayout(self.stackedLayout)
        self.centralLayout.addLayout(self.buttonsLayout)
        
        self.stackedLayout.currentChanged.connect(self.pageChanged)

    # метод для отображения/скрытия кнопок в зависимости от текущей страницы
    def pageChanged(self):
        if self.stackedLayout.currentIndex() - 1 == 0:
            self.previousButton.hide()
        else:
            self.previousButton.show()

        if self.stackedLayout.currentIndex() + 1 >= self.stackedLayout.count():
            self.nextButton.hide()
        else:
            self.nextButton.show()

    # методы для переключения страниц
    def nextPage(self):
        self.stackedLayout.setCurrentIndex(self.stackedLayout.currentIndex() + 1)

    def previousPage(self):
        self.stackedLayout.setCurrentIndex(self.stackedLayout.currentIndex() - 1)
