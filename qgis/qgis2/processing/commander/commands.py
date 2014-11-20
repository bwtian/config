from qgis.core import *
import processing

def removeall():
	mapreg = QgsMapLayerRegistry.instance()
	mapreg.removeAllMapLayers()

def load(*args):
	processing.load(args[0])
