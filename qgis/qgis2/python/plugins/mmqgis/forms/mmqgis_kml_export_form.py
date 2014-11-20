# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_kml_export_form.ui'
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

class Ui_mmqgis_kml_export_form(object):
    def setupUi(self, mmqgis_kml_export_form):
        mmqgis_kml_export_form.setObjectName(_fromUtf8("mmqgis_kml_export_form"))
        mmqgis_kml_export_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_kml_export_form.setEnabled(True)
        mmqgis_kml_export_form.resize(373, 279)
        mmqgis_kml_export_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_kml_export_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 240, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_kml_export_form)
        self.label.setGeometry(QtCore.QRect(10, 180, 108, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.outfilename = QtGui.QLineEdit(mmqgis_kml_export_form)
        self.outfilename.setGeometry(QtCore.QRect(10, 200, 261, 31))
        self.outfilename.setReadOnly(False)
        self.outfilename.setObjectName(_fromUtf8("outfilename"))
        self.browseoutfile = QtGui.QPushButton(mmqgis_kml_export_form)
        self.browseoutfile.setGeometry(QtCore.QRect(280, 200, 79, 26))
        self.browseoutfile.setObjectName(_fromUtf8("browseoutfile"))
        self.sourcelayer = QtGui.QComboBox(mmqgis_kml_export_form)
        self.sourcelayer.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.sourcelayer.setObjectName(_fromUtf8("sourcelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_kml_export_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 108, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_2 = QtGui.QLabel(mmqgis_kml_export_form)
        self.label_2.setGeometry(QtCore.QRect(190, 60, 151, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.descriptionfields = QtGui.QListWidget(mmqgis_kml_export_form)
        self.descriptionfields.setGeometry(QtCore.QRect(190, 80, 161, 91))
        self.descriptionfields.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.descriptionfields.setObjectName(_fromUtf8("descriptionfields"))
        item = QtGui.QListWidgetItem()
        self.descriptionfields.addItem(item)
        item = QtGui.QListWidgetItem()
        self.descriptionfields.addItem(item)
        item = QtGui.QListWidgetItem()
        self.descriptionfields.addItem(item)
        item = QtGui.QListWidgetItem()
        self.descriptionfields.addItem(item)
        item = QtGui.QListWidgetItem()
        self.descriptionfields.addItem(item)
        self.namefield = QtGui.QComboBox(mmqgis_kml_export_form)
        self.namefield.setGeometry(QtCore.QRect(10, 80, 161, 31))
        self.namefield.setObjectName(_fromUtf8("namefield"))
        self.descriptionseparator = QtGui.QComboBox(mmqgis_kml_export_form)
        self.descriptionseparator.setGeometry(QtCore.QRect(10, 140, 161, 31))
        self.descriptionseparator.setObjectName(_fromUtf8("descriptionseparator"))
        self.label_3 = QtGui.QLabel(mmqgis_kml_export_form)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 108, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(mmqgis_kml_export_form)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 151, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(mmqgis_kml_export_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_kml_export_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_kml_export_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_kml_export_form)

    def retranslateUi(self, mmqgis_kml_export_form):
        mmqgis_kml_export_form.setWindowTitle(QtGui.QApplication.translate("mmqgis_kml_export_form", "Google Maps KML Export", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mmqgis_kml_export_form", "Output KML File", None, QtGui.QApplication.UnicodeUTF8))
        self.outfilename.setText(QtGui.QApplication.translate("mmqgis_kml_export_form", "data.csv", None, QtGui.QApplication.UnicodeUTF8))
        self.browseoutfile.setText(QtGui.QApplication.translate("mmqgis_kml_export_form", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("mmqgis_kml_export_form", "Source Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("mmqgis_kml_export_form", "Description Fields", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.descriptionfields.isSortingEnabled()
        self.descriptionfields.setSortingEnabled(False)
        item = self.descriptionfields.item(0)
        item.setText(QtGui.QApplication.translate("mmqgis_kml_export_form", "Alpha", None, QtGui.QApplication.UnicodeUTF8))
        item = self.descriptionfields.item(1)
        item.setText(QtGui.QApplication.translate("mmqgis_kml_export_form", "Beta", None, QtGui.QApplication.UnicodeUTF8))
        item = self.descriptionfields.item(2)
        item.setText(QtGui.QApplication.translate("mmqgis_kml_export_form", "Gamma", None, QtGui.QApplication.UnicodeUTF8))
        item = self.descriptionfields.item(3)
        item.setText(QtGui.QApplication.translate("mmqgis_kml_export_form", "Delta", None, QtGui.QApplication.UnicodeUTF8))
        item = self.descriptionfields.item(4)
        item.setText(QtGui.QApplication.translate("mmqgis_kml_export_form", "Epsilon", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionfields.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(QtGui.QApplication.translate("mmqgis_kml_export_form", "Name Field", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("mmqgis_kml_export_form", "Description Separator", None, QtGui.QApplication.UnicodeUTF8))

