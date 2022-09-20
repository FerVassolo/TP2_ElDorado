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

def lagrange(x, y, z):
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
