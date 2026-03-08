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
        self.inputArea.returnPressed.connect(self.addWord)

        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.itemSelectionChanged.connect(self.itemSelected)

        self.groupCountLabel = QtWidgets.QLabel("Группы с чётным количеством символов")
        self.groupLabel = QtWidgets.QLabel()

        self.groupCountLabel.hide()
        self.groupLabel.hide()

        self.centralLayout.addWidget(self.pageName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addWidget(self.taskLabel)
        self.centralLayout.addWidget(self.inputArea)
        self.centralLayout.addWidget(self.listWidget)
        self.centralLayout.addWidget(self.groupCountLabel)
        self.centralLayout.addWidget(self.groupLabel)
        
    def addWord(self):
        sentence = self.inputArea.text()

        if sentence == "" or sentence.count(" ") == len(sentence) or len(sentence) > (sentence.count("0") + sentence.count("1") + sentence.count(" ")):
            return

        self.inputArea.clear()
        self.listWidget.addItem(sentence)

    def itemSelected(self):
        sentence = self.listWidget.selectedItems()[0].text().split(" ")
        sortedItem = []

        for word in sentence:
            if len(word) % 2 == 0:
                sortedItem.append(word)

        if len(sortedItem) == 0:
            self.groupCountLabel.hide()
            self.groupLabel.hide()
            return
        
        self.groupCountLabel.show()
        self.groupLabel.show()

        self.groupLabel.setText(" ".join(sortedItem))

