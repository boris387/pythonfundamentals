from pprint import pprint, pp

def pretty_display(pretty_list):
    for x in pretty_list:
        pprint(x)
    return pretty_list

pretty_list = (120000, 250000)

pretty_display(pretty_list)

