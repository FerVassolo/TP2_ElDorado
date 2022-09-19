import matplotlib.pyplot as plt
from geoPositionCSVReaderFile import geoPositionCSVReader

latitud, longitud = geoPositionCSVReader("ship_geo_position.csv", 20000, interval = 100)
latitud2, longitud2 = geoPositionCSVReader("seaquake_geo_position.csv", 7000, interval = 50)



plt.plot(latitud, longitud, label="Ship")
plt.plot(latitud2, longitud2, label="Seaquake")


plt.xlabel("latitud")
plt.ylabel("longitud")
plt.xticks([-40, 0, 40])
plt.legend()
plt.grid(True)
plt.show()