#Autor: José Luis Macías Vázquez, Grupo 03
# 1. Escribir una cadena y regresa la cadena alternando mayúsculas y minúsculas, la primera letra de la cadena que regresa
# siempre es mayúscula 2. Pide una cadena y entrega la verdadeo o falso según tenga todas las vocales o no.



def combinarLetras(palabras):

    acumulador = ""

    contador = 1

    for idx in palabras:

        if contador == 1:

            idx = idx.upper ()

        elif contador == 0:

            idx = idx.lower()

        acumulador = acumulador + idx

        contador =- contador

    return(acumulador)


def contineLasVocales(palabras):

    cambiarAMinusculas = palabras.lower()

    a = "a"

    e = "e"

    i = "i"

    o = "o"

    u = "u"



    if a in cambiarAMinusculas and e in cambiarAMinusculas and i in cambiarAMinusculas and o in cambiarAMinusculas and u in cambiarAMinusculas:


            return True

    else:


            return False


def formarNombreUsuario(nombre, apellido, matricula):

    nombre = nombre.lower()

    apellido = apellido.lower()

    matricula = matricula

    user = nombre[0:4] + apellido[0:3] + matricula[4:8]

    return (user)

def esCorrecto(nombreCompleto):

    nombre = nombreCompleto.split()

    for palabra in nombre:

        letrasMinuscula = palabra[1:]

        letrasMayusculas = palabra[0:1]

        if letrasMayusculas.isupper() and letrasMinuscula.islower():

            return True

        else:

            return False

def traducirTelefono(palabras):

    palabras = palabras.lower()

    num = ""

    for x in palabras:

        if x == "a" or x == "b" or x == "c":

            num = num + "2"

        if x == "d" or x == "e" or x == "f":

            num = num + "3"

        if x == "g" or x == "h" or x == "i":

            num = num + "4"

        if x == "j" or x == "k" or x == "l":

            num = num + "5"

        if x == "m" or x == "n" or x == "o":

            num = num + "6"

        if x == "p" or x == "q" or x == "r" or x == "s":

            num = num + "7"

        if x == "t" or x == "u" or x == "v":

            num = num + "8"

        if x == "w" or x == "x" or x == "y" or x == "z":

            num = num + "9"

        if x == "-":

            num = num + "-"

    return (" 01800 - ", num)




def main():

    palabras = input("Escribe una cadena para tansformar: ")
    print (combinarLetras(palabras))

    palabras =  input("Escribe una cadena para analizar (sin acentos en las vocales): ")
    print(contineLasVocales(palabras))

    nombre = input("Escribe tu nombre: ")
    apellido = input("Escribe tu apellido paterno: ")
    matricula = str(input("Escribe tu matrícula entera: "))
    print("Su nombre de usuario es: " + formarNombreUsuario(nombre, apellido, matricula))

    nombreCompleto = input("Escribe tu nombre completo: ")
    print (esCorrecto(nombreCompleto))

    palabras = input("Escribe las palabras del telefono: ")
    print(traducirTelefono(palabras))


main()