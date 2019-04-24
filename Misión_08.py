# Mariana Coria Rodríguez, A01374765
# Misión 08, cadenas

# Divide restando y calcula el mayor de un conjunto de números
def combinarLetras(cadena):
    cadenaFinal = ""
    for n in range(0, len(cadena)):
        if n % 2 == 0:
            cadenaFinal += cadena[n].upper()
        else:
            cadenaFinal += cadena[n].lower()
    return cadenaFinal


#Identificar si una palabra contiene todas la vocales
def contieneLasVocales(cadena):
    cadena = cadena.lower()
    a = False
    e = False
    i = False
    o = False
    u = False

    for n in cadena:
        if n == "a" or n == "á":
            a = True
        if n == "e" or n == "é":
            e = True
        if n == "i" or n == "í":
            i = True
        if n == "o" or n == "ó":
            o = True
        if n == "u" or n == "ú":
            u = True

    return a and e and i and o and u


#recibir tres parametros y regresar uno combinado
def formarNombreUsuario(nombre, apellido, matricula):
    return nombre.lower()[0:3] + apellido.lower()[0:3] + str(matricula)[5:]


#Seguir reglas de mayusculas
def esCorrecto(cadena):
    contador = 0
    for n in cadena:
        if n.isupper():
            contador = contador + 1
        if n.isspace():
            contador = contador - 1
    return contador is 1


# recibir un numero y regresarlo con formato de letras
def traducirTelefono(cadena):
    cadena = cadena.upper()
    mensajefinal = "01800-"
    for n in cadena[6:]:
        if n == "A" or n == "B" or n == "C":
            mensajefinal += "2"
        elif n == "D" or n == "E" or n == "F":
            mensajefinal += "3"
        elif n == "G" or n == "H" or n == "I":
            mensajefinal += "4"
        elif n == "J" or n == "K" or n == "L":
            mensajefinal += "5"
        elif n == "M" or n == "N" or n == "O":
            mensajefinal += "6"
        elif n == "P" or n == "Q" or n == "R" or n == "S":
            mensajefinal += "7"
        elif n == "T" or n == "U" or n == "V":
            mensajefinal += "8"
        elif n == "W" or n == "X" or n == "Y" or n == "Z":
            mensajefinal += "9"
        else:
            mensajefinal += "-"
    return mensajefinal


#verificar si la contraseña es valida
def esValido(cadena):
    mayuscula = False
    minuscula = False
    especial = False
    digito = False
    digitoConsecutivo = True
    digitoPasado = 22
    for n in cadena:
        if n.isalpha():
            if n == n.upper():
                mayuscula = True
            if n == n.lower():
                minuscula = True
        else:
            if not n.isalnum():
                especial = True
            if n.isdigit():
                digito = True
                if int(n) - 1 == digitoPasado:
                    digitoConsecutivo = False
    return (len(cadena) > 8) and (cadena[0].isalpha()) and mayuscula and minuscula and especial and digito and \
           digitoConsecutivo

'''
def main():
    if combinarLetras("Hola mundo") == "HoLa mUnDo":
        print("correcto combinar letras")
    else:
        print("error combinar letras")
    combinarLetras("Hola como estas")

    if contieneLasVocales("Monterrey") is False:
        print("correcto vocales")
    else:
        print("error vocales")

    if contieneLasVocales("Abuelito") is True:
        print("correcto vocales")
    else:
        print("error vocales")
    contieneLasVocales("áeiou")

    if formarNombreUsuario("Roberto", "Martinez", 12345678) == "robmar678":
        print("correcto nombre usuario")
    else:
        print("error nombre usuario")

    if esCorrecto("Roberto Martinez Roman") is True:
        print("correcto es correcto")
    else:
        print("error es correcto")

    if esCorrecto("RobErto MartInez RomAn") is False:
        print("correcto vocales")
    else:
        print("error es correcto")

    if traducirTelefono("01800-VOY-BIEN") == "01800-869-2436":
        print("correcto TELEFONO")
    else:
        print("error telefono")
    traducirTelefono("01800-BDG-JMPT")

    if esValido("Abcd-7635") is True:
        print("correcto es valido")
    else:
        print("error es valido")

    if esValido("abcd1936") is False:
        print("correcto es valido")
    else:
        print("error es valido")


main()
'''
