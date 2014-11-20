# ##############################################################################
# For software setup
# ##############################################################################
# For NEST_SAR
export NEST_HOME="/home/tian/NEST4C-1.1"
export PATH=$PATH:/home/tian/NEST4C-1.1

## For GMT and GMTSAR
# Default locations of GMT components:
export PATH=/home/tian/Dropbox/linux/trunk/gmt/gmt-dev.svn/GMT/GMT4.5.8/bin:$PATH
export NETCDFHOME=/home/tian/Dropbox/GMT/netcdf-3.6.3
        # executables     /home/tian/GMT/GMT4.5.8/bin
        # library         /home/tian/GMT/GMT4.5.8/lib
        # shared data     /home/tian/GMT/GMT4.5.8/share
        # manual pages    /home/tian/GMT/GMT4.5.8/man/man/man?
        # documentation   /home/tian/GMT/GMT4.5.8/share/doc/gmt

# # Default locations of GMT components:

#location of shared data (including subdirectories coast, cpt, etc.):
export GMT_SHAREDIR=/home/tian/Dropbox/GMT/GMT4.5.8/share
# user-specific configurations (color tables, .gmtdefaults, etc.):
export GMT_USERDIR=/home/tian/Dropbox/GMT/GMT4.5.8/.gmt
# user-specific data (grids, column data):
                # GMT_DATADIR = (undefined)
# other deprecated data directories:
                # GMT_GRIDDIR = (undefined)
                # GMT_IMGDIR = (undefined)

## For Android Develop Envrionmet
# JAVA JDK: Java SE Develop Kit, # test cmd: java, javac, which java
#export JAVA_HOME=/home/tian/Dropbox/Linux_Portable/jdk
#export PATH=${PATH}:$JAVA_HOME/bin
JAVA_HOME=/home/tian/Dropbox/linux/jre1.7.0_67
CLASSPATH=$JAVA_HOME/lib.tools.jar
PATH=$JAVA_HOME/bin:$PATH
export JAVA_HOME CLASSPATH PATH
# Android SDK  #test cmd: adb, android
#export PATH=${PATH}:/home/tian/Dropbox/Linux_Portable/android-sdk/tools
#export PATH=${PATH}:/home/tian/Dropbox/Linux_Portable/android-sdk/platform-tools
# Eclipse
#export PATH=${PATH}:/home/tian/Dropbox/Linux_Portable/eclipse
# R
#export PATH=${PATH}:/home/tian/Dropbox/soft/linux/R/R-3.0.3/bin
#export RSTUDIO_WHICH_R=/home/tian/Dropbox/soft/linux/R/R-3.0.3/bin/R
#cd /bin
#sudo ln -s /home/tian/Dropbox/soft/linux/R/R-3.0.3/bin/R .

# Wed May  7 23:32:09 JST 2014 - MODIS Reprojection Tool modifications
MRT_HOME="~/Dropbox/soft/linux/MRT/MRT"
PATH="$PATH:~/Dropbox/soft/linux/MRT/MRT/bin"
MRT_DATA_DIR="~/Dropbox/soft/linux/MRT/MRT/data"
export MRT_HOME PATH MRT_DATA_DIR

# Wed May  7 23:45:20 JST 2014 - MODIS Reprojection Swath Tool modifications
MRTSWATH_HOME="~/Dropbox/soft/linux/MRT/MRTSwath"
PATH="$PATH:~/Dropbox/soft/linux/MRT/MRTSwath/bin"
MRTSWATH_DATA_DIR="~/Dropbox/soft/linux/MRT/MRTSwath/data"
export MRTSWATH_HOME PATH MRTSWATH_DATA_DIR

    
