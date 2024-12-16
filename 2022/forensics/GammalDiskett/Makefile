all:
	mkfs.msdos -M 0xF0 -n CTFDISK -C floppy.img 1440
	cat flag.txt | gifecho > files/FLAG.GIF
	touch -a -m -t 199612180132.05 files/*
	touch -a -m -t 199612180132.05 files/PHRACK49/*
	mcopy -sm -i floppy.img files/* ::
	mdel -i floppy.img FLAG.GIF

clean:
	rm floppy.img
