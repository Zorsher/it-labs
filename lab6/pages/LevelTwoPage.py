from PySide6 import QtWidgets, QtGui, QtCore
from widgets import TaskBlock, ImageWidget
import random

class LevelTwoPage(QtWidgets.QWidget):
    def __init__(self, parent = ...):
        super().__init__(parent)
        font = QtGui.QFont("Arial")
        font.setBold(True)
        font.setPixelSize(18)

        self.centralLayout = QtWidgets.QVBoxLayout(self)
        self.pageName = QtWidgets.QLabel("Уровень 2")
        self.pageName.setFont(font)

        self.taskLabel = QtWidgets.QLabel("Дан двумерный массив размерности 10х10. Заполнить его случайными числами на отрезке [-25,25]. Определить номера строк массива, суммы элементов которых меньше суммы элементов, стоящих на главной диагонали. Вывести исходный массив и полученный результат на печать.")
        self.taskLabel.setWordWrap(True)

        # кнопка для генерации матрицы
        self.generateButtonLayout = QtWidgets.QHBoxLayout()
        
        self.generateButton = QtWidgets.QPushButton("Сгенерировать матрицу")
        self.generateButton.clicked.connect(self.regenerateMatrix)

        self.generateButtonLayout.addStretch()
        self.generateButtonLayout.addWidget(self.generateButton)
        self.generateButtonLayout.addStretch()

        self.matrixLayout = QtWidgets.QHBoxLayout()

        # левая матрица
        self.leftMatrixLayout = QtWidgets.QVBoxLayout()

        self.leftMatrixLabel = QtWidgets.QLabel("Оригинальный двумерный массив")
        self.leftMatrixLabel.setWordWrap(True)

        self.leftMatrix = QtWidgets.QGridLayout()

        self.leftMatrixLayout.addWidget(self.leftMatrixLabel)
        self.leftMatrixLayout.addLayout(self.leftMatrix)
        self.leftMatrixLayout.addStretch()

        # правый лэйаут
        self.rightLayout = QtWidgets.QVBoxLayout()

        self.rightLabel = QtWidgets.QLabel("Итоги")
        self.rightLabel.setWordWrap(True)

        self.resultLayout = QtWidgets.QVBoxLayout()

        self.rightLayout.addWidget(self.rightLabel)
        self.rightLayout.addLayout(self.resultLayout)
        self.rightLayout.addStretch()


        self.matrixLayout.addLayout(self.leftMatrixLayout)
        self.matrixLayout.addStretch()
        self.matrixLayout.addLayout(self.rightLayout)

        # добавление в основной лэйаут
        self.centralLayout.addWidget(self.pageName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addWidget(self.taskLabel)
        self.centralLayout.addLayout(self.generateButtonLayout)
        self.centralLayout.addLayout(self.matrixLayout)
        self.centralLayout.addStretch()


        self.createMatrix(10, 10)

    def createMatrix(self, k, m):
        for row in range(0, k):
            for column in range(0, m):
                self.leftMatrix.addWidget(QtWidgets.QLabel(), row, column)

        for i in range(0, 10):
            label = QtWidgets.QLabel()
            label.setWordWrap(True)
            self.resultLayout.addWidget(label)

    def clearMatrix(self, k, m):
        for row in range(0, k):
            for column in range(0, m):
                self.leftMatrix.itemAtPosition(row, column).widget().setText("")

        for i in range(0, 10):
            self.resultLayout.itemAt(i).widget().setText("")

    def regenerateMatrix(self):
        self.clearMatrix(10, 10)
        self.generateMatrix(10, 10)
        self.changeresultLayout(10, 10)

    def generateMatrix(self, k, m):
        self.diagonalSum = 0
        for row in range(0, k):
            for column in range(0, m):
                value = random.randint(-25, 25)
                
                if row == column:
                    self.diagonalSum+=value

                self.leftMatrix.itemAtPosition(row, column).widget().setText(f"{value}")


    def changeresultLayout(self, k, m):
        s = 0

        for row in range(0, k):
            rowSum = 0
            for column in range(0, m):
                rowSum+=int(self.leftMatrix.itemAtPosition(row, column).widget().text())

            if rowSum > self.diagonalSum:
                self.resultLayout.itemAt(s).widget().setText(f"Сумма значений строки {row} больше суммы главной диагонали")
                s+=1

        if self.resultLayout.itemAt(0).widget().text() == "":
            self.resultLayout.itemAt(0).widget().setText(f"Сумма значений главной диагонали больше суммы каждой строки")
