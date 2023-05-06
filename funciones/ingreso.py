# Para los % retenidos: 

print("Escriba los % retenidos en los tamices N° 4; N° 10;  N° 20; N° 30; N° 40; N° 60; N° 140; N° 200 : ")
def ingreso():
  
  retenido=[]

  for x in range(100): # Se crea un ciclo en un rango de máximo 100 iteraciones.

    if len(retenido)==8: # Se crea una condición acerca del número de datos en la lista. 
      break # Se detiene el código.
      
    valor = input() # Se crea una variable con el valor que ingrese el usuario.
    prueba = valor.isnumeric() # Se realiza una verificación del dato ingresado. Si es un número será False si es otro caracter será True.

    if prueba == True: # Se imponen dos condiciones para que continue el código.
      valor = float(valor) # Se convierte el valor en número decimal.
      retenido.append(valor) # Se agrega a la lista el valor creado.
      continue # Se continua con el codigo. 

    else:
      print("ingrese algo valido") # Si las condiciones anteriores no se cumplen entonces se imprimira este mensaje.
      continue  # Se continua con el codigo. 

ingreso = ingreso()