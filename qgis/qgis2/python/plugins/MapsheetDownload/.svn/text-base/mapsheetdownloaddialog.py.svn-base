# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MapsheetDownloadDialog
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
import sys,os,string,errno,csv,fnmatch,ftplib,zipfile,shutil,urllib2,threading,time
from ftplib import FTP

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

from ui_mapsheetdownload import Ui_MapsheetDownload
# create the dialog for zoom to point

FTPHOST = 'ftp2.cits.rncan.gc.ca'
THEME_DICT={'BS':'Buildings_Structures',
             'EN':'Energy',
             'FO':'Relief_Landforms',
             'HD':'Hydrography',
             'IC':'Industrial_Commercial',
             'LA':'Administrative_Limit',
             'LI':'MapSheet_Limit',
             'LX':'Places_of_Interest',
             'SS':'Water_Saturated_Soils',
             'TO':'Toponomy',
             'TR':'Transportation',
             'VE':'Vegetation',
            }  

class MapsheetException(Exception):
    pass

class MapsheetDownload(QtGui.QDialog, Ui_MapsheetDownload):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        #self.ui = Ui_MapsheetDownload()
        self.setupUi(self)
        QObject.connect( self.browserButton, SIGNAL( "clicked()" ), self.outputDirectory )
        
    def outputDirectory(self):
        """Open a browser dialog and set the output path"""
        outputDir = self.saveDialog(self)
        if not outputDir:
            return
        self.setOutputFolderPath((outputDir))

    def update_progress_bar(self):
        """Update the progress bar."""
        self.progressBar.setValue(self.progressBar.value() + 1)
        time.sleep(.02)
    
    def setOutputFolderPath(self, outputDir):
        """Set the output file path."""
        self.outputDir.setText(outputDir)
        
    def getFlags(self):
        downloadFlags = [self.downloadCanVec.isChecked(),self.downloadNTDB50k.isChecked(),self.downloadDEM50k.isChecked(),self.downloadTopo50k.isChecked(),self.downloadNTDB250k.isChecked(),self.downloadDEM250k.isChecked(),self.downloadTopo250k.isChecked()]
        return downloadFlags

    def countDownloadFiles(self):
        downloadFlags = self.getFlags()
        numFlags_50k = downloadFlags[0:4].count(True)
        numFlags_250k = downloadFlags[4:].count(True)
        numNTS_50k_Sheets=len(str(self.input50k.text()).split(','))
        numNTS_250k_Sheets=len(str(self.input250k.text()).split(','))
        progressBarRange = (numNTS_50k_Sheets*numFlags_50k) + (numNTS_250k_Sheets*numFlags_250k)
        return progressBarRange

    def accept(self):
        self.Status.clear()
        time.sleep(.02)
        input50k = str(self.input50k.text())
        input250k = str(self.input250k.text())
        outputDir = str(self.outputDir.text())
        progressBarRange = self.countDownloadFiles()
        self.progressBar.setProperty("value", 0)
        self.progressBar.setRange(0,progressBarRange)
        self.Status.setPlainText(str('Download Starting...'))
        time.sleep(.02)
        try:
            self.download(outputDir,input50k,input250k,self.getFlags())
        except MapsheetException as e:
            self.Status.appendPlainText(str(e))
        self.Status.appendPlainText('\nDownload Complete')            
        time.sleep(.02)

        if self.addMapLayers.isChecked():
            try:
                self.addToLayers(outputDir,input50k,input250k,self.getFlags())
            except MapsheetException as e:
                self.Status.appendPlainText(str(e))
        self.update_progress_bar()
        time.sleep(.02)

        
    def saveDialog(self,parent):
        """Opens a browser dialog and returns the selected directory"""
        settings = QSettings()
        key = '/SJ/lastSaveFileDir'
        outDir = settings.value(key)

        outputDir = QFileDialog.getExistingDirectory(parent, parent.tr('Specify output directory'), outDir)
        outputDir = unicode(outputDir)
        if outputDir:
            settings.setValue(key, outDir)
        return outputDir


    def dlCanVec(self,DestinationDirectory,NTS_50k_Sheet):
        """
        Creates CanVecData Sub Directory if it does not already exist.
        Retrieves the ftp file using the FTPHOST global variable and ftpPath
        Downloads the NTS 50k CanVec ftpFile from ftp://ftp2.cits.rncan.gc.ca/pub/canvec/50k_shp/
        Extracts the data to the NTS_50k_Sheet subdirectory 

        FTPHOST = 'ftp2.cits.rncan.gc.ca'
        ftpPath = 'pub/canvec/50k_shp/'
        """
        ftpPath = 'pub/canvec/50k_shp/'
        series50k,mapArea50k,sheet50k = parse50kSheets(NTS_50k_Sheet)

        cwd=os.getcwd()

        d = os.path.join(DestinationDirectory,'CanVecData',NTS_50k_Sheet)
        downloadDir=str(os.path.join(DestinationDirectory,'CanVecData'))
        outfile=os.path.join(downloadDir,'canvec_'+str.lower(NTS_50k_Sheet)+'_shp.zip')

        if not os.path.exists(d):
            os.makedirs(d)
        if os.path.exists(outfile):
            self.Status.appendPlainText('CanVec Mapsheet '+str(NTS_50k_Sheet)+str(' already retrieved from FTP site'))
        else:
            os.chdir(downloadDir)
            ftpFile = 'retr '+ftpPath+series50k+'/'+str.lower(mapArea50k)+'/canvec_'+str.lower(NTS_50k_Sheet)+'_shp.zip'
            self.Status.appendPlainText(str(ftpFile))
            ftp = FTP(FTPHOST)
            ftp.login()
            ftp.retrbinary(ftpFile,open(outfile, 'wb').write)
        os.chdir(cwd)
        zipFileName = os.path.join(downloadDir,'canvec_'+str.lower(NTS_50k_Sheet)+'_shp.zip')

        if os.path.exists(zipFileName):
            zipF = zipfile.ZipFile(zipFileName)
            zipF.extractall(d)

    def dlNTDB50k(self,DestinationDirectory,NTS_50k_Sheet):
        """
        Creates NTDB Sub Directory if it does not already exist.
        Retrieves the ftp file using the FTPHOST global variable and ftpPath
        Downloads the NTS 50k CanVec ftpFile from ftp://ftp2.cits.rncan.gc.ca/pub/bndt/50k_shp_en/
        Extracts the data to the NTS_50k_Sheet subdirectory 

        FTPHOST = 'ftp2.cits.rncan.gc.ca'
        ftpPath = 'pub/canvec/50k_shp/'
        """
        ftpPath = 'pub/bndt/50k_shp_en/'
        series50k,mapArea50k,sheet50k = parse50kSheets(NTS_50k_Sheet)

        cwd=os.getcwd()

        d = os.path.join(DestinationDirectory,'NTDBData',NTS_50k_Sheet)
        downloadDir=str(os.path.join(DestinationDirectory,'NTDBData'))
        outfile=os.path.join(downloadDir,'bndt_'+str.lower(NTS_50k_Sheet)+'_shp_en.zip')

        if not os.path.exists(d):
            os.makedirs(d)
        if os.path.exists(outfile):
            self.Status.appendPlainText('NTDB Mapsheet '+str(NTS_50k_Sheet)+str(' already retrieved from FTP site'))
        else:
            os.chdir(downloadDir)
            ftpFile = 'retr '+ftpPath+series50k+'/'+str.lower(mapArea50k)+'/bndt_'+str.lower(NTS_50k_Sheet)+'_shp_en.zip'
            self.Status.appendPlainText(str(ftpFile))
            ftp = FTP(FTPHOST)
            ftp.login()
            ftp.retrbinary(ftpFile,open(outfile, 'wb').write)
        os.chdir(cwd)
        zipFileName = os.path.join(downloadDir,'bndt_'+str.lower(NTS_50k_Sheet)+'_shp_en.zip')

        if os.path.exists(zipFileName):
            zipF = zipfile.ZipFile(zipFileName)
            zipF.extractall(d)    

    def dlNTDB250k(self,DestinationDirectory,NTS_250k_Sheet):
        """
        Creates NTDB Sub Directory if it does not already exist.
        Retrieves the ftp file using the FTPHOST global variable and ftpPath
        Downloads the NTS 50k CanVec ftpFile from ftp://ftp2.cits.rncan.gc.ca/pub/bndt/50k_shp_en/
        Extracts the data to the NTS_50k_Sheet subdirectory 

        FTPHOST = 'ftp2.cits.rncan.gc.ca'
        ftpPath = 'pub/canvec/50k_shp/'
        """
        ftpPath = 'pub/bndt/250k_shp_en/'
        series250k,mapArea250k = parse250kSheets(NTS_250k_Sheet)

        cwd=os.getcwd()

        d = os.path.join(DestinationDirectory,'NTDBData',NTS_250k_Sheet)
        downloadDir=str(os.path.join(DestinationDirectory,'NTDBData'))
        outfile=os.path.join(downloadDir,'bndt_'+str.lower(NTS_250k_Sheet)+'_shp_en.zip')

        if not os.path.exists(d):
            os.makedirs(d)
        if os.path.exists(outfile):
            self.Status.appendPlainText('NTDB Mapsheet '+str(NTS_250k_Sheet)+' already retrieved from FTP site')
        else:
            os.chdir(downloadDir)
            ftpFile = 'retr '+ftpPath+series250k+'/'+str.lower(mapArea250k)+'/bndt_'+str.lower(NTS_250k_Sheet)+'_shp_en.zip'
            self.Status.appendPlainText(str(ftpFile))
            ftp = FTP(FTPHOST)
            ftp.login()
            ftp.retrbinary(ftpFile,open(outfile, 'wb').write)
        os.chdir(cwd)
        zipFileName = os.path.join(downloadDir,'bndt_'+str.lower(NTS_250k_Sheet)+'_shp_en.zip')

        if os.path.exists(zipFileName):
            zipF = zipfile.ZipFile(zipFileName)
            zipF.extractall(d)

    def dlDEM50k(self,DestinationDirectory,NTS_50k_Sheet):
        """
        Creates DEM Sub Directory if it does not already exist.
        Retrieves the ftp file using the FTPHOST global variable and ftpPath
        Downloads the NTS 50k CanVec ftpFile from ftp://ftp2.cits.rncan.gc.ca/pub/geobase/official/cded/50k_dem/
        Extracts the data to the NTS_50k_Sheet subdirectory 

        FTPHOST = 'ftp2.cits.rncan.gc.ca'
        ftpPath = 'pub/geobase/official/cded/50k_dem/'
        """
        ftpPath = 'pub/geobase/official/cded/50k_dem/'
        series50k,mapArea50k,sheet50k = parse50kSheets(NTS_50k_Sheet)

        cwd=os.getcwd()

        d = os.path.join(DestinationDirectory,'DEM',NTS_50k_Sheet)
        downloadDir=str(os.path.join(DestinationDirectory,'DEM'))
        outfile=os.path.join(downloadDir,str.lower(NTS_50k_Sheet)+'.zip')

        if not os.path.exists(d):
            os.makedirs(d)
        if os.path.exists(outfile):
            self.Status.appendPlainText('DEM Mapsheet '+str(NTS_50k_Sheet)+' already retrieved from FTP site')
        else:
            os.chdir(downloadDir)
            ftpFile = 'retr '+ftpPath+series50k+'/'+str.lower(NTS_50k_Sheet)+'.zip'
            self.Status.appendPlainText(str(ftpFile))
            ftp = FTP(FTPHOST)
            ftp.login()
            ftp.retrbinary(ftpFile,open(outfile, 'wb').write)
        os.chdir(cwd)
        zipFileName = os.path.join(downloadDir,str.lower(NTS_50k_Sheet)+'.zip')

        if os.path.exists(zipFileName):
            zipF = zipfile.ZipFile(zipFileName)
            zipF.extractall(d)  

    def dlDEM250k(self,DestinationDirectory,NTS_250k_Sheet):
        """
        Creates DEM Sub Directory if it does not already exist.
        Retrieves the ftp file using the FTPHOST global variable and ftpPath
        Downloads the NTS 50k CanVec ftpFile from ftp://ftp2.cits.rncan.gc.ca/pub/geobase/official/cded/50k_dem/
        Extracts the data to the NTS_50k_Sheet subdirectory 

        FTPHOST = 'ftp2.cits.rncan.gc.ca'
        ftpPath = 'pub/geobase/official/cded/250k_dem/'
        """
        ftpPath = 'pub/geobase/official/cded/250k_dem/'
        series250k,mapArea250k = parse250kSheets(NTS_250k_Sheet)

        cwd=os.getcwd()

        d = os.path.join(DestinationDirectory,'DEM',NTS_250k_Sheet)
        downloadDir=str(os.path.join(DestinationDirectory,'DEM'))
        outfile=os.path.join(downloadDir,str.lower(NTS_250k_Sheet)+'.zip')

        if not os.path.exists(d):
            os.makedirs(d)
        if os.path.exists(outfile):
            self.Status.appendPlainText('\nDEM Mapsheet '+str(NTS_250k_Sheet)+' already retrieved from FTP site')
        else:
            os.chdir(downloadDir)
            ftpFile = 'retr '+ftpPath+series250k+'/'+str.lower(NTS_250k_Sheet)+'.zip'
            self.Status.appendPlainText(str(ftpFile))
            ftp = FTP(FTPHOST)
            ftp.login()
            ftp.retrbinary(ftpFile,open(outfile, 'wb').write)
        os.chdir(cwd)
        zipFileName = os.path.join(downloadDir,str.lower(NTS_250k_Sheet)+'.zip')

        if os.path.exists(zipFileName):
            zipF = zipfile.ZipFile(zipFileName)
            zipF.extractall(d)      

    def dlTopo50k(self,DestinationDirectory,NTS_50k_Sheet):
        """
        Creates Topo Sub Directory if it does not already exist.
        Retrieves the ftp file using the FTPHOST global variable and ftpPath
        Downloads the Toporama ftpFile from ftp://ftp2.cits.rncan.gc.ca/pub/toporama/50k_utm_tif/
        Extracts the data to the NTS_50k_Sheet subdirectory 

        FTPHOST = 'ftp2.cits.rncan.gc.ca'
        ftpPath = 'pub/toporama/50k_utm_tif/'
        """
        ftpPath = 'pub/toporama/50k_utm_tif/'
        series50k,mapArea50k,sheet50k = parse50kSheets(NTS_50k_Sheet)

        cwd=os.getcwd()

        d = os.path.join(DestinationDirectory,'Topo',NTS_50k_Sheet)
        downloadDir=str(os.path.join(DestinationDirectory,'Topo'))
        outfile=os.path.join(downloadDir,'toporama_'+str.lower(NTS_50k_Sheet)+'_utm.zip')

        if not os.path.exists(d):
            os.makedirs(d)
        if os.path.exists(outfile):
            self.Status.appendPlainText('Toporama Mapsheet '+str(NTS_50k_Sheet)+' already retrieved from FTP site')
        else:
            os.chdir(downloadDir)
            ftpFile = 'retr '+ftpPath+series50k+'/'+str.lower(mapArea50k)+'/toporama_'+str.lower(NTS_50k_Sheet)+'_utm.zip'
            self.Status.appendPlainText(str(ftpFile))
            ftp = FTP(FTPHOST)
            ftp.login()
            ftp.retrbinary(ftpFile,open(outfile, 'wb').write)
        os.chdir(cwd)
        zipFileName = os.path.join(downloadDir,'toporama_'+str.lower(NTS_50k_Sheet)+'_utm.zip')

        if os.path.exists(zipFileName):
            zipF = zipfile.ZipFile(zipFileName)
            zipF.extractall(d) 


    def dlTopo250k(self,DestinationDirectory,NTS_250k_Sheet):
        """
        Creates Topo Sub Directory if it does not already exist.
        Retrieves the ftp file using the FTPHOST global variable and ftpPath
        Downloads the Toporama ftpFile from ftp://ftp2.cits.rncan.gc.ca/pub/canmatrix/250k_300dpi/
        Extracts the data to the NTS_250k_Sheet subdirectory 

        FTPHOST = 'ftp2.cits.rncan.gc.ca'
        ftpPath = 'pub/canmatrix/250k_300dpi/'
        """
        ftpPath = 'pub/canmatrix/250k_300dpi/'
        series250k,mapArea250k = parse250kSheets(NTS_250k_Sheet)

        cwd=os.getcwd()

        d = os.path.join(DestinationDirectory,'Topo',NTS_250k_Sheet)
        downloadDir=str(os.path.join(DestinationDirectory,'Topo'))
        outfile=os.path.join(downloadDir,'canmatrix_'+str.lower(NTS_250k_Sheet)+'_tif.zip')

        if not os.path.exists(d):
            os.makedirs(d)
        if os.path.exists(outfile):
            self.Status.appendPlainText('\nCanMatrix Mapsheet '+str(NTS_250k_Sheet)+' already retrieved from FTP site')
        else:
            os.chdir(downloadDir)
            ftpFile = 'retr '+ftpPath+series250k+'/'+str.lower(mapArea250k)+'/canmatrix_'+str.lower(NTS_250k_Sheet)+'_tif.zip'
            self.Status.appendPlainText(str(ftpFile))
            ftp = FTP(FTPHOST)
            ftp.login()
            ftp.retrbinary(ftpFile,open(outfile, 'wb').write)
        os.chdir(cwd)
        zipFileName = os.path.join(downloadDir,'canmatrix_'+str.lower(NTS_250k_Sheet)+'_tif.zip')

        if os.path.exists(zipFileName):
            zipF = zipfile.ZipFile(zipFileName)
            zipF.extractall(d) 
            
    def download(self,DestinationDirectory,NTS_50k_Sheets,NTS_250k_Sheets,downloadFlags):
        """
        This function is called when the download button is fired
        It splits the input string from the GUI into multiple mapsheets, then for each mapsheet
        it tests to see if the mapsheet name is valid.
        If valid, the appropriate download functions are called according to whether the datasets are requested or not
        """
        NTS_50k_Sheets=NTS_50k_Sheets.split(',')
        NTS_250k_Sheets=NTS_250k_Sheets.split(',')
        self.Status.appendPlainText(str('Checking 50k sheets...\n'))
        time.sleep(0.02)
        for NTS_50k_Sheet in NTS_50k_Sheets:
            NTS_50k_Sheet=str(NTS_50k_Sheet.strip()).lower()
            if not isvalid50k(NTS_50k_Sheet)[0] and isvalid50k(NTS_50k_Sheet)[1]:
                raise MapsheetException(str('50k NTS Mapsheet: '+"'"+NTS_50k_Sheet+"'"+' is invalid. Please check the name'))
                time.sleep(0.02)
                continue
            if not isvalid50k(NTS_50k_Sheet)[0] and not isvalid50k(NTS_50k_Sheet)[1]:
                self.Status.appendPlainText('No 50k NTS Mapsheets were specified')
                time.sleep(0.02)
                continue
            time.sleep(0.02)
            if downloadFlags[0]:
                self.Status.appendPlainText(str('Downloading 1:50k CanVec Data'))
                time.sleep(0.02)
                self.dlCanVec(DestinationDirectory,NTS_50k_Sheet)
                organizeByTheme(NTS_50k_Sheet,DestinationDirectory)
                self.update_progress_bar()
            if downloadFlags[1]:
                self.Status.appendPlainText(str('Downloading 1:50k NTDB Data'))
                time.sleep(0.02)
                self.dlNTDB50k(DestinationDirectory,NTS_50k_Sheet)            
                self.update_progress_bar()
            if downloadFlags[2]:
                self.Status.appendPlainText(str('Downloading 1:50k DEM Data'))
                time.sleep(0.02)
                self.dlDEM50k(DestinationDirectory,NTS_50k_Sheet)            
                self.update_progress_bar()
            if downloadFlags[3]:
                self.Status.appendPlainText(str('Downloading 1:50k Topo Data'))
                time.sleep(0.02)
                self.dlTopo50k(DestinationDirectory,NTS_50k_Sheet)            
                self.update_progress_bar()

        self.Status.appendPlainText(str('Checking 250k sheets...\n'))
        time.sleep(0.02)
        for NTS_250k_Sheet in NTS_250k_Sheets:
            NTS_250k_Sheet=str(NTS_250k_Sheet.strip()).lower()
            if not isvalid250k(NTS_250k_Sheet)[0] and isvalid250k(NTS_250k_Sheet)[1]:
                raise MapsheetException(str('250k NTS Mapsheet: '+"'"+NTS_250k_Sheet+"'"+' is invalid. Please check the name(s)'))
                continue
            if not isvalid250k(NTS_250k_Sheet)[0] and not isvalid250k(NTS_250k_Sheet)[1]:
                self.Status.appendPlainText('No 250k NTS Mapsheets were specified')
                continue
            if downloadFlags[4]:
                self.Status.appendPlainText(str('Downloading 1:250k NTDB Data'))
                time.sleep(0.02)
                self.dlNTDB250k(DestinationDirectory,NTS_250k_Sheet)
                self.update_progress_bar()
            if downloadFlags[5]:
                self.Status.appendPlainText(str('Downloading 1:250k DEM Data'))
                time.sleep(0.02)
                self.dlDEM250k(DestinationDirectory,NTS_250k_Sheet)
                self.update_progress_bar()
            if downloadFlags[6]:
                self.Status.appendPlainText(str('Downloading 1:250k Topo Data'))
                time.sleep(0.02)
                self.dlTopo250k(DestinationDirectory,NTS_250k_Sheet)
                self.update_progress_bar()

        if True in downloadFlags:
            print "\nDownload Complete\n"
        else:
            print  "\nNo Data Downloaded\n"

    def addToLayers(self,DestinationDirectory,NTS_50k_Sheets,NTS_250k_Sheets,downloadFlags):
        """
        This function is called after the download function completes after the ok button is fired.
        It walks into the directories for each download type specified by the download flags and for each NTS sheet specified.
        It then calls the addShapesToCanvas function with adds any file ending with .shp as a layers in the layer tree.
        """
        NTS_50k_Sheets=NTS_50k_Sheets.split(',')
        NTS_250k_Sheets=NTS_250k_Sheets.split(',')
        for NTS_50k_Sheet in NTS_50k_Sheets:
            NTS_50k_Sheet=str(NTS_50k_Sheet.strip()).lower()
            if not isvalid50k(NTS_50k_Sheet)[0] and isvalid50k(NTS_50k_Sheet)[1]:
                raise MapsheetException(str('50k NTS Mapsheet: '+"'"+NTS_50k_Sheet+"'"+' is invalid. Please check the name'))
                continue
            if not isvalid50k(NTS_50k_Sheet)[0] and not isvalid50k(NTS_50k_Sheet)[1]:
                continue
            if downloadFlags[2]:
                d = os.path.join(DestinationDirectory,'DEM',NTS_50k_Sheet)
                os.chdir(d)
                for dirname, dirnames, filenames in os.walk(d):
                    for filename in filenames:
                        DEMFilePath = os.path.join(dirname, filename)
                        addDEMToCanvas(DEMFilePath)
            if downloadFlags[3]:
                d = os.path.join(DestinationDirectory,'Topo',NTS_50k_Sheet)
                os.chdir(d)
                for dirname, dirnames, filenames in os.walk(d):
                    for filename in filenames:
                        TopoFilePath = os.path.join(dirname, filename)
                        addTopoToCanvas(TopoFilePath)
            if downloadFlags[0]:
                d = os.path.join(DestinationDirectory,'CanVecData',NTS_50k_Sheet)
                os.chdir(d)
                for dirname, dirnames, filenames in os.walk(d):
                    for filename in filenames:
                        shapeFilePath = os.path.join(dirname, filename)
                        addShapesToCanvas(shapeFilePath)    
            if downloadFlags[1]:
                d = os.path.join(DestinationDirectory,'NTDBData',NTS_50k_Sheet)
                os.chdir(d)
                for dirname, dirnames, filenames in os.walk(d):
                    for filename in filenames:
                        shapeFilePath = os.path.join(dirname, filename)
                        addShapesToCanvas(shapeFilePath)

        for NTS_250k_Sheet in NTS_250k_Sheets:
            NTS_250k_Sheet=str(NTS_250k_Sheet.strip()).lower()
            if not isvalid250k(NTS_250k_Sheet)[0] and isvalid250k(NTS_250k_Sheet)[1]:
                raise MapsheetException(str('250k NTS Mapsheet: '+"'"+NTS_250k_Sheet+"'"+' is invalid. Please check the name(s)'))
                continue
            if not isvalid250k(NTS_250k_Sheet)[0] and not isvalid250k(NTS_250k_Sheet)[1]:
                continue
            if downloadFlags[5]:
                d = os.path.join(DestinationDirectory,'DEM',NTS_250k_Sheet)
                os.chdir(d)
                for dirname, dirnames, filenames in os.walk(d):
                    for filename in filenames:
                        DEMFilePath = os.path.join(dirname, filename)
                        addDEMToCanvas(DEMFilePath)
            if downloadFlags[6]:
                d = os.path.join(DestinationDirectory,'Topo',NTS_250k_Sheet)
                os.chdir(d)
                for dirname, dirnames, filenames in os.walk(d):
                    for filename in filenames:
                        TopoFilePath = os.path.join(dirname, filename)
                        addTopoToCanvas(TopoFilePath)
            if downloadFlags[4]:
                d = os.path.join(DestinationDirectory,'NTDBData',NTS_250k_Sheet)
                os.chdir(d)
                for dirname, dirnames, filenames in os.walk(d):
                    for filename in filenames:
                        shapeFilePath = os.path.join(dirname, filename)
                        addShapesToCanvas(shapeFilePath)

def createThemeLists(NTS_50k_Sheet,DestinationDirectory):
    """
    Iterates over all .shp in the NTS_50k_Sheet download directory and
    creates a set of themes that are present which belong to the theme dictionary

    The theme dictionary includes:
    _______________________________
    BS - Buildings and Structures
    EN - Energy
    FO - Relief and Landforms
    HD - Hydrography
    IC - Industrial and Commercial
    LA - Adminstrative Limit
    LI - Map Coverage Limit
    LX - Places of Interest
    SS - Water Saturated Soils
    TO - Toponomy
    TR - Transportation
    VE - Vegetation

    The themes can later be organized by feature type if desired (not yet implemented)
    Feature Types:
    0 - Point
    1 - Line
    2 - Area
    _______________________________

    Themes are defined here: ftp://ftp2.cits.rncan.gc.ca/pub/canvec/doc/CanVec_feature_catalogue_en.pdf
    """
    lowerCase50kMapSheet = str.lower(NTS_50k_Sheet)
    d = os.path.join(DestinationDirectory,'CanVecData',NTS_50k_Sheet)
    shpList = getShpList(d)[0]
    shpHeadList = getShpList(d)[1]
    themes = set()
    for shpFile in shpHeadList:
        Theme = shpFile.split('_')[3]
        if Theme not in THEME_DICT:
            print '\nVector layer:',shpFile,'does not belong to a theme\n'
        else:
            themes.add(Theme)
    return themes

def organizeByTheme(NTS_50k_Sheet,DestinationDirectory):
    """
    For each theme present that exists in the theme dictionary, a sub-directory
    representing that themes value will be created if it does not already exist.
    Each file that is part of that theme is then moved into the appropriate sub-directory
    
    Currently this function is done automatically. A flag to organize by theme may be created in the future.
    """
    themes = createThemeLists(NTS_50k_Sheet,DestinationDirectory)
    downloadDir=str(os.path.join(DestinationDirectory,'CanVecData',NTS_50k_Sheet))
    for Theme in themes:
        d=os.path.join(DestinationDirectory,'CanVecData',NTS_50k_Sheet,THEME_DICT[Theme])
        if not os.path.exists(d):
            os.makedirs(d)        
    for fileName in os.listdir(downloadDir):
        fileHead = os.path.splitext(fileName)[0]
        if fileName.endswith('.html') or fileName.endswith('.xml') or fileName.find('.')<0:
            continue
        try:
            Theme = fileHead.split('_')[3]
            if Theme not in THEME_DICT:
                continue
            dst=(os.path.join(downloadDir,THEME_DICT[Theme],fileName))
            if os.path.exists(dst):
                os.unlink(dst)
            shutil.move(os.path.join(downloadDir,fileName),dst)
        except KeyError, IndexError:
            print "Exception", dst,fileHead,Theme
            
def addShapesToCanvas(shapeFilePath):
    layerName = os.path.basename(shapeFilePath)
    root, ext = os.path.splitext(layerName)
    if ext == '.shp':
        layerName = root
        vlayer_new = QgsVectorLayer(shapeFilePath, layerName, "ogr")
        try:
            QgsMapLayerRegistry.instance().addMapLayer(vlayer_new)
        except AttributeError:
            QgsMapLayerRegistry.instance().addMapLayers([vlayer_new])
    return True

def addDEMToCanvas(DEMFilePath):
    layerName = os.path.basename(DEMFilePath)
    root, ext = os.path.splitext(layerName)
    if ext == '.dem':
        layerName = root
        rlayer_new = QgsRasterLayer(DEMFilePath, layerName)
        try:
            QgsMapLayerRegistry.instance().addMapLayer(rlayer_new)
        except AttributeError:
            QgsMapLayerRegistry.instance().addMapLayers([rlayer_new])
    return True

def addTopoToCanvas(TopoFilePath):
    layerName = os.path.basename(TopoFilePath)
    root, ext = os.path.splitext(layerName)
    if ext == '.tif':
        layerName = root
        rlayer_new = QgsRasterLayer(TopoFilePath, layerName)
        try:
            QgsMapLayerRegistry.instance().addMapLayer(rlayer_new)
        except AttributeError:
            QgsMapLayerRegistry.instance().addMapLayers([rlayer_new])
    return True
       
def isvalid50k(string):
    returnValue = True
    inputValue = False
    if len(string)>0:
        inputValue = True
    returnValue = True
    if len(string)!=6:
        returnValue = False
    if returnValue and not string[0:3].isdigit():
        returnValue = False    
    if returnValue and not string[3:4].isalpha():        
        returnValue = False        
    if returnValue and not string[4:6].isdigit():
        returnValue = False
    return returnValue,inputValue
    
def isvalid250k(string):
    inputValue = False
    if len(string)>0:
        inputValue = True
    returnValue = True
    if len(string)!=4:
        returnValue = False
    if returnValue and not string[0:3].isdigit():
        returnValue = False    
    if returnValue and not string[3:4].isalpha():        
        returnValue = False        
    return returnValue,inputValue
    

def parse50kSheets(NTS_50k_Sheet):
        """
        Parses the NTS 50k mapsheet name, returns map series, map area, and map sheet

        Example: 092h12
        
        Series: 092
        Area:   h
        Sheet:  12
        """
        series50k = NTS_50k_Sheet[0:3]
        mapArea50k = NTS_50k_Sheet[3:4]
        sheet50k = NTS_50k_Sheet[4:6]
        
        return series50k,mapArea50k,sheet50k

def parse250kSheets(NTS_250k_Sheet):
        """
        Parses the NTS 250k mapsheet name, returns map series and map area

        Example: 092h12
        
        Series: 092
        Area:   h
        """
        series250k = NTS_250k_Sheet[0:3]
        mapArea250k = NTS_250k_Sheet[3:4]
        return series250k,mapArea250k
        
def getShpList(Dir):
    """
    Returns a list of shapefiles in the cwd
    """
    shpHeadList = []    
    shpList = []
    for fileName in os.listdir(Dir):
        fileHead = os.path.splitext(fileName)[0]
        fileTail = os.path.splitext(fileName)[1]
        if fileName.endswith('.shp'):
            shpHeadList.append(str(fileHead))
            shpList.append(str(fileName))
    return shpList,shpHeadList
