# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_merge_form.ui'
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

class Ui_mmqgis_merge_form(object):
    def setupUi(self, mmqgis_merge_form):
        mmqgis_merge_form.setObjectName(_fromUtf8("mmqgis_merge_form"))
        mmqgis_merge_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_merge_form.setEnabled(True)
        mmqgis_merge_form.resize(372, 346)
        mmqgis_merge_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_merge_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 310, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_merge_form)
        self.label.setGeometry(QtCore.QRect(10, 250, 121, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.outfilename = QtGui.QLineEdit(mmqgis_merge_form)
        self.outfilename.setGeometry(QtCore.QRect(10, 270, 261, 21))
        self.outfilename.setReadOnly(False)
        self.outfilename.setObjectName(_fromUtf8("outfilename"))
        self.browseoutfile = QtGui.QPushButton(mmqgis_merge_form)
        self.browseoutfile.setGeometry(QtCore.QRect(280, 270, 79, 26))
        self.browseoutfile.setObjectName(_fromUtf8("browseoutfile"))
        self.label_4 = QtGui.QLabel(mmqgis_merge_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 141, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.sourcelayers = QtGui.QListWidget(mmqgis_merge_form)
        self.sourcelayers.setGeometry(QtCore.QRect(10, 30, 341, 211))
        self.sourcelayers.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.sourcelayers.setObjectName(_fromUtf8("sourcelayers"))
        item = QtGui.QListWidgetItem()
        self.sourcelayers.addItem(item)
        item = QtGui.QListWidgetItem()
        self.sourcelayers.addItem(item)
        item = QtGui.QListWidgetItem()
        self.sourcelayers.addItem(item)
        item = QtGui.QListWidgetItem()
        self.sourcelayers.addItem(item)
        item = QtGui.QListWidgetItem()
        self.sourcelayers.addItem(item)

        self.retranslateUi(mmqgis_merge_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_merge_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_merge_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_merge_form)

    def retranslateUi(self, mmqgis_merge_form):
        mmqgis_merge_form.setWindowTitle(QtGui.QApplication.translate("mmqgis_merge_form", "Merge Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mmqgis_merge_form", "Output Shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.outfilename.setText(QtGui.QApplication.translate("mmqgis_merge_form", "merge.csv", None, QtGui.QApplication.UnicodeUTF8))
        self.browseoutfile.setText(QtGui.QApplication.translate("mmqgis_merge_form", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("mmqgis_merge_form", "Select Source Layers", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.sourcelayers.isSortingEnabled()
        self.sourcelayers.setSortingEnabled(False)
        item = self.sourcelayers.item(0)
        item.setText(QtGui.QApplication.translate("mmqgis_merge_form", "Alpha", None, QtGui.QApplication.UnicodeUTF8))
        item = self.sourcelayers.item(1)
        item.setText(QtGui.QApplication.translate("mmqgis_merge_form", "Beta", None, QtGui.QApplication.UnicodeUTF8))
        item = self.sourcelayers.item(2)
        item.setText(QtGui.QApplication.translate("mmqgis_merge_form", "Gamma", None, QtGui.QApplication.UnicodeUTF8))
        item = self.sourcelayers.item(3)
        item.setText(QtGui.QApplication.translate("mmqgis_merge_form", "Delta", None, QtGui.QApplication.UnicodeUTF8))
        item = self.sourcelayers.item(4)
        item.setText(QtGui.QApplication.translate("mmqgis_merge_form", "Epsilon", None, QtGui.QApplication.UnicodeUTF8))
        self.sourcelayers.setSortingEnabled(__sortingEnabled)

