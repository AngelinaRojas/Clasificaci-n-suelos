from funciones.tabla import *

if Pasa[0] < 60:
  d60 = 9.5+((60-100)*((4.75-9.5)/(Pasa[0]-100))) # Se interpola el valor del diametro del tamíz por donde pasa el 60 % de la muestra.

  DD1 = [] # Se crea una lista vacia para almacenar posteriormente los datos. 
  PoD1 = [30, 10] #Se crea una lista con los valores del % que pasa a los que debemos determinar la apertura.
  Pos1 = [] # Se crea una lista donde se guardará la posición de los valores.
  for i in (0,1): # Se crea un ciclo en un rango establecido. 
    for  k in range(0, len(Pasa)): # Se crea un ciclo con un rango entre 0 y la longitud de los valores que tenemos en la tabla. 
      if Pasa[k] <= PoD1[i]: # Se pone una condicional donde la posición k de la lista de los porcentajes pasa será menor que la posición i en la lista creada anteriormente. 
        Pos1.append(k) # Se agrega a k en la lista de posiciones.
        break # Se rompe el ciclo. 
    di = (PoD1[i]-Pasa[Pos1[i]])*(Apertura[Pos1[i]-1]-Apertura[Pos1[i]])/(Pasa[Pos1[i]-1]-Pasa[Pos1[i]])+Apertura[Pos1[i]] # Esta formula nos ayuda a interpolar los diámetros requeridos.
    DD1.append(di) # Agregamos a la lista creada anteriormente el valor de d1.
  d30 = DD1[0] # definimos el d30 con la posición 0 de la lista DD.
  d10 = DD1[1] # definimos el d10 con la posición 0 de la lista DD.

  CU=d60/d10 #Calculamos el coeficiente de curvatura.
  CC=(d30**2)/(d10*d60) # Calculamos el coeficiente de uniformidad. 

  # Imprimimos los datos anteriormente hallados:
  print("El díametro en mm del tamíz por donde pasa el 60 % es: ", d60) 
  print("El díametro en mm del tamíz por donde pasa el 30 % es: ", d30)
  print("El díametro en mm del tamíz por donde pasa el 10 % es: ", d10)
  print("El coeficiente de curvatura es: ", CC)
  print("El coeficiente de uniformidad es: ", CU)

else:

  DD = [] # Se crea una lista vacia para almacenar posteriormente los datos. 
  PoD = [60, 30, 10] #Se crea una lista con los valores del % que pasa a los que debemos determinar la apertura.
  Pos = [] # Se crea una lista donde se guardará la posición de los valores.
  for i in (0,1,2): # Se crea un ciclo en un rango establecido. 
    for  k in range(0, len(Pasa)): # Se crea un ciclo con un rango entre 0 y la longitud de los valores que tenemos en la tabla. 
      if Pasa[k] <= PoD[i]: # Se pone una condicional donde la posición k de la lista de los porcentajes pasa será menor que la posición i en la lista creada anteriormente. 
        Pos.append(k) # Se agrega a k en la lista de posiciones.
        break # Se rompe el ciclo. 
    di = (PoD[i]-Pasa[Pos[i]])*(Apertura[Pos[i]-1]-Apertura[Pos[i]])/(Pasa[Pos[i]-1]-Pasa[Pos[i]])+Apertura[Pos[i]] # Esta formula nos ayuda a interpolar los diámetros requeridos.
    DD.append(di) # Agregamos a la lista creada anteriormente el valor de d1.
  d60 = DD[0] # definimos el d60 con la posición 0 de la lista DD.
  d30 = DD[1] # definimos el d30 con la posición 0 de la lista DD.
  d10 = DD[2] # definimos el d10 con la posición 0 de la lista DD.

  CU=d60/d10 #Calculamos el coeficiente de curvatura.
  CC=(d30**2)/(d10*d60) # Calculamos el coeficiente de uniformidad. 

  # Imprimimos los datos anteriormente hallados:
  print("El díametro en mm del tamíz por donde pasa el 60 % es: ", d60) 
  print("El díametro en mm del tamíz por donde pasa el 30 % es: ", d30)
  print("El díametro en mm del tamíz por donde pasa el 10 % es: ", d10)
  print("El coeficiente de curvatura es: ", CC)
  print("El coeficiente de uniformidad es: ", CU)