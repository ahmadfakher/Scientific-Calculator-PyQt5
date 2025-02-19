from PyQt5 import QtCore, QtGui, QtWidgets
import re
import math
def main():
    class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(670, 515)
                MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.outputlabel = QtWidgets.QLabel(self.centralwidget)
                self.outputlabel.setGeometry(QtCore.QRect(20, 0, 631, 61))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(28)
                font.setBold(True)
                font.setWeight(75)
                self.outputlabel.setFont(font)
                self.outputlabel.setFrameShape(QtWidgets.QFrame.Box)
                self.outputlabel.setFrameShadow(QtWidgets.QFrame.Plain)
                self.outputlabel.setLineWidth(2)
                self.outputlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.outputlabel.setObjectName("outputlabel")
                self.NineButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("9"))
                self.NineButton.setGeometry(QtCore.QRect(490, 150, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.NineButton.setFont(font)
                self.NineButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.NineButton.setObjectName("NineButton")
                self.SixButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("6"))
                self.SixButton.setGeometry(QtCore.QRect(490, 230, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.SixButton.setFont(font)
                self.SixButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.SixButton.setObjectName("SixButton")
                self.ThreeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("3"))
                self.ThreeButton.setGeometry(QtCore.QRect(490, 310, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.ThreeButton.setFont(font)
                self.ThreeButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.ThreeButton.setObjectName("ThreeButton")
                self.DecimalButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.dot_it())
                self.DecimalButton.setGeometry(QtCore.QRect(350, 390, 31, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.DecimalButton.setFont(font)
                self.DecimalButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.DecimalButton.setObjectName("DecimalButton")
                self.DevideButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("/"))
                self.DevideButton.setGeometry(QtCore.QRect(580, 150, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.DevideButton.setFont(font)
                self.DevideButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.DevideButton.setObjectName("DevideButton")
                self.TwoButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("2"))
                self.TwoButton.setGeometry(QtCore.QRect(400, 310, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.TwoButton.setFont(font)
                self.TwoButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.TwoButton.setObjectName("TwoButton")
                self.ZeroButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("0"))
                self.ZeroButton.setGeometry(QtCore.QRect(490, 390, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.ZeroButton.setFont(font)
                self.ZeroButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.ZeroButton.setObjectName("ZeroButton")
                self.MultiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("*"))
                self.MultiplyButton.setGeometry(QtCore.QRect(490, 70, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.MultiplyButton.setFont(font)
                self.MultiplyButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.MultiplyButton.setObjectName("MultiplyButton")
                self.FiveButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("5"))
                self.FiveButton.setGeometry(QtCore.QRect(400, 230, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.FiveButton.setFont(font)
                self.FiveButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.FiveButton.setObjectName("FiveButton")
                self.EightButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("8"))
                self.EightButton.setGeometry(QtCore.QRect(400, 150, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.EightButton.setFont(font)
                self.EightButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.EightButton.setObjectName("EightButton")
                self.OneButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("1"))
                self.OneButton.setGeometry(QtCore.QRect(310, 310, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.OneButton.setFont(font)
                self.OneButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.OneButton.setObjectName("OneButton")
                self.SignButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.plus_minus_it())
                self.SignButton.setGeometry(QtCore.QRect(200, 390, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.SignButton.setFont(font)
                self.SignButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.SignButton.setObjectName("SignButton")
                self.ModButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("%"))
                self.ModButton.setGeometry(QtCore.QRect(400, 390, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.ModButton.setFont(font)
                self.ModButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.ModButton.setObjectName("ModButton")
                self.FourButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("4"))
                self.FourButton.setGeometry(QtCore.QRect(310, 230, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.FourButton.setFont(font)
                self.FourButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.FourButton.setObjectName("FourButton")
                self.SevenButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("7"))
                self.SevenButton.setGeometry(QtCore.QRect(310, 150, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.SevenButton.setFont(font)
                self.SevenButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.SevenButton.setObjectName("SevenButton")
                self.EPowerButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("math.exp("))
                self.EPowerButton.setGeometry(QtCore.QRect(200, 230, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.EPowerButton.setFont(font)
                self.EPowerButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.EPowerButton.setObjectName("EPowerButton")
                self.YPowerXButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("math.pow("))
                self.YPowerXButton.setGeometry(QtCore.QRect(110, 310, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.YPowerXButton.setFont(font)
                self.YPowerXButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.YPowerXButton.setObjectName("YPowerXButton")
                self.SqrtButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.root_it())
                self.SqrtButton.setGeometry(QtCore.QRect(200, 70, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.SqrtButton.setFont(font)
                self.SqrtButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.SqrtButton.setObjectName("SqrtButton")
                self.LogButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("math.log10("))
                self.LogButton.setGeometry(QtCore.QRect(20, 230, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.LogButton.setFont(font)
                self.LogButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.LogButton.setObjectName("LogButton")
                self.CosineButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("math.cos("))
                self.CosineButton.setGeometry(QtCore.QRect(110, 150, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.CosineButton.setFont(font)
                self.CosineButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.CosineButton.setObjectName("CosineButton")
                self.LnButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("math.log("))
                self.LnButton.setGeometry(QtCore.QRect(110, 230, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.LnButton.setFont(font)
                self.LnButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.LnButton.setObjectName("LnButton")
                self.SquareButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.square_it())
                self.SquareButton.setGeometry(QtCore.QRect(110, 70, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.SquareButton.setFont(font)
                self.SquareButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.SquareButton.setObjectName("SquareButton")
                self.FactorialButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("math.factorial("))
                self.FactorialButton.setGeometry(QtCore.QRect(20, 310, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.FactorialButton.setFont(font)
                self.FactorialButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.FactorialButton.setObjectName("FactorialButton")
                self.TanButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("math.tan("))
                self.TanButton.setGeometry(QtCore.QRect(200, 150, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.TanButton.setFont(font)
                self.TanButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.TanButton.setObjectName("TanButton")
                self.SinButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("math.sin("))
                self.SinButton.setGeometry(QtCore.QRect(20, 150, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.SinButton.setFont(font)
                self.SinButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.SinButton.setObjectName("SinButton")
                self.ClearButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("c"))
                self.ClearButton.setGeometry(QtCore.QRect(580, 70, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.ClearButton.setFont(font)
                self.ClearButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 0, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 0, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.ClearButton.setObjectName("ClearButton")
                self.AddButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("+"))
                self.AddButton.setGeometry(QtCore.QRect(580, 310, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.AddButton.setFont(font)
                self.AddButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.AddButton.setObjectName("AddButton")
                self.MinusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("-"))
                self.MinusButton.setGeometry(QtCore.QRect(580, 230, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.MinusButton.setFont(font)
                self.MinusButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.MinusButton.setObjectName("MinusButton")
                self.EqualButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.math_it())
                self.EqualButton.setGeometry(QtCore.QRect(580, 390, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.EqualButton.setFont(font)
                self.EqualButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.EqualButton.setObjectName("EqualButton")
                self.AbsButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("abs("))
                self.AbsButton.setGeometry(QtCore.QRect(200, 310, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.AbsButton.setFont(font)
                self.AbsButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.AbsButton.setObjectName("AbsButton")
                self.DenominatorButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("1/"))
                self.DenominatorButton.setGeometry(QtCore.QRect(20, 70, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(24)
                self.DenominatorButton.setFont(font)
                self.DenominatorButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.DenominatorButton.setObjectName("DenominatorButton")
                self.ExpButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("math.e"))
                self.ExpButton.setGeometry(QtCore.QRect(20, 390, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.ExpButton.setFont(font)
                self.ExpButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.ExpButton.setObjectName("ExpButton")
                self.PiButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("math.pi"))
                self.PiButton.setGeometry(QtCore.QRect(110, 390, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.PiButton.setFont(font)
                self.PiButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.PiButton.setObjectName("PiButton")
                self.deleteButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.remove_it())
                self.deleteButton.setGeometry(QtCore.QRect(400, 70, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.deleteButton.setFont(font)
                self.deleteButton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.deleteButton.setObjectName("deleteButton")
                self.closebracketbutton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it(")"))
                self.closebracketbutton.setGeometry(QtCore.QRect(350, 70, 31, 71))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.closebracketbutton.setFont(font)
                self.closebracketbutton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.closebracketbutton.setObjectName("closebracketbutton")
                self.openbracketbutton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("("))
                self.openbracketbutton.setGeometry(QtCore.QRect(310, 70, 31, 71))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.openbracketbutton.setFont(font)
                self.openbracketbutton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.openbracketbutton.setObjectName("openbracketbutton")
                self.commabutton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it(","))
                self.commabutton.setGeometry(QtCore.QRect(310, 390, 31, 71))
                font = QtGui.QFont()
                font.setPointSize(28)
                self.commabutton.setFont(font)
                self.commabutton.setStyleSheet("QPushButton{\n"
        "     border-radius: 15px;\n"
        "    background-color: rgb(169,169,169) ;\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:rgb(0 ,0 ,0);\n"
        "    color: rgb(255 ,255, 255);\n"
        "}")
                self.commabutton.setObjectName("commabutton")
                MainWindow.setCentralWidget(self.centralwidget)
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                
        def root_it(self):
                screen = float(self.outputlabel.text())
                squareroot = math.pow(screen, 0.5)
                self.outputlabel.setText(str(squareroot))

        def square_it(self):
                screen = float(self.outputlabel.text())
                squared = math.pow(screen, 2)
                self.outputlabel.setText(str(squared))
                
        def dot_it(self):
                screen = self.outputlabel.text()
                if screen[-1] == ".":
                        pass
                elif screen[-1] in ['+', '-', '/', '=', 'X']:
                        self.outputlabel.setText(f'{screen}.')
                elif screen[-1] == "%":
                        pass
                else:
                        m=re.search('(\.[0-9]+)$', screen) 
                if m == None:
                        self.outputlabel.setText(f'{screen}.')
                else:
                        pass
        
        def math_it(self):
                try:
                        screen = self.outputlabel.text()
                        answer = eval(screen)
                        self.outputlabel.setText(str(answer))
                except:
                        self.outputlabel.setText("ERROR")    
        
        def plus_minus_it(self):
                screen = self.outputlabel.text()
                if "-" in screen:
                        self.outputlabel.setText(screen.replace("-", ""))
                else:
                        self.outputlabel.setText(f'-{screen}')
        def remove_it(self):
                screen = self.outputlabel.text()
                screen = screen[:-1]
                self.outputlabel.setText(screen)
        
        def press_it(self, pressed):
                if pressed == "c":
                        self.outputlabel.setText("0")
                else:
                        if self.outputlabel.text() == "0":
                                self.outputlabel.setText("")
                        self.outputlabel.setText(f'{self.outputlabel.text()}{pressed}')        
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "project"))
                self.outputlabel.setText(_translate("MainWindow", "0"))
                self.NineButton.setText(_translate("MainWindow", "9"))
                self.SixButton.setText(_translate("MainWindow", "6"))
                self.ThreeButton.setText(_translate("MainWindow", "3"))
                self.DecimalButton.setText(_translate("MainWindow", "."))
                self.DevideButton.setText(_translate("MainWindow", "÷"))
                self.TwoButton.setText(_translate("MainWindow", "2"))
                self.ZeroButton.setText(_translate("MainWindow", "0"))
                self.MultiplyButton.setText(_translate("MainWindow", "x"))
                self.FiveButton.setText(_translate("MainWindow", "5"))
                self.EightButton.setText(_translate("MainWindow", "8"))
                self.OneButton.setText(_translate("MainWindow", "1"))
                self.SignButton.setText(_translate("MainWindow", "+/-"))
                self.ModButton.setText(_translate("MainWindow", "%"))
                self.FourButton.setText(_translate("MainWindow", "4"))
                self.SevenButton.setText(_translate("MainWindow", "7"))
                self.EPowerButton.setText(_translate("MainWindow", "e^x"))
                self.YPowerXButton.setText(_translate("MainWindow", "y^x"))
                self.SqrtButton.setText(_translate("MainWindow", "√"))
                self.LogButton.setText(_translate("MainWindow", "log"))
                self.CosineButton.setText(_translate("MainWindow", "cos"))
                self.LnButton.setText(_translate("MainWindow", "ln"))
                self.SquareButton.setText(_translate("MainWindow", "x^2"))
                self.FactorialButton.setText(_translate("MainWindow", "x!"))
                self.TanButton.setText(_translate("MainWindow", "tan"))
                self.SinButton.setText(_translate("MainWindow", "sin"))
                self.ClearButton.setText(_translate("MainWindow", "C"))
                self.AddButton.setText(_translate("MainWindow", "+"))
                self.MinusButton.setText(_translate("MainWindow", "-"))
                self.EqualButton.setText(_translate("MainWindow", "="))
                self.AbsButton.setText(_translate("MainWindow", "|x|"))
                self.DenominatorButton.setText(_translate("MainWindow", "1/x"))
                self.ExpButton.setText(_translate("MainWindow", "e"))
                self.PiButton.setText(_translate("MainWindow", "𝞹"))
                self.deleteButton.setText(_translate("MainWindow", "<<"))
                self.closebracketbutton.setText(_translate("MainWindow", ")"))
                self.openbracketbutton.setText(_translate("MainWindow", "("))
                self.commabutton.setText(_translate("MainWindow", ","))


    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
        
main()