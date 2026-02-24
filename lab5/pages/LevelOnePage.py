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

        self.taskLabel = QtWidgets.QLabel("Дан одномерный массив размерности 20. Заполнить его случайными числами на отрезке [-25,25]. Вычислить  сумму всех ненулевых элементов с нечетными индексами. Вывести на печать исходный массив и полученные результаты.")
        self.taskLabel.setWordWrap(True)

        self.generateButtonLayout = QtWidgets.QHBoxLayout()
        
        self.generateButton = QtWidgets.QPushButton("Сгенерировать массив")
        self.generateButton.clicked.connect(self.generateArray)

        self.generateButtonLayout.addStretch()
        self.generateButtonLayout.addWidget(self.generateButton)
        self.generateButtonLayout.addStretch()

        # массив
        self.arrayLayout = QtWidgets.QVBoxLayout()

        self.arrayLabel = QtWidgets.QLabel("Одномерный массив")
        self.array = QtWidgets.QHBoxLayout()

        self.arrayLayout.addWidget(self.arrayLabel)
        self.arrayLayout.addLayout(self.array)

        #  результаты
        self.resultLabel = QtWidgets.QLabel("")

        # добавление в основной лэйаут
        self.centralLayout.addWidget(self.pageName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addWidget(self.taskLabel)
        self.centralLayout.addLayout(self.generateButtonLayout)
        self.centralLayout.addLayout(self.arrayLayout)
        self.centralLayout.addWidget(self.resultLabel)
        self.centralLayout.addStretch()

        self.createArray()

    def createArray(self, len = 20):
        for i in range(0, len):
            self.array.addWidget(QtWidgets.QLabel(""))

    def generateArray(self):
        s = 0

        for i in range(0, 20):
            value = random.randint(-25, 25)

            if i % 2 != 0 and value != 0:
                s+=value

            self.array.itemAt(i).widget().setText(f"{value}")

        self.resultLabel.setText(f"Сумма всех ненулевых нечётных элементов = {s}")