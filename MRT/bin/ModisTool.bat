@echo off
 
rem     *****************
rem     * ModisTool.bat *
rem     *****************
 
rem Set the MRT_HOME environmental var to the MRT installation
rem directory.
 
set MRT_HOME=d:\R\MRT
 
rem Set the MRT_DATA_DIR environmental var to the MRT data directory.
 
set MRT_DATA_DIR=d:\R\MRT\data
 
rem Set the PATH environment variable to include the MRT executables.
 
set Path=d:\R\MRT\bin;%Path%
 
rem Run the Java GUI.
rem Change the java.exe path to reflect the directory structure on your machine.
rem Quotes are only necessary to handle blank spaces in the pathnames.
 
"C:\Program Files\Java\jdk1.7.0_03\jre\bin\java.exe" -jar "d:\R\MRT\bin\ModisTool.jar"
 
