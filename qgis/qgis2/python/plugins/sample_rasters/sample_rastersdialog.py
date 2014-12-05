# -*- coding: utf-8 -*-
"""
/***************************************************************************
 sample_rastersDialog
                                 A QGIS plugin
 Sample rasters from raster class
                             -------------------
        begin                : 2014-02-06
        copyright            : (C) 2014 by Luis Fernando Chimelo Ruiz
        email                : ruiz.ch@gmail.com
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

from PyQt4 import QtCore, QtGui
from sample_rasters_gui import Ui_Form
# create the dialog for zoom to point


class sample_rastersDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_Form()
        self.ui.setupUi(self)
