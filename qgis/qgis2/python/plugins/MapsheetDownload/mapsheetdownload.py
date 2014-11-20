# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MapsheetDownload
                                 A QGIS plugin
 Download CanVec, NTDB, DEM, Topo data for Canada
                              -------------------
        begin                : 2013-01-31
        copyright            : (C) 2013 by Casey Vandenberg / SJ Geophysics
        email                : casey.vandenberg@sjgeophysics.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import sys

# Import the PyQt and QGIS libraries
from PyQt4.Qt import QApplication
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
import mapsheetdownloaddialog

class MapsheetDownload:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/mapsheetdownload"
        # initialize locale
        localePath = ""
        #locale = QSettings().value("locale/userLocale").toString()[0:2]
        locale = QSettings().value("locale/userLocale")

        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/mapsheetdownload_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        #self.dlg = MapsheetDownload()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/mapsheetdownload/NTSDownload_Icon.png"), "NTS Data Download", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&NTS Data Download", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&NTS Data Download", self.action)
        self.iface.removeToolBarIcon(self.action)

    '''
    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            pass
    '''
    def run(self):
        dialog = mapsheetdownloaddialog.MapsheetDownload()
        dialog.NTS_50k_Sheet='092h09'
        dialog.exec_()  
        
if __name__ == "__main__":
    QApp = QCoreApplication.instance() 
    MapsheetDownload(QApp)

