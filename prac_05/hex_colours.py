"""
Prac 05 - Hex Colours

"""

HEX_COLOURS = {"ALICEBLUE": "#f0f8ff", "CADETBLUE": "#5f9ea0", "CHOCOLATE": "#d2691e", "DARKSLATEGREY": "#2f4f4f",
               "FIREBRICK": "#b22222", "HOTPINK": "#ff69b4", "LAVENDER": "#e6e6fa", "LINEN": "#faf0e6",
               "MAGENTA": "#ff00ff"}

colour = input("Please enter a colour name >").upper()

while colour != "":
    if colour in HEX_COLOURS:
        print("{}'s colour code is {}.".format(colour, HEX_COLOURS[colour]))
    else:
        print("We don't have that colour")

    colour = input("Please enter a colour name >").upper()
