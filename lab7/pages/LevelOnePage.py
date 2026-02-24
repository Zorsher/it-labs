from PySide6 import QtWidgets, QtGui, QtCore
import random

class LevelOnePage(QtWidgets.QWidget):
    def __init__(self, parent = ...):
        super().__init__(parent)
        self.font_ = QtGui.QFont("Arial")
        self.font_.setBold(True)
        self.font_.setPixelSize(18)

        self.centralLayout = QtWidgets.QVBoxLayout(self)
        self.pageName = QtWidgets.QLabel("Уровень 1")
        self.pageName.setFont(self.font_)

        self.taskLabel = QtWidgets.QLabel("Дана строка, состоящая из групп нулей и единиц. Найти и вывести на экран группы с четным количеством символов.")
        self.taskLabel.setWordWrap(True)


        self.inputArea = QtWidgets.QLineEdit()

        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.listWidget.addItems(["a", "b", "c"])

        self.listWidget.itemClicked.connect(self.itemClicked)


        self.centralLayout.addWidget(self.pageName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addWidget(self.listWidget)
        
    def itemClicked(self, item: QtWidgets.QListWidgetItem):
        