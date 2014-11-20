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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "NTS Data Download"


def description():
    return "Download CanVec, NTDB, DEM, Topo data for Canada"


def version():
    return "Version 0.1"


def icon():
    return "NTSDownload_Icon.png"

def category():
  return "SJGeophysics"

def qgisMinimumVersion():
    return "1.8"

def qgisMaximumVersion():
	return '2.9'

def author():
    return "Casey Vandenberg / SJ Geophysics"

def email():
    return "casey.vandenberg@sjgeophysics.com"

def classFactory(iface):
    # load MapsheetDownload class from file MapsheetDownload
    from mapsheetdownload import MapsheetDownload
    return MapsheetDownload(iface)
