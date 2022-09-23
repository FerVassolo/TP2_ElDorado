import csv
import os

from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
from Lagrange import search10ClosePoints, biseccion, bisec



best10 = search10ClosePoints("ship_geo_position", bisec[0], bisec[1])



best10x = []
best10y = []

for elm in best10:
    best10x.append(elm[0])
    best10y.append(elm[1])
x = np.array(best10x)
y = np.array(best10y)



plt.figure()
u = plt.plot(x,y,'ro') # plot the points
t = np.linspace(0, 1, len(x))# parameter t to parametrize x and y
pxLagrange = interp1d(t, x) # X(T)
pyLagrange = interp1d(t, y) # Y(T)
n = 1000
ts = np.linspace(t[0],t[-1],n)
xLagrange = pxLagrange(ts) # lagrange x coordinates
yLagrange = pyLagrange(ts) # lagrange y coordinates
plt.plot(xLagrange, yLagrange, 'b-', label="Polynomial")
plt.scatter(xLagrange, yLagrange)

plt.show()


# Esta implementacion es realmente fea, pero funciona
xList = []
yList = []
lista = []
with open (os.path.dirname(os.path.realpath(__file__)) +"/CSVFiles/interpolation_of_possible_location.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(xLagrange)
    csv_writer.writerow(yLagrange)
    with open (os.path.dirname(os.path.realpath(__file__)) +"/CSVFiles/interpolation_of_possible_location.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        i = 0
        for elm in csv_reader:
            if i<1000:
                xList.append(elm)
            else:
                yList.append(elm)
            i+=1
        i = 0
        for elm in xList[0]:
            lista.append([elm])
        print(lista)
        for elm in xList[1]:
            lista[i].append(elm)
            i+=1
        print(lista)
        csv_file.close()
with open (os.path.dirname(os.path.realpath(__file__)) +"/CSVFiles/interpolation_of_possible_location.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    for elm in lista:
        csv_writer.writerow(elm)
