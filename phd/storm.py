""" Functions for storms.

    So instead of creating storms as objects and such we are going to do
    things in a more functional way and just create a library of functions.
"""


def maximum_wind_speed(storm):
    """ Return max wind speed our of all data lines """
    max_speed = 0
    for data_line in storm['data']:
        if data_line["maximum_sustained_wind"] > max_speed:
            max_speed = data_line["maximum_sustained_wind"]
    return max_speed


def made_landfall(storm):
    """ Returns bool of whether of not the storm made landfall at any point. """
    for data_line in storm["data"]:
        if 'L' in data_line["identifier"]:
            return True
    return False


def name(storm):
    return storm['header']['name']


def has_name(storm):
    return "UNNAMED" == name(storm)


def year(storm):
    return storm['header']['year']
