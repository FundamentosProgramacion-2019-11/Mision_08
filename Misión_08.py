# Guillermo De Anda Casas , A01375892
# Código con los programas de la Misión 8


vocales = ["a", "e", "i", "o", "u"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def hacerMinusculas(cadena):
    cadenaMinusculas = cadena.lower()
    return cadenaMinusculas


def combinacionLetras(palabra):
    palabraMayus = palabra.upper()
    palabraMinus = palabra.lower()
    combinada = ""
    for letra in range(0, len(palabra), 2):
        combinada = combinada + palabraMayus[letra] + palabraMinus[letra + 1]
    return combinada


def combinarLetras(palabra):
    if len(palabra) % 2 != 0:
        palabraEnPar = palabra + " "
        return combinacionLetras(palabraEnPar)[:-1]
    else:
        return combinacionLetras(palabra)


def contieneLasVocales(palabra):
    palabra = hacerMinusculas(palabra)
    for vocal in vocales:
        if not vocal in palabra:
            return False
    return True


def formarNombreUsuario(nombre, apellido, matricula):
    nombre = hacerMinusculas(nombre)
    apellido = hacerMinusculas(apellido)
    matricula = str(matricula)
    nombreUsuario = nombre[:3:]
    apellidoUsuario = apellido[:3:]
    matriculaUsuario = matricula[4::]
    usuario = nombreUsuario + apellidoUsuario + matriculaUsuario
    return usuario


def esCorrecto(nombre):
    nombreSeparado = nombre.split()
    resultado = True
    for palabra in nombreSeparado:
        palabra = palabra[1::]
        for letra in palabra:
            if letra.isupper():
                resultado = False
    for palabra in nombreSeparado:
        primeraLetra = palabra[:1:]
        for letra in primeraLetra:
            if letra.islower():
                resultado = False
    if resultado == False:
        return resultado
    else:
        return resultado


def traducirTelefono(telefono):
    telefono = str(telefono)
    guion = ["-", "_", " "]
    numeroDos = ["A", "B", "C", "a", "b", "c"]
    numeroTres = ["D", "E", "F", "d", "e", "f"]
    numeroCuatro = ["G", "H", "I", "g", "h", "i"]
    numeroCinco = ["J", "K", "L", "j", "k", "l"]
    numeroSeis = ["M", "N", "O", "m", "n", "o"]
    numeroSiete = ["P", "Q", "R", "S", "p", "q", "r", "s"]
    numeroOcho = ["T", "U", "V", "t", "u", "v"]
    numeroNueve = ["W", "X", "Y", "Z", "w", "x", "y", "z"]
    telefonoPorCorregir = telefono[5::]
    telefonoTraducido = ""
    for caracter in telefonoPorCorregir:
        for letra in numeroDos:
            if letra in caracter:
                telefonoTraducido += "2"
        for letra in numeroTres:
            if letra in caracter:
                telefonoTraducido += "3"
        for letra in numeroCuatro:
            if letra in caracter:
                telefonoTraducido += "4"
        for letra in numeroCinco:
            if letra in caracter:
                telefonoTraducido += "5"
        for letra in numeroSeis:
            if letra in caracter:
                telefonoTraducido += "6"
        for letra in numeroSiete:
            if letra in caracter:
                telefonoTraducido += "7"
        for letra in numeroOcho:
            if letra in caracter:
                telefonoTraducido += "8"
        for letra in numeroNueve:
            if letra in caracter:
                telefonoTraducido += "9"
        for letra in guion:
            if letra in caracter:
                telefonoTraducido += "-"
    return "01800" + telefonoTraducido


def esValido(password):
    resultado = True
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    if len(password) < 8:   # Tiene 8 caracteres o mas
        resultado = False

    if password.isalnum():  # Contiene al menos una caracter especial
        resultado = False


    mayusculas = 0
    minusculas = 0
    digito = 0
    for letra in password:  # Contiene una Mayúscula, una minúscula y un dígito
        if letra.isupper():
            mayusculas += 1
        elif letra.islower():
            minusculas += 1
        elif letra.isnumeric():
            digito += 1
    if mayusculas == 0 or minusculas == 0 or digito == 0:
        resultado = False


    if password.isnumeric():    # No sea formada por solo números
        resultado = False


    for letra in password[0]:    # No inicie con un número
        for numero in numeros:
            if numero in letra:
                resultado = False


    separacion = 0
    for numero in numeros:  # No contiene dígitos consecutivos
        if numero in password:
            while separacion == 0:
                separacion += 1
                numeroPassword = password.split(numero)
                soloNumeros = numeroPassword[1]
                # Comprueba si la cadena es solo números
                if soloNumeros.isnumeric():
                    soloNumeros = soloNumeros[0]
                    soloNumero = int(soloNumeros)
                    numeroAntecesor = soloNumero - 1
                    numeroAntecesorCadena = str(numeroAntecesor)
                    numeroPorEncontrar = numeroAntecesorCadena + soloNumeros
                    if numeroPorEncontrar in password:
                        resultado = False


                soloNumero = ""     # Convierte la cadena en una que solo contenga números, y que no sean consecutivos
                for letra in soloNumeros:
                    for numero in numeros:
                        if letra is numero:
                            soloNumero += letra
                soloNumero = int(soloNumero[0])
                numeroAntecesor = soloNumero - 1
                numeroAntecesorCadena = str(numeroAntecesor)
                numeroPorEncontrar = numeroAntecesorCadena + str(soloNumero)
                if numeroPorEncontrar in password:
                    resultado = False
    return resultado



# Par e impar
# combinarLetras("Hola mundo")
# combinarLetras("Hola ¿como estas?")


#print(contieneLasVocales("Monterrey"))
#print(contieneLasVocales("Abuelito"))

# Trabajé con 7 dígitos en vez de los 8 que usted marca en el ejemplo.
# print(formarNombreUsuario("Roberto", "Martínez", 12345678))
# print(formarNombreUsuario("Guillermo", "DeAnda", 1375892))

# print(esCorrecto("Guillermo De Anda Casas"))
# print(esCorrecto("maría FerNanda GArcIa GAStélum"))


# 01-800-XXX-XXXX
#print("01800" + traducirTelefono("01800-VOY-BIEN"))


#print(esValido("Abcd-7635"))