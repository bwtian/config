#-------------------------------------------
# Makefile for MODIS Reprojection Tool (MRT)
#-------------------------------------------

!INCLUDE ../nmake.opt

LDFLAGS = $(MRTLIB) $(HDFLIB) $(GEOLIB) $(TIFFLIB) 
MV = move
CP = copy
RM = del

INCS = $(INCS) -I../gctp -I../geolib -I../shared_src

#--------------------------
# Define the include files:
#--------------------------
INC = hdf2rb.h

#-----------------------------------------
# Define the source code and object files:
#-----------------------------------------
SRC	= \
	hdf2rb.c convert_image.c no_res.c

OBJ = $(SRC:.c=.obj)

#-----------------------------
# Define the object libraries:
#-----------------------------
GEOLIB = ../geolib/libgeolib.lib ../gctp/libgctp.lib
HDFLIB = $(LIBDIR)/libhdfeos.lib $(LIBDIR)/libmfhdf.lib $(LIBDIR)/libdf.lib $(LIBDIR)/libjpeg.lib $(LIBDIR)/libz.lib $(LIBDIR)/libsz.lib
TIFFLIB = $(LIBDIR)/libgeotiff.lib $(LIBDIR)/libtiff.lib
MRTLIB = ../shared_src/libmrt.lib

#-----------------------
# Define the executable:
#-----------------------
EXE = hdf2rb.exe

#-----------------------------
# Targets for each executable:
#-----------------------------
default: $(EXE)

$(EXE): $(OBJ) $(INC)
	$(CC) $(CFLAGS) $(OBJ) $(EXTRA_OBJ) $(LDFLAGS)

install:
	$(MV) $(EXE) ../bin

clean:
	-$(RM) $(OBJ) *.pdb *.idb *.ilk *.lib *.exp $(EXE)

copy-makefile:
	-@if NOT EXIST Makefile.orig $(CP) Makefile Makefile.orig
	$(CP) Makefile.$(CPMAKEFILEEXT) Makefile

#-------------------------------------
# Rules for compiling the object files
#-------------------------------------

$(OBJ): $(INC)

.c.obj:
	$(CC) $(CFLAGS) $(INCS) -c $<

