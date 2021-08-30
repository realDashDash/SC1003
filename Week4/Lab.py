from sense_hat import SenseHat
sense = SenseHat()
    
def getSpeed():
    error_counter = 0
    while   (error_counter < 3):
        try:
            speed = float(input("Enter the scroll speed: "))
            return speed
        except:
            error_counter += 1
            print("Enter numbers only. (", error_counter, ")")
    else:
        print("You have exceeded the number of trials allowed. Bye!")
        return -1
    
def getColor(colorName, name):
    error_counter = 0
    while (error_counter < 3):
        try:
            prompt = "Enter " + colorName + " channel of the " + name + ": "
            color = int(input(prompt))
            if (color > 255 or color < 0):
                error_counter += 1
                print("Enter numbers only. (", error_counter, ")")
            else:
                return color
                break
        except:
            error_counter += 1
            print("Enter numbers only. (", error_counter, ")")
    else:
        print("You have exceeded the number of trials allowed. Bye!")
        return -1

colors = ["red", "green", "blue"]
flag = True
msg_colors = []
bg_colors = []
if flag:
    for color in colors:
        temp = getColor(color, "message")
        if temp == -1:
            flag = False
            break
        else:
            msg_colors.append(temp) 
if flag:
    for color in colors:
        temp = getColor(color, "background")
        if temp == -1:
            flag = False
            break
        else:
            bg_colors.append(temp) 
if flag:
    temp = getSpeed()
    if temp == -1:
        flag = False
    else:
        speed = temp
    
if flag:
    color_msg = (msg_colors[0], msg_colors[1], msg_colors[2])
    color_bg = (bg_colors[0], bg_colors[1], bg_colors[2])
    
    # Display message
    sense.show_message("This is fun!", text_colour = color_msg, back_colour = color_bg, scroll_speed = speed)
