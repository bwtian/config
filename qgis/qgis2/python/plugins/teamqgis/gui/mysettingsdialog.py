#-----------------------------------------------------------
#
# teamqgis is a QGIS plugin which allows you to browse a multiple selection.
#
# Copyright    : (C) 2013 Denis Rouzaud
# Email        : denis.rouzaud@gmail.com
#
#-----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this progsram; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#---------------------------------------------------------------------

from PyQt4.Qt import Qt
from PyQt4.QtCore import pyqtSlot, SIGNAL
from PyQt4.QtGui import QDialog, QSizePolicy, QListWidgetItem
from qgis.gui import QgsMessageBar
from qgis.core import QgsProject

from ..qgissettingmanager import SettingDialog

from ..core.mysettings import MySettings

from ..ui.ui_settings import Ui_Settings


class MySettingsDialog(QDialog, Ui_Settings, SettingDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.settings = MySettings()
        SettingDialog.__init__(self, self.settings)

        self.bar = QgsMessageBar()
        self.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.layout().addWidget(self.bar, 0, 0, 1, 2)

        self.proj = QgsProject.instance()

        allowedClasses, hasAllowedClasses = self.proj.readListEntry("teamqgis", "allowedClasses")
        if hasAllowedClasses: self.addEditableItems(allowedClasses)

        self.addClassLineEdit.textEdited.connect(self.addClassLineEdit_textEdited)
        self.addClassLineEdit.textChanged.connect(self.addClassLineEdit_textChanged)

        self.classesListWidget.itemSelectionChanged.connect(self.classesListWidget_selectionChanged)

        classesListWidgetModel = self.classesListWidget.model()
        classesListWidgetModel.rowsRemoved.connect(self.classesListWidgetModel_dataChanged)
        classesListWidgetModel.rowsInserted.connect(self.classesListWidgetModel_dataChanged)
        classesListWidgetModel.dataChanged.connect(self.classesListWidgetModel_dataChanged)
        classesListWidgetModel.layoutChanged.connect(self.classesListWidgetModel_dataChanged)

    def addClassLineEdit_textChanged(self):
        if self.addClassLineEdit.text() == "": self.addClassButton.setEnabled(False)

    def addClassLineEdit_textEdited(self):
        self.addClassButton.setEnabled(True)

    def closeEvent(self, event):
        self.addClassLineEdit.textEdited.disconnect(self.addClassLineEdit_textEdited)
        self.addClassLineEdit.textChanged.disconnect(self.addClassLineEdit_textChanged)

    def classesListWidget_selectionChanged(self):
        if self.classesListWidget.count() > 0:
            self.removeClassButton.setEnabled(True)
        else:
            self.removeClassButton.setEnabled(False)

    def classesListWidgetModel_dataChanged(self, *arg):
        if self.classesListWidget.count() > 0:
            self.removeClassButton.setEnabled(True)
        else:
            self.removeClassButton.setEnabled(False)
        allowedClasses = [self.classesListWidget.item(n).text() for n in 
                range(self.classesListWidget.count())]
        self.proj.writeEntry('teamqgis', 'allowedClasses', allowedClasses)
        self.proj.emit(SIGNAL("allowedClassesChanged()"))

    def addEditableItem(self, item):
        # Don't iterate over each character when a single item is passed:
        newItem = QListWidgetItem(item)
        newItem.setData(Qt.UserRole, item)
        newItem.setFlags(newItem.flags() | Qt.ItemIsEditable)
        self.classesListWidget.addItem(newItem)

    def addEditableItems(self, items):
        for item in items:
            self.addEditableItem(item)

    @pyqtSlot(name="on_removeClassButton_clicked")
    def removeClassButton_clicked(self):
        self.classesListWidget.takeItem(self.classesListWidget.currentRow())

    @pyqtSlot(name="on_addClassButton_clicked")
    def addClassButton_clicked(self):
        newClass = self.addClassLineEdit.text()
        self.addClassLineEdit.clear()
        if newClass != "":
            existingClasses = [self.classesListWidget.item(n).text() for n in range(self.classesListWidget.count())]
            if newClass in existingClasses:
                self.bar.pushMessage("Error", '"%s" already in allowed classes list'%newClass, level=QgsMessageBar.WARNING, duration=3)
            else:
                self.addEditableItem(newClass)
        self.addClassButton.setEnabled(False)
