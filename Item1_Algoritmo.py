import numpy as np

def diferencias_finita(l, t, a, m, n, f=lambda:None, g=lambda:None):
    if n < 2 or m < 2: return print("ERROR: n < 2 or m < 2")
    # Paso 1
    h = l/m
    k = t/n
    y = (a*k)/h

    w = np.zeros((m+1, n+1)) # Matriz W PlaceHolder
    # Paso 2
    for j in range(1, n+1):
        w[0, j] = 0
        w[m, j] = 0

    # Paso 3
    w[0, 0] = f(0)
    w[m, 0] = f(l)

    # Paso 4
    for i in range(1, m):
        w[i, 0] = f(i*h)
        w[i, 1] = (1-(y**2))*f(i*h) + ((y**2)/2)*(f((i+1)*h)+f((i-1)*h)) + k*g(i*h)

    # Paso 5
    for j in range(1, n):
        for i in range(1, m):
            w[i, j+1] = 2*(1-(y**2))*w[i, j] + (y**2)*(w[i+1, j] + w[i-1, j]) - w[i, j-1]

    resultados = [] # Salida (x, t, w) para cada i, j.
    # Paso 6
    for j in range(n+1):
        t = j*k
        for i in range(m+1):
            x = i*h
            resultados.append((x, t, w[i, j]))

    # Paso 7
    return resultados

