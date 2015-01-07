#-------------------------------------------
# Makefile for MODIS Reprojection Tool (MRT)
#-------------------------------------------

!INCLUDE ../nmake.opt

LDFLAGS = $(HDFLIB)
CP = copy
MV = move
RM = del

#--------------------------
# Define the include files:
#--------------------------
INC = append_meta.h

#-----------------------------------------
# Define the source code and object files:
#-----------------------------------------
SRC	= \
	append_meta.c

OBJ = $(SRC:.c=.obj)

#-----------------------------
# Define the object libraries:
#-----------------------------
HDFLIB = $(LIBDIR)/libmfhdf.lib $(LIBDIR)/libdf.lib $(LIBDIR)/libjpeg.lib $(LIBDIR)/libz.lib $(LIBDIR)/libsz.lib

#-----------------------
# Define the executable:
#-----------------------
EXE = append_meta.exe

#-----------------------------
# Targets for each executable:
#-----------------------------
all: $(EXE)

$(EXE): $(OBJ) $(INC)
	$(CC) $(CFLAGS) $(SRC) $(EXTRA_OBJ) $(LDFLAGS)

install:
	$(MV) $(EXE) ../bin

clean:
	-$(RM) $(OBJ) *.pdb *.ilk *.idb $(EXE)

copy-makefile:
	-@if NOT EXIST Makefile.orig $(CP) Makefile Makefile.orig
	$(CP) Makefile.$(CPMAKEFILEEXT) Makefile

