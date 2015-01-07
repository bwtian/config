#-------------------------------------------
# Makefile for MODIS Reprojection Tool (MRT)
#-------------------------------------------

!INCLUDE ../nmake.opt

LDFLAGS = $(HDFLIB) $(GEOLIB)
MV = move
CP = copy
RM = del

INCS = $(INCS) -I../gctp -I../geolib

#--------------------------
# Define the include files:
#--------------------------
INC =

#-----------------------------------------
# Define the source code and object files:
#-----------------------------------------
SRC	= \
	hdflist.c

OBJ = $(SRC:.c=.obj)

#-----------------------------
# Define the object libraries:
#-----------------------------
GEOLIB = ../gctp/libgctp.lib
HDFLIB = $(LIBDIR)/libhdfeos.lib $(LIBDIR)/libmfhdf.lib $(LIBDIR)/libdf.lib $(LIBDIR)/libjpeg.lib $(LIBDIR)/libz.lib $(LIBDIR)/libsz.lib

#-----------------------
# Define the executable:
#-----------------------
EXE = hdflist.exe

#-----------------------------
# Targets for each executable:
#-----------------------------
all: $(EXE)

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

.c.o:
	$(CC) $(CFLAGS) $(INCS) -c $<

