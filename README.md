whereonearth-airport
--

_Forking GeoPlanet one place type a time._

This is an active but still experimental project to create a community-driven
project to maintain and update the Creative Commons licensed GeoPlanet dataset.

Rather than create a single repository with every record the plan is to create
smaller datasets organized by placetype in the hopes that they will be more
manageable to download and to update by users interested in particular place types.

Each location (building) is stored as a separate GeoJSON file. GeoJSON was
chosen because it has wide support in variety of GIS tools, most programming
languages (and specifically JavaScript), can be edited using any old text editor
(or Github's own "edit this page" functionality) and allows for any number of
custom key/value pairs using the GeoJSON _properties_ dictionary.

The naming convention for records is the building's Where On Earth (WOE) ID
followed by a ".json" extension. Records are stored in nested directories that
correspond to their WOE ID. The top level directory would be the first three
digits of a WOE ID, the second level directory would be the following three
digits (four through six) and so on until their are no more digits in the WOE
ID. For example, given the WOE ID ID 12521721 the full path of the record
would be: [data/125/217/21/12521721.json](https://github.com/straup/whereonearth-airport/blob/master/data/125/217/21/12521721.json)

This repository includes airports from GeoPlanet (versions 7.3 through 7.6) as
compiled by [woedb](http://woe.spum.org). Where possible records have already
been updated to include corresponding FAA, ICAO, IATA and Geonames IDs. Coverage
is far from complete. Records have been cross-referenced against the
[whereonearth-building](https://github.com/straup/whereonearth-building/)
repository and pointers to buildings parented by individual airports have been added.

Each record contains a bounding box or a complex polygon defining the contour of
the airport. Polygons are sourced from the January 2010 release of the [Flickr Alpha Shapes](http://code.flickr.com/blog/2011/01/08/flickr-shapefiles-public-dataset-2-0/).

A word about Github
--

In the long-run Github may not be the best venue for managing all of these
records. But it's not an entirely crazy idea either so we're going to try it for
a while because it's easy and safe.

See also
--

* [whereonearth-building](https://github.com/straup/whereonearth-building/)

* [woe.spum.org](http://woe.spum.org)

* [building=yes](http://buildingequalsyes.spum.org/)

* [GeoPlanet data downloads](http://developer.yahoo.com/geo/geoplanet/data/)

* [Flickr Alpha Shapes](http://code.flickr.com/blog/2011/01/08/flickr-shapefiles-public-dataset-2-0/)
