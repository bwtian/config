# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_label_form.ui'
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

class Ui_mmqgis_label_form(object):
    def setupUi(self, mmqgis_label_form):
        mmqgis_label_form.setObjectName(_fromUtf8("mmqgis_label_form"))
        mmqgis_label_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_label_form.setEnabled(True)
        mmqgis_label_form.resize(372, 234)
        mmqgis_label_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_label_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 190, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_label_form)
        self.label.setGeometry(QtCore.QRect(10, 130, 261, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(mmqgis_label_form)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 131, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.filename = QtGui.QLineEdit(mmqgis_label_form)
        self.filename.setGeometry(QtCore.QRect(10, 150, 261, 31))
        self.filename.setReadOnly(False)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.browse = QtGui.QPushButton(mmqgis_label_form)
        self.browse.setGeometry(QtCore.QRect(280, 150, 79, 26))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.labelattribute = QtGui.QComboBox(mmqgis_label_form)
        self.labelattribute.setGeometry(QtCore.QRect(10, 90, 351, 27))
        self.labelattribute.setObjectName(_fromUtf8("labelattribute"))
        self.sourcelayer = QtGui.QComboBox(mmqgis_label_form)
        self.sourcelayer.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.sourcelayer.setObjectName(_fromUtf8("sourcelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_label_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 121, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(mmqgis_label_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_label_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_label_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_label_form)

    def retranslateUi(self, mmqgis_label_form):
        mmqgis_label_form.setWindowTitle(QtGui.QApplication.translate("mmqgis_label_form", "Create Label Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mmqgis_label_form", "Output Shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("mmqgis_label_form", "Label Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.filename.setText(QtGui.QApplication.translate("mmqgis_label_form", "labels.shp", None, QtGui.QApplication.UnicodeUTF8))
        self.browse.setText(QtGui.QApplication.translate("mmqgis_label_form", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("mmqgis_label_form", "Source Layer", None, QtGui.QApplication.UnicodeUTF8))

