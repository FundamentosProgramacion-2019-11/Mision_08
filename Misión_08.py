# Autor: Ronaldo Estefano lira Buendia
# Ejercicio de cadenas


def combinarLetras(cadena):
    totalPalabras = len(cadena)
    x = ''
    for y in range(0, totalPalabras):
        z = cadena[y]
        if y % 2 == 0:
            Mayuscula = z.upper()
            x = x + Mayuscula
        else:
            minuscula = z.lower()
            x = x + minuscula
    return x


def contieneLasVocales(cadena2):
    vocales = cadena2.lower()
    if "a" in vocales and "e" in vocales and "i" in vocales and "o" in vocales and "u" in vocales:
        return "True"
    else:
        return "False"


def formarNombreUsuario(nombre, apellido, matricula):
    nom = nombre[:3:]
    apell = apellido[0:3:]
    matri = matricula[5:len(matricula):]
    x = nom + apell + matri
    usuario = x.lower()
    return usuario


def esCorrecto(nombreCompleto):
    nombre2 = nombreCompleto.title()
    if nombre2 == nombreCompleto:
        return "True"
    else:
        return "False"


def traducirTelefono(mensaje):
    mensaje1 = mensaje.replace("A", "2")
    mensaje2 = mensaje1.replace("B", "2")
    mensaje3 = mensaje2.replace("C", "2")
    mensaje4 = mensaje3.replace("D", "3")
    mensaje5 = mensaje4.replace("E", "3")
    mensaje6 = mensaje5.replace("F", "3")
    mensaje7 = mensaje6.replace("G", "4")
    mensaje8 = mensaje7.replace("H", "4")
    mensaje9 = mensaje8.replace("I", "4")
    mensaje10 = mensaje9.replace("J", "5")
    mensaje11 = mensaje10.replace("K", "5")
    mensaje12 = mensaje11.replace("L", "5")
    mensaje13 = mensaje12.replace("M", "6")
    mensaje14 = mensaje13.replace("N", "6")
    mensaje15 = mensaje14.replace("O", "6")
    mensaje16 = mensaje15.replace("P", "7")
    mensaje17 = mensaje16.replace("Q", "7")
    mensaje18 = mensaje17.replace("R", "7")
    mensaje19 = mensaje18.replace("S", "7")
    mensaje20 = mensaje19.replace("T", "8")
    mensaje21 = mensaje20.replace("U", "8")
    mensaje22 = mensaje21.replace("V", "8")
    mensaje23 = mensaje22.replace("W", "9")
    mensaje24 = mensaje23.replace("X", "9")
    mensaje25 = mensaje24.replace("Y", "9")
    mensaje25 = mensaje25.replace("Z", "9")

    return mensaje25

def main():
    cadena = input("Inserte palabra/as en minuscula: ")
    combinarLetras(cadena)
    cadena2 = input("Inserte palabra: ")
    contieneLasVocales(cadena2)
    nombre = input("Inserte su nombre: ")
    apellido = input("Ingrese su apellido: ")
    matricula = input("Ingrese su matricula: ")
    formarNombreUsuario(nombre, apellido, matricula)
    nombreCompleto = input("Inserte su nombre completo: ")
    esCorrecto(nombreCompleto)
    mensaje = input("Introduce tu mensaje, recuerda que despues de cada palabra poner guion y como el ejemplo 01800-XXX-XXX: ")
    traducirTelefono(mensaje)
    print(combinarLetras(cadena))
    print(contieneLasVocales(cadena2))
    print(formarNombreUsuario(nombre, apellido, matricula))
    print(esCorrecto(nombreCompleto))
    print(traducirTelefono(mensaje))


main()