""" This file contains the main code for parsing HURDAT2 csv style data.
"""

def get_storms(filename):
    """ Parse file and return a list of storms.

        A storm is a dictionary containing a header dictionary and
        data dictionary.
    """
    lines = get_lines(filename)

    storms = []
    curr_storm = None
    for line in lines:
        if is_header_line(line):
            # When we get a data line, push the current storm and start again.
            storms.append(curr_storm)
            curr_storm = dict(header=header_line_to_dict(line), data=[])
        else:
            curr_storm['data'].append(data_line_to_dict(line))

    # FIXME: Being lazy and removing the first None list index.
    storms = storms[1:]

    return storms

def is_header_line(line):
    """ Check if the line is a header line."""
    # TODO FIXME: This is a rather rash assumption for a header line.
    if len(line.split(',')) == 4:
        return True
    else:
        return False

def get_lines(filename):
    with open(filename, 'rb') as f:
        return f.readlines()

def header_line_to_dict(header_string, strip=True, typed=True):
    """ Returns dictionary form from a string.

        Args:
            data_string (string): String in HURDAT2 data line format.
            strip (bool, optional): Wether to strip whitespace of values.
                HURDAT specifies data as a range of characters,
                whitespace and all. Typically said whitespace isn't usefull
                so we strip it by default.

        TODO: Possibly in the feature we can also type data here.
              As opposed to everything being a string.
    """
    hs = header_string
    # Yeah, we typically don't advise this indentation style...
    # But it makes it clearer and HURDAT is special.
    header_dict = {}
    header_dict["basin"] =          hs[0:2]
    header_dict["number_in_year"] = hs[2:4]
    header_dict["year"] =           hs[4:8]
    header_dict["name"] =           hs[18:28]
    header_dict["number_of_rows"] = hs[33:36]

    # Strip if necessary.
    if strip:
        header_dict = {k: str.strip(v) for k, v in header_dict.items()}

    # FIXME: I feel like this is horribly hardcoded.
    if typed:
        header_dict["basin"] = str(header_dict["basin"])
        header_dict["number_in_year"] = int(header_dict["number_in_year"])
        header_dict["year"] = int(header_dict["year"])
        header_dict["name"] = str(header_dict["name"])
        header_dict["number_of_rows"] = int(header_dict["number_of_rows"])

    return header_dict

def data_line_to_dict(data_string, strip=True, typed=True):
    """ Returns dictionary form from a string.

        Args:
            data_string (string): String in HURDAT2 data line format.
            strip (bool, optional): Wether to strip whitespace of values.
                HURDAT specifies data as a range of characters,
                whitespace and all. Typically said whitespace isn't usefull
                so we strip it by default.

        TODO: Possibly in the feature we can also type data here.
              As opposed to everything being a string.
    """
    ds = data_string

    # Yeah, we typically don't advise this indentation style...
    # But it makes it clearer and HURDAT is special.
    data_dict = {}
    data_dict["year"] = ds[0:4]
    data_dict["month"] = ds[4:6]
    data_dict["day"] = ds[6:8]
    data_dict["hour"] = ds[10:12]
    data_dict["minutes"] = ds[12:14]
    data_dict["identifier"] = ds[16]
    data_dict["status"] = ds[19:21]
    data_dict["latitude"] = ds[23:27]
    data_dict["latitude_hemisphere"] = ds[27]
    data_dict["longitude"] = ds[30:35]
    data_dict["longitude_hemisphere"] = ds[35]
    data_dict["maximum_sustained_wind"] = ds[38:41]
    data_dict["minimum_pressure"] = ds[43:47]

    # Strip if necessary.
    if strip:
        data_dict = {k: str.strip(v) for k, v in data_dict.items()}

    if typed:
        data_dict["year"] = int(data_dict["year"])
        data_dict["month"] = int(data_dict["month"])
        data_dict["day"] = int(data_dict["day"])
        data_dict["hour"] = int(data_dict["hour"])
        data_dict["minutes"] = int(data_dict["minutes"])
        data_dict["identifier"] = str(data_dict["identifier"])
        data_dict["status"] = str(data_dict["status"])
        data_dict["latitude"] = float(data_dict["latitude"])
        data_dict["latitude_hemisphere"] = str(data_dict["latitude_hemisphere"])
        data_dict["longitude"] = float(data_dict["longitude"])
        data_dict["longitude_hemisphere"] = str(data_dict["longitude_hemisphere"])
        data_dict["maximum_sustained_wind"] = int(data_dict["maximum_sustained_wind"])
        data_dict["minimum_pressure"] = int(data_dict["minimum_pressure"])

    return data_dict
