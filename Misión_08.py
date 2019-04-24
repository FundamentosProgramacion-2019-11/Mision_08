#Autor: María Fernanda García Gastélum A01376181, grupo 03
#Completar misión 8


def combinarLetras(cadena):
    may = cadena.upper() #Convierte en mayúscula
    min = cadena.lower() #Convierte en minúscula
    nuevaCadena= "" #Empieza acumulador
    if len(cadena)% 2 == 0: #determinar si el número de letras en la cadena es par
        for letra in range(0, len(cadena), 2):
            nuevaCadena= nuevaCadena + may[letra] + min[letra+1] #Acumular en la nueva cadena
    else:
        cadenaImpar = cadena + " " #No funcionaba con numero impar, agregar un espacio para volverlo par
        minImpar = cadenaImpar.lower()
        for letra in range(0, len(cadenaImpar), 2):
            nuevaCadena= nuevaCadena + may[letra] + minImpar[letra+1]

    return nuevaCadena


def contieneLasVocales(cadena):
    #Empezar contador para cada vocal, si todas las vocales son mayor a 1, se cumple la condicion
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for vocal in cadena:
        #No puedo poner todas las vocales en un if porque no funcionaría
        if vocal == "a" or vocal == "A" or vocal == "á" or vocal == "Á": #Así no importa si es mayúscula o minúscula o si tiene acentos
            a += 1
        elif vocal == "e" or vocal == "E" or vocal == "é" or vocal == "É":
            e += 1
        elif vocal == "i" or vocal == "I" or vocal == "í" or vocal == "Í":
            i += 1
        elif vocal == "o" or vocal == "O" or vocal == "ó" or vocal == "Ó":
            o += 1
        elif vocal == "u" or vocal == "U" or vocal == "ú" or vocal == "Ú":
            u += 1
    if a >= 1 and e >= 1 and i >= 1 and o >= 1 and u >= 1: #Verificar que tenga todas las vocales
        return True
    else:
        return False


def formarNombreUsuario(nombre, apellido, matricula):
    nombreMin = nombre.lower() #convierte en minuscula
    apellidoMin = apellido.lower()
    nuevaMatricula = str(matricula)
    usuario = nombreMin[0:3:1] + apellidoMin[0:3:1] + nuevaMatricula[4::]
    return usuario


def esCorrecto(nombreCompleto):
    nombre = nombreCompleto
    separados = nombre.split() #esto separa las palabras
    resultado = True
    for palabra in separados:
        #definir cual es la primera letra de cada palabra
        primeraLetra = palabra[0:1:]
        otrasLetras = palabra[1::]
        if primeraLetra.islower() or otrasLetras.isupper():
            resultado = False

    return resultado


def traducirTelefono(numero):
    #hay que hacer que el número se vuelva string
    nNumero = str(numero)
    #directorio para telefono
    n2 = ["A", "B", "C"]
    n3 = ["D", "E", "F"]
    n4 = ["G", "H", "I"]
    n5 = ["J", "K", "L"]
    n6 = ["M", "N", "O"]
    n7 = ["P", "Q", "R", "S"]
    n8 = ["T", "U", "V"]
    n9 = ["W", "X", "Y", "Z"]
    #Empieza acumulador
    nuevoNumero= "01800" + "-"
    for n in nNumero[0::]:
        #Ver si la letra está dentro de nuestro directorio y su equivalente en número
        if n in n2:
            #Sumar esto al acumulador
            nuevoNumero += "2"
        elif n in n3:
            nuevoNumero += "3"
        elif n in n4:
            nuevoNumero += "4"
        elif n in n5:
            nuevoNumero += "5"
        elif n in n6:
            nuevoNumero += "6"
        elif n in n7:
            nuevoNumero += "7"
        elif n in n8:
            nuevoNumero += "8"
        elif n in n9:
            nuevoNumero += "9"
        elif n == "-":
            nuevoNumero += "-"
    return nuevoNumero


def main():
    #cadena = "Abuelito"
    #combinarLetras(cadena)
    #contieneLasVocales(cadena)
    #nombre = input("Escribe tu nombre: ")
    #apellido = input("Escribe tu apellido paterno: ")
    #matricula = input("Escribe tu matrícula sin 'A0': ")
    #formarNombreUsuario(nombre, apellido, matricula)
    #nombreCompleto = input("Escribe tu nombre completo: ")
    #print(esCorrecto(nombreCompleto))
    #numero = input("Escribe la cadena en formato (01800-XXX-XXX): 01800-")
    #traducirTelefono(numero)


main()