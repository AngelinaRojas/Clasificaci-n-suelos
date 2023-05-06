import matplotlib.pyplot as plt
import numpy as np
import math

def grafica(LL,IP): # Se crea una función para realizar la gráfica de la carta de plasticidad.
  x = np.arange(0, 100) # Se determina el rango en x.
  y = (x-8)*0.9 # Se define la función de la línea A. 
  z = (x-20)*0.73 # Se define la función de la línea U. 
  
  plt.plot(x,y, color="blue", linewidth=2.0, linestyle="--", label= "LINEA U") # Se gráfica la línea A.
  plt.plot(x,z, color="purple", linewidth=2.0, linestyle="--", label= "LINEA A") # Se gráfica la línea U.


  # Para hacer una linea vertical en x=50:
  plt.axvline(x=50, ymin=0, ymax=1, color="red", linewidth=1.5, linestyle="--") 

  # Para hacer dos lineas horizontales en y=4 y y=7:
  plt.axhline(y=4, xmin=0.124444, xmax=0.254795, color="green", linewidth=1.5, linestyle="--")
  plt.axhline(y=7, xmin=0.157778, xmax=0.2958904, color="brown", linewidth=1.5, linestyle="--")

  # Para acomodar la escala vertical y horizontal: 
  rango_x = range(0, 101,10) # Se define de la grilla el rango en x y la distancia entre cada valor en x.
  plt.xticks(rango_x) # Se gráfica lo anterior. 
  rango_y = range(0, 71,10) # Se define de la grilla el rango en y y la distancia entre cada valor en y
  plt.yticks(rango_y) # Se gráfica lo anterior. 

  #para poner los límites en el eje y y en el eje x: 
  plt.ylim(0, 70)
  plt.xlim(0, 100)
  
  # A continuación se escribiran los diferentes tipos de suelo:
  plt.text(68, 46, 'CH', fontsize=9, fontweight="bold") 
  plt.text(33, 17, 'CL', fontsize=9, fontweight="bold") 
  plt.text(35, 6, 'ML', fontsize=9, fontweight="bold") 
  plt.text(70, 17, 'MH', fontsize=9, fontweight="bold") 

  # Para el suelo CL-ML, dado que no cabe en el espacio, se pondrá de la siguiente forma:
  px = 20 #Se define la coordenada x de donde se quiere que apunte la flecha.
  py = 5 #Se define la coordenada y de donde se quiere que apunte la flecha.
  nota = plt.annotate("CL-ML",fontweight="bold", xy=(px, py), xycoords='data', # Se define el texto que se quiere poner.
         xytext=(10, 21), # Se definen las coordenadas en donde se requiere ubicar el texto.
         fontsize=9, # Tamaño del texto 
         arrowprops=dict(arrowstyle="->", # definición de la flecha. 
         connectionstyle="arc3,rad=.2")) # propiedades de la linea de la flecha. 

  # para sombrear la grafica por coordenadas:

  plt.fill([12.444444, 15.777778, 29.589041, 25.479452], [4, 7, 7, 4], color = "lightgreen")
  plt.fill_between([20, 50, 50], [0, 21.9, 0], color = "#ffffa2")
  plt.fill([ 15.777778,50,50, 29.589041], [ 7, 37.8,21.9,7], color = "#FFB6C1")
  plt.fill([ 50,100,100, 50], [ 37.8, 82.8,58.4,21.9], color = "#ffb48a")
  plt.fill([ 50,50,100, 100], [ 0, 21.9,58.4,0], color = "#87CEFA")
  
  # para las lineas de referencia 
  plt.axvline(x=LL, ymin=0, ymax=1, color="black", linewidth=0.8, linestyle=(0, (1, 2, 5, 2, 5, 2, 1, 2))) 
  plt.axhline(y=IP, xmin=0, xmax=1, color="black", linewidth=0.8, linestyle=(0, (1, 2, 5, 2, 5, 2, 1, 2)))


  plt.scatter(LL, IP, color = "black",marker="*") # Para gráficar el punto con coordenadas (LL,IP).
  plt.title("CARTA DE PLASTICIDAD",fontsize=15, style="italic", fontweight="bold") # Para poner el titulo de la gráfica.
  plt.xlabel("LIMITE LIQUIDO (LL)",fontsize=10, style="italic", fontweight="bold") # Para poner el titulo en el eje x.
  plt.ylabel("INDICE DE PLASTICIDAD (IP)",fontsize=10, style="italic", fontweight="bold") # Para poner el titulo en el eje y.
  plt.grid(color='gray', ls="--", lw = 0.7) # Para poner la grilla. 
  plt.legend() # Para imprimir las leyendas de cada línea. 
  plt.show() # Para mostrar la gráfica.