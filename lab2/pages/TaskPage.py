from PySide6 import QtWidgets, QtGui, QtCore
from widgets.ScrollArea import ScrollArea

import math

class ParameterLayout(QtWidgets.QHBoxLayout):
    """Параметр для задачи. Состоит из названия параметра и поля для ввода его значения"""
    textChanged = QtCore.Signal(str, str)
    def __init__(self, param):
        super().__init__()
        self.param = param
        self.paramLabel = QtWidgets.QLabel(f"{param} = ")

        self.paramInput = QtWidgets.QTextEdit()
        self.paramInput.setFixedHeight(30)
        self.paramInput.textChanged.connect(self.newText)

        self.addWidget(self.paramLabel)
        self.addWidget(self.paramInput)

    def newText(self):
        self.textChanged.emit(self.paramInput.toPlainText(), self.param)

class TaskBlock(QtWidgets.QVBoxLayout):
    """Блок с задачей. Состоит из множества параметров задач"""
    def __init__(self, taskText: str, params: list[str], toFoundList: list[str], funcs: list):
        super().__init__()
        self.funcs = funcs
        self.toFoundList = toFoundList
        self.paramsDict = {}

        self.taskTextLabel = QtWidgets.QLabel(taskText)
        self.taskTextLabel.setWordWrap(True)

        self.addWidget(self.taskTextLabel)

        for param in params:
            self.paramsDict[param] = None

            paramLayout = ParameterLayout(param)
            paramLayout.textChanged.connect(self.paramChanged)

            self.addLayout(paramLayout)

        for _ in range(0, len(funcs)):
            self.addWidget(QtWidgets.QLabel(""), alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

    # Функция вызываемая при изменении параметра
    def paramChanged(self, value, param):
        try:
            self.paramsDict[param] = float(value)
        except: 
            return

        for param, value in self.paramsDict.items():
            if value == None:
                return
            
            try:
                float(value)
            except:
                return
        
        for index, func in enumerate(self.funcs):
            result = func(*list(self.paramsDict.values()))

            answerLabel = self.itemAt(self.count() - (len(self.funcs) - index)).widget()
            answerLabel.setText(f"{self.toFoundList[index]} = {result}")

class TaskPage(ScrollArea):
    """Страница с задачами"""
    def __init__(self, parent = ...):
        super().__init__(layoutType=QtWidgets.QVBoxLayout, ignore_scroll_down=True)
        font = QtGui.QFont("Arial")
        font.setBold(True)
        font.setPixelSize(18)

        # Первая задача
        self.firstTask = TaskBlock(
            "1.Скорость первого автомобиля V1 км/ч, второго — V2 км/ч, расстояние между ними S км. Определить расстояние между ними через T часов, если автомобили удаляются друг от друга.",
            ["S", "V1", "V2", "T"],
            ["Sобщ"],
            [lambda S, V1, V2, T: S + (V1 + V2) * T]
        )

        # Вторая задача
        self.secondTask = TaskBlock(
            "2. Дана длина ребра куба. Найти площадь грани, площадь полной поверхности и объем этого куба. ",
            ["a"],
            ["S грани", "S полной поверхности", "V"],
            [lambda a: a**2, lambda a: (a**2)*6, lambda a: a**3]
        )

        #Третья задача
        self.thirdTask = TaskBlock(
            "3. Дано целое четырехзначное число. Используя операции div и mod, найти сумму его цифр.",
            ["N"],
            ["n1", "n2", "n3", "n4", "Сумма"],
            [lambda N: N // 1000, 
             lambda N: (N // 100) % 10, 
             lambda N: (N // 10) % 10, 
             lambda N: N % 10,
             lambda N: (N // 1000) + ((N // 100) % 10) + ((N // 10) % 10) + (N % 10)
             ]
        )

        # Четвёртая задача
        self.fourthTask = TaskBlock(
            "4. Найти периметр и площадь прямоугольной трапеции с основаниями a и b (a > b) и острым углом alpha (угол дан в радианах).",
            ["a", "b", "alpha"],
            ["P", "S"],
            [lambda a, b, alpha: a + b + (abs(a - b) * (1 + math.sin(alpha)) / math.cos(alpha)) if 0 < alpha < math.pi/2 else None,
             lambda a, b, alpha: (abs(a**2 - b**2) / 2) * math.tan(alpha) if 0 < alpha < math.pi/2 else None]
        )

        # Пятая задача
        self.fifthTask = TaskBlock(
            "5. Надо покрасить крышу и стенки цилиндрического бака. Диаметр бака 35 м, высота 8,6 м. Сколько банок с краской потребуется, если одной банки хватает для покраски 236 кв. м?",
            ["d", "h"],
            ["Количество банок"],
            [lambda d, h: math.ceil(((math.pi * d * h) + ((math.pi * d**2)/4))/236)]
        )

        # Добавление задач на страницу
        self.addWidget(self.firstTask)
        self.addWidget(self.secondTask)
        self.addWidget(self.thirdTask)
        self.addWidget(self.fourthTask)
        self.addWidget(self.fifthTask)
