#-------------------------------------------
# Makefile for MODIS Reprojection Tool (MRT)
#-------------------------------------------

!INCLUDE ../nmake.opt

LDFLAGS = $(HDFLIB)
MV = move
CP = copy
RM = del

#--------------------------
# Define the include files:
#--------------------------
INC =

#-----------------------------------------
# Define the source code and object files:
#-----------------------------------------
SRC	= \
	dumpmeta.c

OBJ = $(SRC:.c=.obj)

#-----------------------------
# Define the object libraries:
#-----------------------------
HDFLIB = $(LIBDIR)/libmfhdf.lib $(LIBDIR)/libdf.lib $(LIBDIR)/libjpeg.lib $(LIBDIR)/libz.lib $(LIBDIR)/libsz.lib

#-----------------------
# Define the executable:
#-----------------------
EXE = dumpmeta.exe

#-----------------------------
# Targets for each executable:
#-----------------------------
all: $(EXE)

$(EXE): $(OBJ) $(INC)
	$(CC) $(CFLAGS) $(OBJ)$(EXTRA_OBJ) $(LDFLAGS)

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

.c.o:
	$(CC) $(CFLAGS) $(INCS) -c $<

