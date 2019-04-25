# Autor: Juan Carlos Flores García A01376511. Grupo 02.
# Descripción: Programa que genera figuras, realiza operaciones, e imprime un menu con diferentes opciones a elegir.

def combinarLetras(cadena):
    acumulador = ""
    str(cadena)
    cadena.lower()
    for n in cadena:
        if(n % 2) != 0:
            letra = n.upper()
            acumulador = acumulador + letra
    return acumulador

def contieneLasVocales(cadena):
    for n in cadena:
        n.upper()
        if "a" in cadena and "e" in cadena and "i" in cadena and "o" in cadena and "u" in cadena:
            return True
        else:
            return False


def formarNombreUsuario(nombre, apellido, matricula):
    parte1 = nombre[0:3]
    parte2 = apellido[0:3]
    parte3 = matricula[4:7]
    nombreUsuario = parte1 + parte2 + parte3
    return nombreUsuario.lower()


def esCorrecto(nombre):
    listaNombre = nombre.split()
    for nombre in listaNombre:
        mayuscula = nombre[0:1]
        minuscula = nombre[1]
        if minuscula.upper() or mayuscula.islower():
            return True
        else:
            return False



def main():
    #combinar = combinarLetras("HolaMundo")
    #print(combinar)

    vocal = input("Ingresa la palabra: ")
    print(contieneLasVocales(vocal))

    nombreUsuario = input("Ingresa tu nombre: ")
    apellidoUsuario = input("Ingresa tu apellido paterno: ")
    matriculaUsuario = input("Ingresa tu matrícula de 7 dígitos: ")
    cuentaUsuario = formarNombreUsuario(nombreUsuario, apellidoUsuario, matriculaUsuario)
    print(cuentaUsuario)

    nombre = input("Ingresa tu primer nombre y tus dos apellidos: ")
    nombreCorrecto = esCorrecto(nombre)
    print(nombreCorrecto)


main()
