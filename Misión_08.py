# Autor: Juan Carlos Flores García A01376511. Grupo 02.
# Programa que realiza operaciones usando cadenas.

# Función que recibe una cadena y luego regresa otra cadena con las mayúsculas y minúsculas combinadas.
def combinarLetras(cadena):
    contador = 1
    acumulador = ""
    cadena.lower()
    for n in cadena:
        if n == 1:
            n = n.upper()
        elif n == 0:
            n = n.lower()
        acumulador = acumulador + n
        contador =- contador
    return acumulador


# Esta función recibe una cadena y luego regresa True si la cadena contiene todas las vocales y de lo contrario False.
def contieneLasVocales(cadena):
    for n in cadena:
        n.upper()
        if "a" in cadena and "e" in cadena and "i" in cadena and "o" in cadena and "u" in cadena:
            return True
        else:
            return False


# Función que recibe el nombre, apellido y matrícula y luego regresa un nombre de usuario.
def formarNombreUsuario(nombre, apellido, matricula):
    parte1 = nombre[0:3]
    parte2 = apellido[0:3]
    parte3 = matricula[4:7]
    nombreUsuario = parte1 + parte2 + parte3
    return nombreUsuario.lower()


# Función que recibe una cadena con el nombre y apellidos del usuario y verifica que el uso de mayúsculas es correcto.
def esCorrecto(nombre):
    listaNombre = nombre.split()
    for nombre in listaNombre:
        mayuscula = nombre[0:1]
        minuscula = nombre[1]
        if minuscula.islower() and mayuscula.isupper():
            return True
        else:
            return False


# Función que traduce las letras de un número telefónico a números basados en la tabla proporcionada.
def traducirTelefono(telefono):
    numero = ""
    telefono1 = telefono.upper()
    for n in telefono1:
        if n == "-":
            numero = numero + "-"
        if n == "A" or n == "B" or n == "C":
            numero = numero + "2"
        if n == "D" or n == "E" or n == "F":
            numero = numero + "3"
        if n == "G" or n == "H" or n == "I":
            numero = numero + "4"
        if n == "J" or n == "K" or n == "L":
            numero = numero + "5"
        if n == "M" or n == "N" or n == "O":
            numero = numero + "6"
        if n == "P" or n == "Q" or n == "R" or n == "S":
            numero = numero + "7"
        if n == "T" or n == "U" or n == "V":
            numero = numero + "8"
        if n == "W" or n == "X" or n == "Y" or n == "Z":
            numero = numero + "9"
        numeroTraducido = "01800" + numero
    return (numeroTraducido)


# Función principal.
def main():
    combinar = input("Ingresa la palabra a combinar: ")
    combinada = combinarLetras(combinar)
    print(combinada)

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

    telefono = input("Ingresa el teléfono con el formato 01800-XXX-XXXX: ")
    telefonoTraducido = traducirTelefono(telefono)
    print(telefonoTraducido)

# Llamada a la función principal.
main()

