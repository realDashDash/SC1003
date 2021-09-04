from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

def randCol():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def clear():
  for i in range(8):
    for j in range(8):
      sense.set_pixel(i, j, (0, 0, 0))

clear()
sense.set_pixel(0, 0, randCol())
sense.set_pixel(0, 7, randCol())
sense.set_pixel(7, 0, randCol())
sense.set_pixel(7, 7, randCol())

while (True):
  clear()
  sense.set_pixel(randint(0, 7), randint(0, 7), randCol())
  sense.set_pixel(randint(0, 7), randint(0, 7), randCol())
  sense.set_pixel(randint(0, 7), randint(0, 7), randCol())
  sense.set_pixel(randint(0, 7), randint(0, 7), randCol())
  time.sleep(1)
  
