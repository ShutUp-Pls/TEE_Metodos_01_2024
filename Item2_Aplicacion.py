import csv # Para exportar los resultados a un archivo CSV para facilitar trabajo con geogebra
import numpy as np

from Item1_Algoritmo import diferencias_finita

# DEFINICIÓN DE CONDICIONES INICIALES
'''
- Condición inicial f(x) para el metodo:
u(x,0) = f(x)

- En el problema se define:
u(x,t) = sin(pi*x)*cos(2*pi*t)

- De lo anterior obtenemos que la condición inicial f(x) es:
u(x,0) = f(x) = sin(pi*x)
'''

def f(x): return np.sin((np.pi)*x)

'''
- Condición inicial g(x) para el metodo:
∂u/∂t(x,0) = g(x)

- En el problema se define:
∂u/∂t(x,0) = 0

- De lo anterior obtenemos que la condición inicial g(x) es:
∂u/∂t(x,0) = g(x) = 0
'''

def g(x): return 0

'''
- El metodo aproxima solución bajo los intervalos:
0 < x < L | 0 < t < T

- Los intervalos que define el problema son:
0 < x < 1 | 0 < t < 1

- Por lo tanto: L = 1 | T = 1
'''

L = 1
T = 1

'''
- La ecuación de onda que aproxima el metodo es:
(∂²u/∂t²(x,t)) - (alpha²)*(∂²u/∂x²(x,t)) = 0

- La ecuación de onda dada por el problema es:
(∂²u/∂t²) - (4)*(∂²u/∂x²) = 0

- De lo anterior podemos obtener el valor de 'alpha':
alpha² = 4 | alpha = ±2
'''

alpha = 2

# Parametros dados por la actividad 3 (Variar para )
M = 10
N = 10

# Cálculo de las aproximaciones
resultados = diferencias_finita(L, T, alpha, M, N, f, g)

# Guardar para exportar los resultados como .csv
# Usar .csv facilita su incersión a softwares de graficos
# GeoGebra en su versión classic permite la inserción de tablas
if True:
    with open('resultados.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["x", "y", "z"])
        for res in resultados:
            writer.writerow([res[0], res[1], res[2]])