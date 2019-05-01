# Autor: Juan Carlos Flores García A01376511. Grupo 02.
# Programa que realiza operaciones usando cadenas.

# Función que recibe una cadena y luego regresa otra cadena con las mayúsculas y minúsculas combinadas.
def combinarLetras(cadena):
    contarLetras = 1
    acumularLetras = ""
    for n in cadena:
        if contarLetras == -1:
            letra = n.lower()
        elif contarLetras == 1:
            letra = n.upper()
        contarLetras =- contarLetras
        acumularLetras = acumularLetras + letra
    return acumularLetras


# Esta función recibe una cadena y luego regresa True si la cadena contiene todas las vocales y de lo contrario False.
def contieneLasVocales(cadena):
    nuevaCadena = cadena.lower()
    if "a" in nuevaCadena and "e" in nuevaCadena and "i" in nuevaCadena and "o" in nuevaCadena and "u" in nuevaCadena:
        return True
    else:
        return False


# Función que recibe el nombre, apellido y matrícula y luego regresa un nombre de usuario.
def formarNombreUsuario(nombre, apellido, matricula):
    usuarioParte1 = str(nombre)[0:3]
    usuarioParte2 = str(apellido)[0:3]
    usuarioParte3 = str(matricula)[4:7]
    nombreUsuario = usuarioParte1.lower() + usuarioParte2.lower() + usuarioParte3
    return nombreUsuario


# Función que recibe una cadena con el nombre y apellidos del usuario y verifica que el uso de mayúsculas es correcto.
def esCorrecto(nombre):
    listaNombre = nombre.split()
    acumulador = 0
    for nombre in listaNombre:
        minusculas = nombre[1:]
        if minusculas.islower() and nombre[0].isupper():
            acumulador = acumulador + 1
    if acumulador == 3:
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
