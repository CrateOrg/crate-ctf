import struct
import math
import turtle

file2 = open( "/dev/input/mice", "rb" )
file = open("data.bin", 'rb')

def turtleRender(dx, dy, bLeft):
    if bLeft:
        turtle.pd()
    else:
        turtle.pu()
    turtle.radians()
    angle = 3.14/2
    distance = abs(complex(dx, dy))
    if dx == 0:
        if dy < 0:
            angle = -(3.14/2)

    else:
        angle = math.atan(dy/dx)
        if dx < 0:
            angle += 3.14
    turtle.setheading(angle)
    turtle.fd(distance/2)
    print(angle)
def getMouseEvent():
    buf = file.read(3)
    button = buf[0]
    bLeft = button & 0x1
    bMiddle = ( button & 0x4 ) > 0
    bRight = ( button & 0x2 ) > 0
    x,y = struct.unpack( "bb", buf[1:] )
    print ("L:%d, M: %d, R: %d, x: %d, y: %d\n" % (bLeft,bMiddle,bRight, x, y) )
    turtleRender(x,y, bLeft)
    #file2.write(buf)
while( 1 ):
  getMouseEvent()
file.close()
file2.close()
