# Autor: Mario Hernández Cárdenas, A01375869
# Misión_08, Tarea sobre cadenas


def combinarLetras(cadena):
    cadenaMayusculas = cadena.upper()
    cadenaMinusculas = cadena.lower()
    palabra = ""
    if len(cadena) % 2 == 0:
        for letra in range(0, len(cadena), 2):
            palabra = palabra + cadenaMayusculas[letra] + cadenaMinusculas[letra + 1]
    else:
        cadenaModificada = cadena + " "  # Hace una nueva cadena con un espacio extra que le permite correr al programa sin un indice inexistente
        cadenaMinusModificada = cadenaModificada.lower()
        for letra in range(0, len(cadenaModificada), 2):
            palabra = palabra + cadenaMayusculas[letra] + cadenaMinusModificada[letra + 1]
    print(palabra)


def contieneLasVocales(cadena):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    letraA = ["a", "á", "A", "Á"]
    letraE = ["e", "é", "E", "É"]
    letraI = ["i", "í", "I", "Í"]
    letraO = ["o", "ó", "O", "Ó"]
    letraU = ["u", "ú", "U", "Ú"]
    for letra in cadena:
        for aLetra in letraA:
            if aLetra in letra:
                a += 1
                print("a =", a)
        for eLetra in letraE:
            if eLetra in letra:
                e += 1
                print("e =", e)
        for iLetra in letraI:
            if iLetra in letra:
                i += 1
                print("i = ", i)
        for oLetra in letraO:
            if oLetra in letra:
                o += 1
                print("o =", o)
        for uLetra in letraU:
            if uLetra in letra:
                u += 1
                print("u =", u)

    if a >= 1 and e >= 1 and i >= 1 and o >= 1 and u >= 1:
        print(True)
        return True
    else:
        print(False)
        return False


def formarNombreUsuario(nombre, apellido, matricula):
    nombre = nombre.lower()
    apellido = apellido.lower()
    matricula = str(matricula)
    nom = nombre[:3:]
    ape = apellido[:3:]
    mat = matricula[5::]
    usuario = nom + ape + mat
    print(usuario)


def esCorrecto(nombre):
    nombreSeparado = nombre.split()
    for palabra in nombreSeparado:
        for letra in palabra[0]:
            if letra.islower():
                print(False)
                return False
        for letra in palabra[1::]:
            if letra.isupper():
                print(False)
                return False
    print(True)
    return True


def traducirTelefono(numero):
    numero = str(numero)
    numeroConLetras = numero.upper()
    numero2 = ["A", "B", "C"]
    numero3 = ["D", "E", "F"]
    numero4 = ["G", "H", "I"]
    numero5 = ["J", "K", "L"]
    numero6 = ["M", "N", "O"]
    numero7 = ["P", "Q", "R", "S"]
    numero8 = ["T", "U", "V"]
    numero9 = ["W", "X", "Y", "Z"]
    guion = ["-"]
    numeroBien = numero[:5:]
    for letra in numeroConLetras:
        for numero in numero2:
            if numero in letra:
                numeroBien += "2"
        for numero in numero3:
            if numero in letra:
                numeroBien += "3"
        for numero in numero4:
            if numero in letra:
                numeroBien += "4"
        for numero in numero5:
            if numero in letra:
                numeroBien += "5"
        for numero in numero6:
            if numero in letra:
                numeroBien += "6"
        for numero in numero7:
            if numero in letra:
                numeroBien += "7"
        for numero in numero8:
            if numero in letra:
                numeroBien += "8"
        for numero in numero9:
            if numero in letra:
                numeroBien += "9"
        for numero in guion:
            if numero in letra:
                numeroBien += "-"
    print(numeroBien)


# EXTRA
def esValido(contrasena):
    reglasCumplidas = 0
    letraMayuscula = 0
    letraMinuscula = 0
    digito = 0
    # 1. Tiene 8 caracteres o más
    if len(contrasena) >= 8:
        reglasCumplidas += 1

    # 3. Contiene al menos un carácter especial
    if not contrasena.isalnum():
        reglasCumplidas += 1

    # 2. Contiene al menos una mayúscula y una minúscula
    # 4. Además contiene al menos 1 dígito
    for letra in contrasena:
        if letra.isupper():
            letraMayuscula += 1
        elif letra.islower():
            letraMinuscula += 1
        elif letra.isnumeric():
            digito += 1
    if letraMayuscula >= 1 and letraMinuscula >= 1 and digito >= 1:
        reglasCumplidas += 2

    # 5. Comienza con una letra
    for caracter in contrasena[0]:
        if not caracter.isnumeric():
            reglasCumplidas += 1

    # 6. No contiene dígitos consecutivos
    vezSeparado = 0
    contrasenaSeparada = ""
    for caracter in contrasena:
        if caracter.isnumeric():
            while vezSeparado == 0:
                vezSeparado += 1
                contrasenaSeparada = contrasena.split(caracter)

    # Comprueba que la cadena tenga solo numeros
    soloNumeros = ""
    for caracter in contrasenaSeparada[1]:
        if caracter.isnumeric():
            soloNumeros += caracter

    # Obtiene el par de números consecutivos
    segundoNumero = soloNumeros[0]
    numeroAntecesor = str(int(segundoNumero) - 1)
    numerosConsecutivos = numeroAntecesor + segundoNumero
    if not numerosConsecutivos in contrasena:
        reglasCumplidas += 1

    # Comprueba que todas las reglas se hayan cumplido
    if reglasCumplidas == 6:
        print(True)
        return True
    else:
        print(False)
        return False


# Todas las pruebas que hice
'''
# Par e impar
combinarLetras("Hola mundo")
combinarLetras("Hola como estas")


contieneLasVocales("Monterrey")
contieneLasVocales("Abuelitos")
contieneLasVocales("reumático")
contieneLasVocales("escuálido")


formarNombreUsuario("Roberto", "Martínez", 12345678)
formarNombreUsuario("Mario", "Hernández", 1375869)


esCorrecto("Roberto Martínez Román")
esCorrecto("roberto MARtinez RoMan")


# 01-800-XXX-XXXX
# Como nunca encontré la solución a poner el número como entero y cadena, inmediatamente le mandé el número como cadena
traducirTelefono("01800-VOY-BIEN")
traducirTelefono("01800-ADG-JMPT")
traducirTelefono("01800-DGJ-MPTZ")


esValido("Abcd-7635")   # True
esValido("abcd1936")    # False, falta carácter especial
esValido("1513-Abdc")   # False, no empieza con letra
esValido("A123-bcgsd")  # False, tiene números consecutivos
esValido("aBcd-7418")   # True
esValido("Abc-1479")    # True
'''
