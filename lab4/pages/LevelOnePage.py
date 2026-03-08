from PySide6 import QtWidgets, QtGui, QtCore
from widgets import TaskBlock, ImageWidget
import math

class LevelOnePage(QtWidgets.QWidget):
    """Страница первого задания"""
    def __init__(self, parent = ...):
        super().__init__(parent)
        font = QtGui.QFont("Arial")
        font.setBold(True)
        font.setPixelSize(18)

        # основной макет
        self.centralLayout = QtWidgets.QVBoxLayout(self)
        self.pageName = QtWidgets.QLabel("Уровень 1")
        self.pageName.setFont(font)

        # макет для формул
        self.funcsLayout = QtWidgets.QHBoxLayout()
        self.funcsLayout.addStretch()

        for i in (0, 1):
            self.funcsLayout.addWidget(QtWidgets.QLabel(f"{i+1}."))
            self.funcsLayout.addWidget(ImageWidget(f"formula{i}.jpg"))

        self.funcsLayout.addStretch()

        # блок задания
        self.taskBlock = TaskBlock(
            "Нахождение значения функции по её аналитической формуле и как сумму с использованием оператора for. |x| <= pi/2",
            ["x"],
            ["Значение функции 1", "Значение функции 2"],
            [self.valueOneChanged, self.valueTwoChanged]
        )

        # добавляем элементы на страницу
        self.centralLayout.addWidget(self.pageName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addLayout(self.funcsLayout)
        self.centralLayout.addLayout(self.taskBlock)
        self.centralLayout.addStretch()

    # функция для нахождения значения функции по её аналитической формуле
    def valueOneChanged(self, x):
        if not abs(x) <= math.pi/2:
            return "x не находится в промежутке |x| <= pi/2"
        
        return (math.pi/4)*math.sin(x)
    
    # функция для нахождения значения функции как сумму с использованием оператора for
    def valueTwoChanged(self, x):
        if not abs(x) <= math.pi/2:
            return "x не находится в промежутке |x| <= pi/2"
        
        s = 0

        for n in range(1, 51):
            s+=math.cos(2*n*x)/((2*n - 1)*(2*n + 1))

        return 0.5 - s
