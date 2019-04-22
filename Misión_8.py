# Autor: Roberto Emmanuel González Muñoz A01376803
# Programa que combina letras checa si tiene vocales,
# forma un nombre de usuario y checa si un nombre esta escrito correctamente.


def combinarLetras(cadena):
    counter = 0
    cadenaB = []
    for i in range(len(cadena)):
        counter += 1
        if counter % 2 == 0:
            letra = cadena[i].lower()
            cadenaB.append(letra)
        else:
            letra = cadena[i].upper()
            cadenaB.append(letra)

    cadenaS = (cadenaB[0]+cadenaB[1]+cadenaB[2]+cadenaB[3]+cadenaB[4]+cadenaB[5]+cadenaB[6]
          +cadenaB[7]+cadenaB[8]+cadenaB[9])

    print(cadenaS)
    return cadenaS


def contieneLasVocales(cadena):
    cadena = cadena.lower()
    a = cadena.find("a")
    e = cadena.find("e")
    i = cadena.find("i")
    o = cadena.find("o")
    u = cadena.find("u")

    if (a != -1) and (e != -1) and (i != -1) and (o != -1) and (u != -1):
        return True
    else:
        return False


def formarNombreUsuario(nombre):
    n = nombre.lower()
    nombreUsuario = n.split()

    nombre = nombreUsuario[0]
    apellido = nombreUsuario[1]
    matricula = nombreUsuario[2]
    usuario = (nombre[0:3])+(apellido[0:3])+(matricula[5:8])

    return usuario


def esCorrecto(cadenaNombre):
    cadenaSplit =cadenaNombre.split()
    nombre = cadenaSplit[0]
    apellido1 = cadenaSplit[1]
    apellido2 = cadenaSplit[2]

    n = nombre[0].isupper()
    ap1 = apellido1[0].isupper()
    ap2 = apellido2[0].isupper()

    if (n == True) and (ap1 == True) and (ap2 == True):
        return True
    else:
        return False


def traducirTelefono(numeroFormato):

    numero = numeroFormato.split("-")
    numeroSinFormato = []
    for palabra in range(1, len(numero[1])):
        numeroSinFormato.append("-")
        for letra in numero[palabra]:
            if (letra == "A") or (letra == "B") or (letra == "C"):
                numeroSinFormato.append("2")

            elif (letra == "D") or (letra == "E") or (letra == "F"):
                numeroSinFormato.append("3")

            elif (letra == "G") or (letra == "H") or (letra == "I"):
                numeroSinFormato.append("4")

            elif (letra == "J") or (letra == "K") or (letra == "L"):
                numeroSinFormato.append("5")

            elif (letra == "M") or (letra == "N") or (letra == "O"):
                numeroSinFormato.append("6")

            elif (letra == "P") or (letra == "Q") or (letra == "R") or (letra == "S"):
                numeroSinFormato.append("7")

            elif (letra == "T") or (letra == "U") or (letra == "V"):
                numeroSinFormato.append("8")

            elif (letra == "W") or (letra == "X") or (letra == "Y") or (letra == "Z"):
                numeroSinFormato.append("9")

    numeroFinal = numero[0]+numeroSinFormato[0] + numeroSinFormato[1] + numeroSinFormato[2] + numeroSinFormato[3] + numeroSinFormato[4] + numeroSinFormato[5] + numeroSinFormato[6] + numeroSinFormato[7]+ numeroSinFormato[8]
    print(numeroFinal)

    return numeroFinal


def esValido(password):
    if len(password) >= 8:
        if password.isupper() and password.islower() and password.isalpha() and password.startswith(str):
            for i in range(160, 255):
                if password.count(chr(i)) >= 1:
                    return True
                else:
                    return False


def main():
    cadena = "Hola mundo"
    nombreUsuario = "Roberto González 01376803"
    cadenaNombre2Apellidos = "Roberto González Muñoz"
    numeroTelefonico = "01800-VOY-BIEN"
    password = "Abcd-7635" # True, if abcd1936 False.

    combinarLetras(cadena)
    vocales = contieneLasVocales(cadena)
    usuario = formarNombreUsuario(nombreUsuario)
    es = esCorrecto(cadenaNombre2Apellidos)
    traducirTelefono(numeroTelefonico) # Formato "01800-XXX-XXXX" X = son letras
    esValido(password)

    print(vocales)
    print(usuario)
    print(es)


main()