# Jose Luis Mata Lomeli; A01377205
# Mision 8: Cadenas

#1: Recibe una cadena y regresa una nueva alternando mayuscula y minuscula.
# La cadena resultante siempre inicia mayuscula
def combinarLetras(palabra):
    mayus = palabra.upper()
    min = palabra.lower()
    combinar = ""

    if len(palabra) % 2 ==0:
        for letra in range(0, len(palabra), 2): # Para cada letra desde el inicion de la palabra al final, de 2 en 2...
            combinar = combinar + mayus[letra] + min[letra + 1]

    else:
        cadenaModificada = palabra + " "  # Hace una nueva cadena con un espacio extra que le permite correr al programa sin un indice inexistente
        cadenaMinusModificada = cadenaModificada.lower()
        for letra in range(0, len(cadenaModificada), 2):
            palabra = palabra + mayus[letra] + cadenaMinusModificada[letra + 1]

    return combinar


#2: Recibe una cadena y regresa TRUE si la cadena contiene TODAS las VOCALES
def contieneLasVocales(palabra):

    vocalA = ["a", "á", "A", "Á"]
    vocalE = ["e", "é", "E", "É"]
    vocalI = ["i", "í", "I", "Í"]
    vocalO = ["o", "ó", "O", "Ó"]
    vocalU = ["u", "ú", "U", "Ú"]

    a = 0
    e = 0
    i = 0
    o = 0
    u = 0


    for letra in palabra:

        for vocal in vocalA:
            if vocal in letra:
                a += 1

        for vocal in vocalE:
            if vocal in letra:
                e += 1

        for vocal in vocalI:
            if vocal in letra:
                i += 1

        for vocal in vocalO:
            if vocal in letra:
                o += 1

        for vocal in vocalU:
            if vocal in letra:
                u += 1

    if a >= 1 and e >= 1 and i >= 1 and o >= 1 and u >= 1:
        return True
    else:
        return False



#3: Recibe 3 parametros: Nombre, A.Pat y Matricula entera (7 digitos)
# Regresa: los 3 primeros caracteres del nombre + los 3 primeros del Apellido + los 3 primeros de la Matricula
def formarNombreUsuario(nombre, apellido, matricula):

    nombre = nombre.lower() #Transformar nombre y apellido a minuscula
    apellido = apellido.lower()
    matricula = str(matricula)  #Convertir la matricula a un string

    nombreUsuario = nombre[:3]
    apellidoUsuario = apellido[:3]
    matriculaUsuario = matricula[4:7]

    Usuario = nombreUsuario + apellidoUsuario + matriculaUsuario

    return Usuario


#4: Recibe una cadena que representa el nombre de la persona (nombre y apellidos).
# Regresa TRUE si la letra inicial de cada palabra es Mayuscula y lo demas minuscula
def esCorrecto(cadena):
    nombre = cadena.split()
    for palabra in nombre:
        for letra in palabra[0]:
            if letra.islower():
                return False

        for letra in palabra[1::]:
            if letra.isupper():
                return False

    return True


#5 Recibe un numero telefonico en el formato "01800-XXX-XXXX" y regresa los digitos numericos
# Ejem: 01800-VOY-BIEN = 01800-869-2436
def traducirTelefono(numero):
    num = str(numero)   #String
    letras = num.upper()

    tecla2 = ["A", "B", "C"]
    tecla3 = ["D", "E", "F"]
    tecla4 = ["G", "H", "I"]
    tecla5 = ["J", "K", "L"]
    tecla6 = ["M", "N", "O"]
    tecla7 = ["P", "Q", "R", "S"]
    tecla8 = ["T", "U", "V"]
    tecla9 = ["W", "X", "Y", "Z"]
    guion = ["-"]
    numCompleto = num[:5:]

    for i in letras:
        for numeros in guion:
            if numeros == i:
                numCompleto += "-"

        for numeros in tecla2:
            if numeros == i:
                numCompleto += "2"

        for numeros in tecla3:
            if numeros == i:
                numCompleto += "3"

        for numeros in tecla4:
            if numeros == i:
                numCompleto += "4"

        for numeros in tecla5:
            if numeros == i:
                numCompleto += "5"

        for numeros in tecla6:
            if numeros == i:
                numCompleto += "6"

        for numeros in tecla7:
            if numeros == i:
                numCompleto += "7"

        for numeros in tecla8:
            if numeros == i:
                numCompleto += "8"

        for numeros in tecla9:
            if numeros == i:
                numCompleto += "9"

    return numCompleto



def main():

    print(combinarLetras("hola todos"))
    print(contieneLasVocales("Abecedario"))
    print(formarNombreUsuario("Agustin", "Mata", 1377205))
    print(esCorrecto("Agustin Mata Lomeli"))
    print(traducirTelefono("01800-VOY-BIEN"))

main()

