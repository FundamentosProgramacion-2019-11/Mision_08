#Autor: Elizabeth Citlalli Zapata Cortes, A01746002
#Reliza los ejercicios de cadenas de la MISION_08


def combinarLetras(cadena):
    #Alterna mayusculas y minúsculas

    combinada = ""   #acumulador de cadenas

    for i in range (len(cadena)):
        if i%2 != 0:        #diferenciar si es par o impar
            combinada+= cadena[i].lower()
        else:
            combinada += cadena[i].upper()

    return combinada


def contieneLasVocales(cadena2):
    #regresa TRUE si contiene todas la vocales, regresa FALSE si no es así

    vocales = 'aeiouAEIOU'  #reconoce vocales en mayuscula y minuscula

    for letra in cadena2:
        if letra in vocales:
            return True
        else:
            return False


def formarNombreUsuario(nombre, apellido, matricula):
    #Regresa un nombre de usuario: 3 primeros caracteres nombre+3 primeros caracteres apellido+últimos 3 num matrícula

    name = nombre[:3:]
    lastName = apellido[:3:]
    num = str(matricula)[-3::]  #convertir los enteros a cadena

    usuario = name.lower() + lastName.lower() + num

    return usuario


def esCorrecto(nombrePersona):
    #Regresa TRUE si el nombre de la persona sigue la regla de mayúscula y minúscula, si no es así regresa False

    dividirNombre = nombrePersona.split()    #cómo los va a identificar si cada parte de la cadena empieza en mayuscula

    regla= 0    #cuenta si las tres partes de la cadena cumplen la regla

    for letra in dividirNombre:
        if letra[:1:].isupper() and letra[1::].islower():  #sigue formato: Nombre Apellido Apellido
            regla += 1
        else:
            return False

    if regla ==3:
        return True


def traducirTelefono(numeroTelefonico):
    #Recibe un número telefónico formato ("01800-XXX-XXX") "01800-VOY-BIEN" y regresa cadena del numero "01800-869-2436"

    nuevoNumero = " "   #va acumulndo el número traducido

    for letra in numeroTelefonico:
        if letra == "A" or letra == "B" or letra == "C":
            nuevoNumero += "2"
        elif letra == "D" or letra == "E" or letra == "F":
            nuevoNumero += "3"
        elif letra == "G" or letra == "H" or letra == "I":
            nuevoNumero += "4"
        elif letra == "J" or letra == "K" or letra == "L":
            nuevoNumero += "5"
        elif letra == "M" or letra == "N" or letra == "O":
            nuevoNumero += "6"
        elif letra == "P" or letra == "Q" or letra == "R" or letra == "S":
            nuevoNumero += "7"
        elif letra == "T" or letra == "U" or letra == "V":
            nuevoNumero += "8"
        elif letra == "W" or letra == "X" or letra == "Y" or letra == "Z":
            nuevoNumero += "9"
        elif letra == "-":
            nuevoNumero += "-"

    traducido = "01800"+nuevoNumero

    return traducido


#EXTRA
def esValido(password):
    #Revisa si el password es válido al seguir las reglas indicadas.

    strPassword = password    #convertir a cadena

    valido = 0  #contador de reglas que se cumplieron

    for letra in strPassword:
        if len(strPassword) >= 8:  #1. Tiene 8 o más caracteres
            valido += 1
        elif strPassword.islower() and strPassword.isupper(): #2. Contiene una letra mayúscula y una letra minuscula
            valido += 1
        elif not letra.isalnum(): #3. Contiene un caracter especial
            valido += 1
        elif letra.isdigit(): #4. Tieneal menos 1 dígito
            valido += 1
        elif letra[:1].isalpha(): #5.Comienza con una letra
            valido += 1
        elif not strPassword[letra].isdigit() and strPassword[letra+1].isdigit(): #6.No tiene digitos consecutivos
            if (int(password[letra +1])) == (int(password[letra]) + 1):
                return False
            else:
                valido += 1

    if valido >= 6:
        return True
    else:
        return False


def main():
    #EJERCICIO1
    print("Combinar mayúsuclas y minúsculas")
    cadena = input("Teclear cadena: ")
    ejercicio1 = combinarLetras(cadena)
    print(ejercicio1)
    print()

    #EJERCICIO 2
    print("Contiene todas la vocales")
    cadena2 = input("Teclear cadena: ")
    ejercicio2 = contieneLasVocales(cadena2)
    print(ejercicio2)
    print()

    #EJERCICIO 3
    print("Formar nombre de usuario")
    nombre = input("Teclear nombre: ")
    apellido = input("Teclear un apellido: ")
    matricula = input("Teclear matricula: ")
    ejercicio3 = formarNombreUsuario(nombre, apellido, matricula)
    print(ejercicio3)
    print()

    #EJERCICIO 4
    print("Se utilizan correctamente las mayúsculas y minúscula")
    nombrePersona = input("Teclear primer nombre, primer apellido y segundo apellido: ")
    ejercicio4 = esCorrecto(nombrePersona)
    print(ejercicio4)
    print()

    #EJERCICIO 5
    print("Traducir número telefónico de letra mayúscula a dígito con el formato 01800- XXX- XXXX")
    numeroTelefonico = input("Teclear número telefonico: ")
    ejercicio5 = traducirTelefono(numeroTelefonico)
    print(ejercicio5)
    print()

    #EXTRA EJERCICIO 6
    print("Verificar si el formato de la contraseña es válida")
    password = input("Teclea la contaseña: ")
    ejercicio6Extra = esValido(password)
    print(ejercicio6Extra)


main()