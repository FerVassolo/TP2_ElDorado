import matplotlib.pyplot as plt
from geoPositionCSVReaderFile import geoPositionCSVReader
from geoPositionCSVWritterFile import geoPositionCSVWritter

latitud, longitud = geoPositionCSVReader(
    "ship_geo_position.csv", 10500, lowerRange=9500, interval=100
)
latitud2, longitud2 = geoPositionCSVReader(
    "seaquake_geo_position.csv", 1750, lowerRange=750, interval=50
)

geoPositionCSVWritter("ship_geo_position_precise.csv", latitud, longitud)
plt.plot(latitud, longitud, label="Ship")
plt.plot(latitud2, longitud2, label="Seaquake")


plt.xlabel("latitud")
plt.ylabel("longitud")
plt.xticks([-40, 0, 40])
plt.legend()
plt.grid(True)
plt.show()
