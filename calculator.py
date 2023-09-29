import sys
from PyQt5.QtWidgets import QPushButton, QLabel, QDesktopWidget, QApplication, QMainWindow
from main import *
class Calculator(QMainWindow):
    expr = ""
    post_sign=['.','%','/','*','-','+']
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        screenSize = QDesktopWidget().screenGeometry()
        self.height = screenSize.height()
        self.width = screenSize.width()
        self.setFixedSize(int(self.width/4.2),int(self.height/1.5))
        self.ui.num0.clicked.connect(lambda:self.append_data('0'))
        self.ui.num0.setShortcut("0")
        self.ui.num1.clicked.connect(lambda:self.append_data('1'))
        self.ui.num1.setShortcut("1")
        self.ui.num2.clicked.connect(lambda:self.append_data('2'))
        self.ui.num2.setShortcut("2")
        self.ui.num3.clicked.connect(lambda:self.append_data('3'))
        self.ui.num3.setShortcut("3")
        self.ui.num4.clicked.connect(lambda:self.append_data('4'))
        self.ui.num4.setShortcut("4")
        self.ui.num5.clicked.connect(lambda:self.append_data('5'))
        self.ui.num5.setShortcut("5")
        self.ui.num6.clicked.connect(lambda:self.append_data('6'))
        self.ui.num6.setShortcut("6")
        self.ui.num7.clicked.connect(lambda:self.append_data('7'))
        self.ui.num7.setShortcut("7")
        self.ui.num8.clicked.connect(lambda:self.append_data('8'))
        self.ui.num8.setShortcut("8")
        self.ui.num9.clicked.connect(lambda:self.append_data('9'))
        self.ui.num9.setShortcut("9")
        self.ui.subtract.clicked.connect(lambda:self.append_data('-'))
        self.ui.subtract.setShortcut("-")
        self.ui.add.clicked.connect(lambda:self.append_data('+'))
        self.ui.add.setShortcut("+")
        self.ui.multiply.clicked.connect(lambda:self.append_data('*'))
        self.ui.multiply.setShortcut("*")
        self.ui.divide.clicked.connect(lambda:self.append_data('/'))
        self.ui.divide.setShortcut("/")
        self.ui.modulas.clicked.connect(lambda:self.append_data('%'))
        self.ui.modulas.setShortcut("%")
        self.ui.decimal.clicked.connect(lambda:self.append_data('.'))
        self.ui.decimal.setShortcut(".")
        self.ui.equals.clicked.connect(lambda:self.append_data('='))
        self.ui.equals.setShortcut("Return")
        self.ui.clrscr.clicked.connect(lambda:self.append_data('c'))
        self.ui.clrscr.setShortcut("c")
        self.ui.backspace.clicked.connect(lambda:self.append_data('del'))
        self.ui.backspace.setShortcut("backspace")
        self.show()

    def append_data(self,data):
        if data=='=':
            if data=='=' and (self.expr[-1] not in self.post_sign):
                try:
                    result = str(eval(self.expr))
                    self.ui.out.setText(self.expr+"\n="+result)
                except ZeroDivisionError:
                    self.ui.out.setText(self.expr+"\n="+"Division By Zero Exception")
            else:
                pass
        elif data=='c':
            self.expr=""
            self.ui.out.clear()
        elif data=='del':
            if self.expr=="":
                pass
            else:
                self.expr = self.expr[0:len(self.expr)-1]
                self.ui.out.setText(self.expr)
        elif data in self.post_sign and self.expr[-1] in self.post_sign:
            pass
        else:
            self.expr = self.expr + data
            self.ui.out.setText(self.expr)

app = QApplication(sys.argv)
calc = Calculator()
calc.show()
sys.exit(app.exec_())
