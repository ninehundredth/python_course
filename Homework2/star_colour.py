#!/usr/bin/env python
def import_temperature():
    # function purpose is fool proof
    try:
        temperature = int(input("What's the star's temperature? "))
    except KeyboardInterrupt:
        print("Cancelled, exiting...")
        # temperature = 0
        # in this exception var temperature might be referenced before the assignment
        # therefore added this useless assignment
        exit()
    except ValueError:
        print("Wrong input, enter integer numbers only")
        temperature = import_temperature()
    return temperature


def identify_colour(temperature):
    # switcher dictionary contains temperature-colour correspondence
    # only one key takes bool True value, the rest keys are False
    # thus, function references the True key and returns its value - the colour string
    switcher = {
        (800 <= temperature < 3500): "Red",
        (3500 <= temperature < 5000): "Orange",
        (5000 <= temperature <= 6000): "Yellow",
        (6000 < temperature < 9500): "White",
        (9500 <= temperature): "Blue"
    }
    return switcher.get(True, "Unknown")


resume: str = ""
# This is used when user wants to run the program several times
while not resume == "n":
    temperature = import_temperature()
    colour = identify_colour(temperature)
    print("The colour of the star is {}".format(colour))
    resume = input("Again (y/n)? ")
