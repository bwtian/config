# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_plugin_mask.ui'
#
# Created: Tue Jun  3 10:59:48 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName(_fromUtf8("MainDialog"))
        MainDialog.resize(695, 779)
        self.verticalLayout_4 = QtGui.QVBoxLayout(MainDialog)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox = QtGui.QGroupBox(MainDialog)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.stylePreview = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stylePreview.sizePolicy().hasHeightForWidth())
        self.stylePreview.setSizePolicy(sizePolicy)
        self.stylePreview.setFrameShape(QtGui.QFrame.Box)
        self.stylePreview.setLineWidth(1)
        self.stylePreview.setMidLineWidth(0)
        self.stylePreview.setText(_fromUtf8(""))
        self.stylePreview.setObjectName(_fromUtf8("stylePreview"))
        self.horizontalLayout_4.addWidget(self.stylePreview)
        self.editStyleBtn = QtGui.QPushButton(self.groupBox)
        self.editStyleBtn.setObjectName(_fromUtf8("editStyleBtn"))
        self.horizontalLayout_4.addWidget(self.editStyleBtn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.bufferGroup = QtGui.QGroupBox(MainDialog)
        self.bufferGroup.setFlat(False)
        self.bufferGroup.setCheckable(True)
        self.bufferGroup.setChecked(False)
        self.bufferGroup.setObjectName(_fromUtf8("bufferGroup"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.bufferGroup)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.bufferGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.bufferUnits = QtGui.QLineEdit(self.bufferGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bufferUnits.sizePolicy().hasHeightForWidth())
        self.bufferUnits.setSizePolicy(sizePolicy)
        self.bufferUnits.setObjectName(_fromUtf8("bufferUnits"))
        self.horizontalLayout_3.addWidget(self.bufferUnits)
        self.label_4 = QtGui.QLabel(self.bufferGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.bufferSegments = QtGui.QLineEdit(self.bufferGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bufferSegments.sizePolicy().hasHeightForWidth())
        self.bufferSegments.setSizePolicy(sizePolicy)
        self.bufferSegments.setObjectName(_fromUtf8("bufferSegments"))
        self.horizontalLayout_3.addWidget(self.bufferSegments)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.bufferGroup)
        self.simplifyGroup = QtGui.QGroupBox(MainDialog)
        self.simplifyGroup.setCheckable(True)
        self.simplifyGroup.setChecked(True)
        self.simplifyGroup.setObjectName(_fromUtf8("simplifyGroup"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.simplifyGroup)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.simplifyGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.simplifyTolerance = QtGui.QLineEdit(self.simplifyGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simplifyTolerance.sizePolicy().hasHeightForWidth())
        self.simplifyTolerance.setSizePolicy(sizePolicy)
        self.simplifyTolerance.setObjectName(_fromUtf8("simplifyTolerance"))
        self.horizontalLayout_5.addWidget(self.simplifyTolerance)
        self.label_3 = QtGui.QLabel(self.simplifyGroup)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addWidget(self.simplifyGroup)
        self.labelingGroup = QtGui.QGroupBox(MainDialog)
        self.labelingGroup.setCheckable(False)
        self.labelingGroup.setChecked(False)
        self.labelingGroup.setObjectName(_fromUtf8("labelingGroup"))
        self.labelingLayout = QtGui.QVBoxLayout(self.labelingGroup)
        self.labelingLayout.setObjectName(_fromUtf8("labelingLayout"))
        self.verticalLayout_4.addWidget(self.labelingGroup)
        self.saveLayerGroup = QtGui.QGroupBox(MainDialog)
        self.saveLayerGroup.setCheckable(True)
        self.saveLayerGroup.setChecked(False)
        self.saveLayerGroup.setObjectName(_fromUtf8("saveLayerGroup"))
        self.verticalLayout = QtGui.QVBoxLayout(self.saveLayerGroup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filePath = QtGui.QLineEdit(self.saveLayerGroup)
        self.filePath.setObjectName(_fromUtf8("filePath"))
        self.horizontalLayout.addWidget(self.filePath)
        self.browseBtn = QtGui.QPushButton(self.saveLayerGroup)
        self.browseBtn.setObjectName(_fromUtf8("browseBtn"))
        self.horizontalLayout.addWidget(self.browseBtn)
        self.formatLbl = QtGui.QLabel(self.saveLayerGroup)
        self.formatLbl.setObjectName(_fromUtf8("formatLbl"))
        self.horizontalLayout.addWidget(self.formatLbl)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.saveLayerGroup)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(MainDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(MainDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MainDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MainDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(QtGui.QApplication.translate("MainDialog", "Define a mask", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setToolTip(QtGui.QApplication.translate("MainDialog", "Style to use for mask layer", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainDialog", "Style", None, QtGui.QApplication.UnicodeUTF8))
        self.editStyleBtn.setText(QtGui.QApplication.translate("MainDialog", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.bufferGroup.setToolTip(QtGui.QApplication.translate("MainDialog", "Buffer around the mask geometry", None, QtGui.QApplication.UnicodeUTF8))
        self.bufferGroup.setTitle(QtGui.QApplication.translate("MainDialog", "Buffer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainDialog", "Units", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainDialog", "Segments", None, QtGui.QApplication.UnicodeUTF8))
        self.bufferSegments.setText(QtGui.QApplication.translate("MainDialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.simplifyGroup.setToolTip(QtGui.QApplication.translate("MainDialog", "On-the-fly simplification used for the mask geometry used in expressions ($mask_geometry)", None, QtGui.QApplication.UnicodeUTF8))
        self.simplifyGroup.setTitle(QtGui.QApplication.translate("MainDialog", "On-the-fly simplification", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainDialog", "Tolerance", None, QtGui.QApplication.UnicodeUTF8))
        self.simplifyTolerance.setText(QtGui.QApplication.translate("MainDialog", "1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainDialog", "pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.labelingGroup.setToolTip(QtGui.QApplication.translate("MainDialog", "If a layer is checked here, its labeling options will be modified in order that its labels will be only visible from inside the mask\'s polygon", None, QtGui.QApplication.UnicodeUTF8))
        self.labelingGroup.setTitle(QtGui.QApplication.translate("MainDialog", "Limit labeling to mask\'s polygon", None, QtGui.QApplication.UnicodeUTF8))
        self.saveLayerGroup.setToolTip(QtGui.QApplication.translate("MainDialog", "Whether the save the mask layer. By default a memory layer is created", None, QtGui.QApplication.UnicodeUTF8))
        self.saveLayerGroup.setTitle(QtGui.QApplication.translate("MainDialog", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.browseBtn.setText(QtGui.QApplication.translate("MainDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.formatLbl.setText(QtGui.QApplication.translate("MainDialog", "\'\'", None, QtGui.QApplication.UnicodeUTF8))

