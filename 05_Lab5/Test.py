# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.InputLine = QLineEdit(Form)
        self.InputLine.setObjectName(u"InputLine")
        self.InputLine.setEnabled(True)
        self.InputLine.setGeometry(QRect(20, 20, 331, 20))
        self.clearBtn = QPushButton(Form)
        self.clearBtn.setObjectName(u"clearBtn")
        self.clearBtn.setGeometry(QRect(40, 60, 75, 23))
        self.printBtn = QPushButton(Form)
        self.printBtn.setObjectName(u"printBtn")
        self.printBtn.setGeometry(QRect(250, 60, 75, 23))

        self.retranslateUi(Form)
        self.clearBtn.clicked.connect(self.InputLine.clear)
        self.printBtn.clicked.connect(self.InputLine.clear)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"User Interface", None))
        self.InputLine.setText(QCoreApplication.translate("Form", u"Enter Your Text Here", None))
        self.clearBtn.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.printBtn.setText(QCoreApplication.translate("Form", u"Print", None))
    # retranslateUi

