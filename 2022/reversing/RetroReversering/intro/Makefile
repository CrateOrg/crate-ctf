CC = lcc -Wa-l -Wl-m -Wl-j
AS = lcc -Wa-l -Wl-m -Wl-j

TARGET = intro.gb
OBJS = intro.o music/output.o music/gbt_player.o music/gbt_player_bank1.o

all: $(TARGET)

%.o: %.s
	$(AS) -c -o $@ $<

%.o: %.c
	$(CC) -c -o $@ $<

$(TARGET): $(OBJS)
	$(CC) -o $(TARGET) -Wl-yt1 -Wl-yo4 -Wl-ya0 $(OBJS)

clean:
	rm -rf $(TARGET) $(OBJS) *.asm *.ihx *.lst *.noi *.map *.sym music/*.sym music/*.map music/*.lst music/*.asm *~
