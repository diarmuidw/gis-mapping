
from mapnik import *

# Map
m = Map(600,300,'+proj=latlong +datum=WGS84')
m.background = Color('steelblue')

# Styles
'''
poly = PolygonSymbolizer(Color('lavender'))
line = LineSymbolizer(Color('slategray'),.3)
s,r = Style(),Rule()
r.symbols.extend([poly,line])
s.rules.append(r)
m.append_style('My Style',s)
'''



s = Style()
r=Rule()
r.symbols.append(RasterSymbolizer())
s.rules.append(r)
m.append_style('My Style',s)

# Layer
'''
lyr = Layer('world')
lyr.datasource = Shapefile(file='../data/world_borders')
lyr.srs = '+proj=latlong +datum=WGS84'
lyr.styles.append('My Style')
m.layers.append(lyr)
'''

bbox = '-10.038071,51.9587,-9.7284,52.137'
bbox = '-180,-90,180,90'
bbox = bbox.split(',')
ll = Coord(float(bbox[0]), float(bbox[1]))
tr = Coord(float(bbox[2]), float(bbox[3]))
map_bbox = Envelope(ll, tr)
'''
raster = Raster(file='OSI_50000_Raster_IG_modified.tif',lox=-10.038071,loy=51.9587,hix=-9.7284,hiy=52.137) 
lyr = Layer('Tiff Layer')
lyr.datasource = raster
m.layers.append(lyr)
lyr.styles.append('My Style')
print m.layers[0]
# Render
'''


r1 = Gdal(file='/home/bluekulu/Development/mapniktest/test/TrueMarble.16km.2700x1350.tif')
lyr1=Layer('gdaltif')
lyr1.datasource = r1
m.layers.append(lyr1)







m.zoom_to_box(map_bbox)
render_to_file(m, 'k2.png')
