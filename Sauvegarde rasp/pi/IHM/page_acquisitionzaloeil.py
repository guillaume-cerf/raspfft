# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\cyril\Documents\ENSAM_PC\GIE2\Projet Raspberry\Programmation\IHM\Qt_designer\page_acquisitionzaloeil.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from matplotlibwidget_linux import MatplotlibWidget ####evite probleme en allant sur raspberry : a été copié dans le dossier "Projet Raspberry" et est à mettre sur clé USB

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
        #Acquisition.showFullScreen()  #affichage plein ecran
        self.gridLayout = QtGui.QGridLayout(Acquisition)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.progressBar = QtGui.QProgressBar(Acquisition)
        self.progressBar.setProperty("value", 8)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
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
        self.gridLayout.addLayout(self.verticalLayout, 5, 5, 1, 1)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.gridLayout.addLayout(self.formLayout_3, 5, 7, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 5, 6, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 4, 3, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 2, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 5, 4, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 6, 3, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 5, 2, 1, 1)
        self.matplotlibwidget = MatplotlibWidget(Acquisition) ##Avec hold=True pour superposer, les titres ne fonctionnent pas
        self.matplotlibwidget.setObjectName(_fromUtf8("matplotlibwidget"))
        self.gridLayout.addWidget(self.matplotlibwidget, 5, 3, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout, 7, 2, 1, 5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.label = QtGui.QLabel(Acquisition)
        self.label.setMaximumSize(QtCore.QSize(150, 40))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../ensam-logo.jpg")))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 2, 1, 5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem15, 8, 2, 1, 1)

        self.retranslateUi(Acquisition)
        QtCore.QMetaObject.connectSlotsByName(Acquisition)

    def retranslateUi(self, Acquisition):
        Acquisition.setWindowTitle(_translate("Acquisition", "ACQUISITION", None))
        self.checkBox_accelx.setText(_translate("Acquisition", "Accélération en x", None))
        self.checkBox_accely.setText(_translate("Acquisition", "Accélération en y", None))
        self.checkBox_accelz.setText(_translate("Acquisition", "Accélération en z", None))
        self.comboBox_FourrierTempo.setItemText(0, _translate("Acquisition", "         Temporel", None))
        self.comboBox_FourrierTempo.setItemText(1, _translate("Acquisition", "         Fourrier", None))
        self.PushButton_Fermer.setText(_translate("Acquisition", "Fermer", None))
        self.PushButton_Nouveau.setText(_translate("Acquisition", "Nouveau", None))
        self.PushButton_Reglages.setText(_translate("Acquisition", "Réglages", None))
        self.PushButton_Exporter.setText(_translate("Acquisition", "Exporter", None))
       


       
