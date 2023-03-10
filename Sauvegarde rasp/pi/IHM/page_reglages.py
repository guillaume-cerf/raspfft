# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\cyril\Documents\ENSAM_PC\GIE2\Projet Raspberry\Programmation\IHM\Qt_designer\page_reglages.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Reglages(object):
    def setupUi(self, Reglages):
        Reglages.setObjectName(_fromUtf8("Reglages"))
        Reglages.resize(518, 312)
        #Reglages.setMaximumSize(QtCore.QSize(518, 512))
        #Reglages.showMaximized()  #plein écran
        #Reglages.showFullScreen()  #affichage plein ecran
        self.gridLayout = QtGui.QGridLayout(Reglages)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox_freq = QtGui.QComboBox(Reglages)
        self.comboBox_freq.setObjectName(_fromUtf8("comboBox_freq"))
        self.comboBox_freq.addItem(_fromUtf8(""))
        self.comboBox_freq.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_freq, 5, 3, 1, 1)
        self.comboBox_accel = QtGui.QComboBox(Reglages)
        self.comboBox_accel.setObjectName(_fromUtf8("comboBox_accel"))
        self.comboBox_accel.addItem(_fromUtf8(""))
        self.comboBox_accel.addItem(_fromUtf8(""))
        self.comboBox_accel.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_accel, 2, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 5, 1, 1)
        self.label_freq = QtGui.QLabel(Reglages)
        self.label_freq.setObjectName(_fromUtf8("label_freq"))
        self.gridLayout.addWidget(self.label_freq, 5, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.label_accel = QtGui.QLabel(Reglages)
        self.label_accel.setObjectName(_fromUtf8("label_accel"))
        self.gridLayout.addWidget(self.label_accel, 2, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 9, 3, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 6, 3, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 1, 3, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 0, 3, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 2, 4, 1, 1)
        self.PushButton_retour = QtGui.QPushButton(Reglages)
        self.PushButton_retour.setObjectName(_fromUtf8("PushButton_retour"))
        self.gridLayout.addWidget(self.PushButton_retour, 7, 4, 1, 1)
        self.PushButton_valider = QtGui.QPushButton(Reglages)
        self.PushButton_valider.setObjectName(_fromUtf8("PushButton_valider"))
        self.gridLayout.addWidget(self.PushButton_valider, 8, 4, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 7, 5, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 7, 3, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 7, 2, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 7, 1, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 7, 0, 1, 1)

        self.retranslateUi(Reglages)
        QtCore.QMetaObject.connectSlotsByName(Reglages)

    def retranslateUi(self, Reglages):
        Reglages.setWindowTitle(_translate("Reglages", "REGLAGES", None))
        self.comboBox_freq.setItemText(0, _translate("Reglages", "      200 Hz", None))
        self.comboBox_freq.setItemText(1, _translate("Reglages", "      400 Hz", None))
        self.comboBox_accel.setItemText(0, _translate("Reglages", "      ± 2g", None))
        self.comboBox_accel.setItemText(1, _translate("Reglages", "      ± 4g", None))
        self.comboBox_accel.setItemText(2, _translate("Reglages", "      ± 8g", None))
        self.label_freq.setText(_translate("Reglages", "Fréquence d\'échantillionnage :", None))
        self.label_accel.setText(_translate("Reglages", "     Gamme d\'accélération :", None))
        self.PushButton_retour.setText(_translate("Reglages", "Retour", None))
        self.PushButton_valider.setText(_translate("Reglages", "Valider", None))

