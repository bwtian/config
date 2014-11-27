set SAGA=C:/PROGRA~1/QGISBR~1/apps\saga
set SAGA_MLB=C:/PROGRA~1/QGISBR~1/apps\saga\modules
PATH=PATH;%SAGA%;%SAGA_MLB%
saga_cmd shapes_polygons "Polygon Centroids" -POLYGONS "C:/Users/QGIS/.qgis2/python/plugins\processing\tests\data\polygons.shp" -CENTROIDS "C:\Users\QGIS\AppData\Local\Temp\processing\b3ea6d19297c431898ba164855eb90e2\CENTROIDS.shp"
exit