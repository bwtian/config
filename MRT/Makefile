# Makefile for MS Visual C compilers.
#

!INCLUDE nmake.opt

CP = copy

all:	append_meta hdf2rb resample update_tile_meta dumpmeta hdflist sdslist mrtmosaic fcgtiff gtiff_composite revendian

shared_src::
	cd shared_src
	$(MAKE)
	cd ..

gctp::
	cd gctp
	$(MAKE)
	cd ..

geolib::
	cd geolib
	$(MAKE)
	cd ..

append_meta::
	cd append_meta
	$(MAKE)
	cd ..

hdf2rb: shared_src gctp geolib
	cd hdf2rb
	$(MAKE)
	cd ..

resample: shared_src gctp geolib
	cd resample
	$(MAKE)
	cd ..

update_tile_meta::
	cd update_tile_meta
	$(MAKE)
	cd ..

dumpmeta::
	cd dumpmeta
	$(MAKE)
	cd ..

hdflist::
	cd hdflist
	$(MAKE)
	cd ..

sdslist::
	cd sdslist
	$(MAKE)
	cd ..

mrtmosaic: shared_src gctp geolib
	cd mrtmosaic
	$(MAKE)
	cd ..

fcgtiff::
	cd fcgtiff
	$(MAKE)
	cd ..

gtiff_composite::
	cd gtiff_composite
	$(MAKE)
	cd ..

revendian: shared_src
	cd revendian
	$(MAKE)
	cd ..

clean:
	cd shared_src
	$(MAKE) clean
	cd ..
	cd gctp
	$(MAKE) clean
	cd ..
	cd geolib
	$(MAKE) clean
	cd ..
	cd append_meta
	$(MAKE) clean
	cd ..
	cd hdf2rb
	$(MAKE) clean
	cd ..
	cd resample
	$(MAKE) clean
	cd ..
	cd update_tile_meta
	$(MAKE) clean
	cd ..
	cd dumpmeta
	$(MAKE) clean
	cd ..
	cd hdflist
	$(MAKE) clean
	cd ..
	cd sdslist
	$(MAKE) clean
	cd ..
	cd mrtmosaic
	$(MAKE) clean
	cd ..
	cd fcgtiff
	$(MAKE) clean
	cd ..
	cd gtiff_composite
	$(MAKE) clean
	cd ..
	cd revendian
	$(MAKE) clean
	cd ..

install:
	cd shared_src
	$(MAKE) install
	cd ..
	cd gctp
	$(MAKE) install
	cd ..
	cd geolib
	$(MAKE) install
	cd ..
	cd append_meta
	$(MAKE) install
	cd ..
	cd hdf2rb
	$(MAKE) install
	cd ..
	cd resample
	$(MAKE) install
	cd ..
	cd update_tile_meta
	$(MAKE) install
	cd ..
	cd dumpmeta
	$(MAKE) install
	cd ..
	cd hdflist
	$(MAKE) install
	cd ..
	cd sdslist
	$(MAKE) install
	cd ..
	cd mrtmosaic
	$(MAKE) install
	cd ..
	cd fcgtiff
	$(MAKE) install
	cd ..
	cd gtiff_composite
	$(MAKE) install
	cd ..
	cd revendian
	$(MAKE) install
	cd ..

copy-makefile:
	cd shared_src
	$(MAKE) -f Makefile.win CPMAKEFILEEXT=$(CPMAKEFILEEXT) copy-makefile
	cd ..
	cd gctp
	$(MAKE) -f Makefile.win CPMAKEFILEEXT=$(CPMAKEFILEEXT) copy-makefile
	cd ..
	cd geolib
	$(MAKE) -f Makefile.win CPMAKEFILEEXT=$(CPMAKEFILEEXT) copy-makefile
	cd ..
	cd append_meta
	$(MAKE) -f Makefile.win CPMAKEFILEEXT=$(CPMAKEFILEEXT) copy-makefile
	cd ..
	cd hdf2rb
	$(MAKE) -f Makefile.win CPMAKEFILEEXT=$(CPMAKEFILEEXT) copy-makefile
	cd ..
	cd hdflist
	$(MAKE) -f Makefile.win CPMAKEFILEEXT=$(CPMAKEFILEEXT) copy-makefile
	cd ..
	cd resample
	$(MAKE) -f Makefile.win CPMAKEFILEEXT=$(CPMAKEFILEEXT) copy-makefile
	cd ..
	cd update_tile_meta
	$(MAKE) -f Makefile.win CPMAKEFILEEXT=$(CPMAKEFILEEXT) copy-makefile
	cd ..
	cd dumpmeta
	$(MAKE) -f Makefile.win CPMAKEFILEEXT=$(CPMAKEFILEEXT) copy-makefile
	cd ..
	cd sdslist
	$(MAKE) -f Makefile.win CPMAKEFILEEXT=$(CPMAKEFILEEXT) copy-makefile
	cd ..
	cd mrtmosaic
	$(MAKE) -f Makefile.win CPMAKEFILEEXT=$(CPMAKEFILEEXT) copy-makefile
	cd ..
	cd fcgtiff
	$(MAKE) -f Makefile.win CPMAKEFILEEXT=$(CPMAKEFILEEXT) copy-makefile
	cd ..
	cd gtiff_composite
	$(MAKE) -f Makefile.win CPMAKEFILEEXT=$(CPMAKEFILEEXT) copy-makefile
	cd ..
	cd revendian
	$(MAKE) -f Makefile.win CPMAKEFILEEXT=$(CPMAKEFILEEXT) copy-makefile
	cd ..
	

