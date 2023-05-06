# Para adquirir los datos del usuario para la carta de plasticidad, se creará una función. 
def datos_IP(): 
   # Para el índice de plasticidad:

  ingreso_2 = input("Ingrese el valor del índice de plasticidad: ") # Se le solicita al usuario ingresar el valor. 
  prueba_2 = ingreso_2.isnumeric() # Se realiza una verificación del dato ingresado. Si es un número será False si es otro caracter será True.

  if prueba_2 == True: # Se imponen dos condiciones para que continue el código.
    IP = int(ingreso_2) # Se convierte el valor en número entero.

  else:
    print("ingrese algo valido") # Si las condiciones anteriores no se cumplen entonces se imprimira este mensaje.

    for x in range(100):
      
      valor = input() # Se crea una variable con el valor que ingrese el usuario.
      prueba = valor.isnumeric() # Se realiza una verificación del dato ingresado. Si es un número será False si es otro caracter será True.

      if prueba == True: # Se imponen dos condiciones para que continue el código.
        IP = int(valor) # Se convierte el valor en número decimal.
        break # Se continua con el codigo. 

      else:
        print("ingrese algo valido") # Si las condiciones anteriores no se cumplen entonces se imprimira este mensaje.
        continue  # Se continua con el codigo.
  return IP