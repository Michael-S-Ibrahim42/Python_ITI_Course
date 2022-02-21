# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SimpleGUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Lab")
        Form.resize(400, 300)
        self.textField = QLineEdit(Form)
        self.textField.setObjectName(u"textField")
        self.textField.setGeometry(QRect(10, 50, 231, 20))
        self.printBtn = QPushButton(Form)
        self.printBtn.setObjectName(u"printBtn")
        self.printBtn.setEnabled(False)
        self.printBtn.setGeometry(QRect(10, 80, 75, 23))
        self.clrBtn = QPushButton(Form)
        self.clrBtn.setObjectName(u"clrBtn")
        self.clrBtn.setEnabled(False)
        self.clrBtn.setGeometry(QRect(160, 80, 81, 23))
        self.printActivation = QCheckBox(Form)
        self.printActivation.setObjectName(u"printActivation")
        self.printActivation.setGeometry(QRect(289, 50, 91, 20))
        self.clrActivation = QCheckBox(Form)
        self.clrActivation.setObjectName(u"clrActivation")
        self.clrActivation.setGeometry(QRect(289, 70, 91, 20))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 0, 101, 31))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)

        self.retranslateUi(Form)
        self.clrBtn.clicked.connect(self.textField.clear)
        QObject.connect(self.printBtn, SIGNAL("clicked()"), printFn)
        QObject.connect(self.printBtn, SIGNAL("clicked()"), self.textField.clear)
        QObject.connect(self.clrActivation, SIGNAL("clicked(bool)"), self.clrBtn.setEnabled)
        QObject.connect(self.printActivation, SIGNAL("clicked(bool)"), self.printBtn.setEnabled)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.textField.setText(QCoreApplication.translate("Form", u"Enter your text here", None))
        self.printBtn.setText(QCoreApplication.translate("Form", u"Print", None))
        self.clrBtn.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.printActivation.setText(QCoreApplication.translate("Form", u"Activate Print", None))
        self.clrActivation.setText(QCoreApplication.translate("Form", u"Activate Clear", None))
        self.label.setText(QCoreApplication.translate("Form", u"Simple GUI", None))
    # retranslateUi
    
def printFn():
  print(Form.textField.text())

app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())