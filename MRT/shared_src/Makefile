#-------------------------------------------
# Makefile for MODIS Reprojection Tool (MRT)
#-------------------------------------------

!INCLUDE ../nmake.opt

OPTFLAGS = $(OPTFLAGS) -D "_LIB"

ARCHIVE =	libmrt.lib
INCS =	 	$(INCS) -I../gctp -I../geolib
CP = 		copy
RM =		del

#--------------------------
# Define the include files:
#--------------------------
INC	 =\
	 mrt_error.h loc_prot.h loc_prot_mosaic.h \
	 shared_mosaic.h shared_resample.h

#-----------------------------------------
# Define the source code and object files:
#-----------------------------------------
SRC	= \
        abortex.c fileoc.c init_md.c proc_arg.c space2us.c addmeta.c \
	gctp_call.c initfile.c projutil.c struplow.c addmeta_mosaic.c \
	hdf_init.c logh.c rb_io.c tif_init.c mrt_error.c \
	hdf_init_mosaic.c modproj.c rb_oc.c tif_io.c filebuf.c \
	hdf_io.c msgh.c rdhdfhdr.c tif_oc.c filedesc.c hdf_oc.c \
	print_md.c read_hdr.c writ_hdr.c fileio.c hdf_oc_mosaic.c \
	print_proj.c read_prm.c usage.c

OBJ =	$(SRC:.c=.obj)

#-------------------------------
# Rules for building the archive
#-------------------------------
$(ARCHIVE): $(OBJ) $(INC)
	$(AR) /out:$(ARCHIVE) $(OBJ)

all:	$(ARCHIVE)

install:
#	mv $(ARCHIVE) ../lib

clean:
	-$(RM) $(OBJ) *.ilk *.pdb *.idb $(ARCHIVE)

copy-makefile:
	-@if NOT EXIST Makefile.orig $(CP) Makefile Makefile.orig
	$(CP) Makefile.$(CPMAKEFILEEXT) Makefile

