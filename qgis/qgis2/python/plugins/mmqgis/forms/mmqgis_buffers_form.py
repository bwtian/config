# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/mmqgis_buffers_form.ui'
#
# Created: Thu Jul 10 14:26:03 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mmqgis_buffers_form(object):
    def setupUi(self, mmqgis_buffers_form):
        mmqgis_buffers_form.setObjectName(_fromUtf8("mmqgis_buffers_form"))
        mmqgis_buffers_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_buffers_form.setEnabled(True)
        mmqgis_buffers_form.resize(372, 315)
        mmqgis_buffers_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_buffers_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 280, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_buffers_form)
        self.label.setGeometry(QtCore.QRect(10, 220, 261, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.filename = QtGui.QLineEdit(mmqgis_buffers_form)
        self.filename.setGeometry(QtCore.QRect(10, 240, 261, 31))
        self.filename.setReadOnly(False)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.browse = QtGui.QPushButton(mmqgis_buffers_form)
        self.browse.setGeometry(QtCore.QRect(280, 240, 79, 26))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.sourcelayer = QtGui.QComboBox(mmqgis_buffers_form)
        self.sourcelayer.setGeometry(QtCore.QRect(10, 30, 351, 31))
        self.sourcelayer.setObjectName(_fromUtf8("sourcelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 121, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.buffershape = QtGui.QComboBox(mmqgis_buffers_form)
        self.buffershape.setGeometry(QtCore.QRect(200, 90, 161, 31))
        self.buffershape.setObjectName(_fromUtf8("buffershape"))
        self.label_6 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_6.setGeometry(QtCore.QRect(200, 70, 121, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.radius = QtGui.QLineEdit(mmqgis_buffers_form)
        self.radius.setGeometry(QtCore.QRect(10, 150, 161, 31))
        self.radius.setObjectName(_fromUtf8("radius"))
        self.label_8 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_8.setGeometry(QtCore.QRect(10, 130, 81, 22))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.radiusunit = QtGui.QComboBox(mmqgis_buffers_form)
        self.radiusunit.setGeometry(QtCore.QRect(10, 90, 161, 31))
        self.radiusunit.setObjectName(_fromUtf8("radiusunit"))
        self.label_9 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 81, 22))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_7 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_7.setGeometry(QtCore.QRect(200, 130, 121, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.radiusattribute = QtGui.QComboBox(mmqgis_buffers_form)
        self.radiusattribute.setGeometry(QtCore.QRect(200, 150, 161, 31))
        self.radiusattribute.setObjectName(_fromUtf8("radiusattribute"))
        self.selectedonly = QtGui.QCheckBox(mmqgis_buffers_form)
        self.selectedonly.setGeometry(QtCore.QRect(10, 190, 181, 20))
        self.selectedonly.setObjectName(_fromUtf8("selectedonly"))

        self.retranslateUi(mmqgis_buffers_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_buffers_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_buffers_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_buffers_form)

    def retranslateUi(self, mmqgis_buffers_form):
        mmqgis_buffers_form.setWindowTitle(QtGui.QApplication.translate("mmqgis_buffers_form", "Create Buffers", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mmqgis_buffers_form", "Output Shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.filename.setText(QtGui.QApplication.translate("mmqgis_buffers_form", "temp.shp", None, QtGui.QApplication.UnicodeUTF8))
        self.browse.setText(QtGui.QApplication.translate("mmqgis_buffers_form", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("mmqgis_buffers_form", "Source Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("mmqgis_buffers_form", "Buffer Shape", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("mmqgis_buffers_form", "Fixed Radius", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("mmqgis_buffers_form", "Radius Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("mmqgis_buffers_form", "Radius Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.selectedonly.setText(QtGui.QApplication.translate("mmqgis_buffers_form", "Selected Features Only", None, QtGui.QApplication.UnicodeUTF8))

