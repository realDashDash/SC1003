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
image_pixels =[B, B, B, B, B, B, B, B,
               B, B, B, Y, B, B, B, B,
               B, B, Y, Y, Y, B, B, B,
               B, Y, B, Y, B, Y, B, B,
               B, B, B, Y, B, B, B, B,
               B, B, B, B, Y, B, B, B,
               B, B, B, Y, B, B, B, B, 
               B, B, B, B, B, B, B, G]
raspi = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
heart = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
question_mark = [
O, O, O, R, R, O, O, O,
O, O, R, O, O, R, O, O,
O, O, O, O, O, R, O, O,
O, O, O, O, R, O, O, O,
O, O, O, R, O, O, O, O,
O, O, O, R, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, R, O, O, O, O
]

image = [image_pixels, raspi, heart, question_mark]
counter = 0
while(True):
    sense.set_pixels(image[counter % 4])
    time.sleep(1)
    counter += 1
