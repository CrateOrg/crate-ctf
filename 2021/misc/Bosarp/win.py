from math import sin, cos, sqrt, atan2, radians
import re

data = []
with open("track.gpx") as f:
    data = f.readlines()

#  clat = 55.411893
#  clon = 13.263022
clat = 55.41189
clon = 13.26302

distances = []
for line in data:
    if "lat" in line and "lon" in line:
        lat, lon = re.findall('"([^"]*)"', line)
        lat = float(lat)
        lon = float(lon)

        # https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
        R = 6373.0
        lat1 = radians(clat)
        lon1 = radians(clon)
        lat2 = radians(lat)
        lon2 = radians(lon)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c

        distances.append(distance)


average = sum(distances)/len(distances)
print("Number of distances:", len(distances))
print("Average:", average)

answer = ""
for distance in distances:
    if distance <= average:
        answer += "0"
    else:
        answer += "1"

for i in range(0, len(answer), 7):
    chunk = answer[i:i+7]
    print(chr(int(chunk, 2)), end="")
print()
