import sys
fil = str(sys.argv[1])
f = open(fil, "r")
ingredienser = []
for line in f:
    for word in line.split(','):
        if "\"Title\":\"" in word:
            word = word.split("\"")
            namn = word[3]
        if "\"CookingTimeAbbreviated\":\"" in word:
            word = word.split("\"")
            tid = word[3]
        if "\"Ingredient\":\"" in word:
            word = word.split("\"")
            if word[3] not in ingredienser:
                ingredienser.append(word[3])

print("{\"namn\":\""+namn+"\",\"tid\":\""+tid+"\",\"ingredienser\":"+str(ingredienser).replace ("'", "\"")+"}")
f.close()
