set SAGA=C:/PROGRA~1/QGISBR~1/apps\saga
set SAGA_MLB=C:/PROGRA~1/QGISBR~1/apps\saga\modules
PATH=PATH;%SAGA%;%SAGA_MLB%
saga_cmd shapes_lines "Line-Polygon Intersection" -LINES "D:/tian/greenTuff/greenTuffL.shp" -POLYGONS "D:/tian/greenTuff/hkdLand_141127_113019.shp" -METHOD 0 -INTERSECT "C:\Users\QGIS\AppData\Local\Temp\processing\f86b8db5f1764ea2ab071a3810f19271\INTERSECT.shp"
exit