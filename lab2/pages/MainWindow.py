from PySide6 import QtWidgets, QtGui, QtCore
from pages.HelloPage import HelloPage
from pages.TaskPage import TaskPage

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
        self.taskPage = TaskPage(self)

        # добавление в макет
        self.centralLayout.addWidget(self.helloPage)
        self.centralLayout.addWidget(self.taskPage)

    # переход на следующую страницу
    def nextPage(self):
        self.adjustSize()
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.centralLayout.setCurrentIndex(self.centralLayout.currentIndex() + 1)