#!/usr/bin/env python

from mapnik import *

mapfile = 'kerrygeotiff.xml'
map_output = 'kerry.png'
projection = '+proj=latlong +datum=WGS84'

m = Map(600, 300)
load_map(m, mapfile)
bbox = Envelope(Coord(-180, -90), Coord(180,90))
m.zoom_to_box(bbox) 
render_to_file(m, map_output)

