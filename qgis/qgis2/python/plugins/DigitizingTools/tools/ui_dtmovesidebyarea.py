# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools/ui_dtmovesidebyarea.ui'
#
# Created by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DtMoveSideByArea(object):
    def setupUi(self, DtMoveSideByArea):
        DtMoveSideByArea.setObjectName(_fromUtf8("DtMoveSideByArea"))
        DtMoveSideByArea.resize(322, 171)
        self.gridLayout = QtGui.QGridLayout(DtMoveSideByArea)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(DtMoveSideByArea)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.area_label = QtGui.QLabel(DtMoveSideByArea)
        self.area_label.setMinimumSize(QtCore.QSize(112, 0))
        self.area_label.setText(_fromUtf8(""))
        self.area_label.setObjectName(_fromUtf8("area_label"))
        self.horizontalLayout.addWidget(self.area_label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(DtMoveSideByArea)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.targetArea = QtGui.QLineEdit(DtMoveSideByArea)
        self.targetArea.setReadOnly(False)
        self.targetArea.setObjectName(_fromUtf8("targetArea"))
        self.horizontalLayout_2.addWidget(self.targetArea)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.moveButton = QtGui.QPushButton(DtMoveSideByArea)
        self.moveButton.setObjectName(_fromUtf8("moveButton"))
        self.horizontalLayout_3.addWidget(self.moveButton)
        self.buttonClose = QtGui.QPushButton(DtMoveSideByArea)
        self.buttonClose.setObjectName(_fromUtf8("buttonClose"))
        self.horizontalLayout_3.addWidget(self.buttonClose)
        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 5, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(DtMoveSideByArea)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.radioFixed = QtGui.QRadioButton(DtMoveSideByArea)
        self.radioFixed.setChecked(True)
        self.radioFixed.setObjectName(_fromUtf8("radioFixed"))
        self.verticalLayout.addWidget(self.radioFixed)
        self.radioVariable = QtGui.QRadioButton(DtMoveSideByArea)
        self.radioVariable.setObjectName(_fromUtf8("radioVariable"))
        self.verticalLayout.addWidget(self.radioVariable)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 1)

        self.retranslateUi(DtMoveSideByArea)
        QtCore.QMetaObject.connectSlotsByName(DtMoveSideByArea)

    def retranslateUi(self, DtMoveSideByArea):
        DtMoveSideByArea.setWindowTitle(QtGui.QApplication.translate("DtMoveSideByArea", "Parallel Move Side By Area", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DtMoveSideByArea", "Area of the selected polygon:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DtMoveSideByArea", "Target Area:", None, QtGui.QApplication.UnicodeUTF8))
        self.moveButton.setText(QtGui.QApplication.translate("DtMoveSideByArea", "Move Side", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClose.setText(QtGui.QApplication.translate("DtMoveSideByArea", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DtMoveSideByArea", "Size of side to be moved:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioFixed.setText(QtGui.QApplication.translate("DtMoveSideByArea", "Fixed", None, QtGui.QApplication.UnicodeUTF8))
        self.radioVariable.setText(QtGui.QApplication.translate("DtMoveSideByArea", "Variable", None, QtGui.QApplication.UnicodeUTF8))

