# Autor: Yasmín Landaverde Nava
# Descripción: ejercicios de cadenas

# EJERCICIO 1
def combinarLetras(cadena):
    combinacion = ""
    for i in range(0, len(cadena), 1):
        letra = cadena[i]
        if i % 2 == 0:
            combinacion += letra.upper()
        else:
            combinacion += letra.lower()
    return combinacion

# EJERCICIO 2
def contieneLasVocales(palabra):
    palabraCorrecta = palabra.lower()
    vocales = 0
    if "a" in palabraCorrecta:
        vocales += 1
    if "e" in palabraCorrecta:
        vocales += 1
    if "i" in palabraCorrecta:
        vocales += 1
    if "o" in palabraCorrecta:
        vocales += 1
    if "u" in palabraCorrecta:
        vocales += 1

    if vocales == 5:
        return True
    else:
        return False

# EJERCICIO 3
def formarNombreUsuario(nombre, apellido, matricula):
    nombre3 = nombre.lower()[0:3]
    apellido3 = apellido.lower()[0:3]
    matricula3 =str(matricula)
    mat03 = (matricula3[4:8])
    nombreUsuario =  nombre3 + apellido3 + mat03
    return (nombreUsuario)

# EJERCICIO 4
def esCorrecto(nombre):
    nombre = nombre.split()
    for palabra in nombre:
        for letra in palabra[0]:
            if letra.islower():
                return False
        for letra in palabra[1::]:
            if letra.isupper():
                return False
    return True

# EJERCICIO 5
def traducirTelefono(numero):
    marcacion= numero.split("-")
    palabraCero = marcacion[0]
    palabraUno = marcacion[1]
    palabraDos = marcacion[2]
    space = "-"
    digito = ""

    for valor in palabraUno:
        if valor == "A" or valor == "B" or valor == "C":
            digito = digito + "2"
        if valor == "D" or valor == "E"  or valor == "F":
            digito = digito + "3"
        if valor == "G" or valor == "H" or valor == "I":
            digito = digito + "4"
        if valor == "J" or valor == "K" or valor == "L":
            digito = digito + "5"
        if valor == "M" or valor == "N" or valor == "O":
            digito = digito + "6"
        if valor == "P" or valor == "Q" or valor == "R" or valor == "S":
            digito = digito + "7"
        if valor == "T" or valor == "U" or valor == "V":
            digito = digito + "8"
        if valor == "W" or valor == "X" or valor == "Y" or valor == "Z":
            digito = digito + "9"

    digitoDos = ""
    for valor in palabraDos:
        if valor == "A" or valor == "B" or valor == "C":
            digitoDos = digitoDos + "2"
        if valor == "D" or valor == "E"  or valor == "F":
            digitoDos = digitoDos + "3"
        if valor == "G" or valor == "H" or valor == "I":
            digitoDos = digitoDos + "4"
        if valor == "J" or valor == "K" or valor == "L":
            digitoDos = digitoDos + "5"
        if valor == "M" or valor == "N" or valor == "O":
            digitoDos = digitoDos + "6"
        if valor == "P" or valor == "Q" or valor == "R" or valor == "S":
            digitoDos = digitoDos + "7"
        if valor == "T" or valor == "U" or valor == "V":
            digitoDos = digitoDos + "8"
        if valor == "W" or valor == "X" or valor == "Y" or valor == "Z":
            digitoDos = digitoDos + "9"


    final = palabraCero + space + digito + space + digitoDos
    return final




def main():
    frase = "hola  MUNDO"
    resultado = combinarLetras(frase)
    print (resultado)

    palabra = "abuelito"
    vocales = contieneLasVocales(palabra)
    print (vocales)

    nombre = "Yasmín"
    apellido = "Landaverde"
    matricula = "1745725"
    usuario = formarNombreUsuario(nombre, apellido, matricula)
    print(usuario)

    nombre = "Yasmin Landaverde Nava"
    error = esCorrecto(nombre)
    print (error)

    numero = "01800-VOY-BIEN"
    num = traducirTelefono(numero)
    print (num)


main()