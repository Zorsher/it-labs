from PySide6 import QtWidgets, QtGui, QtCore

class HelloPage(QtWidgets.QWidget):
    nextPage = QtCore.Signal()
    def __init__(self, parent = ...,):
        super().__init__(parent)
        self.centralLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.centralLayout)

        font = QtGui.QFont("Arial")
        font.setBold(True)
        font.setPixelSize(26)

        self.testLabel = QtWidgets.QLabel()
        self.testLabel.setText("""Лабораторная работа № 2. Простые линейные структуры\nРаботу выполнил:\nстудент группы ИВТ-11\nВишняков Павел Сергеевич\nВариант 4""")
        self.testLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.testLabel.setWordWrap(True)
        self.testLabel.setFont(font)

        font.setPixelSize(18)

        self.nextPageButton = QtWidgets.QPushButton("Начать")
        self.nextPageButton.setFixedHeight(40)
        self.nextPageButton.setObjectName("green")
        self.nextPageButton.setFont(font)
        self.nextPageButton.clicked.connect(self.nextPage.emit)

        self.centralLayout.addWidget(self.testLabel)
        self.centralLayout.addWidget(self.nextPageButton)

