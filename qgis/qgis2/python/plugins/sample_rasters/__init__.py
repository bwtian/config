# -*- coding: utf-8 -*-
"""
/***************************************************************************
 sample_rasters
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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "Sample Rasters"


def description():
    return "Sample rasters from raster class"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "2.0"

def author():
    return "Luis Fernando Chimelo Ruiz"

def email():
    return "ruiz.ch@gmail.com"

def classFactory(iface):
    # load sample_rasters class from file sample_rasters
    from sample_rasters import sample_rasters
    return sample_rasters(iface)
