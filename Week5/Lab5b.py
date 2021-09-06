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

def image_pixels(X):
    image = [O, O, O, O, O, O, O, O,
             O, O, O, X, O, O, O, O,
             O, O, X, X, X, O, O, O,
             O, X, O, X, O, X, O, O,
             O, O, O, X, O, O, O, O,
             O, O, O, X, O, O, O, O,
             O, O, O, X, O, O, O, O, 
             O, O, O, O, O, O, O, O]
    return image
    
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

def question_mark(X):
    img = [
        O, O, O, X, X, O, O, O,
        O, O, X, O, O, X, O, O,
        O, O, O, O, O, X, O, O,
        O, O, O, O, X, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, X, O, O, O, O]
    return img

def clear():
  for i in range(8):
    for j in range(8):
      sense.set_pixel(i, j, (0, 0, 0))
      
colors = [G, Y, B, R, P]
image = [image_pixels, heart, question_mark]
counter = 0

while(True):
    clear()
    sense.set_rotation(90*randint(0, 3))
    sense.set_pixels(image[counter % 3](colors[randint(0, 4)]))
    time.sleep(1)
    counter += 1
