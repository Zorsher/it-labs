from PySide6 import QtCore, QtWidgets, QtGui

class ImageWidget(QtWidgets.QWidget):
    """Виджет для отображения изображения"""
    def __init__(self, path):
        super().__init__()
        self.setFixedHeight(400)

        self.imageBackground = QtWidgets.QLabel(self)
        self.image = QtGui.QPixmap(f"images/{path}")

        self.setFixedSize(self.image.size())
        self.imageBackground.setPixmap(self.image)
