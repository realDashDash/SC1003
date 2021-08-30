from sense_hat import SenseHat
sense = SenseHat()

"""
# a) Basic Program Sttructure

# Display the message
sense.show_message("This is fun!")

# Change the orientation of the message by 180 degree
sense.set_rotation(180)
sense.show_message("This is fun!")

# Add the text colour parameter to message
sense.show_message("This is fun!", text_colour = (255, 255, 0))
sense.show_message("This is fun!", text_colour = (255, 0, 255))

# Change the background color of the message
sense.show_message("This is fun!", back_colour = (255, 0, 0))

# Change the speed of the display
sense.show_message("This is fun!", scroll_speed = 0.5)

print("Success!")
"""

"""
# b) Use of Variables

# Set parameters
color_msg = (255, 0, 255)
color_bg = (0, 0, 255)
speed = 0.5

# Display message
sense.show_message("I got it", text_colour = color_msg, back_colour = color_bg, scroll_speed = speed)
print("Success!")
"""

# c) Challenge -  Use of data types

# input rgb channels
msg_r = int(input("Enter red channel of the message: "))
msg_g = int(input("Enter green channel of the message: "))
msg_b = int(input("Enter blue channel of the message: "))

bg_r = int(input("Enter red channel of the background: "))
bg_g = int(input("Enter green channel of the background: "))
bg_b = int(input("Enter blue channel of the background: "))

color_msg = (msg_r, msg_g, msg_b)
color_bg = (bg_r, bg_g, bg_b)

speed = float(input("Enter the scroll speed: "))

# Display message
sense.show_message("I got it", text_colour = color_msg, back_colour = color_bg, scroll_speed = speed)
print("Success!")
