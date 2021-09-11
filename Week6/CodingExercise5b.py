from CodingExercise5a import get_color

flag = True
if (flag):
    r_int = get_color("red")
    if (r_int == None):
        flag = False
if (flag):
    g_int = get_color("green")
    if (g_int == None):
        flag = False
if (flag):
    b_int = get_color("blue")
    if (b_int == None):
        flag = False

if (flag):   
    msg_color = (r_int, g_int, b_int)

print(msg_color)
# sense.show_message("I got it!", text_colour = msg_color)