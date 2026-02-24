from PySide6 import QtWidgets, QtGui, QtCore
from widgets import TaskBlock
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
            "Написать программу, определяющую, будут ли прямые A1x + B1y + C1 = 0 и A2x + B2y + C2 = 0 перпендикулярны. Если нет, то найти угол между ними.",
            ["A1", "B1", "C1", "A2", "B2", "C2"],
            ["Угол"],
            [self.findAngle]
        )

        self.centralLayout.addWidget(self.pageName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addLayout(self.taskBlock)
        self.centralLayout.addStretch()

    def findAngle(self, a1, b1, c1, a2, b2, c2):
        scalar = a1 * a2 + b1 * b2

        if scalar == 0:
            return "90°. Прямые перпендикулярны"
        
        angle = round(math.degrees(math.acos((abs(scalar)) / (math.sqrt(a1**2 + b1**2) * math.sqrt(a2**2 + b2**2)))), 1)

        if angle == 0:
            return "0°. Прямые параллельны"
        else:
            return f"{angle}°"