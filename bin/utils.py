import json
import re

def write_json(data, out, indent=2): 

    encoded = json.JSONEncoder(indent=indent)
    encoded = encoded.iterencode(data)

    float_pat = re.compile(r'^-?\d+\.\d+$')

    for atom in encoded:
        if float_pat.match(atom):
            out.write('%.6f' % float(atom))
        else:
            out.write(atom)

def woeid2path(id):

    tmp = str(id)
    parts = []

    while len(tmp) > 3:
        parts.append(tmp[0:3])
        tmp = tmp[3:]

    if len(tmp):
        parts.append(tmp)

    return "/".join(parts)

def scrub_placetype(type):
    type = type.lower()
    type = type.replace(" ", "-")
    return type


