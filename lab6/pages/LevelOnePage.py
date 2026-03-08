from PySide6 import QtWidgets, QtGui, QtCore
import random

class LevelOnePage(QtWidgets.QWidget):
    """Страница первого задания"""
    def __init__(self, parent = ...):
        super().__init__(parent)
        self.font_ = QtGui.QFont("Arial")
        self.font_.setBold(True)
        self.font_.setPixelSize(18)

        # основной макет
        self.centralLayout = QtWidgets.QVBoxLayout(self)
        self.pageName = QtWidgets.QLabel("Уровень 1")
        self.pageName.setFont(self.font_)

        # задание
        self.taskLabel = QtWidgets.QLabel("Дан двумерный массив размерности 10х10. Заполнить его случайными числами на отрезке   [-25,25]. Заменить на -1 элементы массива, лежащие выше главной диагонали. Вывести исходный   массив  и полученный результат на печать.")
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


        # правая матрица
        self.rightMatrixLayout = QtWidgets.QVBoxLayout()

        self.rightMatrixLabel = QtWidgets.QLabel("Изменённый двумерный массив")
        self.rightMatrixLabel.setWordWrap(True)

        self.rightMatrix = QtWidgets.QGridLayout()

        self.rightMatrixLayout.addWidget(self.rightMatrixLabel)
        self.rightMatrixLayout.addLayout(self.rightMatrix)
        self.rightMatrixLayout.addStretch()

        # добавление в основной лэйаут
        self.matrixLayout.addLayout(self.leftMatrixLayout)
        self.matrixLayout.addStretch()
        self.matrixLayout.addLayout(self.rightMatrixLayout)

        self.centralLayout.addWidget(self.pageName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addWidget(self.taskLabel)
        self.centralLayout.addLayout(self.generateButtonLayout)
        self.centralLayout.addLayout(self.matrixLayout)
        self.centralLayout.addStretch()

        self.createMatrix(10, 10)

    # создание матрицы
    def createMatrix(self, k, m):
        for row in range(0, k):
            for column in range(0, m):
                self.leftMatrix.addWidget(QtWidgets.QLabel(), row, column)
                self.rightMatrix.addWidget(QtWidgets.QLabel(), row, column)

    # функция регенерации матрицы
    def regenerateMatrix(self):
        self.generateMatrix(self.leftMatrix, 10, 10)
        self.changeRightMatrix(10, 10)

    # функция для генерации матрицы
    def generateMatrix(self, grid: QtWidgets.QGridLayout, k, m):
        for row in range(0, k):
            for column in range(0, m):
                value = random.randint(-25, 25)
                self.leftMatrix.itemAtPosition(row, column).widget().setText(f"{value}")

    # функция для определения результата
    def changeRightMatrix(self, k, m):
        for row in range(0, k):
            for column in range(0, m):
                if row+1 == column:
                    self.rightMatrix.itemAtPosition(row, column).widget().setText("-1")
                    # self.rightMatrix.addWidget(newLabel, row, column)
                    continue
                    
                self.rightMatrix.itemAtPosition(row, column).widget().setText(self.leftMatrix.itemAtPosition(row, column).widget().text())
                # self.rightMatrix.addWidget(QtWidgets.QLabel(self.leftMatrix.itemAtPosition(row, column).widget().text()), row, column)
