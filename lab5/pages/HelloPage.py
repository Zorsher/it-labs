from PySide6 import QtWidgets, QtGui, QtCore

class HelloPage(QtWidgets.QWidget):
    def __init__(self, parent = ...,):
        super().__init__(parent)
        self.centralLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.centralLayout)

        font = QtGui.QFont("Arial")
        font.setBold(True)
        font.setPixelSize(26)

        self.testLabel = QtWidgets.QLabel()
        self.testLabel.setText("""Лабораторная работа № 5. Одномерные массивы\nРаботу выполнил:\nстудент группы ИВТ-11\nВишняков Павел Сергеевич\nВариант 4""")
        self.testLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.testLabel.setWordWrap(True)
        self.testLabel.setFont(font)

        self.centralLayout.addWidget(self.testLabel)


