# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_search_form.ui'
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

class Ui_mmqgis_search_form(object):
    def setupUi(self, mmqgis_search_form):
        mmqgis_search_form.setObjectName(_fromUtf8("mmqgis_search_form"))
        mmqgis_search_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_search_form.setEnabled(True)
        mmqgis_search_form.resize(596, 396)
        mmqgis_search_form.setMouseTracking(False)
        self.results = QtGui.QListWidget(mmqgis_search_form)
        self.results.setGeometry(QtCore.QRect(10, 200, 571, 151))
        self.results.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.results.setObjectName(_fromUtf8("results"))
        self.label_5 = QtGui.QLabel(mmqgis_search_form)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 121, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.donebutton = QtGui.QPushButton(mmqgis_search_form)
        self.donebutton.setGeometry(QtCore.QRect(270, 360, 79, 31))
        self.donebutton.setAutoDefault(False)
        self.donebutton.setObjectName(_fromUtf8("donebutton"))
        self.searchlayer = QtGui.QComboBox(mmqgis_search_form)
        self.searchlayer.setGeometry(QtCore.QRect(10, 20, 421, 31))
        self.searchlayer.setObjectName(_fromUtf8("searchlayer"))
        self.label_4 = QtGui.QLabel(mmqgis_search_form)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 121, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.search = QtGui.QPushButton(mmqgis_search_form)
        self.search.setGeometry(QtCore.QRect(470, 20, 79, 31))
        self.search.setObjectName(_fromUtf8("search"))
        self.label_3 = QtGui.QLabel(mmqgis_search_form)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 131, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.attribute1 = QtGui.QComboBox(mmqgis_search_form)
        self.attribute1.setGeometry(QtCore.QRect(10, 80, 171, 31))
        self.attribute1.setObjectName(_fromUtf8("attribute1"))
        self.label_6 = QtGui.QLabel(mmqgis_search_form)
        self.label_6.setGeometry(QtCore.QRect(190, 60, 101, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.comparison1 = QtGui.QComboBox(mmqgis_search_form)
        self.comparison1.setGeometry(QtCore.QRect(190, 80, 101, 31))
        self.comparison1.setObjectName(_fromUtf8("comparison1"))
        self.label_7 = QtGui.QLabel(mmqgis_search_form)
        self.label_7.setGeometry(QtCore.QRect(300, 60, 71, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.value1 = QtGui.QLineEdit(mmqgis_search_form)
        self.value1.setGeometry(QtCore.QRect(300, 80, 281, 31))
        self.value1.setObjectName(_fromUtf8("value1"))
        self.comparison2 = QtGui.QComboBox(mmqgis_search_form)
        self.comparison2.setGeometry(QtCore.QRect(190, 140, 101, 31))
        self.comparison2.setObjectName(_fromUtf8("comparison2"))
        self.value2 = QtGui.QLineEdit(mmqgis_search_form)
        self.value2.setGeometry(QtCore.QRect(300, 140, 281, 31))
        self.value2.setObjectName(_fromUtf8("value2"))
        self.attribute2 = QtGui.QComboBox(mmqgis_search_form)
        self.attribute2.setGeometry(QtCore.QRect(10, 140, 171, 31))
        self.attribute2.setObjectName(_fromUtf8("attribute2"))
        self.label_8 = QtGui.QLabel(mmqgis_search_form)
        self.label_8.setGeometry(QtCore.QRect(10, 120, 131, 22))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.retranslateUi(mmqgis_search_form)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_search_form)

    def retranslateUi(self, mmqgis_search_form):
        mmqgis_search_form.setWindowTitle(QtGui.QApplication.translate("mmqgis_search_form", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("mmqgis_search_form", "Results", None, QtGui.QApplication.UnicodeUTF8))
        self.donebutton.setText(QtGui.QApplication.translate("mmqgis_search_form", "Done", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("mmqgis_search_form", "Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.search.setText(QtGui.QApplication.translate("mmqgis_search_form", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("mmqgis_search_form", "Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("mmqgis_search_form", "Comparison", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("mmqgis_search_form", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("mmqgis_search_form", "And...", None, QtGui.QApplication.UnicodeUTF8))

