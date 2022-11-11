# Create function that returns random color in hexadecimal format
# Create function that returns random tuple contain 3 ints, each int representing value of color as in RGB format
# Create function that will convert RGB into a hexadecimal string and vice versa

import random
def random_hex():
    random_number = random.randint(0,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    return hex_number

print(random_hex())

def random_color():
    levels = range(256)
    return tuple(random.choice(levels) for x in range(3))

print(random_color())