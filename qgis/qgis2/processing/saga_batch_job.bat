set SAGA=C:/PROGRA~1/QGISCH~1/apps\saga
set SAGA_MLB=C:/PROGRA~1/QGISCH~1/apps\saga\modules
PATH=PATH;%SAGA%;%SAGA_MLB%
saga_cmd shapes_polygons "Polygon Centroids" -POLYGONS "C:/Users/phd/.qgis2/python/plugins\processing\tests\data\polygons.shp" -CENTROIDS "C:\Users\phd\AppData\Local\Temp\processing\2945c6f008444c8b968f4ba0dfe651b0\CENTROIDS.shp"
exit