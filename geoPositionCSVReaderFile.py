import csv
import itertools
import os
from tokenize import String


def geoPositionCSVReader(
    csvName: String, uperRange: int, lowerRange: int = 0, interval: int = 1
):
    latitud = []
    longitud = []
    with open(os.path.dirname(os.path.realpath(__file__)) + "\\CSVFiles\\"+csvName, "r") as csvFile:
        csvReader = csv.DictReader(csvFile)

        for row in itertools.islice(csvReader, lowerRange, uperRange, interval):
            latitud.append(float(row["latitud"]))
            longitud.append(float(row["longitud"]))

    return (latitud, longitud)
