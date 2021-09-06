from sense_hat import SenseHat
from random import randint
import time
sense = SenseHat()

G = (0, 255, 0)
R = (255, 0, 0)
O = (0,0,0)

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

''' define:
    Up = 0, Right = 1, Down = 2, Left = 3
'''

def get_acc():
    acceleration = sense.get_accelerometer_raw()
    x = round(acceleration['x'], 1)
    y = round(acceleration['y'], 1)
    if (y > 0.8):
        return 0
    elif (y < -0.8):
        return 2
    elif (x < -0.8):
        return 1
    elif (x > 0.8):
        return 3
    else:
        return None

counter = 0
while (True):
    rotation = randint(0, 3)
    sense.set_rotation(90 * rotation)
    sense.set_pixels(image_pixels(G))

    time_end = time.time() + 1
    flag = False
    while (time.time() < time_end and flag == False):
        in_rot = get_acc()
        if (in_rot == rotation):
            flag = True
    else:
        if (flag == False):
            sense.set_pixels(image_pixels(R))
            time.sleep(0.5)
            sense.show_message("Lose")
            print("Score: ", counter)
            break
        else:
            counter += 1
            time.sleep(time_end - time.time())
        
