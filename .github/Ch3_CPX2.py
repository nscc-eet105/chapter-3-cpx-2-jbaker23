#My name is Jacob Baker and this is Chapter 3 CPX 2 and I completed this on June 23

from adafruit_circuitplayground import cp
import time

num_pixels = 10
#total lights on CPX
BLACK = (0, 0, 0)

while True:
    for num in range(0, 10, 1):
        #this is going forwards
        cp.pixels.fill(BLACK)

        cp.pixels[num] = (255, 0, 255)
        #RGB
        time.sleep(0.1)

    for num in range(9, -1, -1):
        #this is going backwards
        cp.pixels.fill(BLACK)

        cp.pixels[num] = (255, 255, 0)

        time.sleep(0.05)
