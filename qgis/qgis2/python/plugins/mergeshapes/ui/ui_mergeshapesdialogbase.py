# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mergeshapesdialogbase.ui'
#
# Created: Tue Jul 23 15:51:30 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MergeShapesDialog(object):
    def setupUi(self, MergeShapesDialog):
        MergeShapesDialog.setObjectName(_fromUtf8("MergeShapesDialog"))
        MergeShapesDialog.resize(377, 373)
        self.verticalLayout = QtGui.QVBoxLayout(MergeShapesDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.chkListMode = QtGui.QCheckBox(MergeShapesDialog)
        self.chkListMode.setObjectName(_fromUtf8("chkListMode"))
        self.verticalLayout.addWidget(self.chkListMode)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblGeometry = QtGui.QLabel(MergeShapesDialog)
        self.lblGeometry.setObjectName(_fromUtf8("lblGeometry"))
        self.horizontalLayout_3.addWidget(self.lblGeometry)
        self.cmbGeometry = QtGui.QComboBox(MergeShapesDialog)
        self.cmbGeometry.setObjectName(_fromUtf8("cmbGeometry"))
        self.cmbGeometry.addItem(_fromUtf8(""))
        self.cmbGeometry.addItem(_fromUtf8(""))
        self.cmbGeometry.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.cmbGeometry)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label = QtGui.QLabel(MergeShapesDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.leInputDir = QtGui.QLineEdit(MergeShapesDialog)
        self.leInputDir.setObjectName(_fromUtf8("leInputDir"))
        self.horizontalLayout.addWidget(self.leInputDir)
        self.btnSelectDir = QtGui.QPushButton(MergeShapesDialog)
        self.btnSelectDir.setObjectName(_fromUtf8("btnSelectDir"))
        self.horizontalLayout.addWidget(self.btnSelectDir)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtGui.QLabel(MergeShapesDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.leOutShape = QtGui.QLineEdit(MergeShapesDialog)
        self.leOutShape.setObjectName(_fromUtf8("leOutShape"))
        self.horizontalLayout_2.addWidget(self.leOutShape)
        self.btnSelectFile = QtGui.QPushButton(MergeShapesDialog)
        self.btnSelectFile.setObjectName(_fromUtf8("btnSelectFile"))
        self.horizontalLayout_2.addWidget(self.btnSelectFile)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.chkAddFileName = QtGui.QCheckBox(MergeShapesDialog)
        self.chkAddFileName.setObjectName(_fromUtf8("chkAddFileName"))
        self.verticalLayout.addWidget(self.chkAddFileName)
        self.chkAddFilePath = QtGui.QCheckBox(MergeShapesDialog)
        self.chkAddFilePath.setObjectName(_fromUtf8("chkAddFilePath"))
        self.verticalLayout.addWidget(self.chkAddFilePath)
        self.chkAddToCanvas = QtGui.QCheckBox(MergeShapesDialog)
        self.chkAddToCanvas.setObjectName(_fromUtf8("chkAddToCanvas"))
        self.verticalLayout.addWidget(self.chkAddToCanvas)
        self.progressFeatures = QtGui.QProgressBar(MergeShapesDialog)
        self.progressFeatures.setProperty("value", 0)
        self.progressFeatures.setObjectName(_fromUtf8("progressFeatures"))
        self.verticalLayout.addWidget(self.progressFeatures)
        self.progressFiles = QtGui.QProgressBar(MergeShapesDialog)
        self.progressFiles.setProperty("value", 0)
        self.progressFiles.setObjectName(_fromUtf8("progressFiles"))
        self.verticalLayout.addWidget(self.progressFiles)
        self.buttonBox = QtGui.QDialogButtonBox(MergeShapesDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MergeShapesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MergeShapesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MergeShapesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MergeShapesDialog)

    def retranslateUi(self, MergeShapesDialog):
        MergeShapesDialog.setWindowTitle(QtGui.QApplication.translate("MergeShapesDialog", "Merge shapefiles", None, QtGui.QApplication.UnicodeUTF8))
        self.chkListMode.setText(QtGui.QApplication.translate("MergeShapesDialog", "Select by layers in the folder", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGeometry.setText(QtGui.QApplication.translate("MergeShapesDialog", "Shapefile type", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGeometry.setItemText(0, QtGui.QApplication.translate("MergeShapesDialog", "Polygon", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGeometry.setItemText(1, QtGui.QApplication.translate("MergeShapesDialog", "Line", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGeometry.setItemText(2, QtGui.QApplication.translate("MergeShapesDialog", "Point", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MergeShapesDialog", "Input directory", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectDir.setText(QtGui.QApplication.translate("MergeShapesDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MergeShapesDialog", "Output shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectFile.setText(QtGui.QApplication.translate("MergeShapesDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAddFileName.setText(QtGui.QApplication.translate("MergeShapesDialog", "Add column with file name", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAddFilePath.setText(QtGui.QApplication.translate("MergeShapesDialog", "Add column with file path", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAddToCanvas.setText(QtGui.QApplication.translate("MergeShapesDialog", "Add result to map canvas", None, QtGui.QApplication.UnicodeUTF8))

