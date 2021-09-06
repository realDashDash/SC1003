from sense_hat import SenseHat
from random import randint
import time
sense = SenseHat()

G = (0, 255, 0)
Y = (255, 255, 0)
B = (0, 0, 255)
R = (255, 0, 0)
W = (255,255,255)
O = (0,0,0)
P = (255,105, 180)

def heart(X):
    img = [
        O, O, O, O, O, O, O, O,
        O, X, X, O, X, X, O, O,
        X, X, X, X, X, X, X, O,
        X, X, X, X, X, X, X, O,
        O, X, X, X, X, X, O, O,
        O, O, X, X, X, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, O, O, O, O, O,]
    return img

def clear():
  for i in range(8):
    for j in range(8):
      sense.set_pixel(i, j, (0, 0, 0))
      
colors = [G, Y, B, R, P]
counter = 0
sense.set_rotation(0)
while(True):
    clear()
    sense.set_pixels(heart(colors[randint(0, 4)]))
    time.sleep(1)
    counter += 1
