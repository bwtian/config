# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample_rasters_gui.ui'
#
# Created: Thu Feb 13 22:25:42 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(433, 455)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 413, 393))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelDecimal = QtGui.QLabel(self.layoutWidget)
        self.labelDecimal.setObjectName(_fromUtf8("labelDecimal"))
        self.gridLayout.addWidget(self.labelDecimal, 5, 2, 1, 1)
        self.labelRasterClass = QtGui.QLabel(self.layoutWidget)
        self.labelRasterClass.setObjectName(_fromUtf8("labelRasterClass"))
        self.gridLayout.addWidget(self.labelRasterClass, 0, 0, 1, 2)
        self.labelRasters = QtGui.QLabel(self.layoutWidget)
        self.labelRasters.setObjectName(_fromUtf8("labelRasters"))
        self.gridLayout.addWidget(self.labelRasters, 3, 0, 1, 1)
        self.labelSaveCsv = QtGui.QLabel(self.layoutWidget)
        self.labelSaveCsv.setObjectName(_fromUtf8("labelSaveCsv"))
        self.gridLayout.addWidget(self.labelSaveCsv, 6, 0, 1, 1)
        self.pushButtonSaveCsv = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonSaveCsv.setObjectName(_fromUtf8("pushButtonSaveCsv"))
        self.gridLayout.addWidget(self.pushButtonSaveCsv, 7, 3, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 9, 0, 1, 4)
        self.listWidget = QtGui.QListWidget(self.layoutWidget)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 4, 0, 1, 4)
        self.lineEditSaveCsv = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditSaveCsv.setObjectName(_fromUtf8("lineEditSaveCsv"))
        self.gridLayout.addWidget(self.lineEditSaveCsv, 7, 0, 1, 3)
        self.comboBoxRasterClass = QtGui.QComboBox(self.layoutWidget)
        self.comboBoxRasterClass.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBoxRasterClass.setObjectName(_fromUtf8("comboBoxRasterClass"))
        self.gridLayout.addWidget(self.comboBoxRasterClass, 1, 0, 1, 4)
        self.labelNoData = QtGui.QLabel(self.layoutWidget)
        self.labelNoData.setObjectName(_fromUtf8("labelNoData"))
        self.gridLayout.addWidget(self.labelNoData, 2, 0, 1, 1)
        self.lineEditNoData = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditNoData.setObjectName(_fromUtf8("lineEditNoData"))
        self.gridLayout.addWidget(self.lineEditNoData, 2, 1, 1, 1)
        self.labelDisconsiderar = QtGui.QLabel(self.layoutWidget)
        self.labelDisconsiderar.setObjectName(_fromUtf8("labelDisconsiderar"))
        self.gridLayout.addWidget(self.labelDisconsiderar, 2, 2, 1, 1)
        self.lineEditDisconsiderar = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditDisconsiderar.setObjectName(_fromUtf8("lineEditDisconsiderar"))
        self.gridLayout.addWidget(self.lineEditDisconsiderar, 2, 3, 1, 1)
        self.lineEditDecimal = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditDecimal.setObjectName(_fromUtf8("lineEditDecimal"))
        self.gridLayout.addWidget(self.lineEditDecimal, 5, 3, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 420, 301, 29))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonExit = QtGui.QPushButton(self.layoutWidget1)
        self.pushButtonExit.setObjectName(_fromUtf8("pushButtonExit"))
        self.horizontalLayout.addWidget(self.pushButtonExit)
        self.pushButtonOk = QtGui.QPushButton(self.layoutWidget1)
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.horizontalLayout.addWidget(self.pushButtonOk)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Sample rasters", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDecimal.setText(QtGui.QApplication.translate("Form", "Decimal", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRasterClass.setText(QtGui.QApplication.translate("Form", "Raster with the classes", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRasters.setText(QtGui.QApplication.translate("Form", "Rasters", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSaveCsv.setText(QtGui.QApplication.translate("Form", "Save csv", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSaveCsv.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNoData.setText(QtGui.QApplication.translate("Form", "NoData", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDisconsiderar.setText(QtGui.QApplication.translate("Form", "Disconsider", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonExit.setText(QtGui.QApplication.translate("Form", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOk.setText(QtGui.QApplication.translate("Form", "Ok", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

