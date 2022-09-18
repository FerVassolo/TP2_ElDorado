import csv
import itertools
import os
from tokenize import String


def geoPositionCSVReader(
    csvName: String, lowerRange: int, uperRange: int
):
    latitud = []
    longitud = []
    with open(os.path.dirname(os.path.realpath(__file__)) + "\\CSVFiles\\"+csvName, "r") as csvFile:
        csvReader = csv.DictReader(csvFile)

        for row in itertools.islice(csvReader, lowerRange, uperRange):
            latitud.append(row["latitud"])
            longitud.append(row["longitud"])

    return (latitud, longitud)
