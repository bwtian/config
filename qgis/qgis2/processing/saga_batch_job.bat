set SAGA=C:/PROGRA~1/QGISBR~1/apps\saga
set SAGA_MLB=C:/PROGRA~1/QGISBR~1/apps\saga\modules
PATH=PATH;%SAGA%;%SAGA_MLB%
saga_cmd shapes_tools "Merge Shapes Layers" -MAIN "C:\Users\QGIS\AppData\Local\Temp\processing\796f9fea265543c1a5f9ab5cbcbbafd7\OUTPUT.shp" -LAYERS "D:/tian/greenTuff/greenTuffL.shp" -OUT "C:\Users\QGIS\AppData\Local\Temp\processing\c002371f3b1e452bb87d945c70f381fa\OUT.shp"
exit