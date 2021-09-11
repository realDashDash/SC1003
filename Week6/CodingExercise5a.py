# from sense_hat import SenseHat
# sense = SenseHat()
# sense.set_rotation(180)

def get_color(color_name):
    ''' Function: input the value of an expected color, and judge if it is approperiate
        Input: expected color name
        Output: if input is approperiate, return value; else return Null
    '''
    keep_looping = True
    error = 0
    while(keep_looping):
        color_str = input("Enter the value of the " + color_name + " color for message (0 to 255): ")
        try: 
            color_int = int(color_str)
            if (color_int >= 0 and color_int <= 255):
                return color_int
            else:
                error += 1
        except:
            error += 1
        if (error == 3):
            keep_looping = False
    else:
        print("You failed to many times!")
        return None

# r_int = get_color("red")
# g_int = get_color("green")
# b_int = get_color("blue")
# msg_color = (r_int, g_int, b_int)

# sense.show_message("I got it!", text_colour = msg_color)