# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/mmqgis_animate_rows_form.ui'
#
# Created: Thu Jun  5 21:02:08 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mmqgis_animate_rows_form(object):
    def setupUi(self, mmqgis_animate_rows_form):
        mmqgis_animate_rows_form.setObjectName(_fromUtf8("mmqgis_animate_rows_form"))
        mmqgis_animate_rows_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_animate_rows_form.setEnabled(True)
        mmqgis_animate_rows_form.resize(394, 311)
        mmqgis_animate_rows_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_animate_rows_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 270, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layernames = QtGui.QListWidget(mmqgis_animate_rows_form)
        self.layernames.setGeometry(QtCore.QRect(15, 30, 361, 151))
        self.layernames.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.layernames.setObjectName(_fromUtf8("layernames"))
        self.label_5 = QtGui.QLabel(mmqgis_animate_rows_form)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 121, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.browseoutfile = QtGui.QPushButton(mmqgis_animate_rows_form)
        self.browseoutfile.setGeometry(QtCore.QRect(300, 220, 79, 31))
        self.browseoutfile.setObjectName(_fromUtf8("browseoutfile"))
        self.label = QtGui.QLabel(mmqgis_animate_rows_form)
        self.label.setGeometry(QtCore.QRect(20, 200, 161, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.outdirname = QtGui.QLineEdit(mmqgis_animate_rows_form)
        self.outdirname.setGeometry(QtCore.QRect(20, 220, 271, 31))
        self.outdirname.setReadOnly(False)
        self.outdirname.setObjectName(_fromUtf8("outdirname"))

        self.retranslateUi(mmqgis_animate_rows_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_animate_rows_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_animate_rows_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_animate_rows_form)

    def retranslateUi(self, mmqgis_animate_rows_form):
        mmqgis_animate_rows_form.setWindowTitle(QtGui.QApplication.translate("mmqgis_animate_rows_form", "Animate Rows", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("mmqgis_animate_rows_form", "Layers to Animate", None, QtGui.QApplication.UnicodeUTF8))
        self.browseoutfile.setText(QtGui.QApplication.translate("mmqgis_animate_rows_form", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mmqgis_animate_rows_form", "Image Output Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.outdirname.setText(QtGui.QApplication.translate("mmqgis_animate_rows_form", "frames", None, QtGui.QApplication.UnicodeUTF8))

