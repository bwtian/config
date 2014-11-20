# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_gridify_form.ui'
#
# Created: Fri Dec 20 08:54:19 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mmqgis_gridify_form(object):
    def setupUi(self, mmqgis_gridify_form):
        mmqgis_gridify_form.setObjectName(_fromUtf8("mmqgis_gridify_form"))
        mmqgis_gridify_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_gridify_form.setEnabled(True)
        mmqgis_gridify_form.resize(368, 240)
        mmqgis_gridify_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_gridify_form)
        self.buttonBox.setGeometry(QtCore.QRect(100, 200, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_gridify_form)
        self.label.setGeometry(QtCore.QRect(10, 130, 108, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(mmqgis_gridify_form)
        self.label_2.setGeometry(QtCore.QRect(190, 70, 67, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(mmqgis_gridify_form)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 68, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.filename = QtGui.QLineEdit(mmqgis_gridify_form)
        self.filename.setGeometry(QtCore.QRect(10, 150, 261, 28))
        self.filename.setReadOnly(False)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.browse = QtGui.QPushButton(mmqgis_gridify_form)
        self.browse.setGeometry(QtCore.QRect(280, 150, 79, 26))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.vspacing = QtGui.QLineEdit(mmqgis_gridify_form)
        self.vspacing.setGeometry(QtCore.QRect(190, 90, 171, 28))
        self.vspacing.setObjectName(_fromUtf8("vspacing"))
        self.hspacing = QtGui.QLineEdit(mmqgis_gridify_form)
        self.hspacing.setGeometry(QtCore.QRect(10, 90, 151, 28))
        self.hspacing.setObjectName(_fromUtf8("hspacing"))
        self.sourcelayer = QtGui.QComboBox(mmqgis_gridify_form)
        self.sourcelayer.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.sourcelayer.setObjectName(_fromUtf8("sourcelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_gridify_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 108, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(mmqgis_gridify_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_gridify_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_gridify_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_gridify_form)

    def retranslateUi(self, mmqgis_gridify_form):
        mmqgis_gridify_form.setWindowTitle(QtGui.QApplication.translate("mmqgis_gridify_form", "Gridify", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mmqgis_gridify_form", "Output Shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("mmqgis_gridify_form", "V Spacing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("mmqgis_gridify_form", "H Spacing", None, QtGui.QApplication.UnicodeUTF8))
        self.filename.setText(QtGui.QApplication.translate("mmqgis_gridify_form", "grid.shp", None, QtGui.QApplication.UnicodeUTF8))
        self.browse.setText(QtGui.QApplication.translate("mmqgis_gridify_form", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.vspacing.setText(QtGui.QApplication.translate("mmqgis_gridify_form", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.hspacing.setText(QtGui.QApplication.translate("mmqgis_gridify_form", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("mmqgis_gridify_form", "Source Layer", None, QtGui.QApplication.UnicodeUTF8))

