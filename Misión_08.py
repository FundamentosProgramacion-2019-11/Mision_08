#Autor: Katia Hernández Barrera
#Descripción: cinco problemas resueltos utilizando cadenas


def combinarLetras(cadena1):
    combinar = " "
    for i in range(len(cadena1)):
        if (i%2 == 0):
            combinar += cadena1[i].upper()
        else:
            combinar += cadena1[i].lower()
    return combinar



def contieneLasVocales(cadena):
    cadena = cadena.lower()
    if "a" in cadena and "e"in cadena and "i" in cadena and "o" in cadena and "u" in cadena:
        return True
    else:
        return False



def formarNombreUsuario(nombre, apellido, matricula):
    nombre = nombre.lower()
    apellido = apellido.lower()
    nom = (nombre[0:3])
    ap = (apellido[0:3])
    mat = (matricula[5:8])
    usuario = nom + ap + mat
    return usuario

def esCorrecto(nombreCompleto):
    nombre = nombreCompleto.split()
    correcto = 0

    for letra in nombre:
        mayuscula = letra[0:1]
        minuscula = letra[1:]
    if minuscula.islower() and mayuscula.isupper():
        correcto += 1

    if correcto == 3:
        return True
    else:
        return False


def traducirTelefono(telefono):
    tel = (telefono[7:14])
    t = " "
    for i in tel:
        if i == "a" or i == "b" or i =="c":
            t += "2"
        elif i == "d" or i == "e" or i == "f":
            t += "3"
        elif i == "g" or i == "h" or i == "i":
            t += "4"
        elif i == "j" or i == "k" or i =="l":
            t += "5"
        elif i == "m" or i == "n" or i == "o":
            t += "6"
        elif i == "p" or i == "q" or i == "r" or i =="s":
            t += "7"
        elif i == "t" or i == "u" or i =="v":
            t += "8"
        elif i == "w" or i =="x" or i == "y" or i == "z":
            t += "9"
        elif i == "-":
            t += "-"
    final = "01800" + t
    return final





def main():
    cadena1 = input("Escribe algo: ")
    combinado = combinarLetras(cadena1)
    print(combinado)
    print("                  ")
    cadena = input("escriba una palabra: ")
    vocales = contieneLasVocales(cadena)
    print(vocales)
    print("                  ")
    nombre = input("¿Cuál es tu nombre?")
    apellido = input("¿Cuál es tu apellido?")
    matricula = input("¿Cuál es tu matrícula?")
    usuario = formarNombreUsuario(nombre, apellido,matricula)
    print(usuario)
    print("                     ")
    nombreCompleto = input("Nombre completo: ")
    correcto = esCorrecto(nombreCompleto)
    print(correcto)
    print("                                ")
    telefono = str(input("Inserte teléfono"))
    traducir = traducirTelefono(telefono)
    print(traducir)





main()