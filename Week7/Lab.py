
from sense_hat import SenseHat
from random import randint
import time
sense = SenseHat()


# Get orientation
def get_ori():
    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']
    print("pitch {0} roll {1}".format(round(pitch,0), round(roll,0)))
    return round(pitch, 0), round(roll, 0)

# Dislay Settings
w = (255, 255, 255) # white
b = (0, 0, 0) # black
r = (255, 0, 0)
g = (0, 255, 0)

# Sample board
# board = [[r,r,r,r,r,r,r,r],
#         [r,b,b,b,b,b,b,r],
#         [r,b,b,b,b,b,b,r],
#         [r,b,b,b,b,b,b,r],
#         [r,b,b,b,b,b,b,r],
#         [r,b,b,b,b,b,b,r],
#         [r,b,b,b,b,b,b,r],
#         [r,r,r,r,r,r,r,r] ]
# Self-defined board
board = [[r,r,r,r,b,b,b,r],
        [r,b,b,b,b,b,b,r],
        [b,b,b,b,r,r,r,r],
        [r,r,b,b,r,b,b,r],
        [r,b,b,b,b,b,b,b],
        [r,b,b,r,b,b,b,b],
        [r,b,b,r,b,b,b,r],
        [r,r,r,r,r,r,r,r] ]
        
    
# Dislay Board and marble:
def display_board(board, x, y):
    new_board = board
    new_board[y][x] = w #marble position
    board_1d = sum(new_board, [])
#    print(board_1d)
    sense.set_pixels(board_1d)

# Check if the marble hit the wall
def check_wall(x, y, new_x, new_y):
    if board[new_y][new_x] != r:
        return new_x, new_y
    elif board[new_y][x] != r:
        return x, new_y
    elif board[y][new_x] != r:
        return new_x, y
    else:
        return x, y

# Moving the marble
def move_marble(pitch, roll, x, y):
    new_x = x #assume no change to start with
    new_y = y #assume no change to start with

    if 1 < pitch < 179 and x != 0:
        new_x -= 1 # move left
    elif 359 > pitch > 179 and x != 7:
        new_x += 1 # move right

    if 1 < roll < 179 and y != 7:
        new_y += 1 # move up
    elif 359 > roll > 179 and y != 0:
        new_y -= 1 # move down

    new_x, new_y = check_wall(x, y, new_x, new_y)
    return new_x, new_y

def Game():
    game_over = False
    
    # Base positon of the marble
    x = 1
    y = 1
    
    # set target
    tar = True
    while(tar):
        tar_x = randint(0, 7)
        tar_y = randint(0, 7)
        if  board[tar_y][tar_x] != r:
            board[tar_y][tar_x] = g
            tar = False
        else:
            pass

    while (not game_over):
        pitch, roll = get_ori()
        x, y = move_marble(pitch, roll, x, y)
        new_board = board
        new_board[y][x] = w #marble position
        board_1d = sum(new_board, [])
        sense.set_pixels(board_1d)
        if x == tar_x and y == tar_y:
            game_over = True
        else:
            new_board[y][x] = b
        time.sleep(0.02)
    else:
        sense.set_rotation(180)
        sense.show_message("Yay!")
    
if __name__ == "__main__":
    Game()
