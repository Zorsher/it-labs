from PySide6 import QtWidgets, QtGui, QtCore

greeterText = "Лабораторная работа № 1. Программирование сложных арифметических выражений\nРаботу выполнил:\nстудент группы ИВТ-11\nВишняков Павел Сергеевич\nВариант 4"

class HelloPage(QtWidgets.QWidget):
    """Приветственная страница приложения"""
    nextPage = QtCore.Signal() # сигнал для отправки в основное окно
    def __init__(self, parent = ...,):
        super().__init__(parent)
        # основной макет
        self.centralLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.centralLayout)

        font = QtGui.QFont("Arial")
        font.setBold(True)
        font.setPixelSize(26)

        # приветствующая надпись
        self.greeterLabel = QtWidgets.QLabel()
        self.greeterLabel.setText(greeterText)
        self.greeterLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.greeterLabel.setWordWrap(True)
        self.greeterLabel.setFont(font)

        font.setPixelSize(18)

        # кнопка запуска программы
        self.nextPageButton = QtWidgets.QPushButton("Начать")
        self.nextPageButton.setFixedHeight(40)
        self.nextPageButton.setObjectName("green")
        self.nextPageButton.setFont(font)
        self.nextPageButton.clicked.connect(self.nextPage.emit) # сигнал о нажатии кнопки

        self.centralLayout.addWidget(self.greeterLabel)
        self.centralLayout.addWidget(self.nextPageButton)

