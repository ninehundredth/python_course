#!/usr/bin/env python
stars_list = {
    "Sirius": 9940,
    "Altair": 7700,
    "Algol": 7500,
    "Aldebaran": 3910,
    "Arcturus": 4286,
    "Betelgeuse": 3500,
    "Sun": 5772,
    "Pollux": 4865,
    "Fomalhaut": 8590,
    "Vega": 9602,
    "Rigel": 11000,
    "Antares": 18500,
    "Canopus": 7350,
    "Deneb": 8525,
    "Capella": 3700,
    "Epsilon Pegasi": 4379,
    "Bellatrix": 22000,
    "Gamma Draconis": 3930,
    "Alpha Cassiopeiae": 4530
}
output = {"Red": [], "Orange": [], "Yellow": [], "White": [], "Blue": []}

def identify_colour(temperature):
    """switcher dictionary contains temperature-colour correspondence
    only one key takes bool True value, the rest keys are False
    thus, function references the True key and returns its value - the colour string"""
    switcher = {
        (800 <= temperature <= 3500): "Red",
        (3500 < temperature < 5000): "Orange",
        (5000 <= temperature <= 6000): "Yellow",
        (6000 < temperature < 9500): "White",
        (9500 <= temperature): "Blue"
    }
    return switcher.get(True, "Unknown")


def crier(output: dict):
    """takes dictionary of type
    colour: stars list
    and formats it to
    colour: stars list separated by commas
    while skipping keys (colours) which don't have any values (stars)"""
    for colour in output.keys():
        if output[colour]:
            print(colour + ': ' + ", ".join(output[colour]))


for star, temperature in stars_list.items():
    colour = identify_colour(temperature)
    output[colour].append(star)
crier(output)
