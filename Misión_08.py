#Autor: Daniela Estrella Tovar
# Desarrollo y resolución de problemas mediante cadenas.

#Ejercicio 1

def combinarLetras(cadena):
    combinada = ""

    for i in range(len(cadena)):
        if (i%2==0):
            combinada += cadena[i].upper()
        else:
            combinada += cadena[i].lower()

    return combinada

#Ejercicio 2
def contieneLasVocales(cadena):
    palabra = cadena.lower()
    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"
    if a in palabra and e in palabra and i in palabra and o in palabra and u in palabra:
        return True
    else:
        return False

#Ejercicio 3
def formarNombreUsuario(nombre, apellido,matricula):
    nombre = nombre.lower()
    apellido= apellido.lower()

    nom = nombre[:3:]
    ape = apellido[:3:]
    mat = str(matricula)[-3::]

    formar = nom + ape + mat
    return formar

#Ejercicio 4
def esCorrecto(nombre):
    nombresep = nombre.split()
    condicion = 0
    for letra in nombresep:
        mayus = letra[0:1]
        minus = letra[1:]
        if mayus.isupper() and minus.islower():
            condicion += 1
            if condicion == 3:
                return True
        else:
            return False

#Ejercicio 5
def traducirTelefono(telefono):
    num = ""
    telefono = telefono.upper()
    for digito in telefono:
        if digito == "A" or digito == "B" or digito == "C":
            num = num + "2"
        if digito == "D" or digito == "E" or digito == "F":
            num = num + "3"
        if digito == "G" or digito == "H" or digito == "I":
            num = num + "4"
        if digito == "J" or digito == "K" or digito == "L":
            num = num + "5"
        if digito == "M" or digito == "N" or digito == "O":
            num = num + "6"
        if digito == "P" or digito == "Q" or digito == "R" or digito == "S":
            num = num + "7"
        if digito == "T" or digito == "U" or digito == "V":
            num = num + "8"
        if digito == "W" or digito == "X" or digito == "Y" or digito == "Z":
            num = num + "9"
        if digito == "-":
            num = num + "-"
    traduccion = "01800" + num
    return traduccion

#Ejercicio Extra
def esValido(clave):
    valido = 0
    #Condición 1
    if len(clave) >= 8:
        valido += 1
    #Condición 2
    for letra in clave:
        mayus= letra[0:1]
        if letra.islower():
            valido += 1
        if letra.isupper():
            valido += 1
    #Condicion 3
    if not clave.isalnum():
        valido += 1
    #Condicion 4
    if clave.isdigit():
        valido += 1
    #Condicion 5
    if clave[0].isalpha():
        valido += 1
    for n in range(0, len(clave)-1):
        if clave[n].isdigit() and clave[n].isdigit():
            if not (int(clave[n])+1) == (int(clave[n+1])):
                valido += 1

    #Resultado
    if valido == 7:
        return True
    else:
        return False



def main():
    print("Alternando Letras")
    c = input("Teclea la frase:")
    result = combinarLetras(c)
    print(combinarLetras(result))

    print("Comprueba si tu palabra contiene todas las vocales: ")
    texto = input("Teclea tu palabra: ")
    vocales= contieneLasVocales(texto)
    print(vocales)

    print("Forma tu nombre de usuario: ")
    nombre = input("Teclea tu nombre: ")
    apellido = input("Teclea tu apellido: ")
    matricula = input("Teclea tu matrícula(7 dígitos): ")
    usuario= formarNombreUsuario(nombre, apellido, matricula)
    print(usuario)

    print("Comprueba si tu nombre cumple con las reglas de las mayúsculas: ")
    nombre = input("Ingresa tu nombre completo: ")
    reglasM = esCorrecto(nombre)
    print(reglasM)

    print("Traduce el número: ")
    telefono = input("Ingresa el número de teléfono en el formato 01800 - XXX - XXXX : ")
    traduccion = traducirTelefono(telefono)
    print(traduccion)


    print("Comprueba si tu contraseña es válida: ")
    contra = input("Ingresa tu contraseña: ")
    validez = esValido(contra)
    print(validez)



main()