from sense_hat import SenseHat
from random import randint
import time
sense = SenseHat()

acceleration = sense.get_accelerometer_raw()
x = round(acceleration['x'], 1)
y = round(acceleration['y'], 1)
z = acceleration['z']
while True:
    print(x, y, sep = '\t')
    time.sleep(0.75)
