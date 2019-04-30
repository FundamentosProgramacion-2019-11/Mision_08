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


def contieneLasVocales(cadena2):  # detecta si la palabra tiene todas las vocales
    vocales = "aeiuoAEIOU"
    soloVocales = ""
    for letra in cadena2:
        if letra in vocales:
            soloVocales = soloVocales+letra.lower()
    if "a" in soloVocales and "e" in soloVocales and "o" in soloVocales and "u" in soloVocales and "i" in soloVocales:
        return True
    else:
        return False





def formarNombreUsuario(nombre, apellido, matricula):
    nombre = nombre.lower()[0:3]
    apellido = apellido.lower()[0:3]
    newapellido = apellido
    matriculastr = str(matricula)
    matriculastr = matriculastr[4:]
    newnum = matriculastr

    newnameform = nombre + newapellido + newnum
    return newnameform


def esCorrecto(cadena4):
    if cadena4 == cadena4.title():
        return True
    else:
        return False

def traducirTelefono(numeroTel):
    numero = numeroTel
    a =""
    for i in numero:
        if i in "-0123456789":
            a = a + i
        elif i in "ABC":
            a = a + "2"
        elif i in "DEF":
            a = a + "3"
        elif i in "GHI":
            a = a + "4"
        elif i in "JKL":
            a = a + "5"
        elif i in "MNO":
            a = a + "6"
        elif i in "PQRS":
            a = a + "7"
        elif i in "TUV":
            a = a + "8"
        elif i in "WXYZ":
            a = a + "9"
    return a


def main():
    cadena = input("Escribe la cadena que quieres alternar: ")
    combinarLetras(cadena)
    nueva= combinarLetras(cadena)
    print(nueva)



    nombre = input("Cual es tu nombre?: ")
    apellido = input("tu apellido paterno?: ")
    matricula = int(input("Su matricula pero solo los 7 digitos enteros: "))
    new3 = formarNombreUsuario(nombre, apellido, matricula)
    print(new3)


    cadena4 = input("Cual es su nombre completo: ")
    new4 = esCorrecto(cadena4)
    print(new4)


    numeroTel = str(input("pon el numero: "))
    traducirTelefono(numeroTel)
    nueva5 = traducirTelefono(numeroTel)
    print(nueva5)

main()
