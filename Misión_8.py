# Autor: Victor Manuel Cerón Navarrete
# Descripción: Misión 8 Cadena

def combinarLetras(cadena):
    palabra = ""  # funciona de acomulador
    posicionLetra = 1  # Se sumará y restará a si mismo dependiendo de si su posición da 1 o 0
    for n in cadena:
        if posicionLetra == 1:  # Da la primera posición como 1, lo que hace que sea mayuscula

            n = n.upper()
            posicionLetra = 0

        elif posicionLetra == 0:

            n = n.lower()
            posicionLetra = 1

        palabra = palabra + n  # escribe la letra

    return palabra


def contieneLasVocales(palabra):
    letraA = 0
    letraE = 0
    letraI = 0
    letraO = 0
    letraU = 0

    for i in palabra:
        if i == "a" or i == "A":
            letraA = letraA + 1
        elif i == "e" or i == "E":
            letraE = letraE + 1
        elif i == "i" or i == "I":
            letraI = letraI + 1
        elif i == "o" or i == "O":
            letraO = letraO + 1
        elif i == "u" or i == "U":
            letraU = letraU + 1

    if letraA >= 1 and letraE >= 1 and letraI >= 1 and letraO >= 1 and letraU >= 1:
        return True
    else:
        return False


def formarNombreUsuario(nombreUsuario, apellidoUsuario, matriculaUsuario):
    nombreUsuario = nombreUsuario.lower()  # El nombre y apellido los hace todos minúscula
    apellidoUsuario = apellidoUsuario.lower()
    matriculaUsuario = str(matriculaUsuario)
    usuario = nombreUsuario[0:3] + apellidoUsuario[0:3] + matriculaUsuario[4:]
    print("Tu usuario es:", usuario)
    return usuario


def esCorrecto(persona):
    nombre = persona.split()
    for nom in nombre:
        for y in nom[0]:  # y es la primera letra
            if y.islower():
                return False
        for z in nom[1::]:
            if z.isupper():
                return False


    else:
        return True

    # def traducirTelefono(telefono):
    telefono = str(telefono)

    numerodos = ("A", "a", "B", "b", "C", "c")
    numerotres = ("D", "d", "E", "e", "F", "f")
    numerocuatro = ("G", "g", "H", "h", "I", "i")
    numerocinco = ("J", "j", "K", "k", "L", "l")
    numeroseis = ("M", "m", "N", "n", "O", "o")
    numerosiete = ("P", "p", "Q", "q", "R", "r", "S", "s")
    numeroocho = ("T", "t", "U", "u", "V", "v")
    numeronueve = ("W", "w", "X", "x", "Y", "y", "Z", "z")

    solonumeros = telefono[6:]

    for x in solonumeros:
        if

    # No pude prof, perdon :(


def main():
    cadena = str(input("Teclea tu frase: "))
    palabra = str(input("Teclea tu palabra o frase y te diré si contiene todas las vocales: "))
    nombreUsuario = str(input("Escribe tu primer nombre:"))
    apellidoUsuario = str(input("Escribe tu apellido paterno:"))
    matriculaUsuario = str(input("Teclea tu matrícula:"))
    persona = str(input("Teclea un nombre y dos apellidos. Te diré si tus mayúsculas están bien posicionadas:"))
    combinarLetras(cadena)
    contieneLasVocales(palabra)
    formarNombreUsuario(nombreUsuario, apellidoUsuario, matriculaUsuario)
    esCorrecto(persona)
    # traducirTelefono()


