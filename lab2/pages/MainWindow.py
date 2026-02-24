from PySide6 import QtWidgets, QtGui, QtCore
from pages.HelloPage import HelloPage
from pages.TaskPage import TaskPage

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 600)

        self.centralLayout = QtWidgets.QStackedLayout(self)

        self.helloPage = HelloPage(self)
        self.helloPage.nextPage.connect(self.nextPage)

        self.taskPage = TaskPage(self)


        self.centralLayout.addWidget(self.helloPage)
        self.centralLayout.addWidget(self.taskPage)

    def nextPage(self):
        self.adjustSize()
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.centralLayout.setCurrentIndex(self.centralLayout.currentIndex() + 1)