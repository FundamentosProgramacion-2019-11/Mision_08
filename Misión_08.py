#Autor : Luis Adrian Carmona Villalobos
#Mision 8

def combinarLetras(cadena):
    num=len(cadena)
    a = ""
    for i in range (num):
        if(i%2!=0):
            impar =cadena[i].lower()
            a = a+impar
        elif (i%2==0):
            par =cadena[i].upper()
            a = a+par
    return a


def contieneLasVocales(cadena2): #detecta si la palabra tiene todas las vocales
    vocales = "AEIOUaeiou"
    newcadena2 = ""
    for i in cadena2:
        if i in vocales:
            newcadena2 = newcadena2 +cadena2
            print(True)
            return newcadena2
        else:
            newcadena2 = newcadena2 +cadena2
            print(False)
            return  newcadena2


def formarNombreUsuario(nombre, apellido, matricula):
    matriculastr = str(matricula)
    newcadena3 = print(nombre.lower()[0:3]+apellido.lower()[0:3]+matriculastr[0:3])
    return newcadena3


def esCorrecto(cadena4):
    if cadena4 == cadena4.title():
        print(True)
    else:
        print(False)

def traducirTelefono(numeroTel):
    num =len(numeroTel)
    acumulador = ""
    for i in range(num):
        if i == "1" or "2" or "3" or "4" or "5" or "0":
            i = "1"
            acumulador += i
        elif num == "A" or "B" or "C":
            num ="2"
            acumulador = acumulador+ num


    return acumulador

def main():
    cadena = input("Escribe la cadena que quieres alternar: ")
    combinarLetras(cadena)
    nueva= combinarLetras(cadena)
    print(nueva)

    cadena2 = input("Escribe una cadena: ")
    contieneLasVocales(cadena2)

    nombre = input("Cual es tu nombre?: ")
    apellido = input("tu apellido paterno?: ")

    matricula = int(input("Su matricula pero solo los 7 digitos enteros: "))
    formarNombreUsuario(nombre,apellido,matricula)

    cadena4 = input("Cual es su nombre completo: ")
    esCorrecto(cadena4)


    numeroTel = str(input("pon tu cadena: "))
    traducirTelefono(numeroTel)
    nueva = traducirTelefono(numeroTel)
    print(nueva)


main()
