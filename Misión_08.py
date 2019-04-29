#Cecilia Daniela Olivares Hernández, a01745727, Grupo 03

#Ejercicio 1: Esta función recibe una cadena y la regresa alternando mayúsculas con minúsculas
def combinarLetras(cadena):
    myM = ""
    rango = len(cadena) #El rango va a ser toda la cadena desde el primer valor hasta el ultimo
    for i in range(rango):
        if (i%2 != 0): #Si el indice es un numero PAR entonces la letra será mayúscula
            myM += cadena[i].lower()
        else: #Si el indice es un numero IMPAR entonces la letra será minúscula
            myM += cadena[i].upper()
    return myM


#Ejercicio 2: En esta función, el usuario ingresa una palabra. Si esta contiene todas las vocales, imprimira True. False si no
def contieneLasVocales(cadena):
    cadena = cadena.lower() #Si el usuario ingresa letras en mayúsculas, se convertiran en minúsculas para facilitar la realización del programa
    numA = 0 #El contador de las veces que aparece cada una de las vocales
    numE = 0
    numI = 0
    numO = 0
    numU = 0

    for c in cadena:
        if c == "a":
            numA += 1 #Se suman las veces que van apareciendo las vocales
        if c == "e":
            numE += 1
        if c == "i":
            numI += 1
        if c == "o":
            numO += 1
        if c == "u":
            numU += 1
    if numA >= 1 and numE >= 1 and numI >= 1 and numO >= 1 and numU >= 1: #Si aparecen todas las vocales al menos una vez, sera verdadero
        return True
    else:
        return False


#Ejercicio 3: Esta función recibe un nombre, un apellido y una matrícula mayor a 3 digitos.
             #Regresa el nombre del usuario (carácteres en minúsculas) formado por:
             #3 primeras letras del nombre + 3 primeras letras de apellido + ultimos 3 digitos de la matrícula.
def formarNombreUsuario(nombre, apellidoPaterno, matrícula):
    c = ""
    n = nombre.lower()[0:3] #Calcula los 3 primeros digitos del nombre
    c += n
    aP = apellidoPaterno.lower()[0:3] #Calcula los 3 primeros digitos del apellido
    c += aP
    strm = str(matrícula) #Convierte los numeros en una cadena
    for i in range(len(strm)):
        if (i <= 2): #si la matrícula es menor o igual a 3 digitos, marcará error
            m = """
Error. La matrícula debe tener más de 3 digitos"""
        if (i >= 3): #Solo acepta una matricula mayor a 3 digitos
            m= strm[-3::] #El valor de m va a ser igual a los ultimos 3 digitos de la matrícula
    c += m
    return c


#Ejercicio 4: Esta función recibe 1 nombre y 2 apellidos y regresa True si las reglas de mayúsculas están bien aplicadas, False en otro caso.
def esCorrecto(cadena):
    división = cadena.split() #Descompone la cadena en sus duferentes palabras de las que se compone
    true = 0 #El contador de las veces que la palabra es verdadera
    false = 0 #El contador de las veces que la palabra es falsa
    for letra in división:
        capital =  letra[0:1] #Hace referencia a la primera letra de cada palabra
        len = letra[1::] #Hace refecencia al resto de letras a excepción de la primera de cada palabra
        if capital.isupper() and len.islower():
            true += 1 #Se suman las veces que la palabra es verdadera
        else:
            false += 1 #Se suman las veces que la palabra es falsa
    if true == 3: #Sera verdadero si es que las 3 palabras (nombre y los 2 apellidos) son correctas y la regla de mayúsculas está bien aplicada
        return True
    elif false >= 1: #Sera verdadero si es que alguna o todas las 3 palabras son incorrectas y la regla de mayúsculas no está bien aplicada
        return False


#Ejercicio 5: En esta función, el usuario ingresa letras en el formato 01800-XXX-XXXX y la función lo traduce a digitos
def traducirTelefono(num):
    n = ""
    num = num.upper() #Si el usuario ingresa letras en minúsculas, esto las pasa a mayúsculas

    for c in num:
        if c == "-":
            n = n+"-"
        if c == "A" or c == "B" or c == "C":
            n = n+"2"
        if c == "D" or c == "E" or c == "F":
            n = n+"3"
        if c == "G" or c == "H" or c == "I":
            n = n+"4"
        if c == "J" or c == "K" or c == "L":
            n = n+"5"
        if c == "M" or c == "N" or c == "O":
            n = n+"6"
        if c == "P" or c == "Q" or c == "R" or c == "S":
            n = n+"7"
        if c == "T" or c == "U" or c == "V":
            n = n+"8"
        if c == "W" or c == "X" or c == "Y" or c == "Z":
            n = n+"9"
    numero = "01800" + n
    return numero

#Ejercicio 6 EXTRA: Esta función regresa True si cumple con las reglas indicadas para ingresar una contraseña valida
def esValido(password):
    #Condición 1
    cont = len(password)
    for i in range(cont): #La contraseña debe ser igual o mayor a 8 carácteres
        if (i >= 7):
            return True
        else:
            return False

    # Condición 2
    min = 0
    may = 0
    for c in password:
        if c.islower():
            min += 1 #Debe haber al menos 1 letra minúscula
        if c.isupper():
            may += 1 #Debe haber al menos 1 letra mayúscula
    if min >= 1 and may >= 1:
        return True #si hay ina o más letras minúsculas y mayúsculas, sera verdadero
    else:
        return False

    # Condición 3
    if not password.isalnum(): #Si la contraseña no solo se conforma por letras y numeros (cuenta con carácteres especiales), es verdadero
        return True
    else:
        return False
    #print(cEspecial)

    # Condición 4
    if not password.isdigit(): #Si no son solo numeros los que conforman la cadena
        return True
    else:
        return False
    #print(digito)

    # Condición 5
    if password[0].isalpha(): #El primer caracter debe ser una letra. Si sí, es verdadero.
        return True
    else:
        return False
    #print(pLetra)

    # Condición 6
    c = len(password)
    for i in range (0, c-1): #Se resta -1 para que la cadena no marque que esta fuera de rango
        if password[i].isdigit() and password[i+1].isdigit(): #Indica que los carácteres son digitos consecutivos
            if (int(password[i + 1])) == (int(password[i]) + 1): #señalamos que el segundo caracter es digito consecutivo delprimero
                return True #Los digitos son consecutivos
            else:
                return False
    #print(consecutivo)

    # Comprobación
    if long == True and myM == True and cEspecial == True and digito == True and pLetra == True and consecutivo == False:
        return True
    else:
        return False


def main():
    #Funcion1
    c = input("""Inserta una cadena. (Ejemplo: "Hola Mundo"): """)
    ej1 = combinarLetras(c)
    print(ej1)
    # Funcion2
    palabra = input("""Inserta una palabra. (Ejemplo: "Monterrey"): """)
    ej2 = contieneLasVocales(palabra)
    print(ej2)
    # Funcion3
    nombre = input("Ingresa el nombre del usuario: ")
    apellidoPaterno = input("Ingresa el apellido paterno del usuario: ")
    matrícula = int(input("Ingresa la matrícula del usuario. (Mayor a 3 digitos): "))
    formarNombreUsuario(nombre, apellidoPaterno, matrícula)
    ej3 = formarNombreUsuario(nombre, apellidoPaterno, matrícula)
    print(ej3)
    # Funcion4
    nombre = input("Ingresa 1 nombre y 2 apellidos sencillos: ")
    ej4 = esCorrecto(nombre)
    print(ej4)
    # Funcion5
    número = input("Ingresa un número telefónico en el formato 01800-XXX-XXXX. (Ej: 01800-VOY-BIEN) 01800-")
    ej5 = traducirTelefono(número)
    print(ej5)
    # Funcion 6
    contraseña = input("Ingresa una contraseña: ")
    ej6 = esValido(contraseña)
    print(ej6)

main()


