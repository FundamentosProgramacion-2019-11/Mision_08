# Yadira Fuentes Calderón A01745235
# Programa que cumple la funcion de llamar cadenas y cambiar estas

def combinarLetras(cadena):
    acumulador = ""
    for letra in range(len(cadena)):
        if letra%2== 0:
            acumulador += cadena[letra].upper()
        else:
            acumulador += cadena[letra].lower()

    return acumulador


def contieneLasVocales(cadenaVocales):
    vocales = cadenaVocales.lower()
    if "a" in vocales and "e" in vocales and "i" in vocales and "o" in vocales and "u" in vocales:
        return True
    else:
        return False


def formarNombreUsuario(nombre, apellidoPaterno, matrícula):
    nombre = nombre.lower()
    apellidoPaterno = apellidoPaterno.lower()

    nombreUsuario = nombre[0:3] + apellidoPaterno[0:3] + str(matrícula)[4:7]
    return nombreUsuario


def esCorrecto(nombrePersona):
    nombrePersona = nombrePersona.split()
    contador= 0

    for letra in nombrePersona:
        mayuscula = letra[0:1]
        minuscula = letra[1:]
        if mayuscula.isupper() and minuscula.islower():
            contador+=1
            if contador == 3:
                return True
        else:
            return False


def traducirTelefono(numeroTelefono):
    acumulador = ""
    numeroTelefono = numeroTelefono.upper()

    for numeros in numeroTelefono:
        if numeros == "A" or numeros == "B" or numeros == "C":
            acumulador = acumulador + "2"
        if numeros == "D" or numeros == "E" or numeros == "F":
            acumulador = acumulador + "3"
        if numeros == "G" or numeros == "H" or numeros == "I":
            acumulador = acumulador + "4"
        if numeros == "J" or numeros == "K" or numeros == "L":
            acumulador = acumulador + "5"
        if numeros == "M" or numeros == "N" or numeros == "O":
            acumulador = acumulador + "6"
        if numeros == "P" or numeros == "Q" or numeros == "R" or numeros == "S":
            acumulador = acumulador + "7"
        if numeros == "T" or numeros == "U" or numeros == "V":
            acumulador = acumulador + "8"
        if numeros == "W" or numeros == "X" or numeros == "Y" or numeros == "Z":
            acumulador = acumulador + "9"
        if numeros == "-":
            acumulador= acumulador + "-"

    numeroDeTelefono= "01800"+acumulador
    return numeroDeTelefono


def main():
    cadena = input("Escribe una frase y las letras se alternaran (mayusculas, minusculas): ")
    frase = combinarLetras(cadena)
    print(frase)

    print()

    cadenaVocales = input("Escribe otra frase y te dire si esta tiene todas las vocales o no: ")
    tieneVocales = contieneLasVocales(cadenaVocales)
    print(tieneVocales)

    print()

    print ("Se creara un nombre de usuario de acuerdo a tu nombre, apellido y matricula")
    nombre = input("Escribe tu nombre: ")
    apellidoPaterno = input("Escribe tu apellido aterno: ")
    matrícula = input("Escribe tu matricula: ")
    nombreUsuario = formarNombreUsuario(nombre, apellidoPaterno, matrícula)
    print(nombreUsuario)

    print()

    nombrePersona = input("Escribe tu nombre y tu apellido y te dire si esta bien escrito o no: ")
    nombreUsuario = esCorrecto(nombrePersona)
    print(nombreUsuario)

    print()

    numeroTelefono = input("Inserta un codigo de telefono y se pasara a numeros (ejemplo: 01800-YADI-FUENTES): ")
    telefonoTraducido = traducirTelefono(numeroTelefono)
    print(telefonoTraducido)


main()