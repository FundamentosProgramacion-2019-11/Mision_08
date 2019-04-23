# Paulina Guerrero Ruiz A01024519
# Cadenas


# Cadena 1: Cambiar una palabra común a una palabra que tenga minusculas y mayusculas intercaladas

def combinarLetras(cadena):

        d = ""         # acumulador
        c = 1          # contador


        for i in cadena:
            if c == 1:
                letra = i.upper()   # esto lo usamos para las mayusculas, dependiendo de la cantidad de letras
            elif c == -1:
                letra = i.lower()  # aqui igual pero en el caso de minusculas
            d = d + letra
            c = -c
        return d


# Cadena 2: Informarle a nuestro usuario si la palabra que me están dando tiene todas las vocales o no

def contieneLasVocales(cadena):

    cadena1 = cadena.lower()     # eso para convertir la palabra en minusculas
    xA = 0
    xE = 0
    xI = 0                       # contadores
    xO = 0
    xU = 0
    x= 1

    for c in cadena1:
        if c == "a" or "á" or "A":      # dependiendo de cuantas vocales tenga la palabra, se vas acumulando
            xA += 1
        if c == "e" or "é" or "E":
            xE += 1
        if c == "i" or "í" or "I":
            xI += 1
        if c == "o" or "ó" or "O":
            xO += 1
        if c == "u" or "ú" or "U":
            xU += 1
    if xA >= 1 and xE >= 1 and xI >= 1 and xO >= 1 and xU >= 1:     # condicionante, si cumple con esto, pasa a ser True, si no, false
        print("True: Tu palabra contiene todas las vocales")
    else:
        print("False: Vuelve a intentarlo, por favor")

# Cadena 3: En este ejercicio el usuario nos dará sus datos y nosotros tenemos que entregarle un nombre de usuario conformado por esos mismos datos

def formarNombreUsuario(nombre, apellido, matricula):

    nombre = nombre.lower()   # convertimos las letras en minusculas para que sea mas comodo su uso (?)
    apellido = apellido.lower()
    matricula = str(matricula)
    x = nombre[0:3]   # rango de caracteres desde el incio hasta el 3
    y = apellido[0:3]
    z = matricula[4:7]
    final = x + y + z
    print("Tu nombre de usuario seria: ",final)


# Cadena 4: Aqui el usuario nos dará sus datos y tenemos que indicarle si están correctamente escritos o no

def esCorrecto(ortografia):

    palabras = ortografia.split()
    c1 = 0      #contadores
    c2 = 0
    for p in palabras:
        minusculas = p[1:]
        mayuscula = p[0:1]
        if mayuscula.isupper() and minusculas.islower():
            c1 += 1
        else:
            c2 += 1
    if c1 == 3:
        print("Ortografia correcta")
    elif c2 >= 1:
        print("Ortografia incorrecta")

# Cadena 5: Esta cadena recibe un numero con un formato especifico como si fuera de celular viejito y lo regresa como serian los numeros

def traducirTelefono(numero):
    numero = str(numero)
    letrasTraducidas = numero.upper() #aqui, en teoria todos los caracteres los convertira a mayusculas y no habria necesidad de especificar las minusculas abajo, pero por si acaso
    separador = ["-"]
    n1 = ("Error")    # diccionario que vamos a utilizar para la conversion
    n2 = ("A", "B", "C","a","b","c")
    n3 = ("D", "E", "F","d","f","g")
    n4 = ("G", "H", "I","g","h","i")
    n5 = ("J", "K", "L","j","k","l")
    n6 = ("M", "N", "O","m","n","o")
    n7 = ("P", "Q", "R", "S","p","q","r","s")
    n8 = ("T", "U", "V","t","u","v")
    n9 = ("W", "X", "Y", "Z","w","y","z")

    numerosTraducidos = numero[:5:]   #rango de inicio al 5
    for letra in letrasTraducidas:
        for numero in n2:
            if numero in letra:
                numerosTraducidos += "2"
        for numero in n3:
            if numero in letra:
                numerosTraducidos += "3"
        for numero in n4:
            if numero in letra:
                numerosTraducidos += "4"
        for numero in n5:
            if numero in letra:
                numerosTraducidos += "5"
        for numero in n6:
            if numero in letra:
                numerosTraducidos += "6"
        for numero in n7:
            if numero in letra:
                numerosTraducidos += "7"
        for numero in n8:
            if numero in letra:
                numerosTraducidos += "8"
        for numero in n9:
            if numero in letra:
                numerosTraducidos += "9"
        for numero in separador:
            if numero in letra:
                numerosTraducidos += "-"
    print("La traduccion de tu numero seria: ", numerosTraducidos)  # aqui se imprimen los numero ya traducidos mas el "01800-" que viene por default


def main():
    cadena = input("Por favor teclea la frase que quieres convertir: ")
    print(combinarLetras(cadena))
    #-------------------------
    vocal= input("Por favor teclea una palabra y te diré si tiene todas las vocales: ")
    print (contieneLasVocales(cadena))
    #-------------------------
    nombre= input("Teclea tu nombre: ")
    apellido = input("Teclea únicamente tu primer apellido: ")
    matricula = input("Teclea tu matricula: ")
    formarNombreUsuario(nombre,apellido,matricula)
    #-------------------------
    ortografia= input("Teclea tu nombre completo (incluye tus dos apellidos): ")
    esCorrecto(ortografia)
    #------------------------
    numero= input("Teclea tu telefono en formato 01800-XXX-XXXX para traducirlo: ")
    traducirTelefono(numero)



main()
