from geoPositionCSVReaderFile import geoPositionCSVReader

x, y = geoPositionCSVReader("seaquake_geo_position.csv", 0, 10000)
print(x)
print(y)
