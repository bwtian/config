# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_geometry_export_form.ui'
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

class Ui_mmqgis_geometry_export_form(object):
    def setupUi(self, mmqgis_geometry_export_form):
        mmqgis_geometry_export_form.setObjectName(_fromUtf8("mmqgis_geometry_export_form"))
        mmqgis_geometry_export_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_geometry_export_form.setEnabled(True)
        mmqgis_geometry_export_form.resize(373, 257)
        mmqgis_geometry_export_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_geometry_export_form)
        self.buttonBox.setGeometry(QtCore.QRect(100, 220, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_geometry_export_form)
        self.label.setGeometry(QtCore.QRect(10, 110, 181, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.attfilename = QtGui.QLineEdit(mmqgis_geometry_export_form)
        self.attfilename.setGeometry(QtCore.QRect(10, 130, 261, 21))
        self.attfilename.setReadOnly(False)
        self.attfilename.setObjectName(_fromUtf8("attfilename"))
        self.attbrowse = QtGui.QPushButton(mmqgis_geometry_export_form)
        self.attbrowse.setGeometry(QtCore.QRect(280, 130, 79, 26))
        self.attbrowse.setObjectName(_fromUtf8("attbrowse"))
        self.sourcelayer = QtGui.QComboBox(mmqgis_geometry_export_form)
        self.sourcelayer.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.sourcelayer.setObjectName(_fromUtf8("sourcelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_geometry_export_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 108, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.nodebrowse = QtGui.QPushButton(mmqgis_geometry_export_form)
        self.nodebrowse.setGeometry(QtCore.QRect(280, 80, 79, 26))
        self.nodebrowse.setObjectName(_fromUtf8("nodebrowse"))
        self.label_2 = QtGui.QLabel(mmqgis_geometry_export_form)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 151, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.nodefilename = QtGui.QLineEdit(mmqgis_geometry_export_form)
        self.nodefilename.setGeometry(QtCore.QRect(10, 80, 261, 21))
        self.nodefilename.setReadOnly(False)
        self.nodefilename.setObjectName(_fromUtf8("nodefilename"))
        self.lineterminator = QtGui.QComboBox(mmqgis_geometry_export_form)
        self.lineterminator.setGeometry(QtCore.QRect(230, 180, 121, 22))
        self.lineterminator.setObjectName(_fromUtf8("lineterminator"))
        self.lineterminator.addItem(_fromUtf8(""))
        self.lineterminator.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(mmqgis_geometry_export_form)
        self.label_5.setGeometry(QtCore.QRect(230, 160, 108, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.delimiter = QtGui.QComboBox(mmqgis_geometry_export_form)
        self.delimiter.setGeometry(QtCore.QRect(10, 180, 121, 22))
        self.delimiter.setObjectName(_fromUtf8("delimiter"))
        self.delimiter.addItem(_fromUtf8(""))
        self.delimiter.addItem(_fromUtf8(""))
        self.delimiter.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(mmqgis_geometry_export_form)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 108, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(mmqgis_geometry_export_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_geometry_export_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_geometry_export_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_geometry_export_form)

    def retranslateUi(self, mmqgis_geometry_export_form):
        mmqgis_geometry_export_form.setWindowTitle(QtGui.QApplication.translate("mmqgis_geometry_export_form", "Export Geometry to CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mmqgis_geometry_export_form", "Output Attributes CSV File", None, QtGui.QApplication.UnicodeUTF8))
        self.attfilename.setText(QtGui.QApplication.translate("mmqgis_geometry_export_form", "attributes.csv", None, QtGui.QApplication.UnicodeUTF8))
        self.attbrowse.setText(QtGui.QApplication.translate("mmqgis_geometry_export_form", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("mmqgis_geometry_export_form", "Source Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.nodebrowse.setText(QtGui.QApplication.translate("mmqgis_geometry_export_form", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("mmqgis_geometry_export_form", "Output Nodes CSV File", None, QtGui.QApplication.UnicodeUTF8))
        self.nodefilename.setText(QtGui.QApplication.translate("mmqgis_geometry_export_form", "nodes.csv", None, QtGui.QApplication.UnicodeUTF8))
        self.lineterminator.setItemText(0, QtGui.QApplication.translate("mmqgis_geometry_export_form", "CR-LF", None, QtGui.QApplication.UnicodeUTF8))
        self.lineterminator.setItemText(1, QtGui.QApplication.translate("mmqgis_geometry_export_form", "LF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("mmqgis_geometry_export_form", "Line Terminator", None, QtGui.QApplication.UnicodeUTF8))
        self.delimiter.setItemText(0, QtGui.QApplication.translate("mmqgis_geometry_export_form", "(comma)", None, QtGui.QApplication.UnicodeUTF8))
        self.delimiter.setItemText(1, QtGui.QApplication.translate("mmqgis_geometry_export_form", "(bar)", None, QtGui.QApplication.UnicodeUTF8))
        self.delimiter.setItemText(2, QtGui.QApplication.translate("mmqgis_geometry_export_form", "(space)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("mmqgis_geometry_export_form", "Delimiter", None, QtGui.QApplication.UnicodeUTF8))

