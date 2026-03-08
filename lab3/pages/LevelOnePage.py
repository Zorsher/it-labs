from PySide6 import QtWidgets, QtGui, QtCore
from widgets import TaskBlock

class LevelOnePage(QtWidgets.QWidget):
    """Страница первого задания"""
    def __init__(self, parent = ...):
        super().__init__(parent)
        font = QtGui.QFont("Arial")
        font.setBold(True)
        font.setPixelSize(18)

        # оснновной макет
        self.centralLayout = QtWidgets.QVBoxLayout(self)
        self.pageName = QtWidgets.QLabel("Уровень 1")
        self.pageName.setFont(font)

        # блок задания
        self.taskBlock = TaskBlock(
            "Написать программу нахождения суммы большего и меньшего из 3 чисел.",
            ["a", "b", "c"],
            ["sum"],
            [lambda a, b, c: max(a, b, c) + min(a, b, c)]
        )

        # добавляем элементы на страницу
        self.centralLayout.addWidget(self.pageName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addLayout(self.taskBlock)
        self.centralLayout.addStretch()