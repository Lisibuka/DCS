# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditSensors.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import pypyodbc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditSensors(object):
    def setupUi(self, EditSensors):
        EditSensors.setObjectName("EditSensors")
        EditSensors.resize(416, 434)
        self.centralwidget = QtWidgets.QWidget(EditSensors)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 110, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 150, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 190, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 70, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 110, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 150, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 190, 47, 13))
        self.label_4.setObjectName("label_4")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(150, 330, 75, 23))
        self.okButton.setObjectName("okButton")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 230, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 270, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 230, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 270, 47, 13))
        self.label_6.setObjectName("label_6")
        EditSensors.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EditSensors)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 416, 21))
        self.menubar.setObjectName("menubar")
        EditSensors.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EditSensors)
        self.statusbar.setObjectName("statusbar")
        EditSensors.setStatusBar(self.statusbar)

        self.retranslateUi(EditSensors)
        QtCore.QMetaObject.connectSlotsByName(EditSensors)

    def retranslateUi(self, EditSensors):
        _translate = QtCore.QCoreApplication.translate
        EditSensors.setWindowTitle(_translate("EditSensors", "MainWindow"))
        self.label.setText(_translate("EditSensors", "Серийный номер"))
        self.label_2.setText(_translate("EditSensors", "Показания"))
        self.label_3.setText(_translate("EditSensors", "Норма"))
        self.label_4.setText(_translate("EditSensors", "Включен"))
        self.okButton.setText(_translate("EditSensors", "OK"))
        self.label_5.setText(_translate("EditSensors", "Тип"))
        self.label_6.setText(_translate("EditSensors", "Станция"))

    def okbutton(self, serialkey):
        try:
            connection = pypyodbc.connect('Driver={SQL Server};'
                                          'Server=WIN-P66F1JER45H\SQLEXPRESS01;'
                                          'Database=rzd;')
            serial = self.lineEdit.text()
            readings= self.lineEdit_2.text()
            normal = self.lineEdit_3.text()
            status = self.lineEdit_4.text()
            type = self.lineEdit_5.text()
            station = self.lineEdit_6.text()
            cursor = connection.cursor()
            sqlquery = "UPDATE Sensors SET [Серийный номер] = '" + serial + "', Показания = '" + readings + "', Норма = '"\
                       + normal + "', Включен = '" + status + "', Тип = '" + type + "', Станция = '" + station + \
                       "' WHERE [Серийный номер] = '" + serialkey + "'"
            cursor.execute(sqlquery)
            connection.commit()
            connection.close()
        except:
            pass