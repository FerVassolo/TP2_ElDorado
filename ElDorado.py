import csv
import numpy as np
import matplotlib.pyplot as plt
import os


def plotting(name, every_nth):
    latiutud = []
    longitud = []
    # EN WINDOWS CREO QUE ES \\CSVFiles\\
    with open (os.path.dirname(os.path.realpath(__file__)) +"/CSVFiles/" + name + ".csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        i = 0
        for row in csv_reader:
            i+=1
            if i%10 == 0:
                latiutud.append(row[0])
                longitud.append(row[1])



    x = np.array(latiutud)
    y = np.array(longitud)


    #plt.plot(latiutud, longitud, "x", ms =0.1) # Estoy pidiendo que marque los puntos seleccionados con x



    fig, ax = plt.subplots()


    ax.plot(x, y, **{'color': 'lightsteelblue', 'marker': '.'})

    for n, label in enumerate(ax.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)
    for n, label in enumerate(ax.yaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)
    plt.tick_params(
        axis='x',
        which='both',
        bottom=False,
        top=False)
    plt.xlabel("Latitud")
    plt.ylabel("Longitud")
    title = ""
    for char in name:
        if char != "_":
            title = title + char
        else:
            title = title + " "
    plt.title(title)
    plt.show()

plotting("seaquake_geo_position", 100)
#plotting("ship_geo_position", 350)



