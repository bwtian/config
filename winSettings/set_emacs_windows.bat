@echo off
del /f %USERPROFILE%\.emacs.d
mklink /D %USERPROFILE%\.emacs.d  "C:\Air\SparkleShare\emacs.d\e1_tianEmacs\"