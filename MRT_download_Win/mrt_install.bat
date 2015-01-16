@ECHO OFF
CLS

REM ===========================================================
REM Modis Reprojection Tool Install Script - Windows Version
REM 
REM Maverick M.  09/07  Java 1.4 or greater is now required.
REM Maverick M.  10/10  Java 1.5 or greater is now required.
REM ===========================================================

REM See if user really wants to do an install
echo+
echo MODIS Reprojection Tool (MRT) Installation
echo ------------------------------------------
echo+
echo To install the Modis Reprojection Tool:
echo+
echo 1. The unzip executable and the MRT_Win.zip installation zip file
echo    must be present in the current directory.
echo 2. You must know the directory path where MRT is to be installed.
echo 3. You must know the path to the Java bin directory on your system.
echo+

REM Check for presence of zip file:
IF EXIST .\MRT_Win.zip GOTO WANTTOINSTALL

echo Error: MRT_Win.zip was not found in the current directory.
echo+
echo MRT installation aborted! Nothing was installed on your system.
echo+
GOTO DONE

:WANTTOINSTALL
REM See if user still wants to do the install:
echo To determine the Java bin directory, click on the Windows Start button
echo and select Find, Files or Folders... Fill in the dialog box to search
echo all local hard drives for a file named java.exe. Make note of the
echo directory containing the most recent version of java.exe.
echo+
echo If java.exe does not appear in the Find Files listing, then Java may not be
echo installed on your system. You must install Java in order to run the MRT
echo GUI.  Java software may be obtained on the World Wide Web at
echo http://java.sun.com.
echo+

PAUSE
CLS

REM Check for unzip executable:
IF EXIST .\unzip.exe GOTO HAVEUNZIP

echo Warning: the unzip executable was not found in the current directory.
echo Unless the unzip program is on your path, the MRT installation
echo will fail.
echo+

:ASKTOPROCEEDFORUNZIP
SET /P MRTPROCEED="Do you wish to proceed with the MRT installation? [y/n] "
IF /I "%MRTPROCEED%" == "Y" GOTO HAVEUNZIP
IF /I "%MRTPROCEED%" == "N" GOTO DONTHAVEUNZIP
GOTO ASKTOPROCEEDFORUNZIP

REM User selected to abort the install:
:DONTHAVEUNZIP
echo+
echo MRT installation aborted at user request!
echo Nothing was installed on your system.
echo+
GOTO DONE

:HAVEUNZIP

REM ======================================================
REM User wants to install the MRT.
REM ======================================================

REM Ask the user where to install the MRT:
echo+
echo Where would you like to install the MRT?
echo+
echo IMPORTANT!
echo 1. Give an absolute path, without wildcards or other special characters.
echo+
echo For example: c:\Modis
echo              c:\program files\MRT
echo              d:\ModisTools\MRT
echo+
echo To install the MRT into a MRT subdirectory in the current directory,
echo just press the ^<Enter^> key.
echo+

:READMRTDIRECTORY
echo Enter the MRT directory path followed by the ^<Enter^> key:
SET MRTINPUT=
SET /P MRTINPUT="> "
IF "%MRTINPUT%" == "" GOTO MRTPWD
GOTO ACCEPTMRTDIRECTORY

:MRTPWD
SET MRTDIRECTORY=%CD%\MRT
GOTO CHECKMRTDIREXISTS

:ACCEPTMRTDIRECTORY
SET MRTDIRECTORY=%MRTINPUT%

REM Check to see if the directory exists, and then ask again
REM if the user wants to proceed with installation.
:CHECKMRTDIREXISTS
IF EXIST "%MRTDIRECTORY%\bin\resample.exe" GOTO MRTDIREXISTS

SET MRTINPUT=
SET /P MRTINPUT="Directory does not exist. Create %MRTDIRECTORY%? [y/n] "
GOTO VERIFYMRTDIR

:MRTDIREXISTS
echo Warning: Directory %MRTDIRECTORY% already exists.
echo Proceeding with install may overwrite existing files.
echo+
SET MRTINPUT=
SET /P MRTINPUT="Proceed with install into %MRTDIRECTORY%? [y/n] "

:VERIFYMRTDIR
REM Make sure user wants to proceed with installation:
IF /I "%MRTINPUT%" NEQ "Y" GOTO ABORTMRTDIR
GOTO UNZIPMRTZIP

:ABORTMRTDIR
echo+
echo MRT installation aborted at user request!
echo Nothing was installed on your system.
echo+
GOTO DONE

:UNZIPMRTZIP
REM ======================================================
REM Unzip the MRT zipfile.
REM ======================================================

REM Unzip the MRT into the correct directory.
REM The -o option forces overwriting existing files.
echo+
echo Unzipping MRT_Win.zip file...
IF EXIST .\unzip.exe GOTO USELOCALZIP

unzip -o MRT_Win.zip -d "%MRTDIRECTORY%"
GOTO UNZIPERRORCHECK

:USELOCALZIP
.\unzip -o MRT_Win.zip -d "%MRTDIRECTORY%" 

:UNZIPERRORCHECK
REM Check to see if there was an error running unzip.
IF %ERRORLEVEL% NEQ 0 GOTO UNZIPFAILED

echo+
echo Unzip executed successfully.
echo+
GOTO ASKWINDOWVERSION

:UNZIPFAILED
echo+
echo Error: unzip failed to execute correctly.
echo+
echo Modis Reprojection Tool installation FAILED!
echo+
echo Possible problems:
echo 1. unzip.exe is not present in the current directory
echo 2. the file MRT_Win.zip is not present in the current directory
echo 3. lack of write privileges in the MRT directory
echo+
echo Please read the installation instructions and try again.
echo+
GOTO DONE

:ASKWINDOWVERSION
REM ================================================
REM Which version of Windows is the user running?
REM ================================================

echo Which version of Windows are you running?
echo 1. Windows XP or later
echo 2. Windows 2000
echo 3. Windows NT

SET /P WINCHOICE="Please select version [1/2/3] "

REM ======================================================
REM Update the PATH and define the MRT_DATA_DIR variable.
REM ======================================================
IF "%WINCHOICE%" == "2" GOTO AUTOEXECMOD

REM Windows NT and XP require a little different handling.
echo Windows NT or XP (or later) installation ...
echo Updating HKEY_CURRENT_USER/Environment variables.
.\reg_set.exe "%MRTDIRECTORY%\bin" "%MRTDIRECTORY%\data" "%MRTDIRECTORY%"
IF ERRORLEVEL 0 GOTO ASKJAVAPATH
echo ERROR updating the HKEY_CURRENT_USER/Environment variables.
GOTO DONE

:AUTOEXECMOD

REM Processing Windows 2000.
REM Modify the user's AUTOEXEC.BAT file.
echo Windows 2000 installation ...
IF EXIST "c:\autoexec.bat" GOTO AUTOEXECEXISTS

echo Updating C:\AUTOEXEC.BAT.
GOTO MODIFYAUTOEXEC

:AUTOEXECEXISTS

echo Updating C:\AUTOEXEC.BAT (old version saved as AUTOEXEC.MRT).
copy c:\autoexec.bat c:\autoexec.mrt

:MODIFYAUTOEXEC

echo set MRT_HOME=%MRTDIRECTORY%>> c:/autoexec.bat
echo set Path=%MRTDIRECTORY%\bin;%%Path%%>> c:/autoexec.bat
echo set MRT_DATA_DIR=%MRTDIRECTORY%\data>> c:/autoexec.bat


:ASKJAVAPATH
REM ======================================================
REM Java installation stuff for the MRT GUI.
REM ======================================================

REM Find out where Java is installed
echo+
echo ======================================================
echo+
echo Where is the Java bin directory located on your system?
echo (This is the directory in which the file java.exe is stored.)
echo+
echo IMPORTANT!
echo 1. Give an absolute path, without wildcards or other special characters.
echo+
echo For example: c:\Program Files\Java\jre1.5.0_10\bin
echo              c:\winnt\JavaSoft\JRE\1.5.0_02\bin
echo              c:\jdk1.5\bin
echo+

:JAVAPATHLOOP
echo Please enter the path to your Java bin directory followed by the ^<Enter^> key:
SET /P JAVADIRECTORY="> "

IF "%JAVADIRECTORY%" == "" GOTO NOJAVADIR
SET LASTCHAR=%JAVADIRECTORY:~-1%
IF "%LASTCHAR%" == "\" GOTO JAVADIRHASBACKSLASH

SET JAVAPATH=%JAVADIRECTORY%\java.exe
GOTO JAVACHECK

:JAVADIRHASBACKSLASH
SET JAVAPATH=%JAVADIRECTORY%java.exe
GOTO JAVACHECK

:NOJAVADIR
SET JAVAPATH=java.exe

:JAVACHECK
REM See if we can find the java executable in Java bin directory.

echo+

IF EXIST "%JAVAPATH%" GOTO JAVABINARYFOUND

echo Warning: %JAVAPATH% not found.
echo+
echo You will be able to run the MRT from the command line, but you may
echo have problems with the MRT GUI. After the installation is completed,
echo try running the ModisTool batch file in the MRT bin directory.
echo If the GUI does not appear, make sure Java is installed on your system.
echo Then locate the Java bin directory and reinstall MRT.
echo+
echo Java software may be obtained on the World Wide Web at http://java.sun.com.
GOTO VALIDATEENTRY

:JAVABINARYFOUND
echo Found %JAVAPATH%. Testing Java version...
echo+
"%JAVAPATH%" -version
echo+
echo IMPORTANT! The Java version must be 1.5 or greater.
echo+
echo If your Java version is less than 1.5, please install a newer version
echo of Java, and then reinstall MRT.
echo+
echo Java software may be obtained on the World Wide Web at http://java.sun.com.

:VALIDATEENTRY
SET MRTINPUT=
SET /P MRTINPUT="Would you like to keep this Java path? [y/n] "
IF /I "%MRTINPUT%" == "Y" GOTO PRESSENTER
IF /I "%MRTINPUT%" == "N" GOTO JAVAPATHLOOP

echo Invalid entry, please try again...
GOTO VALIDATEENTRY

:PRESSENTER
echo+
SET MRTINPUT=
SET /P MRTINPUT="Press the <Enter> key to finish the MRT installation."

REM Go to the MRT directory and construct the mrt.bat file. 
echo @echo off> mrt.bat
echo+ >> mrt.bat
echo rem     *****************>> mrt.bat
echo rem     * ModisTool.bat *>> mrt.bat
echo rem     *****************>> mrt.bat
echo+ >> mrt.bat

echo rem Set the MRT_HOME environmental var to the MRT installation>> mrt.bat
echo rem directory.>> mrt.bat
echo+ >> mrt.bat
echo set MRT_HOME=%MRTDIRECTORY%>> mrt.bat
echo+ >> mrt.bat

echo rem Set the MRT_DATA_DIR environmental var to the MRT data directory.>> mrt.bat
echo+ >> mrt.bat
echo set MRT_DATA_DIR=%MRTDIRECTORY%\data>> mrt.bat
echo+ >> mrt.bat

echo rem Set the PATH environment variable to include the MRT executables.>> mrt.bat
echo+ >> mrt.bat
echo set Path=%MRTDIRECTORY%\bin;%%Path%%>> mrt.bat
echo+ >> mrt.bat

echo rem Run the Java GUI.>> mrt.bat
echo rem Change the java.exe path to reflect the directory structure on your machine.>> mrt.bat
echo rem Quotes are only necessary to handle blank spaces in the pathnames.>> mrt.bat
echo+ >> mrt.bat
echo "%JAVAPATH%" -jar "%MRTDIRECTORY%\bin\ModisTool.jar">> mrt.bat
echo+ >> mrt.bat

REM Create a batch file named ModisTool.bat:
IF EXIST .\mrt.bat GOTO MRTBATEXISTS
GOTO CONGRATS

:MRTBATEXISTS
copy "%MRTDIRECTORY%\bin\ModisTool.bat" "%MRTDIRECTORY%\bin\ModisTool.bak"
move /Y mrt.bat "%MRTDIRECTORY%\bin\ModisTool.bat"

:CONGRATS
echo+
echo+
echo           ****************************************************
echo           * Congratulations! You have successfully installed *
echo           * the Modis Reprojection Tool on your system!      *
echo           ****************************************************
echo+
echo The MRT bin directory was added to the system path, and the
echo MRT_DATA_DIR environmental variable was set to the MRT data
echo directory.
echo+
IF  "%WINCHOICE%" == "2" GOTO WINEXPLAIN
GOTO DONE

:WINEXPLAIN
echo This was accomplished by modifying C:\AUTOEXEC.BAT. The old version was
echo saved as AUTOEXEC.MRT."
echo+
echo These changes will not take effect until you restart your computer.
echo+

:DONE

