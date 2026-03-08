from PySide6 import QtWidgets, QtGui, QtCore

greeterText = "Лабораторная работа № 5. Одномерные массивы\nРаботу выполнил:\nстудент группы ИВТ-11\nВишняков Павел Сергеевич\nВариант 4"

class HelloPage(QtWidgets.QWidget):
    """Приветственная страница приложения"""
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

        # Добавление в макет
        self.centralLayout.addWidget(self.greeterLabel)


