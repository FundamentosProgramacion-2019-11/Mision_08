# Autor: Rosalía Serrano Herrera
# Ejercicios de cadenas

def combinarLetras(cadenaCombinados):
    combinada = ""
    contador = 1

    for palabra in cadenaCombinados:
        if contador == 1:
            letra = palabra.upper()
            combinada = combinada + letra
            contador =- contador
        else:
            letra = palabra.lower()
            combinada = combinada + letra
            contador =- contador

    print(combinada)


def contieneLasVocales(cadenaVocales):
    cadenaVocales.lower()
    vocales = ["a" and "e" and "i" and "o" and "u"]

    for palabra in vocales:
        if palabra in cadenaVocales:
            return True
        else:
            return False


def formarNombreUsuario(nombre, apellido, matricula):
    nombreMinus = nombre.lower()
    apellidoMinus = apellido.lower()
    strMatricula = str(matricula)
    usuarioNombre = nombreMinus[:3:]
    usuarioApellido = apellidoMinus[:3:]
    usuarioMatricula = strMatricula[4:]
    formato = usuarioNombre + usuarioApellido + usuarioMatricula

    return formato


def esCorrecto(nombrePersona):
    nombre = nombrePersona.split()

    for palabra in nombre:
        for primera in palabra[0:1]:
            primera.isupper()

    for palabra in nombre:
        for restantes in palabra[1:]:
            restantes.islower()

    if primera.isupper() and restantes.islower():
        return True
    else:
        return False


def traducirTelefono(numeroTelefonico):
    numeroEscrito = numeroTelefonico[5:]
    dos = ["A", "B", "C"]
    tres = ["D", "E", "F"]
    cuatro = ["G", "H", "I"]
    cinco = ["J", "K", "L"]
    seis =["M", "N", "O"]
    siete = ["P", "Q", "R", "S"]
    ocho = ["T", "U", "V"]
    nueve = ["W", "X", "Y", "Z"]
    guion = ["-"]
    numeroNuevo = "01800" + ""

    for numero in numeroEscrito:
        for letra in dos:
            if letra in numero:
                numeroNuevo += "2"
        for letra in tres:
            if letra in numero:
                numeroNuevo += "3"
        for letra in cuatro:
            if letra in numero:
                numeroNuevo += "4"
        for letra in cinco:
            if letra in numero:
                numeroNuevo += "5"
        for letra in seis:
            if letra in numero:
                numeroNuevo += "6"
        for letra in siete:
            if letra in numero:
                numeroNuevo += "7"
        for letra in ocho:
            if letra in numero:
                numeroNuevo += "8"
        for letra in nueve:
            if letra in numero:
                numeroNuevo += "9"
        for letra in guion:
            if letra in numero:
                numeroNuevo += "-"

    return numeroNuevo


def esValido(password):
    resultado = 0

    if len(password)>=8:
        resultado += 1

    for caracter in password:
        if caracter.isupper():
            resultado += 1
        elif caracter.islower():
            resultado += 1

    if password.isalnum():
        resultado += 1

    if password.isalpha():
        resultado += 1

    if password[:1].isalpha():
        resultado += 1

    if resultado == 6:
        return True
    else:
        return False


def main():
    cadenaCombinados = input("Escribe alguna cadena: ")
    combinarLetras(cadenaCombinados)

    cadenaVocales = input("Ingresa una cadena: ")
    print(contieneLasVocales(cadenaVocales))

    nombre = input("Escribe un nombre: ")
    apellido = input("Escribe un apellido paterno: ")
    matricula = int(input("Escribe una matrícula (SIN A0): "))
    print(formarNombreUsuario(nombre, apellido, matricula))

    nombrePersona = input("Escribe un nombre con apellidos: ")
    print(esCorrecto(nombrePersona))

    numeroTelefonico = input("Ingrea un número de teléfono en formato 01800-XXX-XXXX: " )
    print(traducirTelefono(numeroTelefonico))

    password = input("Teclea un password: ")
    print(esValido(password))


main()