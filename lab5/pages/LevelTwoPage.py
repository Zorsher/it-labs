from PySide6 import QtWidgets, QtGui, QtCore
from widgets import TaskBlock, ImageWidget
import random

class LevelTwoPage(QtWidgets.QWidget):
    """Страница второго задания"""
    def __init__(self, parent = ...):
        super().__init__(parent)
        self.font_ = QtGui.QFont("Arial")
        self.font_.setBold(True)
        self.font_.setPixelSize(18)

        # основной макет
        self.centralLayout = QtWidgets.QVBoxLayout(self)
        self.pageName = QtWidgets.QLabel("Уровень 2")
        self.pageName.setFont(self.font_)

        # блок задания
        self.taskLabel = QtWidgets.QLabel("Дан одномерный массив размерности 20. Заполнить его случайными числами на отрезке [-25,25]. Если элемент массива четный, то прибавить к нему первый элемент, если нечетный – прибавить последний. Первый и последний элементы массива не изменять. Вывести исходный и полученный массивы на печать.")
        self.taskLabel.setWordWrap(True)

        self.generateButtonLayout = QtWidgets.QHBoxLayout()
        
        self.generateButton = QtWidgets.QPushButton("Сгенерировать массив")
        self.generateButton.clicked.connect(self.generateArray)

        self.generateButtonLayout.addStretch()
        self.generateButtonLayout.addWidget(self.generateButton)
        self.generateButtonLayout.addStretch()

        # массивы
        self.arrayLayout = QtWidgets.QVBoxLayout()

        self.firstArrayLabel = QtWidgets.QLabel("Оригинальный массив")
        self.firstArrayLabel.hide()

        self.firstArray = QtWidgets.QHBoxLayout()

        self.secondArrayLabel = QtWidgets.QLabel("Изменнённый массив")
        self.secondArrayLabel.hide()

        self.secondArray = QtWidgets.QHBoxLayout()

        self.arrayLayout.addWidget(self.firstArrayLabel)
        self.arrayLayout.addLayout(self.firstArray)
        self.arrayLayout.addSpacing(50)
        self.arrayLayout.addWidget(self.secondArrayLabel)
        self.arrayLayout.addLayout(self.secondArray)

        # добавление в основной лэйаут
        self.centralLayout.addWidget(self.pageName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addWidget(self.taskLabel)
        self.centralLayout.addLayout(self.generateButtonLayout)
        self.centralLayout.addLayout(self.arrayLayout)
        self.centralLayout.addStretch()

        self.createArray()

    # функция для создания массивов
    def createArray(self, len = 20):
        for i in range(0, len):
            self.firstArray.addWidget(QtWidgets.QLabel(""))
            self.secondArray.addWidget(QtWidgets.QLabel(""))

    # функция для генерации массива
    def generateArray(self):
        self.firstArrayLabel.show()
        self.secondArrayLabel.show()

        for i in range(0, 20):
            value = random.randint(-25, 25)
            self.firstArray.itemAt(i).widget().setText(f"{value}")

        firstValue = int(self.firstArray.itemAt(0).widget().text())
        lastValue = int(self.firstArray.itemAt(self.firstArray.count() - 1).widget().text())

        for j in range(0, 20):
            value = int(self.firstArray.itemAt(j).widget().text())

            if j not in (0, self.firstArray.count() - 1):
                if j % 2 == 0:
                    value+=firstValue
                elif j % 2 != 0:
                    value+=lastValue


            self.secondArray.itemAt(j).widget().setText(f"{value}")
        
