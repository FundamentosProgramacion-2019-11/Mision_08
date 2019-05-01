# Autor: Sofía Daniela Méndez Sandoval, A01242259, Grupo 03.
# Descripción: Misión 8 - Corrección

def combinarLetras(palabra):
    lMa = palabra.upper()
    lMi = palabra.lower()
    pC = ""
    uE = " "

    if len(palabra) % 2 == 0:
        for caracter in range(0, len(palabra), 2):
            pC = pC + lMa[caracter] + lMi[caracter + 1]

    else:
        pP = palabra + uE
        pPm = pP.lower()
        for caracter in range(0, len(pP), 2):
            pC = pC + lMa[caracter] + pPm[caracter + 1]

    lC = len(pC)

    if pC[lC - 1] == " ":
        pC = pC[:lC-1]

    print(pC)

    return pC


def contieneLasVocales(palabra):
    palabra = palabra.lower()
    vocales = ["a", "á", "e", "é", "i", "í", "o", "ó", "u", "ú"]

    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    for caracter in palabra:
        for vA in vocales[0:2]:
            if vA in caracter:
                a += 1
        for vE in vocales[2:4]:
            if vE in caracter:
                e += 1
        for vI in vocales[4:6]:
            if vI in caracter:
                i += 1
        for vO in vocales[6:8]:
            if vO in caracter:
                o += 1
        for vU in vocales[8:10]:
            if vU in caracter:
                u += 1

    if a > 0 and e > 0 and i > 0 and o > 0 and u > 0:
        print("TRUE")

        return True

    else:
        print("FALSE")

        return False


def formarNombreUsuario(nombre, apellido, matricula):
    nombre = nombre.lower()
    apellido = apellido.lower()
    matricula = str(matricula)

    usuario = nombre[:3:] + apellido[:3:] + matricula[4::]

    print(usuario)

    return usuario


def esCorrecto(nombre):
    nombre = nombre.split()

    for palabra in nombre:
        pL = palabra[0]
        pR = palabra[1::]

        if pL.islower() or pR.isupper():
            return False

    return True


def traducirTelefono(telefono):
    telefono = str(telefono)
    telefono = telefono.upper()

    n2 = ["A", "B", "C"]
    n3 = ["D", "E", "F"]
    n4 = ["G", "H", "I"]
    n5 = ["J", "K", "L"]
    n6 = ["M", "N", "O"]
    n7 = ["P", "Q", "R", "S"]
    n8 = ["T", "U", "V"]
    n9 = ["W", "X", "Y", "Z"]

    tN = telefono[:5:]

    for letra in telefono:

        for numero in n2:
            if numero in letra:
                tN += "2"

        for numero in n3:
            if numero in letra:
                tN += "3"

        for numero in n4:
            if numero in letra:
                tN += "4"

        for numero in n5:
            if numero in letra:
                tN += "5"

        for numero in n6:
            if numero in letra:
                tN += "6"

        for numero in n7:
            if numero in letra:
                tN += "7"

        for numero in n8:
            if numero in letra:
                tN += "8"

        for numero in n9:
            if numero in letra:
                tN += "9"

        if "-" in letra:
            tN += "-"

    print(tN)

    return tN