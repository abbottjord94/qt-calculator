#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from UIform import Ui_Form


class MyFirstGuiProgram(Ui_Form):

        def __init__(self, dialog):
            Ui_Form.__init__(self)
            self.setupUi(dialog)
            self.clearButton.clicked.connect(self.clear)
            self.equalButton.clicked.connect(self.calculate)
            self.oneButton.clicked.connect(self.onebutton_Pressed)
            self.twoButton.clicked.connect(self.twobutton_Pressed)
            self.threeButton.clicked.connect(self.threebutton_Pressed)
            self.fourButton.clicked.connect(self.fourbutton_Pressed)
            self.fiveButton.clicked.connect(self.fivebutton_Pressed)
            self.sixButton.clicked.connect(self.sixbutton_Pressed)
            self.sevenButton.clicked.connect(self.sevenbutton_Pressed)
            self.eightButton.clicked.connect(self.eightbutton_Pressed)
            self.nineButton.clicked.connect(self.ninebutton_Pressed)
            self.zeroButton.clicked.connect(self.zerobutton_Pressed)
            self.plusButton.clicked.connect(self.plusbutton_Pressed)
            self.minusButton.clicked.connect(self.minusbutton_Pressed)
            self.multiplyButton.clicked.connect(self.multiplybutton_Pressed)
            self.divideButton.clicked.connect(self.dividebutton_Pressed)
            self.decimalButton.clicked.connect(self.decimalbutton_Pressed)
            self.leftParenthesis.clicked.connect(self.leftParenthesis_Pressed)
            self.rightParenthesis.clicked.connect(self.rightParenthesis_Pressed)
            self.modButton.clicked.connect(self.modbutton_Pressed)

        def clear(self):
            self.calculator_display.setText("")

        def calculate(self):
            expression = self.calculator_display.text()
            self.calculator_display.setText(str(eval(expression)))

        def onebutton_Pressed(self):
            text = self.calculator_display.text()
            text += "1"
            self.calculator_display.setText(text)

        def twobutton_Pressed(self):
            text = self.calculator_display.text()
            text += "2"
            self.calculator_display.setText(text)

        def threebutton_Pressed(self):
            text = self.calculator_display.text()
            text += "3"
            self.calculator_display.setText(text)

        def fourbutton_Pressed(self):
            text = self.calculator_display.text()
            text += "4"
            self.calculator_display.setText(text)

        def fivebutton_Pressed(self):
            text = self.calculator_display.text()
            text += "5"
            self.calculator_display.setText(text)

        def sixbutton_Pressed(self):
            text = self.calculator_display.text()
            text += "6"
            self.calculator_display.setText(text)

        def sevenbutton_Pressed(self):
            text = self.calculator_display.text()
            text += "7"
            self.calculator_display.setText(text)

        def eightbutton_Pressed(self):
            text = self.calculator_display.text()
            text += "8"
            self.calculator_display.setText(text)

        def ninebutton_Pressed(self):
            text = self.calculator_display.text()
            text += "9"
            self.calculator_display.setText(text)

        def zerobutton_Pressed(self):
            text = self.calculator_display.text()
            text += "0"
            self.calculator_display.setText(text)

        def plusbutton_Pressed(self):
            text = self.calculator_display.text()
            text += "+"
            self.calculator_display.setText(text)

        def minusbutton_Pressed(self):
            text = self.calculator_display.text()
            text += "-"
            self.calculator_display.setText(text)

        def multiplybutton_Pressed(self):
            text = self.calculator_display.text()
            text += "*"
            self.calculator_display.setText(text)

        def dividebutton_Pressed(self):
            text = self.calculator_display.text()
            text += "/"
            self.calculator_display.setText(text)

        def decimalbutton_Pressed(self):
            text = self.calculator_display.text()
            text += "."
            self.calculator_display.setText(text)

        def modbutton_Pressed(self):
            text = self.calculator_display.text()
            text += "%"
            self.calculator_display.setText(text)

        def leftParenthesis_Pressed(self):
            text = self.calculator_display.text()
            text += "("
            self.calculator_display.setText(text)

        def rightParenthesis_Pressed(self):
            text = self.calculator_display.text()
            text += ")"
            self.calculator_display.setText(text)

if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        dialog = QtWidgets.QDialog()

        prog = MyFirstGuiProgram(dialog)

        dialog.show()
        sys.exit(app.exec_())
