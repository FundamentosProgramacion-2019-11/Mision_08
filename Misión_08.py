# AQUI agregas tus funciones
#Autor: Marianela Contreras Domínguez
# Misión 8. Programa con funciones de cadenas


#FUNCIÓN 1
#función que recibe una cadena y regresa una con letras en mayúsculas y minúsculas
def combinarLetras(cadena):
  x = 1  # contador para poder ir por cada letra
  new = ""
  for c in cadena:  # se recorre cada caracter(ch) de la cadena
    if (x % 2) != 0:  # si no es par entonces es mayúsculas
      c = c.upper()
      new = new + c
    else:
      c = c.lower()  # si es par entocnes es minúsculas
      new = new + c  # se crea la nueva cadena
    x += 1  # suma el contador para poder recorrer la cadena completa
  return new


#FUNCIÓN 2
# función que recibe una cadena y regresa True si contiene todas las vocales
def contieneLasVocales(cadena):
  cadenaNueva = cadena.lower()  # pasar toda la cadena a minúsculas para poder verificarla

  contador1 = 0
  contador2 = 0
  contador3 = 0
  contador4 = 0
  contador5 = 0
  # ciclo for para pasar letra por letra e ir sumando al contador de cada vocal si la tiene o no
  for letra in cadenaNueva:
    if letra == "a":
      contador1 += 1
    elif letra == "e":
      contador2 += 1
    elif letra == "i":
      contador3 += 1
    elif letra == "o":
      contador4 += 1
    elif letra == "u":
      contador5 += 1

  # si tiene todas, entonces todos los contadores deberían ser diferentes a 0
  if contador1 != 0 and contador2 != 0 and contador3 != 0 and contador4 != 0 and contador5 != 0:
    print("True, tiene todas las vocales")
    return True
  else:
    print("False, no tiene todas las vocales")
    return False


#FUNCIÓN3
#función que recibe tres parámetros: nombre, apellido paterno y matrícula. Regresa un nombre de usuario
def formarNombreUsuario(nombre, apellidoPaterno,matrícula):
    nuevaMatrícula = matrícula % 1000 #con el módulo separamos los 3 últimos números
    nombreletras = nombre[0:3:] #se toman los 3 primeros caractéres del nombre con un operador
    apellidoletras= apellidoPaterno[0:3:]  #se toman los tres primeros del apellido


    nueva= nombreletras+apellidoletras+ str (nuevaMatrícula)  #se suman las variables para crear el nombre de usuario
    return nueva.lower()


#FUNCIÓN 4
#función que recibe como parámetro el nombre de una persona y regresa True si las reglas de mayúsculas están bien escritas.
def esCorrecto(cadena):
    separarEspacios= cadena.split() #separa la cadena por espacios
    iniciales= " "
    n1 = 1
    tamaño1 = 0

    for primerasLetras in separarEspacios:
        iniciales = iniciales + primerasLetras[0]   #toma las iniciales de cada palabra

    while cadena[n1] != " ":
        n1 += 1
    tamaño1 = n1   #para concocer cuántas letras tiene la primer palabra
    n2= tamaño1 + 1

    while cadena[n2] != " ":
        n2 += 1
    tamaño2 = n2-tamaño1 - 1  #para conocer cuántas letras tiene la segunda palabra

    n3 = tamaño1+tamaño2 + 2

    tamaño3 = len(cadena)-n3  #restamos al tamaño total de la cadena, ambos tamaños de las palabras y los dos espacios

    #para juntar todas las letras (excepto iniciales) se utilizan operadores y los tamaños
    letrasRestantes = cadena[1:tamaño1:1] + cadena[(tamaño1 +3):(tamaño1+1+tamaño2):1] + cadena[(tamaño1+tamaño2+3):len(cadena):1]

    #se verifica si las iniciales son mayúsculas y el resto son minúsculas
    if iniciales.isupper()and letrasRestantes.islower():

        return True
    else:

        return False


#FUNCIÓN 5
#función recibe como parámetro un número de teléfono en el formato "01800-XXX-XXXX"
# y regresa una cadena del número de teléfono con los dígitos correspondientes.
def traducirTelefono(númeroTel):
    #se toma el índice que se quiere cambiar, dependiendo de en que grupo se encuentre, se cambia el número
    if númeroTel[6] in ["a","A","b","B","c","C"]:
        letra1 = "2"
    elif númeroTel[6] in ["d","D","e","E","f","F"]:
        letra1 = "3"
    elif númeroTel[6] in ["G","H","I","g","h","i"]:
        letra1 = "4"
    elif númeroTel[6] in ["J","K","L","j","k","l"]:
        letra1 = "5"
    elif númeroTel[6] in ["M", "N", "O","m","n", "o"]:
        letra1= "6"
    elif númeroTel[6]in ["P","Q", "R", "S", "p","q", "r","s"]:
        letra1 = "7"
    elif númeroTel[6] in ["T", "U", "V","t", "u","v"]:
        letra1 = "8"
    elif númeroTel[6] in ["W", "X", "Y", "Z", "w", "y", "z", "x"]:
        letra1= "9"

    #se repite lo mismo con cada índice

    if númeroTel[7] in ["a","A","b","B","c","C"]:
        letra2 = "2"
    elif númeroTel[7] in ["d","D","e","E","f","F"]:
        letra2 = "3"
    elif númeroTel[7] in ["G","H","I","g","h","i"]:
        letra2 = "4"
    elif númeroTel[7] in ["J","K","L","j","k","l"]:
        letra2 = "5"
    elif númeroTel[7] in ["M", "N", "O","m","n", "o"]:
        letra2= "6"
    elif númeroTel[7]in ["P","Q", "R", "S", "p","q", "r","s"]:
        letra2 = "7"
    elif númeroTel[7] in ["T", "U", "V","t", "u","v"]:
        letra2 = "8"
    elif númeroTel[7] in ["W", "X", "Y", "Z", "w", "y", "z", "x"]:
        letra2 = "9"


    if númeroTel[8] in ["a","A","b","B","c","C"]:
        letra3 = "2"
    elif númeroTel[8] in ["d","D","e","E","f","F"]:
        letra3 = "3"
    elif númeroTel[8] in ["G","H","I","g","h","i"]:
        letra3 = "4"
    elif númeroTel[8] in ["J","K","L","j","k","l"]:
        letra3 = "5"
    elif númeroTel[8] in ["M", "N", "O","m","n", "o"]:
        letra3= "6"
    elif númeroTel[8]in ["P","Q", "R", "S", "p","q", "r","s"]:
        letra3 = "7"
    elif númeroTel[8] in ["T", "U", "V","t", "u","v"]:
        letra3 = "8"
    elif númeroTel[8] in ["W", "X", "Y", "Z", "w", "y", "z", "x"]:
        letra3 = "9"

    if númeroTel[10] in ["a","A","b","B","c","C"]:
        letra4 = "2"
    elif númeroTel[10] in ["d","D","e","E","f","F"]:
        letra4 = "3"
    elif númeroTel[10] in ["G","H","I","g","h","i"]:
        letra4 = "4"
    elif númeroTel[10] in ["J","K","L","j","k","l"]:
        letra4 = "5"
    elif númeroTel[10] in ["M", "N", "O","m","n", "o"]:
        letra4= "6"
    elif númeroTel[10]in ["P","Q", "R", "S", "p","q", "r","s"]:
        letra4 = "7"
    elif númeroTel[10] in ["T", "U", "V","t", "u","v"]:
        letra4 = "8"
    elif númeroTel[10] in ["W", "X", "Y", "Z", "w", "y", "z", "x"]:
        letra4 = "9"

    if númeroTel[11] in ["a","A","b","B","c","C"]:
        letra5 = "2"
    elif númeroTel[11] in ["d","D","e","E","f","F"]:
        letra5 = "3"
    elif númeroTel[11] in ["G","H","I","g","h","i"]:
        letra5 = "4"
    elif númeroTel[11] in ["J","K","L","j","k","l"]:
        letra5 = "5"
    elif númeroTel[11] in ["M", "N", "O","m","n", "o"]:
        letra5= "6"
    elif númeroTel[11]in ["P","Q", "R", "S", "p","q", "r","s"]:
        letra5 = "7"
    elif númeroTel[11] in ["T", "U", "V","t", "u","v"]:
        letra5 = "8"
    elif númeroTel[11] in ["W", "X", "Y", "Z", "w", "y", "z", "x"]:
        letra5 = "9"

    if númeroTel[12] in ["a","A","b","B","c","C"]:
        letra6 = "2"
    elif númeroTel[12] in ["d","D","e","E","f","F"]:
        letra6 = "3"
    elif númeroTel[12] in ["G","H","I","g","h","i"]:
        letra6 = "4"
    elif númeroTel[12] in ["J","K","L","j","k","l"]:
        letra6 = "5"
    elif númeroTel[12] in ["M", "N", "O","m","n", "o"]:
        letra6= "6"
    elif númeroTel[12]in ["P","Q", "R", "S", "p","q", "r","s"]:
        letra6 = "7"
    elif númeroTel[12] in ["T", "U", "V","t", "u","v"]:
        letra6 = "8"
    elif númeroTel[12] in ["W", "X", "Y", "Z", "w", "y", "z", "x"]:
        letra6 = "9"

    if númeroTel[13] in ["a","A","b","B","c","C"]:
        letra7 = "2"
    elif númeroTel[13] in ["d","D","e","E","f","F"]:
        letra7 = "3"
    elif númeroTel[13] in ["G","H","I","g","h","i"]:
        letra7 = "4"
    elif númeroTel[13] in ["J","K","L","j","k","l"]:
        letra7 = "5"
    elif númeroTel[13] in ["M", "N", "O","m","n", "o"]:
        letra7= "6"
    elif númeroTel[13]in ["P","Q", "R", "S", "p","q", "r","s"]:
        letra7 = "7"
    elif númeroTel[13] in ["T", "U", "V","t", "u","v"]:
        letra7 = "8"
    elif númeroTel[13] in ["W", "X", "Y", "Z", "w", "y", "z", "x"]:
        letra7 = "9"

    inicio= númeroTel[0:6:1] #se toma el inicio de la cadena que no cambiará
    traducción = inicio + letra1 +letra2 + letra3 + "-" + letra4 +  letra5 + letra6 + letra7
    return traducción


#Función principal del programa y la que correrá
def main():
  #función 1
  cadena = input("Teclea una cadena: ")
  new = combinarLetras(cadena)
  print(new)
  #función2
  cadena = input("Tecela una cadena:")
  contieneLasVocales(cadena)
  #función 3
  nombre = input("Tecela tu nombre:")
  apellidoPaterno = input("Tecela tu apellido paterno:")
  matrícula = int(input("Tecela tu matrícula (sin A0):"))
  nueva = formarNombreUsuario(nombre, apellidoPaterno, matrícula)
  print(nueva.lower())  # se imprimen en minúscula
  #función 4
  cadena = input("Teclea tu nombre completo:")
  if esCorrecto(cadena) == True:
      print("True, es correcto")
  else:
      print("False, es incorrecto")
  #Función 5
  númeroTel = input("Escribe un número telefónico: ")
  traducción = traducirTelefono(númeroTel)
  print(traducción)
main()
