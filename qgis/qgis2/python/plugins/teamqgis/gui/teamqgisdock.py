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

from PyQt4.QtCore import SIGNAL, pyqtSlot, pyqtSignal, Qt, QVariant, QObject
from PyQt4.QtGui import QDockWidget, QIcon, QAction
from qgis.core import QgsPoint, QgsRectangle, QgsFeatureRequest, QgsFeature, QgsProject
from qgis.gui import QgsRubberBand, QgsMessageBar
from qgis.utils import iface

from ..core.mysettings import MySettings
from ..ui.ui_teamqgis import Ui_teamqgis

class teamqgisDock(QDockWidget, Ui_teamqgis):
    dockRemoved = pyqtSignal(str)

    def __init__(self, iface, layer, currentFeature):
        self.iface = iface
        self.layer = layer
        self.proj = QgsProject.instance()
        self.renderer = self.iface.mapCanvas().mapRenderer()
        self.settings = MySettings()
        QDockWidget.__init__(self)
        self.setupUi(self)

        # Track attr warnings so they are not repeated for multiple items
        self.warned_attr_values = []

        self.setWindowTitle("teamqgis: %s" % layer.name())
        if layer.hasGeometryType() is False:
            self.panCheck.setChecked(False)
            self.panCheck.setEnabled(False)
            self.scaleCheck.setChecked(False)
            self.scaleCheck.setEnabled(False)

        self.previousButton.setArrowType(Qt.LeftArrow)
        self.nextButton.setArrowType(Qt.RightArrow)
        icon = QIcon(":/plugins/teamqgis/icons/openform.svg")
        self.editFormButton.setIcon(icon)

        # actions
        icon = QIcon(":/plugins/teamqgis/icons/action.svg")
        self.actionButton.setIcon(icon)
        self.attrAction = layer.actions()
        actions = [self.attrAction[i] for i in range(self.attrAction.size())]
        preferredAction = layer.customProperty("teamqgisPreferedAction", "")
        if preferredAction not in actions:
            dfltAction = self.attrAction.defaultAction()
            if dfltAction > len(actions):
                preferredAction = self.attrAction[dfltAction].name()
        preferredActionFound = False
        for i, action in enumerate(actions):
            qAction = QAction(QIcon(":/plugins/teamqgis/icons/action.svg"), action.name(), self)
            qAction.triggered.connect(lambda: self.doAction(i))
            self.actionButton.addAction(qAction)
            if action.name() == preferredAction:
                self.actionButton.setDefaultAction(qAction)
                preferredActionFound = True
        if len(actions) == 0:
            self.actionButton.setEnabled(False)
        elif not preferredActionFound:
            self.actionButton.setDefaultAction(self.actionButton.actions()[0])

        self.nameComboBoxes = [self.fieldOneNameComboBox, self.fieldTwoNameComboBox, self.fieldThreeNameComboBox]
        self.valueComboBoxes = [self.fieldOneValueComboBox, self.fieldTwoValueComboBox, self.fieldThreeValueComboBox]

        self.updateNameComboBoxes()

        # Restore saved nameComboBox current indices if they exist
        for nameComboBox in self.nameComboBoxes:
            fieldName = self.layer.customProperty("teamqgis" + nameComboBox.objectName())
            if fieldName != None:
                nameComboBox.setCurrentIndex(nameComboBox.findText(fieldName))

        self.rubber = QgsRubberBand(self.iface.mapCanvas())
        self.selectionChanged()
        if currentFeature == self.listCombo.currentIndex():
            self.on_listCombo_currentIndexChanged(currentFeature)
        else:
            self.listCombo.setCurrentIndex(currentFeature)
        self.layer.layerDeleted.connect(self.close)
        self.layer.selectionChanged.connect(self.selectionChanged)
        self.layer.layerModified.connect(self.layerChanged)
        self.layer.editingStopped.connect(self.editingStopped)
        self.layer.editingStarted.connect(self.editingStarted)

        QObject.connect(self.proj, SIGNAL("allowedClassesChanged()"), self.updateValueComboBoxes)

    def updateNameComboBoxes(self):
        fieldNameMap = self.layer.dataProvider().fieldNameMap()
        allFields = fieldNameMap.keys()
        if 'ID' in allFields: allFields.remove('ID')
        if 'FID' in allFields: allFields.remove('FID')
        for nameComboBox in self.nameComboBoxes:
            nameComboBox.clear()
            nameComboBox.addItems(allFields)

    def updateValueComboBoxes(self):
        feature = self.getCurrentItem()
        for (valueComboBox, nameComboBox) in zip(self.valueComboBoxes, 
                self.nameComboBoxes):
            valueComboBox.clear()
            allowedClasses, hasAllowedClasses = self.proj.readListEntry("teamqgis", "allowedClasses")
            if hasAllowedClasses:
                valueComboBox.addItems(allowedClasses)
            attr_value = str(feature[nameComboBox.currentText()])
            if (allowedClasses == None) or (attr_value not in allowedClasses) and (attr_value not in self.warned_attr_values):
                self.iface.messageBar().pushMessage("Class name not in allowed class list",
                    'Assign an allowed class or add "%s" to allowed class list'%attr_value,
                    level=QgsMessageBar.WARNING, duration=3)
                self.warned_attr_values.append(attr_value)
                valueComboBox.addItem(attr_value)
            valueComboBox.setCurrentIndex(valueComboBox.findText(attr_value))

    def setRubber(self, feature):
        self.rubber.setColor(self.settings.value("rubberColor"))
        self.rubber.setWidth(self.settings.value("rubberWidth"))
        ##self.rubber.setLineStyle(Qt.DotLine)
        self.rubber.setBrushStyle(Qt.NoBrush)
        self.rubber.setToGeometry(feature.geometry(), self.layer)

    def closeEvent(self, e):
        self.rubber.reset()
        self.layer.layerDeleted.disconnect(self.close)
        self.layer.selectionChanged.disconnect(self.selectionChanged)
        self.layer.layerModified.disconnect(self.layerChanged)
        self.layer.editingStopped.disconnect(self.editingStopped)
        self.layer.editingStarted.disconnect(self.editingStarted)
        if self.settings.value("saveSelectionInProject"):
            self.layer.setCustomProperty("teamqgisSelection", repr([]))
        self.dockRemoved.emit(self.layer.id())
          
    def selectionChanged(self):
        self.cleanBrowserFields()
        self.rubber.reset()
        nItems = self.layer.selectedFeatureCount()
        if nItems < 1:
            self.close()
            self.layer.emit(SIGNAL("browserNoItem()"))
            return
        self.browseFrame.setEnabled(True)
        self.subset = self.layer.selectedFeaturesIds()
        if self.settings.value("saveSelectionInProject"):
            self.layer.setCustomProperty("teamqgisSelection", repr(self.subset))
        for fid in self.subset:
            self.listCombo.addItem("%u" % fid)
        self.setRubber(self.getCurrentItem())
        self.updateValueComboBoxes()

    def layerChanged(self):
        self.applyChangesButton.setEnabled(True)

    def editingStarted(self):
        for valueComboBox in self.valueComboBoxes:
            valueComboBox.setEnabled(True)
        self.translateRightButton.setEnabled(True)
        self.translateLeftButton.setEnabled(True)
        self.translateUpButton.setEnabled(True)
        self.translateDownButton.setEnabled(True)
        self.editFormButton.setDown(True)

    def editingStopped(self):
        self.applyChangesButton.setEnabled(False)
        for valueComboBox in self.valueComboBoxes:
            valueComboBox.setEnabled(False)
        self.translateRightButton.setEnabled(False)
        self.translateLeftButton.setEnabled(False)
        self.translateUpButton.setEnabled(False)
        self.translateDownButton.setEnabled(False)
        self.editFormButton.setDown(False)

    def cleanBrowserFields(self):
        self.currentPosLabel.setText('0/0')
        self.listCombo.clear()
          
    def panScaleToItem(self, feature):
        if self.panCheck.isChecked() is False:
            return
        featBobo = feature.geometry().boundingBox()
        # if scaling and bobo has width and height (i.e. not a point)
        if self.scaleCheck.isChecked() and featBobo.width() != 0 and featBobo.height() != 0:
            featBobo.scale(self.settings.value("scale"))
            ul = self.renderer.layerToMapCoordinates(self.layer, QgsPoint(featBobo.xMinimum(), featBobo.yMaximum()))
            ur = self.renderer.layerToMapCoordinates(self.layer, QgsPoint(featBobo.xMaximum(), featBobo.yMaximum()))
            ll = self.renderer.layerToMapCoordinates(self.layer, QgsPoint(featBobo.xMinimum(), featBobo.yMinimum()))
            lr = self.renderer.layerToMapCoordinates(self.layer, QgsPoint(featBobo.xMaximum(), featBobo.yMinimum()))
            x = (ul.x(), ur.x(), ll.x(), lr.x())
            y = (ul.y(), ur.y(), ll.y(), lr.y())
            x0 = min(x)
            y0 = min(y)
            x1 = max(x)
            y1 = max(y)
        else:
            panTo = self.renderer.layerToMapCoordinates(self.layer, featBobo.center())
            mapBobo = self.iface.mapCanvas().extent()
            xshift = panTo.x() - mapBobo.center().x()
            yshift = panTo.y() - mapBobo.center().y()
            x0 = mapBobo.xMinimum() + xshift
            y0 = mapBobo.yMinimum() + yshift
            x1 = mapBobo.xMaximum() + xshift
            y1 = mapBobo.yMaximum() + yshift
        self.iface.mapCanvas().setExtent(QgsRectangle(x0, y0, x1, y1))
        self.iface.mapCanvas().refresh()

    def getCurrentItem(self):
        i = self.listCombo.currentIndex()
        if i == -1:
            return None
        f = QgsFeature()
        if self.layer.getFeatures(QgsFeatureRequest().setFilterFid(self.subset[i])).nextFeature(f):
            return f
        else:
            raise NameError("feature not found")

    def doAction(self, i):
        f = self.getCurrentItem()
        self.actionButton.setDefaultAction(self.actionButton.actions()[i])
        self.layer.setCustomProperty("teamqgisPreferedAction", self.attrAction[i].name())
        self.attrAction.doActionFeature(i, f)

    def doTranslate(self, trans):
        # Based on the "doaffine" function in the qgsAffine plugin
        if (self.layer.geometryType() == 2):
            start=1
        else:
            start=0
        if (not self.layer.isEditable()):
            self.iface.messageBar().pushMessage("Layer not in edit mode",
                    'Select a vector layer and choose "Toggle Editing"', level=QgsMessageBar.WARNING)
        else:
            feature = self.getCurrentItem()
            result = feature.geometry()
            i = start
            vertex = result.vertexAt(i)
            fid = feature.id()
            while (vertex != QgsPoint(0, 0)):
                newx = vertex.x() + trans[0] * float(self.settings.value("xres"))
                newy = vertex.y() + trans[1] * float(self.settings.value("yres"))
                result.moveVertex(newx, newy, i)
                i += 1
                vertex = result.vertexAt(i)
            self.layer.changeGeometry(fid, result)
            self.iface.mapCanvas().refresh()
            self.rubber.reset()
            self.setRubber(feature)

    def changeAttribute(self, i, fieldNameComboBox, fieldValueComboBox):
        fieldValueComboBox.setCurrentIndex(i)
        feature = self.getCurrentItem()
        attr_index = self.layer.dataProvider().fieldNameMap()[fieldNameComboBox.currentText()]
        self.layer.changeAttributeValue(feature.id(), attr_index, 
                fieldValueComboBox.currentText())
        self.iface.mapCanvas().refresh()
        self.updateValueComboBoxes()

    def nameComboBox_activated(self, i, nameComboBox):
        self.layer.setCustomProperty('teamqgis' + nameComboBox.objectName(), nameComboBox.currentText())

    @pyqtSlot(name="on_previousButton_clicked")
    def previousFeature(self):
        i = self.listCombo.currentIndex()
        n = max(0, i-1)
        self.listCombo.setCurrentIndex(n)
        self.saveCurrentFeature(n)

    @pyqtSlot(name="on_nextButton_clicked")
    def nextFeature(self):
        self.warned_attr_values = [] # Reset attr warnings
        i = self.listCombo.currentIndex()
        c = self.listCombo.count()
        n = min(i+1, c-1)
        self.listCombo.setCurrentIndex(n)
        self.saveCurrentFeature(n)

    @pyqtSlot(int, name="on_listCombo_activated")
    def saveCurrentFeature(self, i):
        if self.settings.value("saveSelectionInProject"):
            self.layer.setCustomProperty("teamqgisCurrentItem", i)

    @pyqtSlot(int, name="on_fieldOneNameComboBox_activated")
    def fieldOneNameComboBox_activated(self, i):
        self.nameComboBox_activated(i, self.fieldOneNameComboBox)

    @pyqtSlot(int, name="on_fieldTwoNameComboBox_activated")
    def fieldTwoNameComboBox_activated(self, i):
        self.nameComboBox_activated(i, self.fieldTwoNameComboBox)

    @pyqtSlot(int, name="on_fieldThreeNameComboBox_activated")
    def fieldThreeNameComboBox_activated(self, i):
        self.nameComboBox_activated(i, self.fieldThreeNameComboBox)

    @pyqtSlot(int, name="on_listCombo_currentIndexChanged")
    def on_listCombo_currentIndexChanged(self, i):
        feature = self.getCurrentItem()
        if feature is None: 
            return
        self.rubber.reset()
        if self.listCombo.count() > 1:
            self.setRubber(feature)
            self.updateValueComboBoxes()
        # scale to feature
        self.panScaleToItem(feature)
        # Update browser
        self.currentPosLabel.setText("%u/%u" % (i+1, len(self.subset)))
        # emit signal
        self.layer.emit(SIGNAL("browserCurrentItem(long)"), feature.id())
          
    @pyqtSlot(int, name="on_panCheck_stateChanged")
    def on_panCheck_stateChanged(self, i):
        if self.panCheck.isChecked():
            self.scaleCheck.setEnabled(True)
            feature = self.getCurrentItem()
            if feature is None:
                return
            self.panScaleToItem(feature)
        else:
            self.scaleCheck.setEnabled(False)
               
    @pyqtSlot(int, name="on_scaleCheck_stateChanged")
    def on_scaleCheck_stateChanged(self, i):
        if self.scaleCheck.isChecked():
            feature = self.getCurrentItem()
            if feature is None: 
                return
            self.panScaleToItem(feature)

    @pyqtSlot(name="on_editFormButton_clicked")
    def openFeatureForm(self):
        if (self.layer.isEditable()):
            self.layer.commitChanges()
        else:
            self.layer.startEditing()

    @pyqtSlot(name="on_translateRightButton_clicked")
    def doTranslateRight(self):
        self.doTranslate((1, 0))

    @pyqtSlot(name="on_translateLeftButton_clicked")
    def doTranslateLeft(self):
        self.doTranslate((-1, 0))

    @pyqtSlot(name="on_translateUpButton_clicked")
    def doTranslateUp(self):
        self.doTranslate((0, 1))

    @pyqtSlot(name="on_translateDownButton_clicked")
    def doTranslateDown(self):
        self.doTranslate((0, -1))

    @pyqtSlot(name="on_applyChangesButton_clicked")
    def applyChanges(self):
        self.layer.commitChanges()
        self.layer.startEditing()
        self.layer.updateExtents()
        self.iface.mapCanvas().refresh()

    @pyqtSlot(int, name="on_fieldOneValueComboBox_activated")
    def on_fieldOneValueComboBox_activated(self, i):
        self.changeAttribute(i, self.fieldOneNameComboBox, self.fieldOneValueComboBox)

    @pyqtSlot(int, name="on_fieldTwoValueComboBox_activated")
    def on_fieldTwoValueComboBox_activated(self, i):
        self.changeAttribute(i, self.fieldTwoNameComboBox, self.fieldTwoValueComboBox)

    @pyqtSlot(int, name="on_fieldThreeValueComboBox_activated")
    def on_fieldThreeValueComboBox_activated(self, i):
        self.changeAttribute(i, self.fieldThreeNameComboBox, self.fieldThreeValueComboBox)
