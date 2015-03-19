""" This file contains the main code for parsing HURDAT2 csv style data.
"""

def get_storms(filename):
    """ Parse file and return a list of storms. """
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

    return storms

def is_header_line(line):
    """ Check if the line is a header line. """
    # TODO FIXME: This is a rather rash assumption for a header line.
    if len(line.split(',')) == 4:
        return True
    else:
        return False

def get_lines(filename):
    with open(filename, 'rb') as f:
        return f.readlines()

def header_line_to_dict(header_string, stripe=True):
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
    if stripe:
        header_dict = {k: str.strip(v) for k, v in header_dict.items()}

    return header_dict

def data_line_to_dict(data_string, strip=True):
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

    return data_dict
