from PySide6 import QtWidgets, QtGui, QtCore
from widgets import TaskBlock

class LevelFourthPage(QtWidgets.QWidget):
    """Страница четвертого задания"""
    def __init__(self, parent = ...):
        super().__init__(parent)
        font = QtGui.QFont("Arial")
        font.setBold(True)
        font.setPixelSize(18)

        # основной макет
        self.centralLayout = QtWidgets.QVBoxLayout(self)
        self.pageName = QtWidgets.QLabel("Уровень 4")
        self.pageName.setFont(font)

        # картинка с графиком
        self.graphPictureWidget = QtWidgets.QWidget()
        self.graphPictureWidget.setFixedHeight(400)

        self.graphPictureBackground = QtWidgets.QLabel(parent=self.graphPictureWidget)
        self.graphPicture = QtGui.QPixmap("graph.png")

        self.graphPictureWidget.setFixedSize(self.graphPicture.size())
        self.graphPictureBackground.setPixmap(self.graphPicture)
            
        # блок задания
        self.taskBlock = TaskBlock(
            "Составить программу, определяющую для точки с координатами (X,Y), принадлежит ли она заштрихованной области",
            ["x", "y"],
            ["(x; y)"],
            [self.insidePolygon]
        )

        # добавляем элементы на страницу
        self.centralLayout.addWidget(self.pageName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addWidget(self.graphPictureWidget, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addLayout(self.taskBlock)
        self.centralLayout.addStretch()

    # функция для определения принадлежности точки заштрихованной области
    def insidePolygon(self, x, y):
        coords = [(1, 4), (4, 7), (7, 4), (4, 1), (1, 4)]

        intersections = 0

        for i in range(0, len(coords) - 1):
            x1, y1 = coords[i]
            x2, y2 = coords[i+1]

            if (y1 > y) == (y2 > y):
                continue

            intersect = x1 + (((x2 - x1)*(y - y1))/(y2 - y1))

            if x < intersect:
                intersections+=1

        textCoords = f"({x}, {y})"

        if intersections % 2 == 0:
            return textCoords + " находится вне фигуры"
        else:
            return textCoords + " находится внутри фигуры"
            