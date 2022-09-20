import os
import csv
import numpy as np
from scipy.interpolate import interp1d
"""
public static double Lagrange(double x[], double y[], double z){
		int n = x.length;
		double p=0;
		double L;
		for(int i = 0; i <n ; i++){
		   L = 1;
		   for (int j = 0; j < n ; j ++)
			   if (j != i )
                             L = L * (z- x[j])/(x[i]-x[j]);
		    p = p + L* y[i];
		}
		return p;
	}
"""

def lagrangeMio(x, y, z):
    # x: float[], y: float[], z: float
    n = len(x)
    p = 0
    for i in range(0, n):
        L = 1
        for j in range(0, n):
            if (j != i):
                L = L * (z- x[j])/(x[i]-x[j])


        p = p + L * y[i]

    return p

def csv_to_list(name):
    latiutud = []
    longitud = []
    # EN WINDOWS CREO QUE ES \\CSVFiles\\
    with open (os.path.dirname(os.path.realpath(__file__)) +"/CSVFiles/" + name + ".csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        i = 0
        for row in csv_reader:

            if (float(row[0]) > 1 and float(row[0])<5):
                latiutud.append(float(row[0]))
                longitud.append(float(row[1]))
                i+=1


    return latiutud, longitud

ship_geo_pos = csv_to_list("ship_geo_position")
seaquake_geo_pos = csv_to_list("seaquake_geo_position")


def biseccion(x1, y1, x2, y2, a, b, cota):
    error = 100 # damos a error un valor grande cualquiera
    raiz = 0 # iniciamos a la variable raiz en 0, esta será la variable retornada por el método.
    fun1 = interp1d(x1, y1)
    fun2 = interp1d(x2, y2)
    while error > cota:
        aux = raiz # guardamos el último valor de raiz para luego calcular el error.
        raiz = (a + b) / 2

        fa = fun1(a) - fun2(a)
        fraiz = fun1(raiz) - fun2(raiz)
        test = fa * fraiz
        if test < 0:
            b = raiz
            error = abs(raiz - aux)
        elif test > 0:
            a = raiz
            error = abs(raiz -aux)
        else:
            error = 0 # Si el test da 0 significa que f(raiz) = 0 y se termina el ciclo

    return raiz, float(fun1(raiz))

print(biseccion(seaquake_geo_pos[0], seaquake_geo_pos[1], ship_geo_pos[0], ship_geo_pos[1], 2, 4, 0.001))

