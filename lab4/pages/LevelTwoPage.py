from PySide6 import QtWidgets, QtGui, QtCore
from widgets import TaskBlock, ImageWidget
import math

class LevelTwoPage(QtWidgets.QWidget):
    def __init__(self, parent = ...):
        super().__init__(parent)
        font = QtGui.QFont("Arial")
        font.setBold(True)
        font.setPixelSize(18)

        self.centralLayout = QtWidgets.QVBoxLayout(self)
        self.pageName = QtWidgets.QLabel("Уровень 2")
        self.pageName.setFont(font)

        self.taskBlock = TaskBlock(
            "По введённым с клавиатуры значениям A, B, n и X вычислить S",
            ["A", "B", "n", "X"],
            ["S"],
            [self.valueChanged]
        )

        self.centralLayout.addWidget(self.pageName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addWidget(ImageWidget("formula2.jpg"), alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addLayout(self.taskBlock)
        self.centralLayout.addStretch()

    def valueChanged(self, A, B, n, X):
        s = 0

        for i in range(2, 2*int(n), 2):
            s+=((X - A*B*i)/(X + A*B*i))

        return (A+B)*s

