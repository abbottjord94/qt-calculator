# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jordan/Desktop/qt-calculator/form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(232, 196)
        self.calculator_display = QtWidgets.QLineEdit(Form)
        self.calculator_display.setGeometry(QtCore.QRect(10, 10, 211, 41))
        self.calculator_display.setObjectName("calculator_display")
        self.clearButton = QtWidgets.QPushButton(Form)
        self.clearButton.setGeometry(QtCore.QRect(20, 70, 71, 25))
        self.clearButton.setObjectName("clearButton")
        self.plusButton = QtWidgets.QPushButton(Form)
        self.plusButton.setGeometry(QtCore.QRect(20, 100, 31, 25))
        self.plusButton.setObjectName("plusButton")
        self.minusButton = QtWidgets.QPushButton(Form)
        self.minusButton.setGeometry(QtCore.QRect(60, 100, 31, 25))
        self.minusButton.setObjectName("minusButton")
        self.multiplyButton = QtWidgets.QPushButton(Form)
        self.multiplyButton.setGeometry(QtCore.QRect(20, 130, 31, 25))
        self.multiplyButton.setObjectName("multiplyButton")
        self.divideButton = QtWidgets.QPushButton(Form)
        self.divideButton.setGeometry(QtCore.QRect(60, 130, 31, 25))
        self.divideButton.setObjectName("divideButton")
        self.oneButton = QtWidgets.QPushButton(Form)
        self.oneButton.setGeometry(QtCore.QRect(110, 70, 31, 25))
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(Form)
        self.twoButton.setGeometry(QtCore.QRect(150, 70, 31, 25))
        self.twoButton.setObjectName("twoButton")
        self.threeButton = QtWidgets.QPushButton(Form)
        self.threeButton.setGeometry(QtCore.QRect(190, 70, 31, 25))
        self.threeButton.setObjectName("threeButton")
        self.fourButton = QtWidgets.QPushButton(Form)
        self.fourButton.setGeometry(QtCore.QRect(110, 100, 31, 25))
        self.fourButton.setObjectName("fourButton")
        self.fiveButton = QtWidgets.QPushButton(Form)
        self.fiveButton.setGeometry(QtCore.QRect(150, 100, 31, 25))
        self.fiveButton.setObjectName("fiveButton")
        self.sixButton = QtWidgets.QPushButton(Form)
        self.sixButton.setGeometry(QtCore.QRect(190, 100, 31, 25))
        self.sixButton.setObjectName("sixButton")
        self.sevenButton = QtWidgets.QPushButton(Form)
        self.sevenButton.setGeometry(QtCore.QRect(110, 130, 31, 25))
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(Form)
        self.eightButton.setGeometry(QtCore.QRect(150, 130, 31, 25))
        self.eightButton.setObjectName("eightButton")
        self.nineButton = QtWidgets.QPushButton(Form)
        self.nineButton.setGeometry(QtCore.QRect(190, 130, 31, 25))
        self.nineButton.setObjectName("nineButton")
        self.zeroButton = QtWidgets.QPushButton(Form)
        self.zeroButton.setGeometry(QtCore.QRect(150, 160, 31, 25))
        self.zeroButton.setObjectName("zeroButton")
        self.equalButton = QtWidgets.QPushButton(Form)
        self.equalButton.setGeometry(QtCore.QRect(20, 160, 31, 25))
        self.equalButton.setObjectName("equalButton")
        self.decimalButton = QtWidgets.QPushButton(Form)
        self.decimalButton.setGeometry(QtCore.QRect(190, 160, 31, 25))
        self.decimalButton.setObjectName("decimalButton")
        self.leftParenthesis = QtWidgets.QPushButton(Form)
        self.leftParenthesis.setGeometry(QtCore.QRect(110, 160, 16, 25))
        self.leftParenthesis.setObjectName("leftParenthesis")
        self.rightParenthesis = QtWidgets.QPushButton(Form)
        self.rightParenthesis.setGeometry(QtCore.QRect(130, 160, 16, 25))
        self.rightParenthesis.setObjectName("rightParenthesis")
        self.modButton = QtWidgets.QPushButton(Form)
        self.modButton.setGeometry(QtCore.QRect(60, 160, 31, 25))
        self.modButton.setObjectName("modButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.clearButton.setText(_translate("Form", "CLEAR"))
        self.plusButton.setText(_translate("Form", "+"))
        self.minusButton.setText(_translate("Form", "-"))
        self.multiplyButton.setText(_translate("Form", "X"))
        self.divideButton.setText(_translate("Form", "/"))
        self.oneButton.setText(_translate("Form", "1"))
        self.twoButton.setText(_translate("Form", "2"))
        self.threeButton.setText(_translate("Form", "3"))
        self.fourButton.setText(_translate("Form", "4"))
        self.fiveButton.setText(_translate("Form", "5"))
        self.sixButton.setText(_translate("Form", "6"))
        self.sevenButton.setText(_translate("Form", "7"))
        self.eightButton.setText(_translate("Form", "8"))
        self.nineButton.setText(_translate("Form", "9"))
        self.zeroButton.setText(_translate("Form", "0"))
        self.equalButton.setText(_translate("Form", "="))
        self.decimalButton.setText(_translate("Form", "."))
        self.leftParenthesis.setText(_translate("Form", "("))
        self.rightParenthesis.setText(_translate("Form", ")"))
        self.modButton.setText(_translate("Form", "%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
