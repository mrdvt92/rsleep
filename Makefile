NAME	= rsleep
SPEC	= $(NAME).spec
VERSION	= $(shell sed -e '/Version:/!d' -e 's/[^0-9.]*\([0-9.]*\).*/\1/' $(SPEC))
SRCS	= rsleep.c rsleep.pod
AUX	= $(SPEC) Makefile
DISTDIR	= $(NAME)-$(VERSION)

all:	rsleep rsleep.1.gz

rsleep:	rsleep.c
	gcc -o rsleep rsleep.c

rsleep.1:	rsleep.pod
	pod2man rsleep.pod > rsleep.1

rsleep.1.gz:	rsleep.1
	gzip -c rsleep.1 > rsleep.1.gz

test:
	echo 3.3333
	/usr/bin/time --format="%e" ./rsleep -d 3.3333
	echo 0
	/usr/bin/time --format="%e" ./rsleep -d 0
	echo 0.1
	/usr/bin/time --format="%e" ./rsleep -d 0.1
	echo 5
	/usr/bin/time --format="%e" ./rsleep -d
	echo 5 quite
	/usr/bin/time --format="%e" ./rsleep
	echo 1 quite
	/usr/bin/time --format="%e" ./rsleep
	echo 0 quite
	/usr/bin/time --format="%e" ./rsleep 0.0

dist: $(SRCS) $(AUX)
	@echo "Prepare"
	-rm -rf $(DISTDIR)
	@echo "Creating folder $(DISTDIR)"
	mkdir $(DISTDIR)
	@echo "Hardlinking files for tarball"
	ln $(SRCS) $(AUX) $(DISTDIR)
	@echo "Creating tarball $(DISTDIR).tar.gz"
	tar chzfv $(DISTDIR).tar.gz $(DISTDIR)
	@echo "Cleaning up..."
	-rm -rf $(DISTDIR)
	@echo "Finished!"

$(DISTDIR).tar.gz:	dist

rpm:    $(DISTDIR).tar.gz
	rpmbuild -ta $(DISTDIR).tar.gz
