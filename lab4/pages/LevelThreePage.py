from PySide6 import QtWidgets, QtGui, QtCore
from widgets import TaskBlock, ScrollArea
import math

class LevelThreePage(QtWidgets.QWidget):
    def __init__(self, parent = ...):
        super().__init__(parent)
        font = QtGui.QFont("Arial")
        font.setBold(True)
        font.setPixelSize(18)

        self.centralLayout = QtWidgets.QVBoxLayout(self)
        self.pageName = QtWidgets.QLabel("Уровень 3")
        self.pageName.setFont(font)

        self.taskBlock = TaskBlock(
            "Вычислить количество значений функции y=x², пренадлежащих заданнному интервалу (y0, y1)",
            ["y0", "y1", "step"],
            [None],
            [self.findX]
        )

        self.valuesBoxLayout = QtWidgets.QHBoxLayout()

        # Левый лэйаут
        self.whileLayout = QtWidgets.QVBoxLayout()

        self.whileLabel = QtWidgets.QLabel("Цикл While")
        self.whileLabel.setFont(font)

        self.whileScrollArea = ScrollArea()

        self.whileResultLabel = QtWidgets.QLabel()
        self.whileResultLabel.setWordWrap(True)

        self.whileScrollArea.addWidget(self.whileResultLabel)

        self.whileLayout.addWidget(self.whileLabel)
        self.whileLayout.addWidget(self.whileScrollArea)

        # Правый лэйаут
        self.repeatLayout = QtWidgets.QVBoxLayout()

        self.repeatLabel = QtWidgets.QLabel("Цикл Repeat")
        self.repeatLabel.setFont(font)

        self.repeatScrollArea = ScrollArea()

        self.repeatResultLabel = QtWidgets.QLabel()
        self.repeatResultLabel.setWordWrap(True)

        self.repeatScrollArea.addWidget(self.repeatResultLabel)

        self.repeatLayout.addWidget(self.repeatLabel)
        self.repeatLayout.addWidget(self.repeatScrollArea)

        self.valuesBoxLayout.addLayout(self.whileLayout)
        self.valuesBoxLayout.addLayout(self.repeatLayout)

        self.centralLayout.addWidget(self.pageName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addLayout(self.taskBlock)
        self.centralLayout.addLayout(self.valuesBoxLayout)
        # self.centralLayout.addStretch()

    def findX(self, y0, y1, step):
        if y0 < 0 or y1 < 0 or step <= 0:
            return None

        y = y0

        print(y0, y1, step)

        whileText = ""
        repeatText = ""

        while y < y1:
            whileText+=f"(x={round(math.sqrt(y), 2)}, y = {y}), (x = {round(-math.sqrt(y), 2) if math.sqrt(y) != 0 else 0}, y = {y})\n" 
            y+=step

        self.whileResultLabel.setText(whileText)

        y = y0

        while True:
            repeatText+=f"(x={round(math.sqrt(y), 2)}, y = {y}), (x = {round(-math.sqrt(y), 2) if math.sqrt(y) != 0 else 0}, y = {y})\n" 
            
            if y >= y1:
                break 

            y+=step

        self.repeatResultLabel.setText(repeatText)