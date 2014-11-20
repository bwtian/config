# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools/ui_dtmovenodebyarea.ui'
#
# Created by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DtMoveNodeByArea(object):
    def setupUi(self, DtMoveNodeByArea):
        DtMoveNodeByArea.setObjectName(_fromUtf8("DtMoveNodeByArea"))
        DtMoveNodeByArea.resize(322, 108)
        self.gridLayout = QtGui.QGridLayout(DtMoveNodeByArea)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(DtMoveNodeByArea)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.area_label = QtGui.QLabel(DtMoveNodeByArea)
        self.area_label.setMinimumSize(QtCore.QSize(112, 0))
        self.area_label.setText(_fromUtf8(""))
        self.area_label.setObjectName(_fromUtf8("area_label"))
        self.horizontalLayout.addWidget(self.area_label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(DtMoveNodeByArea)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.targetArea = QtGui.QLineEdit(DtMoveNodeByArea)
        self.targetArea.setReadOnly(False)
        self.targetArea.setObjectName(_fromUtf8("targetArea"))
        self.horizontalLayout_2.addWidget(self.targetArea)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.moveButton = QtGui.QPushButton(DtMoveNodeByArea)
        self.moveButton.setObjectName(_fromUtf8("moveButton"))
        self.horizontalLayout_3.addWidget(self.moveButton)
        self.buttonClose = QtGui.QPushButton(DtMoveNodeByArea)
        self.buttonClose.setObjectName(_fromUtf8("buttonClose"))
        self.horizontalLayout_3.addWidget(self.buttonClose)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)

        self.retranslateUi(DtMoveNodeByArea)
        QtCore.QMetaObject.connectSlotsByName(DtMoveNodeByArea)

    def retranslateUi(self, DtMoveNodeByArea):
        DtMoveNodeByArea.setWindowTitle(QtGui.QApplication.translate("DtMoveNodeByArea", "Move Node By Area", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DtMoveNodeByArea", "Area of the selected polygon:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DtMoveNodeByArea", "Target Area:", None, QtGui.QApplication.UnicodeUTF8))
        self.moveButton.setText(QtGui.QApplication.translate("DtMoveNodeByArea", "Move Node", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClose.setText(QtGui.QApplication.translate("DtMoveNodeByArea", "Close", None, QtGui.QApplication.UnicodeUTF8))

