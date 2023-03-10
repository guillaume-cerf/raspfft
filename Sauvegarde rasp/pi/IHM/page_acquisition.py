# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\cyril\Documents\ENSAM_PC\GIE2\Projet Raspberry\Programmation\IHM\Qt_designer\page_acquisition.ui'
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

class Ui_Acquisition(object):
    def setupUi(self, Acquisition):
        Acquisition.setObjectName(_fromUtf8("Acquisition"))
        Acquisition.resize(675, 484)
        self.gridLayout = QtGui.QGridLayout(Acquisition)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.gridLayout.addLayout(self.formLayout_2, 3, 0, 1, 1)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.gridLayout.addLayout(self.formLayout_3, 3, 6, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.checkBox_accelx = QtGui.QCheckBox(Acquisition)
        self.checkBox_accelx.setObjectName(_fromUtf8("checkBox_accelx"))
        self.verticalLayout.addWidget(self.checkBox_accelx)
        self.checkBox_accely = QtGui.QCheckBox(Acquisition)
        self.checkBox_accely.setObjectName(_fromUtf8("checkBox_accely"))
        self.verticalLayout.addWidget(self.checkBox_accely)
        self.checkBox_accelz = QtGui.QCheckBox(Acquisition)
        self.checkBox_accelz.setObjectName(_fromUtf8("checkBox_accelz"))
        self.verticalLayout.addWidget(self.checkBox_accelz)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.comboBox_FourrierTempo = QtGui.QComboBox(Acquisition)
        self.comboBox_FourrierTempo.setObjectName(_fromUtf8("comboBox_FourrierTempo"))
        self.comboBox_FourrierTempo.addItem(_fromUtf8(""))
        self.comboBox_FourrierTempo.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox_FourrierTempo)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout, 3, 4, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 5, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 4, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 3, 1, 1)
        self.matplotlibwidget = MatplotlibWidget(Acquisition)
        self.matplotlibwidget.setObjectName(_fromUtf8("matplotlibwidget"))
        self.gridLayout.addWidget(self.matplotlibwidget, 1, 2, 3, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 0, 2, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.progressBar = QtGui.QProgressBar(Acquisition)
        self.progressBar.setProperty("value", 8)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.progressBar)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtGui.QFormLayout.LabelRole, spacerItem9)
        self.gridLayout.addLayout(self.formLayout, 1, 4, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.PushButton_Fermer = QtGui.QPushButton(Acquisition)
        self.PushButton_Fermer.setObjectName(_fromUtf8("PushButton_Fermer"))
        self.horizontalLayout.addWidget(self.PushButton_Fermer)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.PushButton_Nouveau = QtGui.QPushButton(Acquisition)
        self.PushButton_Nouveau.setObjectName(_fromUtf8("PushButton_Nouveau"))
        self.horizontalLayout.addWidget(self.PushButton_Nouveau)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.PushButton_Reglages = QtGui.QPushButton(Acquisition)
        self.PushButton_Reglages.setObjectName(_fromUtf8("PushButton_Reglages"))
        self.horizontalLayout.addWidget(self.PushButton_Reglages)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.PushButton_Exporter = QtGui.QPushButton(Acquisition)
        self.PushButton_Exporter.setObjectName(_fromUtf8("PushButton_Exporter"))
        self.horizontalLayout.addWidget(self.PushButton_Exporter)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 5)

        self.retranslateUi(Acquisition)
        QtCore.QMetaObject.connectSlotsByName(Acquisition)

    def retranslateUi(self, Acquisition):
        Acquisition.setWindowTitle(_translate("Acquisition", "ACQUISITION", None))
        self.checkBox_accelx.setText(_translate("Acquisition", "Accélération en x", None))
        self.checkBox_accely.setText(_translate("Acquisition", "Accélération en y", None))
        self.checkBox_accelz.setText(_translate("Acquisition", "Accélération en z", None))
        self.comboBox_FourrierTempo.setItemText(0, _translate("Acquisition", "         Fourrier", None))
        self.comboBox_FourrierTempo.setItemText(1, _translate("Acquisition", "         Temporel", None))
        self.PushButton_Fermer.setText(_translate("Acquisition", "Fermer", None))
        self.PushButton_Nouveau.setText(_translate("Acquisition", "Nouveau", None))
        self.PushButton_Reglages.setText(_translate("Acquisition", "Réglages", None))
        self.PushButton_Exporter.setText(_translate("Acquisition", "Exporter", None))

from matplotlibwidget import MatplotlibWidget
