from PySide6 import QtWidgets, QtGui, QtCore
from widgets import TaskBlock, ImageWidget
import math

class LevelOnePage(QtWidgets.QWidget):
    def __init__(self, parent = ...):
        super().__init__(parent)
        font = QtGui.QFont("Arial")
        font.setBold(True)
        font.setPixelSize(18)

        self.centralLayout = QtWidgets.QVBoxLayout(self)
        self.pageName = QtWidgets.QLabel("Уровень 1")
        self.pageName.setFont(font)

        self.funcsLayout = QtWidgets.QHBoxLayout()
        self.funcsLayout.addStretch()

        for i in (0, 1):
            self.funcsLayout.addWidget(QtWidgets.QLabel(f"{i+1}."))
            self.funcsLayout.addWidget(ImageWidget(f"formula{i}.jpg"))

        self.funcsLayout.addStretch()

        self.taskBlock = TaskBlock(
            "Нахождение значения функции по её аналитической формуле и как сумму с использованием оператора for. |x| <= pi/2",
            ["x"],
            ["Значение функции 1", "Значение функции 2"],
            [self.valueOneChanged, self.valueTwoChanged]
        )

        self.centralLayout.addWidget(self.pageName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addLayout(self.funcsLayout)
        self.centralLayout.addLayout(self.taskBlock)
        self.centralLayout.addStretch()

    def valueOneChanged(self, x):
        if not abs(x) <= math.pi/2:
            return "x не находится в промежутке |x| <= pi/2"
        
        return (math.pi/4)*math.sin(x)
        
    def valueTwoChanged(self, x):
        if not abs(x) <= math.pi/2:
            return "x не находится в промежутке |x| <= pi/2"
        
        s = 0

        for n in range(1, 51):
            s+=math.cos(2*n*x)/((2*n - 1)*(2*n + 1))

        return 0.5 - s
