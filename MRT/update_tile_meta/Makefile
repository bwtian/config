#-------------------------------------------
# Makefile for MODIS Reprojection Tool (MRT)
#-------------------------------------------

!INCLUDE ../nmake.opt

# Link in MFHDF for getopt

LDFLAGS = $(HDFLIB) $(MRTLIB)
MV = move
CP = copy
RM = del

#--------------------------
# Define the include files:
#--------------------------
INC = update_tile_meta.h

#-----------------------------------------
# Define the source code and object files:
#-----------------------------------------
SRC	= \
	update_tile_meta.c

OBJ = $(SRC:.c=.obj)

#-----------------------------
# Define the object libraries:
#-----------------------------
HDFLIB = $(LIBDIR)/libmfhdf.lib $(LIBDIR)/libdf.lib $(LIBDIR)/libjpeg.lib $(LIBDIR)/libz.lib $(LIBDIR)/libsz.lib

#-----------------------
# Define the executable:
#-----------------------
EXE = update_tile_meta.exe

#-----------------------------
# Targets for each executable:
#-----------------------------
all: $(EXE)

$(EXE): $(OBJ) $(INC)
	$(CC) $(CFLAGS) $(OBJ) $(EXTRA_OBJ)  $(LDFLAGS)

install:
	$(MV) $(EXE) ../bin

clean:
	-$(RM) $(OBJ) *.pdb *.idb *.ilk *.lib *.exp $(EXE)

copy-makefile:
	-@if NOT EXIST Makefile.orig $(CP) Makefile Makefile.orig
	$(CP) Makefile.$(CPMAKEFILEEXT) Makefile

#--------------------------------------
# Rules for compiling the object files:
#--------------------------------------

$(OBJ): $(INC)

.c.obj:
	$(CC) $(CFLAGS) $(INCS) -c $<

