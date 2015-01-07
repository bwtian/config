#!/bin/sh

#================================================================
# MODIS Reprojection Tool Install Script - UNIX Version
# Brad Misterek and John Weiss 02/01
# Gail Schmidt 11/02  Java 1.3 or greater is now required.
#                     Setup mrtdatadir for world.jpg display
# Gail Schmidt 05/04  Modified to no longer create the .login,
#                     .cshrc, .tcshrc, .profile, or .bash_profile
#                     files if they don't already exist
# Maverick M.  09/07  Java 1.4 or greater is now required.    
#              11/02  Java 1.5 or greater is now required.    
#================================================================

# See if user really wants to do an install:
echo
echo "MODIS Reprojection Tool (MRT) Installation"
echo ------------------------------------------
echo
echo "To install the MODIS Reprojection Tool:"
echo
echo "1. The MRT_Linux.zip installation zip file must be present in the"
echo "   current directory."
echo "2. You must know the directory path where MRT is to be installed."
echo "3. You must know the path to the Java bin directory on your system."
echo 

# Check for presence of zip file:
if [ ! -f ./MRT_Linux.zip ] ; then
    echo "Error: MRT_Linux.zip was not found in the current directory."
    echo
    echo "MRT installation aborted! Nothing was installed on your system."
    echo
    exit 1
fi

# See if user wants to continue:
echo "Do you wish to proceed with the MRT installation? [y/n]"
read choice
if [ $choice != "y" -a $choice != "Y" ] ; then
    echo
    echo "MRT installation aborted at user request!"
    echo "Nothing was installed on your system."
    echo
    exit 2
fi

#======================================================
# User wants to install the MRT.
#======================================================

# Ask the user to enter the MRT directory.
echo
echo "Where would you like to install the MRT?"
echo
echo "IMPORTANT NOTE:"
echo "Be sure to give an absolute directory path, without wildcards or"
echo "other special characters. For example: /home/gschmidt/MRT"
echo
echo "To install MRT into a MRT subdirectory in the current directory,"
echo "just press the Enter key."
echo
echo "Enter the MRT directory path:"
read directory

if [ "X$directory" = "X" ] ; then
    directory=`pwd`/MRT
fi

# Check to see if the directory exists, and then ask again
# if the user wants to proceed with installation.
if [ -d "$directory" ] ; then
    echo "Warning: Directory $directory already exists."
    echo "Proceeding with install may overwrite existing files."
    echo
    echo "Proceed with install into $directory? [y/n]"
else
    echo "Directory does not exist. Create $directory? [y/n]"
fi

# Make sure user wants to proceed with installation:
read choice
if [ $choice != "y" -a $choice != "Y" ] ; then
    echo
    echo "MRT installation aborted at user request!"
    echo "Nothing was installed on your system."
    echo
    exit 3
fi

#======================================================
# Unzip the MRT zipfile.
#======================================================

# Unzip MRT into the correct directory.
# The -o option forces overwriting existing files.
echo
echo "Unzipping MRT zip file..."
if [ -f /usr/local/bin/unzip ] ; then
    echo "Unzipping MRT_Linux.zip file with /usr/local/bin/unzip..."
    /usr/local/bin/unzip -o MRT_Linux.zip -d "$directory"
elif [ -f /usr/bin/unzip ] ; then
    echo "Unzipping MRT_Linux.zip file with /usr/bin/unzip..."
    /usr/bin/unzip -o MRT_Linux.zip -d "$directory"
elif [ -f /bin/unzip ] ; then
    echo "Unzipping MRT_Linux.zip file with /bin/unzip..."
    /bin/unzip -o MRT_Linux.zip -d "$directory"
elif [ -f ./unzip ] ; then
    echo "Unzipping MRT_Linux.zip file with ./unzip..."
    ./unzip -o MRT_Linux.zip -d "$directory"
else
    echo "Unzipping MRT_Linux.zip file with unzip..."
    unzip -o MRT_Linux.zip -d "$directory"
fi

# Check to see if there was an error running unzip.
if [ $? -ne 0 ] ; then
    echo
    echo "Error: unzip failed to execute."
    echo
    echo "MODIS Reprojection Tool installation FAILED!"
    echo
    echo "Possible problems:"
    echo "1. the correct unzip executable is not present in /usr/local/bin,"
    echo "   /usr/bin, /bin, the current directory, or in your path."
    echo "2. the file MRT_Linux.zip is not present in the current directory"
    echo "3. lack of write privileges in the MRT directory"
    echo
    echo "Please read the installation instructions and try again."
    echo
    exit 4
else
    echo
    echo "Unzip executed successfully."
    echo
fi

#======================================================
# Java installation stuff for the MRT GUI.
#======================================================

# First try to find java on the user path.
echo "======================================================"
echo
echo "Searching for Java executable..."
javapath=`which java 2> /dev/null`
echo

case $javapath in

    *"no java in"* )
	echo "No Java executable found on your path ($PATH)."
	javapath=java
	;;

    */java )
        echo "Found $javapath. Testing Java version."
	echo
	"$javapath" -version
	echo
	echo "IMPORTANT! The Java version must be 1.5 or greater."
	echo
        echo "Is this the correct Java executable on your system? [y/n]"
	read choice
	if [ $choice != "y" -a $choice != "Y" ] ; then
	    javapath=java
	fi
	;;

    * )
	echo "No Java executable found on your path ($PATH)."
	javapath=java
	;;
esac

# See if user wants to enter java path:
if [ "$javapath" = "java" ] ; then
  echo
  echo "Do you wish to enter the correct path? [y/n]"
  read choice
  echo
  if [ $choice != "y" -a $choice != "Y" ] ; then
    echo "OK, but the MRT GUI may not work correctly!"
  else
    done=0
    while [ $done -eq 0 ]
    do
      echo "Where is the Java bin directory located on your system?"
      echo
      echo "IMPORTANT NOTE:"
      echo "Give an absolute path, without wildcards or other special characters."
      echo "For example: /usr/java/bin"
      echo
      echo "Please enter the path to your Java bin directory:"
      read javapath

      # build whatever path the user desires
      case $javapath in
        "" ) javapath=java ;;
        */ ) javapath=${javapath}java ;;
        * )  javapath=$javapath/java ;;
      esac

      # try to find the java executable in the Java bin directory
      if [ -f "$javapath" ] ; then
        echo
        echo "Found $javapath. Testing Java version."
        echo
        "$javapath" -version
        echo
        echo "IMPORTANT! The Java version must be 1.5 or greater."
        echo
        echo "If your Java version is less than 1.5, ask your sysadmin to install"
        echo "the latest version of Java, and then reinstall the MRT."
        echo
        echo "Java software may be obtained on the World Wide Web at http://java.sun.com."
      else
        echo
        echo "Warning: $javapath not found."
        echo
        echo "You will be able to run the MRT from the command line, but you may"
        echo "have problems with the MRT GUI. After the installation is completed,"
        echo "try running the ModisTool shell script in the MRT bin directory."
        echo "If the GUI does not appear, make sure Java is installed on your system."
        echo "Then locate the Java bin directory and reinstall MRT."
        echo
        echo "You may be able to determine the Java bin directory by typing"
        echo '"which java" (without quotes). You can also typing "find / -name java"'
        echo "(without quotes), but this command may take some time to execute,"
        echo "since it will search your entire file system."
        echo
        echo "If neither command works, it is possible that Java is not installed"
        echo "on your system. In this case, contact your system administrator."
        echo
        echo "Java software may be obtained on the World Wide Web at http://java.sun.com."
      fi

      validentry=0
      while [ $validentry -eq 0 ]
      do
        echo
        echo "Would you like to keep this Java path? [y/n]"
        read javaresponse

        if [ "$javaresponse" = "y" ] || [ "$javaresponse" = "Y" ]; then
          done=1
          validentry=1
        else
          if [ "$javaresponse" = "n" ] || [ "$javaresponse" = "N" ]; then
            validentry=1
          fi
        fi
        if [ $validentry -eq 0 ]; then
          echo "Invalid entry, please try again..."
        fi
      done
    done
  fi
fi

echo
echo "Press the Enter key to finish the MRT installation."
read choice

#=========================================================
# Construct the ModisTool file in the MRT bin directory.
#=========================================================

cd $directory/bin
echo "#!/bin/sh" > ModisTool
echo >> ModisTool

echo "# ****************************************" >> ModisTool
echo "# * ModisTool                            *" >> ModisTool
echo "# * Shell script for running the MRT GUI *" >> ModisTool
echo "# ****************************************" >> ModisTool
echo >> ModisTool

echo "# Set the MRT_HOME environmental var to the MRT installation directory." >> ModisTool
echo >> ModisTool
echo "MRT_HOME=\"$directory\"" >> ModisTool
echo "export MRT_HOME" >> ModisTool
echo >> ModisTool
echo "# Set the MRT_DATA_DIR environmental var to the MRT data directory." >> ModisTool
echo "MRT_DATA_DIR=\"\$MRT_HOME/data\"" >> ModisTool
echo "export MRT_DATA_DIR" >> ModisTool
echo >> ModisTool
echo "# Set the PATH environment variable to include the MRT executables." >> ModisTool
echo >> ModisTool
echo "PATH=\"\$MRT_HOME/bin:\$PATH\"" >> ModisTool
echo "export PATH" >> ModisTool
echo >> ModisTool

echo "# Run the MRT Java GUI." >> ModisTool
echo "\"$javapath\" -jar \"\$MRT_HOME/bin/ModisTool.jar\"" >> ModisTool

# Change permissions to allow execute access.
chmod 755 ModisTool 

#================================================================
# Modify .login, .tcshrc, .cshrc, .profile and .bash_profile
# startup scripts to add the MRT bin directory to the path
# and set the MRT_DATA_DIR env var. Only modify if the file
# already exists.
#================================================================
modify=0
if [ -f $HOME/.login ] ; then
    echo >> $HOME/.login
    echo "# `date` - MODIS Reprojection Tool modifications" >> $HOME/.login
    echo "setenv MRT_HOME \"$directory\"" >> $HOME/.login
    echo "set path = ( \$path:q \"$directory/bin\" )" >> $HOME/.login
    echo "setenv MRT_DATA_DIR \"$directory/data\"" >> $HOME/.login
    echo >> $HOME/.login
    modify=1
fi

if [ -f $HOME/.tcshrc ] ; then
    echo >> $HOME/.tcshrc
    echo "# `date` - MODIS Reprojection Tool modifications" >> $HOME/.tcshrc
    echo "setenv MRT_HOME \"$directory\"" >> $HOME/.tcshrc
    echo "set path = ( \$path:q \"$directory/bin\" )" >> $HOME/.tcshrc
    echo "setenv MRT_DATA_DIR \"$directory/data\"" >> $HOME/.tcshrc
    echo >> $HOME/.tcshrc
    modify=1
fi

if [ -f $HOME/.cshrc ] ; then
    echo >> $HOME/.cshrc
    echo "# `date` - MODIS Reprojection Tool modifications" >> $HOME/.cshrc
    echo "setenv MRT_HOME \"$directory\"" >> $HOME/.cshrc
    echo "set path = ( \$path:q \"$directory/bin\" )" >> $HOME/.cshrc
    echo "setenv MRT_DATA_DIR \"$directory/data\"" >> $HOME/.cshrc
    echo >> $HOME/.cshrc
    modify=1
fi

if [ -f $HOME/.profile ] ; then
    echo >> $HOME/.profile
    echo "# `date` - MODIS Reprojection Tool modifications" >> $HOME/.profile
    echo "MRT_HOME=\"$directory\"" >> $HOME/.profile
    echo "PATH=\"\$PATH:$directory/bin\"" >> $HOME/.profile
    echo "MRT_DATA_DIR=\"$directory/data\"" >> $HOME/.profile
    echo "export MRT_HOME PATH MRT_DATA_DIR" >> $HOME/.profile
    echo >> $HOME/.profile
    modify=1
fi

if [ -f $HOME/.bash_profile ] ; then
    echo >> $HOME/.bash_profile
    echo "# `date` - MODIS Reprojection Tool modifications" >> $HOME/.bash_profile
    echo "MRT_HOME=\"$directory\"" >> $HOME/.bash_profile
    echo "PATH=\"\$PATH:$directory/bin\"" >> $HOME/.bash_profile
    echo "MRT_DATA_DIR=\"$directory/data\"" >> $HOME/.bash_profile
    echo "export MRT_HOME PATH MRT_DATA_DIR" >> $HOME/.bash_profile
    echo >> $HOME/.bash_profile
    modify=1
fi

#========================================================================
# If none of the login or user files were found and modified, then create
# them all since we don't know for sure which one to create.
#========================================================================
if [ $modify -ne 1 ] ; then
    echo >> $HOME/.login
    echo "# `date` - MODIS Reprojection Tool modifications" >> $HOME/.login
    echo "setenv MRT_HOME \"$directory\"" >> $HOME/.login
    echo "set path = ( \$path:q \"$directory/bin\" )" >> $HOME/.login
    echo "setenv MRT_DATA_DIR \"$directory/data\"" >> $HOME/.login
    echo >> $HOME/.login

    echo >> $HOME/.tcshrc
    echo "# `date` - MODIS Reprojection Tool modifications" >> $HOME/.tcshrc
    echo "setenv MRT_HOME \"$directory\"" >> $HOME/.tcshrc
    echo "set path = ( \$path:q \"$directory/bin\" )" >> $HOME/.tcshrc
    echo "setenv MRT_DATA_DIR \"$directory/data\"" >> $HOME/.tcshrc
    echo >> $HOME/.tcshrc

    echo >> $HOME/.cshrc
    echo "# `date` - MODIS Reprojection Tool modifications" >> $HOME/.cshrc
    echo "setenv MRT_HOME \"$directory\"" >> $HOME/.cshrc
    echo "set path = ( \$path:q \"$directory/bin\" )" >> $HOME/.cshrc
    echo "setenv MRT_DATA_DIR \"$directory/data\"" >> $HOME/.cshrc
    echo >> $HOME/.cshrc

    echo >> $HOME/.profile
    echo "# `date` - MODIS Reprojection Tool modifications" >> $HOME/.profile
    echo "MRT_HOME=\"$directory\"" >> $HOME/.profile
    echo "PATH=\"\$PATH:$directory/bin\"" >> $HOME/.profile
    echo "MRT_DATA_DIR=\"$directory/data\"" >> $HOME/.profile
    echo "export MRT_HOME PATH MRT_DATA_DIR" >> $HOME/.profile
    echo >> $HOME/.profile

    echo >> $HOME/.bash_profile
    echo "# `date` - MODIS Reprojection Tool modifications" >> $HOME/.bash_profile
    echo "MRT_HOME=\"$directory\"" >> $HOME/.bash_profile
    echo "PATH=\"\$PATH:$directory/bin\"" >> $HOME/.bash_profile
    echo "MRT_DATA_DIR=\"$directory/data\"" >> $HOME/.bash_profile
    echo "export MRT_HOME PATH MRT_DATA_DIR" >> $HOME/.bash_profile
    echo >> $HOME/.bash_profile
fi

#======================================================
# We be done.
#======================================================

echo
echo "          ****************************************************"
echo "          * Congratulations! You have successfully installed *"
echo "          * the MODIS Reprojection Tool on your system!      *"
echo "          ****************************************************"
echo
echo "                          IMPORTANT NOTICE!!!"
echo
echo "The MRT bin directory has been added to the path for your account,"
echo "and the MRT_DATA_DIR environmental variable has been set to the"
echo "MRT data directory.  This has been accomplished by modifying the"
echo "startup files .login, .cshrc, .tcshrc, .profile, and/or .bash_profile"
echo "in your home directory. These changes will not take effect until you log"
echo "out and log back in again."
echo
echo "The .login, .cshrc, and .tcshrc files have the following lines appended:"
echo
echo "    setenv MRT_HOME $directory"
echo "    set path = ( \$path $directory/bin )"
echo "    setenv MRT_DATA_DIR $directory/data"
echo
echo "The .profile and .bash_profile files have the following lines appended:"
echo
echo "    MRT_HOME=$directory"
echo "    PATH=\$PATH:$directory/bin"
echo "    MRT_DATA_DIR=$directory/data"
echo "    export MRT_HOME PATH MRT_DATA_DIR"
echo

exit 0

