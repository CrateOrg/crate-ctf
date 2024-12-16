.PHONY: all clean

all: flag.txt
	echo "Oraklet har talat - du är en padda!" | python3 docker/generate_message.py > docker/messages.txt
	echo "" >> docker/messages.txt
	echo "Nästa meddelande kommer att vara väldigt spännande!" | python3 docker/generate_message.py >> docker/messages.txt
	echo "" >> docker/messages.txt
	for i in {1..2}; do cat flag.txt | tr --delete '\n'; done | python3 docker/generate_message.py >> docker/messages.txt

clean:
	rm -f docker/messages.txt
