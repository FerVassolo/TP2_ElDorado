import matplotlib.pyplot as plt
from geoPositionCSVReaderFile import geoPositionCSVReader

latitud, longitud = geoPositionCSVReader("ship_geo_position.csv", 20000, interval = 500)
latitud2, longitud2 = geoPositionCSVReader("seaquake_geo_position.csv", 7000, interval = 100)

plt.plot(latitud, longitud)
plt.plot(latitud2, longitud2)
plt.show()