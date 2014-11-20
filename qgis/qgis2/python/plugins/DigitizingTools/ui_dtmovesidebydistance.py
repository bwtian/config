# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools/ui_dtmovesidebydistance.ui'
#
# Created by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DtMoveSideByDistance(object):
    def setupUi(self, DtMoveSideByDistance):
        DtMoveSideByDistance.setObjectName(_fromUtf8("DtMoveSideByDistance"))
        DtMoveSideByDistance.resize(322, 69)
        self.gridLayout = QtGui.QGridLayout(DtMoveSideByDistance)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(DtMoveSideByDistance)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.targetDistance = QtGui.QLineEdit(DtMoveSideByDistance)
        self.targetDistance.setReadOnly(False)
        self.targetDistance.setObjectName(_fromUtf8("targetDistance"))
        self.horizontalLayout_2.addWidget(self.targetDistance)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.moveButton = QtGui.QPushButton(DtMoveSideByDistance)
        self.moveButton.setObjectName(_fromUtf8("moveButton"))
        self.horizontalLayout_3.addWidget(self.moveButton)
        self.buttonClose = QtGui.QPushButton(DtMoveSideByDistance)
        self.buttonClose.setObjectName(_fromUtf8("buttonClose"))
        self.horizontalLayout_3.addWidget(self.buttonClose)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)

        self.retranslateUi(DtMoveSideByDistance)
        QtCore.QMetaObject.connectSlotsByName(DtMoveSideByDistance)

    def retranslateUi(self, DtMoveSideByDistance):
        DtMoveSideByDistance.setWindowTitle(QtGui.QApplication.translate("DtMoveSideByDistance", "Move Side By Distance", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DtMoveSideByDistance", "Move Distance:", None, QtGui.QApplication.UnicodeUTF8))
        self.moveButton.setText(QtGui.QApplication.translate("DtMoveSideByDistance", "Move Side", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClose.setText(QtGui.QApplication.translate("DtMoveSideByDistance", "Close", None, QtGui.QApplication.UnicodeUTF8))

