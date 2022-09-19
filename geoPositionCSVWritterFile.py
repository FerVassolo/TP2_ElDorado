from tokenize import String
import os
import csv


def geoPositionCSVWritter(csvName: String, latitudes, longitudes):
    with open(
        os.path.dirname(os.path.realpath(__file__)) + "\\CSVFiles\\" + csvName, "w"
    ) as csvFile:
        filenames = ["latitud", "longitud"]

        csvWritter = csv.DictWriter(csvFile, fieldnames=filenames)
        csvWritter.writeheader()

        i = 0
        for lat in latitudes:
            csvWritter.writerow({"latitud": lat, "longitud": longitudes[i]})
            i += 1

    csvFile.close()
