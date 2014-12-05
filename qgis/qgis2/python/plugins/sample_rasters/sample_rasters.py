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
"""
#import library cvs
import csv
#Importar library GDAL
from osgeo import gdal
#import library numpy
import numpy as np
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import time
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from sample_rastersdialog import sample_rastersDialog
import os.path


class sample_rasters:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'sample_rasters_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = sample_rastersDialog()
        #INSERT EVERY SIGNAL CONECTION HERE!
        QObject.connect(self.dlg.ui.comboBoxRasterClass, SIGNAL("currentIndexChanged(int)"), self.funcComboBox)    
        QObject.connect(self.dlg.ui.pushButtonSaveCsv, SIGNAL("clicked()"), self.saveCSV)
        QObject.connect(self.dlg.ui.pushButtonOk,SIGNAL("clicked()"),self.processSampleRasters)
        QObject.connect(self.dlg.ui.pushButtonExit,SIGNAL("clicked()"),self.exitProgram)

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/sample_rasters/icon.png"),
            u"Sample rasters", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Sample Rasters", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Sample Rasters", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        gdal.AllRegister
        #Limpar lineEdit Sava CSV
        self.dlg.ui.lineEditSaveCsv.clear()
        #Iniciar varival keysNomes
        self.keysNomes = []
        #Zera as variaveis 
        self.valueProgress = 0
        self.dlg.ui.progressBar.setValue(self.valueProgress)
        #Inserir decima
        self.dlg.ui.lineEditDecimal.setText("4")
        
#        #INSERT EVERY SIGNAL CONECTION HERE!
#        QObject.connect(self.dlg.ui.comboBoxRasterClass, SIGNAL("currentIndexChanged(int)"), self.funcComboBox)    
#        QObject.connect(self.dlg.ui.pushButtonSaveCsv, SIGNAL("clicked()"), self.saveCSV)
#        QObject.connect(self.dlg.ui.pushButtonOk,SIGNAL("clicked()"),self.processSampleRasters)
#        QObject.connect(self.dlg.ui.pushButtonExit,SIGNAL("clicked()"),self.exitProgram)
        #Obter a lista de layers que estÃ¡ aberta no QGIS
        self.allLayerMap = QgsMapLayerRegistry.instance().mapLayers() 
        #Obtem uma lista de todos items que estão no mapa
        self.itensMaps=self.allLayerMap.items()
        #Obtem os nomes dos layers do mapa, a partir das chaves do dicionário
        self.keysNomes = self.allLayerMap.keys()
        #Limpar widget ao iniciar
        self.dlg.ui.comboBoxRasterClass.clear()
        self.dlg.ui.listWidget.clear()
        #Obter apenas os rasters
        #Obtem os layers que estao na lista dos mapas, adiciona o nome e assim busca a gemetria (dicionario)
        self.keysNomesRasters =[]
        for i  in xrange(len(self.allLayerMap.keys())):
            self.layerRasterClass = self.allLayerMap[self.keysNomes[i]] 
            if self.layerRasterClass.type() == QgsMapLayer.RasterLayer:
                self.keysNomesRasters.append(self.keysNomes[i]) 
        if len(self.keysNomesRasters) == 0:
            return QMessageBox.information(self.iface.mainWindow(), "Info", "There are no rasters in QGIS", QMessageBox.Close)
        #Inserir os nomes dos layers no combobox
        self.dlg.ui.comboBoxRasterClass.addItems(self.keysNomesRasters)
        #obter o indice selecionado no comboboxRasterClass
        self.indexComboRasterClass = self.dlg.ui.comboBoxRasterClass.currentIndex()
        #Obter valor Nodata do raster selecionado no combobox
        self.getInfoRasterClasses(self.keysNomesRasters[0])
        self.dlg.ui.lineEditNoData.setText(self.noDataRasterClasses ) 
        #Remover do self.keysNomesRasters o raster que esta no combobox
        self.popkeysNomesRasters = self.keysNomesRasters.pop(0)
        #limpar
        self.dlg.ui.listWidget.clear()
        #Adiciona os layers raster no listView                                    
        self.dlg.ui.listWidget.addItems(self.keysNomesRasters)
        #Adicionar do self.keysNomesRasters o raster que esta no combobox
        self.keysNomesRasters.insert(0,self.popkeysNomesRasters)
        #Inserir None
        self.dlg.ui.lineEditDisconsiderar.setText("None")
        self.dlg.ui.lineEditDisconsiderar.setToolTip('separate values with ";"')   
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            pass
    def getValoreListWidget(self):
        items = self.dlg.ui.listWidget.selectedItems()
        self.namesRastersListWidget = [i.text() for i in items]
        self.namesRastersListWidgetAux =[]
        self.numberBandsRasters = [self.allLayerMap[i].bandCount() for i in self.namesRastersListWidget]
        for cont,v in enumerate (self.namesRastersListWidget):
            if self.numberBandsRasters[cont] > 1:
                [self.namesRastersListWidgetAux.append('band_{i}_'.format(i=i)+str(v)) for i in xrange (1,int(self.numberBandsRasters[cont])+1)]
            else:
                self.namesRastersListWidgetAux.append(v)
       
    def funcComboBox (self):
        '''Em cada mudanca no combobox obtem o valor noData'''
        #obter o indice selecionado no comboboxRasterClass
        self.indexComboRasterClass = self.dlg.ui.comboBoxRasterClass.currentIndex()
        #Obter valor Nodata do raster selecionado no combobox
        self.getInfoRasterClasses(self.keysNomesRasters[self.indexComboRasterClass])
        #inserir no text no Widget lineEditNodata
        self.dlg.ui.lineEditNoData.setText(self.noDataRasterClasses) 
        #Remover do self.keysNomesRasters o raster que esta no combobox
        self.popkeysNomesRasters = self.keysNomesRasters.pop(self.indexComboRasterClass)
        #limpar
        self.dlg.ui.listWidget.clear()
        #Adiciona os layers raster no listView                                    
        self.dlg.ui.listWidget.addItems(self.keysNomesRasters)
        #Adicionar do self.keysNomesRasters o raster que esta no combobox
        self.keysNomesRasters.insert(self.indexComboRasterClass,self.popkeysNomesRasters)

        
    def getInfoRasterClasses(self, nomeRasterClasses):
        '''Obter valor metadados do raster selecionado no combobox'''  
        self.nomeRasterClasses = nomeRasterClasses
        rasterClasses = self.allLayerMap[self.nomeRasterClasses]
        rasterExtent = rasterClasses.extent()
        self.cols = int(rasterClasses.width())
        self.lins = int(rasterClasses.height())
        
        self.sizePixel = rasterClasses.rasterUnitsPerPixelY()
        #Coordenadas de origem
        self.originX = rasterExtent.xMinimum()
        self.originY = rasterExtent.yMaximum()        
        #Atribui as propriedades e funcoes para o vetor a partir do provedor
        self.rasterClassesProvider = rasterClasses.dataProvider()
        #Atribui o caminho e o nome do arquivo para a variável dirFile
        dirFile = self.rasterClassesProvider.dataSourceUri()
        #Separa o arquivo de seu ID (ID corresponde a ordem no QGIS)
        dirFile = dirFile.split('|')
        #Atribui o caminho do arquivo para a variável file_decl    
        file_select = dirFile[0]   
        #Abrir o raster através da bibliotecas GDAL
        rasterSelect = gdal.Open(file_select, gdal.GA_ReadOnly)
        #Ler a banda 1 do raster
        self.bandaRasterSelect = rasterSelect.GetRasterBand(1)        
        #Ler a o raster como array do numpy
        self.arrayRaster = self.bandaRasterSelect.ReadAsArray()       
        #Obter o valor nodata do raster
        self.noDataRasterClasses = str(self.bandaRasterSelect.GetNoDataValue())
        self.noDataRasterClassesNumber = eval(self.noDataRasterClasses)
        
    def processSampleRasters(self):
        if self.dlg.ui.lineEditSaveCsv.text() == "":
            return QMessageBox.information(self.iface.mainWindow(), "Info", "Insert file path CSV", QMessageBox.Close)
            
        
        try:                    
          #Obter valor de casas decimais
          valorCasasDecimais = self.dlg.ui.lineEditDecimal.text()
          valorCasasDecimais = int(valorCasasDecimais)
        except:
            return QMessageBox.information(self.iface.mainWindow(), "Info", "Error: convert decimal value to integer", QMessageBox.Close)
        #Zerar a barra de progreso
        self.valueProgress = 0
        try:
            #Criar o arquivo de escrita csv
            fileOpenCSV = open(self.fileCSV, 'wt')
            self.writerCSV = csv.writer(fileOpenCSV) 
        except:
            return QMessageBox.information(self.iface.mainWindow(), "Info", "File path CSV invalid", QMessageBox.Close)
            
        #Aplicar a funcao getValoreListWidget
        self.getValoreListWidget()
        if len(self.namesRastersListWidget) == 0:
            return QMessageBox.information(self.iface.mainWindow(), "Info", "There are no selected rasters in List", QMessageBox.Close)
            #Destrui as acoes do botao OK
            self.dlg.ui.pushButtonOk.closeEvent()
        #Aplicar a funcao 
        self.getInfoRasterClasses(self.keysNomesRasters[self.indexComboRasterClass])
        #--------------------------------------#
        #obter valores a serem desconsiderados
        if self.dlg.ui.lineEditDisconsiderar.text() == 'None':
            #verificar as condicoes sobre o raster, aplicar apenas com nodata
            condRaster = np.logical_or(self.arrayRaster == self.noDataRasterClassesNumber,self.arrayRaster == 111111119 )
            
        else:
            valuesDesconsider = self.dlg.ui.lineEditDisconsiderar.text().split(';')
            evalDigitDesconsider = [i.isdigit()for i in valuesDesconsider]
            if  False in evalDigitDesconsider:
                return QMessageBox.information(self.iface.mainWindow(), "Info", "Values desconsider aren't number", QMessageBox.Close)
            else:
                textCond = 'np.logical_or(self.arrayRaster == self.noDataRasterClassesNumber'
                for i in valuesDesconsider:
                   textCond = textCond +',self.arrayRaster =='+i  
                   
            textCond = textCond +')' 
            condRaster = eval(textCond)
        
        #------------------------------------------#                           
        inicia = time.time()
        #Remove todos valores iagual a False retorna linha e coluna 
        nd = np.where(condRaster == False)
        #Value barra de progresso
        tam = nd[0].shape[0]        
        cont = 0
        #Escrever no arquivo csv os nomes dos campos
        nomesCamposCSV = ['X','Y',"classes"]     
        [nomesCamposCSV.append(i) for i in self.namesRastersListWidgetAux]
        self.writerCSV.writerow(nomesCamposCSV)
        for nRow,nCol in np.nditer(nd): 
                    cont+=1
                    self.valueProgress = (cont*100)/tam
                    self.dlg.ui.progressBar.setValue(self.valueProgress)                                           
                    valoresLista = []
                    coordX = float(self.originX + ((nCol*self.sizePixel)+(self.sizePixel/2)))
                    valoresLista.append(round(float(coordX),int(valorCasasDecimais)))
                    coordY = float(self.originY - ((nRow*self.sizePixel)+(self.sizePixel/2)))
                    valoresLista.append(round(float(coordY),int(valorCasasDecimais)))
                    identClasses = self.rasterClassesProvider.identify(QgsPoint( coordX  ,coordY ),QgsRaster.IdentifyFormatValue)
                    valuePixelClasses = identClasses.results().values()
                    valoresLista.append(int(valuePixelClasses[0]))                    
                    #Acessa os rasters do QGIS
                    for nameRastersListWidget in self.namesRastersListWidget: 
                        #Acessa o raster 
                        rlayer = self.allLayerMap[nameRastersListWidget]
                        ident = rlayer.dataProvider().identify(QgsPoint( coordX , coordY),QgsRaster.IdentifyFormatValue)
                        #Inseri na lista o valor do pixel
                        valuePixel = ident.results().values()
                        if type(valuePixel[0]) == float:
                            [valoresLista.append(round(i,int(valorCasasDecimais))) for i in  valuePixel]                            
                        elif type(valuePixel[0]) == int:
                            [valoresLista.append(int(i)) for i in  valuePixel] 
                        else:                        
                            [valoresLista.append('None') for i in  valuePixel]
                    #escrever aquivo
                    self.writerCSV.writerow(valoresLista)
                    
        #fechar arquivo CSV
        fileOpenCSV.close()
        fim =time.time()
        print (fim - inicia)/60
        #Mostrar uma mensagem e finalizar o processo
        QMessageBox.information(self.iface.mainWindow(), "Info", "completed process", QMessageBox.Close)
        self.dlg.ui.progressBar.setValue(0)
        self.dlg.ui.lineEditSaveCsv.clear()
        self.fileCSV =""
        
        
    def saveCSV(self):
        self.fileCSV = QFileDialog.getSaveFileName(self.iface.mainWindow(), 'Save file CSV', '.csv', '*.csv')
        self.dlg.ui.lineEditSaveCsv.setText(self.fileCSV)
    def exitProgram(self):
          self.dlg.hide()        
    

