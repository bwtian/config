# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_select_form.ui'
#
# Created: Fri Dec 20 08:54:20 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mmqgis_select_form(object):
    def setupUi(self, mmqgis_select_form):
        mmqgis_select_form.setObjectName(_fromUtf8("mmqgis_select_form"))
        mmqgis_select_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_select_form.setEnabled(True)
        mmqgis_select_form.resize(372, 310)
        mmqgis_select_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_select_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 270, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_select_form)
        self.label.setGeometry(QtCore.QRect(10, 210, 261, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(mmqgis_select_form)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 131, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.filename = QtGui.QLineEdit(mmqgis_select_form)
        self.filename.setGeometry(QtCore.QRect(10, 230, 261, 21))
        self.filename.setReadOnly(False)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.browse = QtGui.QPushButton(mmqgis_select_form)
        self.browse.setGeometry(QtCore.QRect(280, 230, 79, 26))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.selectattribute = QtGui.QComboBox(mmqgis_select_form)
        self.selectattribute.setGeometry(QtCore.QRect(10, 80, 351, 27))
        self.selectattribute.setObjectName(_fromUtf8("selectattribute"))
        self.sourcelayer = QtGui.QComboBox(mmqgis_select_form)
        self.sourcelayer.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.sourcelayer.setObjectName(_fromUtf8("sourcelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_select_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 121, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comparison = QtGui.QComboBox(mmqgis_select_form)
        self.comparison.setGeometry(QtCore.QRect(10, 130, 351, 27))
        self.comparison.setObjectName(_fromUtf8("comparison"))
        self.label_5 = QtGui.QLabel(mmqgis_select_form)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 131, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.value = QtGui.QLineEdit(mmqgis_select_form)
        self.value.setGeometry(QtCore.QRect(10, 180, 351, 22))
        self.value.setObjectName(_fromUtf8("value"))
        self.label_6 = QtGui.QLabel(mmqgis_select_form)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 131, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(mmqgis_select_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_select_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_select_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_select_form)

    def retranslateUi(self, mmqgis_select_form):
        mmqgis_select_form.setWindowTitle(QtGui.QApplication.translate("mmqgis_select_form", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mmqgis_select_form", "Output Shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("mmqgis_select_form", "Select Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.filename.setText(QtGui.QApplication.translate("mmqgis_select_form", "temp.shp", None, QtGui.QApplication.UnicodeUTF8))
        self.browse.setText(QtGui.QApplication.translate("mmqgis_select_form", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("mmqgis_select_form", "Source Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("mmqgis_select_form", "Comparison", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("mmqgis_select_form", "Value", None, QtGui.QApplication.UnicodeUTF8))

