import gpxpy
import pyproj
import math
from datetime import datetime

flag = "cratectf{vi_vill_alla_vandra_till_cirkeln_i_bosarp}"

# Length in meters!
length_zero = 399.2
length_one = 400.8

# center point, church in bösarp
lat_base = 55.411893
long_base = 13.263022

bits = (''.join(format(ord(i),'b').zfill(7) for i in flag).strip(" "))
#'01100100110000011001001100001100011111010011001101111011110111011011111011111111001011011111110101110111011001001011111110001111010011110010110001111011001100101111001110111111100001110011011101001100101111001010111111100001110110011011001111101'
angle_between_points = 2*math.pi/len(bits)

points = []

AEQD = pyproj.Proj(proj='aeqd', lat_0=lat_base, lon_0=long_base, x_0=0, y_0=0)
WGS84 = pyproj.Proj(init='epsg:4326')

start = datetime(2021, 10, 8, 16, 23, 12).timestamp()

for i in range(len(bits)):
    point = bits[i]
    if point == '0':
        x = length_zero * math.cos(i * angle_between_points)
        y = length_zero * math.sin(i * angle_between_points)
    elif point == '1':
        x = length_one * math.cos(i * angle_between_points)
        y = length_one * math.sin(i * angle_between_points)
    else:
        assert(1)
    y_wgs, x_wgs = pyproj.transform(AEQD, WGS84, y, x)
    points.append((x_wgs, y_wgs, start + i * 7))

gpx = gpxpy.gpx.GPX()

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

# Create points:
for point in points:
    gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(point[0], point[1], None, datetime.fromtimestamp(point[2])))

print(gpx.to_xml())


