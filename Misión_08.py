# Yadira Fuentes Calderón A01745235
# Programa que cumple la funcion de llamar cadenas y cambiar estas

def combinarLetras(cadena):
    contador = 1
    acumulador = ""
    for letra in cadena:
        if contador == 0:
            letra = letra.lower()
        elif contador == 1:
            letra = letra.upper()
        acumulador = acumulador + letra
        contador = -contador
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
    matrícula = matrícula.lower()

    nombreUsuario = nombre[0:3] + apellidoPaterno[0:3] + matrícula[4:7]
    return nombreUsuario


def esCorrecto(nombrePersona):
    separar = nombrePersona.split()
    for nombrePersona in separar:
        letraInicial = nombrePersona[0:1]
        letras = nombrePersona[1]
        if letraInicial.islower() or letras.isupper():
            return False
        else:
            return True


def traducirTelefono(numeroTelefono):
    acumulador = ""
    for numeros in numeroTelefono:
        if "A" == numeros or "B" == numeros or "C" == numeros:
            acumulador = acumulador + "2"
        elif "D" == numeros or "E" == numeros or "F" == numeros:
            acumulador = acumulador + "3"
        elif "G" == numeros or "H" == numeros or "I" == numeros:
            acumulador = acumulador + "4"
        elif "J" == numeros or "K" == numeros or "L" == numeros:
            acumulador = acumulador + "5"
        elif "M" == numeros or "N" == numeros or "O" == numeros:
            acumulador = acumulador + "6"
        elif "P" == numeros or "Q" == numeros or "R" == numeros or "S" == numeros:
            acumulador = acumulador + "7"
        elif "T" == numeros or "U" == numeros or "V" == numeros:
            acumulador = acumulador + "8"
        elif "W" == numeros or "X" == numeros or "Y" == numeros or "Z" == numeros:
            acumulador = acumulador + "9"
        print("01800-" + acumulador)


def main():
    cadena = input("Escribe una frase: ")
    frase = combinarLetras(cadena)
    print(frase)

    print()

    cadenaVocales = input("Escribe otra frase: ")
    tieneVocales = contieneLasVocales(cadenaVocales)
    print(tieneVocales)

    print()

    nombre = input("Escribe tu nombre: ")
    apellidoPaterno = input("Escribe tu apellido aterno: ")
    matrícula = input("Escribe tu matricula: ")
    nombreUsuario = formarNombreUsuario(nombre, apellidoPaterno, matrícula)
    print(nombreUsuario)

    print()

    nombrePersona = input("Escribe tu nombre y tu apellido: ")
    nombrePersona = esCorrecto(nombrePersona)
    print(nombrePersona)

    print()

    numeroTelefono = input("Inserta un codigo de telefono: 01800-")
    telefonoTraducido = traducirTelefono(numeroTelefono)
    print(telefonoTraducido)


main()