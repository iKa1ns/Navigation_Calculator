# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import help_win
import sys
from parse import get_rwys
import pdf

class HelpWindow(QtWidgets.QMainWindow, help_win.Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(170, 116)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setPlaceholderText("")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_2.setMaxLength(4)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMaxLength(4)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 170, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 95, 21))
        self.menubar.setObjectName("menubar")       
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.triggered.connect(self.showDialog) 
        self.actionHelp.setObjectName("actionHelp")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.actionHelp)
            
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        self.msg.setText("Error")
        self.msg.setInformativeText('')
        self.msg.setWindowTitle("Error")
        
        
        rx  = QtCore.QRegExp("[a-zA-Z0-9]{100}")    
        val = QtGui.QRegExpValidator(rx) 
        self.lineEdit.setValidator(val)
        self.lineEdit_2.setValidator(val)
        
        self.lineEdit.textChanged[str].connect(self.onChanged)
        self.lineEdit_2.textChanged[str].connect(self.onChanged_1)
        self.pushButton.clicked.connect(self.calculate)
        self.pushButton.setEnabled(False)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Navigation Calculator"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Dest"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.label.setText(_translate("MainWindow", "Runways\nheadings"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Origin"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        
    def showDialog(self):
        self.HelpWindow = HelpWindow()
        self.HelpWindow.show()

    def onChanged(self, text):
        self.comboBox.clear()
        if len(text) == 4:
            array = get_rwys(text.upper())
            if len(array) != 0:
                for i, val in enumerate(array):
                    if i == 0:
                        continue
                    else:
                        self.comboBox.addItem(val)
                if self.comboBox_2.count() != 0:
                    self.pushButton.setEnabled(True)
                else:
                    self.pushButton.setEnabled(False)
            else:
                self.pushButton.setEnabled(False)
                self.msg.setInformativeText('Origin ICAO not found')
                self.msg.exec_()
        else:
            self.pushButton.setEnabled(False)
            
            
    def onChanged_1(self, text):
        self.comboBox_2.clear()
        if len(text) == 4:
            array = get_rwys(text.upper())
            if len(array) != 0:
                for i, val in enumerate(array):
                    if i == 0:
                        continue
                    else:
                        self.comboBox_2.addItem(val)
                if self.comboBox.count() != 0:
                    self.pushButton.setEnabled(True)
                else:
                    self.pushButton.setEnabled(False)
            else:
                self.pushButton.setEnabled(False)
                self.msg.setInformativeText('Dest ICAO not found')
                self.msg.exec_()
        else:
            self.pushButton.setEnabled(False)
    
    def calculate(self):
        air1 = self.lineEdit.text().upper()
        air2 = self.lineEdit_2.text().upper()
        hdg = int(self.comboBox.currentText())
        pdf.create_a_pdf(air1, air2, hdg)
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())