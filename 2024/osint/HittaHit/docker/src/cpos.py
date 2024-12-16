import sys
import json
import os
import random
import string
from datetime import datetime
from geopy.distance import great_circle
from geopy.point import Point

# Position to look for
# Gamla Kyrkogården
#facit = Point('58°23\'32.5"N 11°30\'06.9"E')
# Ernst i svängen
facit = Point('58°23\'15.5"N 11°30\'53.5"E')
flag = 'cratectf{En_av_orterna_är_större}'

result = {
}

def main():
    if len(sys.argv) != 2:
        result["error"] = "Unexpected error!"
        print(json.dumps(result, indent=4))
        sys.exit(2)

    try:
        pos = Point(sys.argv[1])
    except Exception as e:
        result["error"] = "Wrong format of position"
        print(json.dumps(result, indent=4))
        sys.exit(1)
    try:
        gcirc = great_circle(facit, pos).meters
        # result["length"] = gcirc
        
        if gcirc > 1000000.0:
            result["error"] = "Position is way off"
        elif gcirc > 10000.0:
            result["error"] = "Getting there"
        elif gcirc > 1000.0:
            result["error"] = "Getting closer"
        elif gcirc >10.0:
            result["error"] = "Getting real close now"
        else:
            result["output"] = flag
        
        print(json.dumps(result, indent=4))
    except Exception as e:
        result["error"] = "unexpected error!"
        print(json.dumps(result, indent=4))
        sys.exit(1)
    
if __name__ == "__main__":
    main()
