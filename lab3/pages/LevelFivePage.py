from PySide6 import QtWidgets, QtGui, QtCore
from widgets import TaskBlock

class LevelFivePage(QtWidgets.QWidget):
    """Страница пятого задания"""
    def __init__(self, parent = ...):
        super().__init__(parent)
        font = QtGui.QFont("Arial")
        font.setBold(True)
        font.setPixelSize(18)

        # основной макет
        self.centralLayout = QtWidgets.QVBoxLayout(self)
        self.pageName = QtWidgets.QLabel("Оператор выбора")
        self.pageName.setFont(font)

        # блок задания
        self.taskBlock = TaskBlock(
            "Составить программу, позволяющую получить словесное описание школьных отметок (1 — плохо, 2 — неудовлетворительно, 3 — удовлетворительно, 4 — хорошо, 5 — отлично).",
            ["Оценка"],
            ["Оценка"],
            [self.gradeCheck]
        )

        # добавляем элементы на страницу
        self.centralLayout.addWidget(self.pageName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addLayout(self.taskBlock)
        self.centralLayout.addStretch()

    # функция для получения словесного описания школьных отметок
    def gradeCheck(self, grade):
        grade = int(grade)

        if grade == 1:
            return f"{grade} - плохо"
        if grade == 2:
            return f"{grade} - неудовлетворительно"
        if grade == 3:
            return f"{grade} - удовлетворительно"
        if grade == 4:
            return f"{grade} - хорошо"
        if grade == 5:
            return f"{grade} - отлично"
        else:
            return f"{grade} - не существует"