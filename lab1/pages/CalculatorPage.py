from PySide6 import QtWidgets, QtGui, QtCore
import math

class CalculatorPage(QtWidgets.QWidget):
    """Страница с калькулятором"""
    def __init__(self, parent = ...):
        super().__init__(parent)
        self.centralWidget = QtWidgets.QVBoxLayout(self)

        font = QtGui.QFont("Arial")
        font.setBold(True)
        font.setPixelSize(18)

        # создание виджета с вложенной картинкой
        self.formulaPictureWidget = QtWidgets.QWidget()
        self.formulaPictureWidget.setFixedHeight(400)

        self.formulaPictureBackground = QtWidgets.QLabel(parent=self.formulaPictureWidget)
        self.formulaPicture = QtGui.QPixmap("formula.png")

        self.formulaPictureWidget.setFixedSize(self.formulaPicture.size())
        self.formulaPictureBackground.setPixmap(self.formulaPicture)

        # макет для x значений
        self.xAreaLayout = QtWidgets.QHBoxLayout()

        self.xTextLabel = QtWidgets.QLabel("x = ")
        self.xTextEdit = QtWidgets.QTextEdit()
        self.xTextEdit.textChanged.connect(self.valueChanged)
        self.xTextEdit.setFixedHeight(30)

        self.xAreaLayout.addWidget(self.xTextLabel)
        self.xAreaLayout.addWidget(self.xTextEdit)

        # макет для y значений
        self.yAreaLayout = QtWidgets.QHBoxLayout()

        self.yTextLabel = QtWidgets.QLabel("y = ")
        self.yTextEdit = QtWidgets.QTextEdit()
        self.yTextEdit.textChanged.connect(self.valueChanged)
        self.yTextEdit.setFixedHeight(30)

        self.yAreaLayout.addWidget(self.yTextLabel)
        self.yAreaLayout.addWidget(self.yTextEdit)

        # макет для z значений
        self.zAreaLayout = QtWidgets.QHBoxLayout()

        self.zTextLabel = QtWidgets.QLabel("z = ")
        self.zTextEdit = QtWidgets.QTextEdit()
        self.zTextEdit.textChanged.connect(self.valueChanged)
        self.zTextEdit.setFixedHeight(30)

        self.zAreaLayout.addWidget(self.zTextLabel)
        self.zAreaLayout.addWidget(self.zTextEdit)

        # результаты первой формулы
        self.firstResultLabel = QtWidgets.QLabel("")
        self.firstResultLabel.setFont(font)

        # результаты второй формулы
        self.secondResultLabel = QtWidgets.QLabel("")
        self.secondResultLabel.setFont(font)

        # добавление элементов в основной макет
        self.centralWidget.addWidget(self.formulaPictureWidget, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralWidget.addLayout(self.xAreaLayout)
        self.centralWidget.addLayout(self.yAreaLayout)
        self.centralWidget.addLayout(self.zAreaLayout)
        self.centralWidget.addWidget(self.firstResultLabel, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralWidget.addWidget(self.secondResultLabel, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralWidget.addStretch(1)
        
        self.xTextEdit.setText("-0.622")
        self.yTextEdit.setText("3.325")
        self.zTextEdit.setText("5.541")

    def valueChanged(self):
        # Получение корректных значений x, y, z из соответствующих текстовых полей
        try:
            x = float(self.xTextEdit.toPlainText())
        except:
            x = None
        
        try:
            y = float(self.yTextEdit.toPlainText())
        except:
            y = None
        
        try:
            z = float(self.zTextEdit.toPlainText())
        except:
            z = None
        
        # просчёты по формуле 1
        if x != None and y != None:
            a = round(((math.sqrt(abs(x - 1)) - math.cbrt(abs(y)))/(1 + ((x**2)/(x + 2)) + (y**2)/(y + 4))), 3)
            self.firstResultLabel.setText(f"a = {a}")
        else:
            self.firstResultLabel.setText("")

        # просчёты по формуле 2
        if z != None and x != None:
            b = round(x*(math.atan(z) + math.e**-(x + 3)), 3)
            self.secondResultLabel.setText(f"b = {b}")
        else:
            self.secondResultLabel.setText("")
