#Karimn Daniel Hernández Castorena
#Programa que permite al usuario realizar diferentes acciones.

def combinarLetras(cadena):
    contador = 1
    acumulador = ""
    for a in cadena:
        if contador == 0:
            a = a.lower()
        elif contador == 1:
             a = a.upper()
        acumulador = acumulador + a
        contador = - contador
    return acumulador


def contieneLasVocales(cadena):
    xx = cadena.lower()
    a = "a" or "á"
    e = "e" or "é"
    i = "i" or "í"
    o = "o" or "ó"
    u = "u" or "ú"
    if a in xx and e in xx and i in xx and o in xx and u in xx:
        print("Cierto, cuenta con las cinco vocales.")
    else:
        print("Falso, no cuenta con las cinco vocales.")


def formarNombreUsuario(nombre, apellido, matricula):
    n = nombre.lower()
    a = apellido.lower()
    m = str(matricula)
    y = n[0:3] + a[0:3] + m[4:7]
    print()
    print("Tu gamertag es:", y)


def esCorrecto(nom):
    palabras = nom.split()
    contadorcorrecto = 0
    contadorincorrecto = 0
    for l in palabras:
        minusculas = l[1:]
        mayuscula = l[0:1]
        if minusculas.islower() and mayuscula.isupper():
            contadorcorrecto += 1
        else:
            contadorincorrecto += 1
    if contadorcorrecto == 3:
        print("Correcto. La regla si se respeta.")
    elif contadorincorrecto >= 1:
        print("Incorrecto. La regla no se respeta.")



def traducirTelefono(tel):
    acumulador = ""
    for letras in tel:
        if "a" == letras or "b" == letras or "c" == letras:
            acumulador = acumulador + "2"
        elif "d" == letras or "e" == letras or "f" == letras:
            acumulador = acumulador + "3"
        elif "g" == letras or "h" == letras or "i" == letras:
            acumulador = acumulador + "4"
        elif "j" == letras or "k" == letras or "l" == letras:
            acumulador = acumulador + "5"
        elif "m" == letras or "n" == letras or "o" == letras:
            acumulador = acumulador + "6"
        elif "p" == letras or "q" == letras or "r" == letras or "s" == letras:
            acumulador = acumulador + "7"
        elif "t" == letras or "u" == letras or "v" == letras:
            acumulador = acumulador + "8"
        elif "w" == letras or "x" == letras or "y" == letras or "z" == letras:
            acumulador = acumulador + "9"
    print("01800-", acumulador)


def main():
    print()
    cadena = (input("Teclea una palabra para combinarla entre mayúsculas y minúsculas: "))
    print(combinarLetras(cadena))
    print()
    print("-------------------------------------------")
    print()
    v = (input("Teclea una palabra y te diré si contiene todas las vocales: "))
    contieneLasVocales(v)
    print()
    print("-------------------------------------------")
    print()
    nombre = str(input("Teclea tu nombre: "))
    apellido = str(input("Teclea tu apellido: "))
    matrícula = int(input("Teclea tu matrícula: A0"))
    formarNombreUsuario(nombre, apellido, matrícula)
    print()
    print("-------------------------------------------")
    print()
    print("Vamos a analizar si la regla de las mayúsculas es correcta.")
    print()
    print("Introduce tu primer nombre y tus dos apellidos.")
    print("(Para que la regla se cumpla la primera letra de cada palabra debe ser mayúscula)")
    print()
    nom = str(input("¿Cómo te llamas? "))
    esCorrecto(nom)
    print()
    print("-------------------------------------------")
    print()
    print("Traduciremos tu teléfono." )
    print("Introduce dos palabras, una de tres letras y otra de cuatro.")
    tel = str(input("Teclea las palabras (01-800-XXX-XXXX): 01-800-"))
    traducirTelefono(tel)
    print()
    print("-------------------------------------------")
    print()

main()