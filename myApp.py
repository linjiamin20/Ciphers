# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myApp.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import caesar, playfair, vigenere
import re
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setIconSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.MainVerticalGrid = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.MainVerticalGrid.setContentsMargins(10, 10, 10, 10)
        self.MainVerticalGrid.setSpacing(15)
        self.MainVerticalGrid.setObjectName("MainVerticalGrid")
        self.PlainTextLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.PlainTextLabel.setObjectName("PlainTextLabel")
        self.MainVerticalGrid.addWidget(self.PlainTextLabel)
        self.PlainTextContainer = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.PlainTextContainer.setObjectName("PlainTextContainer")
        self.MainVerticalGrid.addWidget(self.PlainTextContainer)
        self.CipherTextLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.CipherTextLabel.setObjectName("CipherTextLabel")
        self.MainVerticalGrid.addWidget(self.CipherTextLabel)
        self.CipherTextContainer = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.CipherTextContainer.setObjectName("CipherTextContainer")
        self.MainVerticalGrid.addWidget(self.CipherTextContainer)
        self.CiphersContainer = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.CiphersContainer.setMinimumSize(QtCore.QSize(0, 90))
        self.CiphersContainer.setObjectName("CiphersContainer")
        self.CipherRBGrid = QtWidgets.QWidget(self.CiphersContainer)
        self.CipherRBGrid.setGeometry(QtCore.QRect(-1, 9, 781, 81))
        self.CipherRBGrid.setObjectName("CipherRBGrid")
        self.CipherGrid = QtWidgets.QHBoxLayout(self.CipherRBGrid)
        self.CipherGrid.setContentsMargins(10, 10, 10, 10)
        self.CipherGrid.setSpacing(15)
        self.CipherGrid.setObjectName("CipherGrid")
        self.CaesarRB = QtWidgets.QRadioButton(self.CipherRBGrid)
        self.CaesarRB.setObjectName("CaesarRB")
        self.CipherGrid.addWidget(self.CaesarRB)
        self.PlayfairRB = QtWidgets.QRadioButton(self.CipherRBGrid)
        self.PlayfairRB.setObjectName("PlayfairRB")
        self.CipherGrid.addWidget(self.PlayfairRB)
        self.VigenereRB = QtWidgets.QRadioButton(self.CipherRBGrid)
        self.VigenereRB.setObjectName("VigenereRB")
        self.CipherGrid.addWidget(self.VigenereRB)
        self.MainVerticalGrid.addWidget(self.CiphersContainer)
        self.KeyLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.KeyLabel.setObjectName("KeyLabel")
        self.MainVerticalGrid.addWidget(self.KeyLabel)
        self.KeyContainer = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.KeyContainer.setObjectName("KeyContainer")
        self.MainVerticalGrid.addWidget(self.KeyContainer)
        self.ButtonGrid = QtWidgets.QHBoxLayout()
        self.ButtonGrid.setContentsMargins(10, 10, 10, 10)
        self.ButtonGrid.setSpacing(15)
        self.ButtonGrid.setObjectName("ButtonGrid")
        self.EncryptButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.EncryptButton.setMinimumSize(QtCore.QSize(0, 40))
        self.EncryptButton.setObjectName("EncryptButton")
        self.EncryptButton.clicked.connect(self.EncryptHandler)
        self.ButtonGrid.addWidget(self.EncryptButton)
        self.DecryptButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.DecryptButton.setMinimumSize(QtCore.QSize(0, 40))
        self.DecryptButton.setObjectName("DecryptButton")
        self.DecryptButton.clicked.connect(self.DecryptHandler)
        self.ButtonGrid.addWidget(self.DecryptButton)
        self.ResetButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ResetButton.setMinimumSize(QtCore.QSize(0, 40))
        self.ResetButton.setObjectName("ResetButton")
        self.ButtonGrid.addWidget(self.ResetButton)
        self.ResetButton.clicked.connect(self.ResettHandler)
        self.MainVerticalGrid.addLayout(self.ButtonGrid)
        self.CipherRBGroup = QtWidgets.QButtonGroup()
        self.CipherRBGroup.addButton(self.CaesarRB, 1)
        self.CipherRBGroup.addButton(self.PlayfairRB, 2)
        self.CipherRBGroup.addButton(self.VigenereRB, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cipher by Mahmoud Ahmedy"))
        self.PlainTextLabel.setText(_translate("MainWindow", "Plain text:"))
        self.CipherTextLabel.setText(_translate("MainWindow", "Ciphered text:"))
        self.CiphersContainer.setTitle(_translate("MainWindow", "GroupBox"))
        self.CaesarRB.setText(_translate("MainWindow", "Caesar Cipher"))
        self.PlayfairRB.setText(_translate("MainWindow", "Playfair Cipher"))
        self.VigenereRB.setText(_translate("MainWindow", "Vigenere Cipher"))
        self.KeyLabel.setText(_translate("MainWindow", "Key"))
        self.EncryptButton.setText(_translate("MainWindow", "Encrypt"))
        self.DecryptButton.setText(_translate("MainWindow", "Decrypt"))
        self.ResetButton.setText(_translate("MainWindow", "Reset"))
    
    def keyErrorMessage(self, msgText):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(msgText)
        msg.setWindowTitle("Key Error")
        msg.exec_()

    def EncryptHandler(self):
        CipherID = self.CipherRBGroup.checkedId()
        plainText = self.PlainTextContainer.toPlainText()
        key = self.KeyContainer.text()
        
        if CipherID == 1:
            if re.match('^[0-9]+$', key):
                cipherText = caesar.Encrypt(plainText, key)
            else:
                cipherText = ''
                self.keyErrorMessage("The key must be an integer value in Caesar cipher")                
                
        if CipherID == 2:
            if re.match('^[a-zA-Z]+$', key):
                cipherText = playfair.Encrypt(plainText, key)
            else:
                cipherText = ''
                self.keyErrorMessage("The key must be a text in Playfair cipher")
        if CipherID == 3:
            if re.match('^[a-zA-Z]+$', key):
                cipherText = vigenere.Encrypt(plainText, key)
            else:
                cipherText = ''
                self.keyErrorMessage("The key must be a text in Vinegere cipher")
               
        self.CipherTextContainer.setPlainText(cipherText)

    def DecryptHandler(self):
        CipherID = self.CipherRBGroup.checkedId()
        cipherText = self.CipherTextContainer.toPlainText()
        key = self.KeyContainer.text()

        if CipherID == 1:
            if re.match('^[0-9]+$', key):
                plainText = caesar.Decrypt(cipherText, key)
            else:
                plainText = ''
                self.keyErrorMessage("The key must be an integer value in Caesar cipher")                
                
        if CipherID == 2:
            if re.match('^[a-zA-Z]+$', key):
                plainText = playfair.Decrypt(cipherText, key)
            else:
                plainText = ''
                self.keyErrorMessage("The key must be a text in Playfair cipher")
        if CipherID == 3:
            if re.match('^[a-zA-Z]+$', key):
                plainText = vigenere.Decrypt(cipherText, key)
            else:
                plainText = ''
                self.keyErrorMessage("The key must be a text in Vinegere cipher")
                   
        self.PlainTextContainer.setPlainText(plainText)

    def ResettHandler(self):
        self.CipherTextContainer.clear()
        self.PlainTextContainer.clear()
        self.KeyContainer.clear()


