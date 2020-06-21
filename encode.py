"""
Functions for encoding/decoding an input string. Code taken directly from
https://hypothesis.readthedocs.io/en/latest/quickstart.html which slightly 
modifies code from the Rosetta Code Wiki.
"""

def encode(input_string):
    if not input_string:
        return []

    count = 1
    prev = ""
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    entry = (character, count)
    lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q