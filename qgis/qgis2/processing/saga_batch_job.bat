set SAGA=C:/PROGRA~1/QGISBR~1/apps\saga
set SAGA_MLB=C:/PROGRA~1/QGISBR~1/apps\saga\modules
PATH=PATH;%SAGA%;%SAGA_MLB%
saga_cmd shapes_lines "Line-Polygon Intersection" -LINES "D:/tian/greenTuff/greenTuffL.shp" -POLYGONS "D:/tian/greenTuff/hkdLand_141127_113019.shp" -METHOD 0 -INTERSECT "C:\Users\QGIS\AppData\Local\Temp\processing\fd4870907b004967b3fca5dbf3e647c1\INTERSECT.shp"
exit