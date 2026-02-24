from PySide6 import QtWidgets, QtGui, QtCore
from widgets import TaskBlock
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
            "В небоскребе N этажей и всего один подъезд; на каждом этаже по 3 квартиры; лифт может останавливаться только на нечетных этажах. Человек садится в лифт и набирает номер нужной ему квартиры M. На какой этаж должен доставить лифт пассажира?",
            ["N", "M"],
            ["Этаж"],
            [lambda N, M: (math.ceil(M / 3) if math.ceil(M / 3) % 2 != 0 else math.ceil(M / 3) - 1) if M <= N * 3 else None]
        )

        self.centralLayout.addWidget(self.pageName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addLayout(self.taskBlock)
        self.centralLayout.addStretch()

