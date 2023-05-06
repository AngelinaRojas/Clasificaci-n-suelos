import pandas as pd 
import math
from funciones.ingreso import retenido

# Para el contenido de la tabla:

# Se crea una serie con el nombre del tamíz.
Tamiz = pd.Series([
    'N° 4',
    'N° 10',
    'N° 20',
    'N° 30',
    'N° 40',
    'N° 60' , 
    'N° 140',
    'N° 200'
])

# Se crea una serie con la apertura de los tamices.

Apertura = pd.Series([
    4.75,
    2,
    0.841,
    0.595,
    0.420,
    0.250,
    0.16,
    0.075
])

Retenida = pd.Series(retenido)

# Para determinar el pocentaje que pasa en cada uno de los tamices:
a = 100-Retenida[0]
b = a-Retenida[1]
c = b-Retenida[2]
d = c-Retenida[3]
e = d-Retenida[4]
f = e-Retenida[5]
g = f-Retenida[6]
h = g-Retenida[7]

# Se crea una lista con los datos anteriores:
Porcentaje = [a,b,c,d,e,f,g,h]
# Se crea una serie con la lista anterior.
Pasa = pd.Series(Porcentaje)
# Crear la estructura con las series creadas anteriormente.
Estructura = pd.DataFrame({
    'Tamiz': Tamiz, 
    'Apertura(mm)': Apertura,
    '% Retenido' : Retenida,
    '% Pasa': Pasa
})

def tabla():
    print(Estructura)
