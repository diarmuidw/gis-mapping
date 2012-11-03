#!/usr/bin/env python

from mapnik import *

mapfile = 'world.xml'
map_output = 'world_tiles.png'
projection = '+proj=latlong +datum=WGS84'

m = Map(600, 300)
load_map(m, mapfile)

bbox = '-10.038071,51.9587,-9.7284,52.137'
#bbox = '-12,51,-8,52'
bbox = bbox.split(',')
ll = Coord(float(bbox[0]), float(bbox[1]))
tr = Coord(float(bbox[2]), float(bbox[3]))
bbox = Envelope(ll, tr)

#bbox = Envelope(Coord(-180.0, -90.0), Coord(180.0, 90.0))
m.zoom_to_box(bbox) 
render_to_file(m, map_output)


#(mapproxy)bluekulu@ubuntu-desktop:~/Development/mapniktest/test$ MAPNIK_MAP_FILE="marble.xml" MAPNIK_TILE_DIR="marble/" /home/bluekulu/Development/mapnikscripts/mapnik/generate_tiles.py
