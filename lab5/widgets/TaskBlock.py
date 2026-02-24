from PySide6 import QtWidgets, QtCore

class ParameterLayout(QtWidgets.QHBoxLayout):
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
            answerLabel.show()

            if result == None:
                answerLabel.hide()
                continue

            answerLabel.setText(f"{self.toFoundList[index]} = {result}")