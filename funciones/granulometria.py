import matplotlib.pyplot as plt
import numpy as np
import math

from funciones.coeficientes import *
from funciones.tabla import *

d60_1 = '{:.2f}'.format(d60) # Para que solo se muestren dos decimales en el d60.
d30_1 = '{:.2f}'.format(d30) # Para que solo se muestren dos decimales en el d30.
d10_1 = '{:.2f}'.format(d10) # Para que solo se muestren dos decimales en el d10.
CC_1 = '{:.2f}'.format(CC) # Para que solo se muestren dos decimales en el CC.
CU_1 = '{:.2f}'.format(CU) # Para que solo se muestren dos decimales en el CU.

def curva_g(): # Se define una función para realizar la gráfica de la curva granulométrica.
# Se determinaron los límites inferior y superior del manual de carreteras del INVIAS, dichos franjas granulométricas 
# Se definieron para mezclas asfálticas en caliente en gradación continuas.

  # Limite inferior.
  w = [37.5, 25, 19, 12.5, 9.5, 4.75, 2, 0.425, 0.18, 0.075]
  z = [100, 75, 65, 47, 40, 28, 17, 7, 4, 2]
  # Limite superior.
  t = [100, 95, 85, 67, 60, 46, 32, 17, 11, 6]
  # Para el tamaño de la figura.
  plt.figure(figsize=(14, 4))


  # Se gráfican los límites.
  plt.plot(w,z, color="#33D7FF", linewidth=1.5, linestyle=":", label= "Límite inferior") # Para gráficar el límite inferior.
  plt.plot(w,t, color="blue", linewidth=1.5, linestyle=":", label= "Límite superior") # Para gráficar el límite superior.


  # Para acomodar la escala y la grilla horizontal: 

  rango_y = range(0,101,10) # Se define de la grilla el rango en x y la distancia entre cada valor en x.
  plt.yticks(rango_y) # Se gráfica lo anterior. 
  plt.plot(Estructura['Apertura(mm)'],Estructura['% Pasa'], color="#FF33A2", linewidth=1.5, linestyle="-",label= "Datos") # Se grafican los datos ingresados por el usuario.
  plt.grid(axis="y",color='gray', ls="-.", lw = 0.7) # Para poner la grilla. 

  # Para gráficar puntos en la sobre la gráfica. 
  plt.scatter(d60, 60, marker='s', s=80, color='purple', label='D60 = '+d60_1)
  plt.scatter(d30, 30, marker='*', s=80, color='purple', label='D30 = '+d30_1)
  plt.scatter(d10, 10, marker='p', s=80, color='purple', label='D10 = '+d10_1)
  plt.scatter(Estructura['Apertura(mm)'], Estructura['% Pasa'], color = "#FF33A2",marker='o')

  # Para acomodar la escala y la grilla vertical 
  
  plt.grid(which="major",axis="x",color='gray', ls="-.", lw = 0.7) 
  plt.grid(which="minor",axis="x",color='gray', ls="-.", lw = 0.7)
  

  plt.xlim(0.075,37.5) # para definir los limites de la grafica. 

  plt.legend(facecolor='#FFEDBE', edgecolor='black') # Para imprimir la leyenda.
  plt.xscale("log") # Para poner la gráfca en escala logaritmica. 
  plt.title("CURVA GRANULOMÉTRICA",fontsize=15, style="italic", fontweight="bold") # Para poner el titulo de la gráfica.
  plt.xlabel("MEDIDA DEL TAMIZ (mm)",fontsize=10, style="italic", fontweight="bold") # Para poner el titulo en el eje x.
  plt.ylabel("% PASA",fontsize=10, style="italic", fontweight="bold") # Para poner el titulo en el eje y.
  plt.gca().invert_xaxis() # Para invertir el eje x.
 
 # Para poner etiquetas con textos. 

  ax2 = plt.twiny() # Para crear otra figura con un eje que se ubique en la parte superior de la gráfica. 
  ax2.set_xscale('log') # Para que la escala de esta figura sea logaritmica. 
  ax2.set_xticks(Apertura) # para ubicar las etiquetas en los valores de la apertura para cada tamíz. 
  ax2.set_xticklabels(Tamiz, rotation=90, fontsize=8, style="italic", fontweight="bold") # Para que los nombres de cada tamíz se ubiquen donde se precisó anteriormente. 
  ax2.set_xlabel('Tamices',style="italic", fontweight="bold") # Para colocar un subtitulo sobre el eje creado. 
  ax2.set_xlim(0.075,37.5) # Para definir el límite en el eje x para está grafica. 
  ax2.invert_xaxis() # Para invertir el eje.
 
  # Para ubicar los límites de cada línea vertical.

  L_No4 = ([4.75,4.75]) 
  L_No10 = ([2,2]) 
  L_No20 = ([0.841,0.841]) 
  L_No30 = ([0.595,0.595]) 
  L_No40 = ([0.42,0.42]) 
  L_No60 = ([0.25,0.25])
  L_No140 = ([0.16,0.16])  
  L_No200 = ([0.075,0.075]) 
  L_rango = ([0,100])

  # Para dibujar una linea vertical en la gráfica sobre el valor asignado para cada tamíz. 

  plt.plot(L_No4, L_rango, color='k', lw='1', ls='--')
  plt.plot(L_No10, L_rango, color='k', lw='1', ls='--')
  plt.plot(L_No20, L_rango, color='k', lw='1', ls='--')
  plt.plot(L_No30, L_rango, color='k', lw='1', ls='--') 
  plt.plot(L_No40, L_rango, color='k', lw='1', ls='--')
  plt.plot(L_No60, L_rango, color='k', lw='1', ls='--')
  plt.plot(L_No140, ([0,54]), color='k', lw='1', ls='--')
  plt.plot(L_No200, L_rango, color='k', lw='1', ls='--')

  # Para poner etiquetas con textos de clasificación de suelos. 

  a = plt.text(5.5, 0, 'Grava(Fina)', fontsize=6,style="italic", fontweight="bold") # Muestra el texto. 
  a.set_bbox(dict(facecolor='white', edgecolor='black')) # Para ponerle un fondo y borde al texto.
  b = plt.text(2.5, 0, 'Arena(Gruesa)', fontsize=6, style="italic", fontweight="bold")# Muestra el texto.
  b.set_bbox(dict(facecolor='white', edgecolor='black'))# Para ponerle un fondo y borde al texto.
  c = plt.text(0.53, 0, 'Arena (Mediana)', fontsize=6, style="italic", fontweight="bold")# Muestra el texto.
  c.set_bbox(dict(facecolor='white', edgecolor='black'))# Para ponerle un fondo y borde al texto.
  d = plt.text(0.11, 0, 'Arena(Fina)', fontsize=6, style="italic", fontweight="bold")# Muestra el texto.
  d.set_bbox(dict(facecolor='white', edgecolor='black'))# Para ponerle un fondo y borde al texto.


  plt.show() # Imprimir la gráfica.