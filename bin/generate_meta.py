#!/usr/bin/env python

import sys
import json
import os
import csv

import utils

import logging
logging.basicConfig(level=logging.INFO)

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

            feature = data['features'][0]
            props = feature['properties']

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

            try:
                centroid = [ props['longitude'], props['latitude'] ]
            except Exception, e:
                logging.error("failed to process %s: %s" % (path, e))
                # wtf?
                continue

            woeid = props['woe:id']

            root = utils.woeid2path(woeid)
            path = "/%s/%s.json" % (root, woeid)

            short = {
                'geometry' : { 'type': 'Point', 'coordinates': centroid },
                'id': feature['id'],
                'properties' : {
                    'name': props['name'],
                    'woe:id': woeid,
                    'href': path
                    }
                }

            for code in ('iata:code', 'icao:code'):
                if props.get(code, False):
                    short['properties'][code] = props[code]

            countries[this_country].append(short)

            if not iso_codes.get(this_country, False):
                iso_codes[this_country] = props['iso']

# generate some basic stats (as a CVS file)

# FIX ME

fh = open('../meta/countries.csv', 'w')

writer = csv.writer(fh)
writer.writerow(('iso', 'woeid', 'airports'))

tmp = {}

for k,v in iso_codes.items():
    tmp[v] = k

codes = tmp.keys()
codes.sort()

for iso in codes:

    woeid = tmp[iso]
    ports = countries[woeid]

    logging.info("%s (%s) : %s airports" % (iso, woeid, len(ports)))
    writer.writerow((iso, woeid, len(ports)))

fh.close()

# Now generate files for each country

for woeid, features in countries.items():

    iso = iso_codes[woeid]

    collection = {
        'type': 'FeatureCollection',
        'features': features,
        'properties': {
            'woe:id': woeid,
            'iso': iso
            }
        }

    # FIX ME

    path = "../meta/%s.json" % iso
    logging.info("write %s" % path)

    fh = open(path, 'w')
    utils.write_json(collection, fh)
    fh.close()
