@echo off
mklink /D %USERPROFILE%\SparkleShare  "C:\Air\SparkleShare\"
mklink %APPDATA%\sparkleshare\config.xml %USERPROFILE%\SparkleShare\config\sparkleshare\configWin.xml