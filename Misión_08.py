#Autor: Aline Villegas Berdejo
#Este programa recibe cadenas y las modifica.


#Recibe una cadena y esa cadena se modifica. Combina letras. Una mayúscula y una minúscula y así sucesivamente en ese orden
def combinarLetras(cadena):
    nuevacad = ""
    for letra in range(0, len(cadena), 1):
        if letra%2 == 0 or letra == 0:
            nuevacad = nuevacad + cadena[letra].upper()
        else:
            nuevacad = nuevacad + cadena[letra].lower()
    return nuevacad


#Recibe una cadena y revisa si tiene todas las vocales y si las tiene regresa True y si no False
def contieneLasVocales(cadena1):
    check = 0
    for letra in cadena1:
        if letra == "a" or letra == "A":
            check = 1

    for letra in cadena1:
        if letra == "e" or letra == "E":
            if check < 2:
                check = check + 1

    for letra in cadena1:
        if letra == "i" or letra == "I":
            if check < 3:
                check = check + 1

    for letra in cadena1:
        if letra == "o" or letra == "O":
            if check < 4:
                check = check + 1

    for letra in cadena1:
        if letra == "u" or letra == "U":
            if check < 5:
                check = check + 1

    if check == 5:
        return True
    else:
        return False


#Recibe parámetros para formar el nombre de un ausuario a partir de los tres primeros caracteres de cada parámetro
def formarNombreUsuario(nombre, apellido, matricula):
    iniciomat = len(matricula) -3

    n1 = nombre[0]
    n2 = nombre[1]
    n3 = nombre[2]

    a1 = apellido[0]
    a2 = apellido[1]
    a3 = apellido[2]

    m1 = matricula[iniciomat]
    m2 = matricula[iniciomat + 1]
    m3 = matricula[iniciomat + 2]

    usuario = n1 + n2 + n3 + a1 + a2 + a3 + m1 + m2 + m3
    return usuario.lower()


#Recibe una cadena (nombre) y revisa si las mayúsuclas están utilizadas de manera correcta. Al principio de cada nombre y apellido
def esCorrecto(cadena2):
    componentes = cadena2.split(" ")
    nombre = componentes[0]
    apellidoPat = componentes[1]
    apellidoMat = componentes[2]
    if nombre[0].isupper() == True:
        if apellidoPat[0].isupper() == True:
            if apellidoMat[0].isupper() == True:
                for x in range(1, len(nombre), 1):
                    if nombre[x].islower():
                        if apellidoPat[x].islower():
                            if apellidoMat[x].islower():
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        else:
            return False
    else:
        return False


#Recibe una cadena que es un numero de teléfono y se traduce a dígitos(números) correspondientes
def traducirTelefono(telefono):
    componentes = telefono.split("-")
    numeros = componentes[0]
    palabra1 = componentes[1]
    palabra1 = palabra1.upper()
    palabra2 = componentes[2]
    palabra2 = palabra2.upper()
    nuevap1 = ""
    nuevap2 = ""

    for letra in palabra1:
        if letra == "A" or letra == "B" or letra == "C":
            nuevap1 = nuevap1 + "2"
        elif letra == "D" or letra == "E" or letra == "F":
            nuevap1 = nuevap1 + "3"
        elif letra == "G" or letra == "H" or letra == "I":
            nuevap1 = nuevap1 + "4"
        elif letra == "J" or letra == "K" or letra == "L":
            nuevap1 = nuevap1 + "5"
        elif letra == "M" or letra == "N" or letra == "O":
            nuevap1 = nuevap1 + "6"
        elif letra == "P" or letra == "Q" or letra == "R" or letra == "S":
            nuevap1 = nuevap1 + "7"
        elif letra == "T" or letra == "U" or letra == "V":
            nuevap1 = nuevap1 + "8"
        elif letra == "W" or letra == "X" or letra == "Y" or letra == "Z":
            nuevap1 = nuevap1 + "9"

    for letra in palabra2:
        if letra == "A" or letra == "B" or letra == "C":
            nuevap2 = nuevap2 + "2"
        elif letra == "D" or letra == "E" or letra == "F":
            nuevap2 = nuevap2 + "3"
        elif letra == "G" or letra == "H" or letra == "I":
            nuevap2 = nuevap2 + "4"
        elif letra == "J" or letra == "K" or letra == "L":
            nuevap2 = nuevap2 + "5"
        elif letra == "M" or letra == "N" or letra == "O":
            nuevap2 = nuevap2 + "6"
        elif letra == "P" or letra == "Q" or letra == "R" or letra == "S":
            nuevap2 = nuevap2 + "7"
        elif letra == "T" or letra == "U" or letra == "V":
            nuevap2 = nuevap2 + "8"
        elif letra == "W" or letra == "X" or letra == "Y" or letra == "Z":
            nuevap2 = nuevap2 + "9"
    nuevotel = numeros + "-" + nuevap1 + "-" + nuevap2
    return nuevotel


#Extra. Revisa que un password tenga las características necesarias si es así regresa true, de lo contrario regresa False.
def esValido(password):
    if len(password) >= 8:
        largo = True
    else:
        largo = False
    mayus = 0
    minus = 0
    mayuscula = False
    minuscula = False
    caracter = False
    digito = False
    for letra in password:
        if letra.isupper():
            mayuscula = True
            mayus = mayus +1
        if mayus == 0:
            mayuscula = False
        if letra.islower():
            minuscula = True
            minus = minus +1
        if minus == 0:
            mayuscula = False
        if letra == "!" or letra == "@" or letra == "#" or letra == "$" or letra == "%" or letra == "&" or letra == "/" or letra == "(" or letra == ")" or letra == "=" or letra == "?" or letra == "¿" or letra == "¡" or letra == "+" or letra == "-" or letra == "_" or letra == "." or letra == "," or letra == "<" or letra == ">":
            caracter = True
        else:
            caracter = False
        if letra == "0" or letra == "1" or letra == "2" or letra == "3" or letra == "4" or letra == "5" or letra == "6" or letra == "7" or letra == "8" or letra == "9" or letra == "10":
        #if letra.isdigit():
            digito = True
        else:
            digito = False
    if password[0].isalpha():
        primera = True
    else:
        primera = False

    if largo == True and mayuscula == True and minuscula == True and caracter == True and digito == True and primera == True:
        return True
    else:
        return False


def main():
    cadena= str(input("Teclea la cadena que quieres combinar (mayúscula, minúscula y así sucesivamente): "))
    print("La combinación es: " , combinarLetras(cadena) , "\n")

    cadena1= str(input("Teclea la cadena que quieres comprobar(si tiene todas las vocales):"))
    print("Contiene las vocales: " , contieneLasVocales(cadena1), "\n")

    nombre= str(input("Tecla tu nombre: "))
    apellido= str(input("Teclea tu apellido paterno: "))
    matricula= str(input("Teclea matrícula de 7 dígitos (únicamente números): "))
    print("Tu usuario es: " , formarNombreUsuario(nombre, apellido, matricula), "\n")

    cadena2 = str(input("Teclea nombre completo (Nombre, Apellido paterno, Apellido materno): "))
    print("Las mayúsculas y minúsculas están acomodadas correctamente? ", esCorrecto(cadena2), "\n")

    telefono = str(input("Teclea un número de teléfono en el formato 01800-XXX-XXXX: "))
    print("El número es:" , traducirTelefono(telefono), "\n")

    password = str(input("Escribe tu password para comprobar su validez: "))
    print("El password es válido?:",  esValido(password))

main()