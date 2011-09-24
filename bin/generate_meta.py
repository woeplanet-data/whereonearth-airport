#!/usr/bin/env python

import pprint

import json
import os

countries = {}
iso_codes = {}

if __name__ == '__main__':

    # FIX ME

    airports = '../data'

    for root, dirs, files in os.walk(airports):

        for f in files:

            path = os.path.join(root, f)

            fh = open(path)
            data = json.load(fh)

            props = data['features'][0]['properties']

            this_woeid = props['woe:id']
            this_country = None

            if not props.get('hierarchy', False):
                continue

            for mt in props['hierarchy']:
                nspred, value = mt.split("=")

                if nspred == 'woe:country':
                    this_country = int(value)
                    break

            if not countries.get(this_country, False):
                countries[this_country] = []

            countries[this_country].append(this_woeid)

            if not iso_codes.get(this_country, False):
                iso_codes[this_country] = props['iso']

for woeid, ports in countries.items():
    print "%s: %s" % (iso_codes[woeid], len(ports))

# print pprint.pformat(countries)
