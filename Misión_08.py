#Autor: Mariana Teyssier Cervantes
#Misión 08 - CADENAS


def combinarLetras(cadena):
    mayusculas = cadena.upper()
    minusculas = cadena.lower()
    combinar = " "
    for letra in range(0, len(cadena), 2):
        combinar = combinar + mayusculas[letra] + minusculas[letra +1]

    print(combinar)


def contieneLasVocales(cadena):
    vocalA = ["a", "A"]
    vocalE = ["e", "E"]
    vocalI = ["i", "I"]
    vocalO = ["o", "O"]
    vocalU = ["u", "U"]
    a=0
    e=0
    i=0
    o=0
    u=0
    for letra in cadena:
        for aVocal in vocalA:
            if aVocal in letra:
                a+=1
        for eVocal in vocalE:
            if eVocal in letra:
                e+=1
        for iVocal in vocalI:
            if iVocal in letra:
                i+=1
        for oVocal in vocalO:
            if oVocal in letra:
                o+=1
        for uVocal in vocalU:
            if uVocal in letra:
                u+=1

    if a >=1 and e >=1 and i >=1 and o >=1 and u >=1:
        print(True)
        return True
    else:
        print(False)
        return False


def formarNombreUsuario(nombre, apellido, matricula):
    nombre = nombre.lower()
    apellido = apellido.lower()
    matricula = str(matricula)
    n = nombre[:3:]
    a = apellido [:3:]
    m = matricula[4:]
    usuario = n + a + m
    print(usuario)


def esCorrecto(cadena):
    nombre = cadena.split()
    for palabra in nombre:
        for letra in palabra[0]:
            if letra.islower():
                print(False)
                return False
        for letra in palabra [1::]:
            if letra.isupper():
                print(False)
                return False
    print(True)
    return True


def traducirTelefono(numeros):
    numeros = str(numeros)
    letras = numeros.upper()
    guion = ["-"]
    N2 = ["A", "B", "C"]
    N3 = ["D", "E", "F"]
    N4 = ["G", "H", "I"]
    N5 = ["J", "K", "L"]
    N6 = ["M", "N", "O"]
    N7 = ["P", "Q", "R", "S"]
    N8 = ["T", "U", "V"]
    N9 = ["W", "X", "Y", "Z"]
    numCompleto = numeros[:5:]

    for letra in letras:
        for numeros in N2:
            if numeros in letra:
                numCompleto += "2"
        for numeros in N3:
            if numeros in letra:
                numCompleto += "3"
        for numeros in N4:
            if numeros in letra:
                numCompleto += "4"
        for numeros in N5:
            if numeros in letra:
                numCompleto += "5"
        for numeros in N6:
            if numeros in letra:
                numCompleto += "6"
        for numeros in N7:
            if numeros in letra:
                numCompleto += "7"
        for numeros in N8:
            if numeros in letra:
                numCompleto += "8"
        for numeros in N9:
            if numeros in letra:
                numCompleto += "9"
        for numeros in guion:
            if numeros in letra:
                numCompleto += "-"
    print(numCompleto)



def main():
    combinarLetras("Hola Mundo")
    contieneLasVocales("Abuelito")
    formarNombreUsuario("Mariana", "Teyssier", 1745234)
    esCorrecto("Mariana Teyssier Cervantes")
    traducirTelefono("01800-VOY-BIEN")


main()