set HOME=C:\Users\willin
set GISRC=C:\Users\willin\.qgis2\\processing\processing.gisrc
set GRASS_SH=C:/PROGRA~2/QGISVA~1/apps\msys\bin\sh.exe
set PATH=C:/PROGRA~2/QGISVA~1/apps\msys\bin;C:/PROGRA~2/QGISVA~1/apps\msys\lib;%PATH%
set WINGISBASE=C:/PROGRA~2/QGISVA~1/apps\grass\grass-6.4.3
set GISBASE=C:/PROGRA~2/QGISVA~1/apps\grass\grass-6.4.3
set GRASS_PROJSHARE=C:/PROGRA~2/QGISVA~1/apps\grass\grass-6.4.3\share\proj
set GRASS_MESSAGE_FORMAT=gui
if "%GRASS_ADDON_PATH%"=="" set PATH=%WINGISBASE%\bin;%WINGISBASE%\lib;%PATH%
if not "%GRASS_ADDON_PATH%"=="" set PATH=%WINGISBASE%\bin;%WINGISBASE%\lib;%GRASS_ADDON_PATH%;%PATH%

set GRASS_VERSION=6.4.0
if not "%LANG%"=="" goto langset
FOR /F "usebackq delims==" %%i IN (`"%WINGISBASE%\etc\winlocale"`) DO @set LANG=%%i
:langset

set PATHEXT=%PATHEXT%;.PY
set PYTHONPATH=%PYTHONPATH%;%WINGISBASE%\etc\python;%WINGISBASE%\etc\wxpython\n
g.gisenv.exe set="MAPSET=PERMANENT"
g.gisenv.exe set="LOCATION=temp_location"
g.gisenv.exe set="LOCATION_NAME=temp_location"
g.gisenv.exe set="GISDBASE=C:\Users\willin\AppData\Local\Temp\processing\grassdata"
g.gisenv.exe set="GRASS_GUI=text"
g.proj -c proj4="+proj=utm +zone=30 +ellps=intl +towgs84=-87,-98,-121,0,0,0,0 +units=m +no_defs"
v.in.ogr min_area=0.0001 snap=-1 dsn="C:/PROGRA~2/QGISVA~1/apps/qgis/./python/plugins\processing\tests\data" layer=points output=tmp1395242611742 --overwrite -o
g.region n=4458983.8488 s=4458921.97814 e=270855.745301 w=270778.60198 res=1
v.voronoi input=tmp1395242611742 output=outputcdb1ed67849146388de828554508f450 --overwrite
v.out.ogr -s -c -e -z input=outputcdb1ed67849146388de828554508f450 dsn="C:\Users\willin\AppData\Local\Temp\processing\a01e2a0457f743ac8007516226866b65" format=ESRI_Shapefile olayer=output type=auto

exit
