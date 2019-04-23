#Bruno Omar Jiménez Mancilla A01748931
#Un programa que permite realizar distintas funciones relacionadas con cadenas

def combinarLetras(cadena):
    inv = ""
    z = 0
    for letra in cadena:
        if z == 0:
            inv = inv + letra.upper()
            z = 1
        elif z == 1:
            inv = inv + letra.lower()
            z = 0
    return inv

def contieneLasVocales(cadena):
    if (("a" in cadena) == True) and (("e" in cadena) == True) and (("i" in cadena) == True) and (("o" in cadena) == True) and (("u" in cadena) == True):
        return True
    else:
        return False


def traducirTelefono(tel):
    frase = tel[6:]
    telefonoTr = "01800-"
    for t in frase:
        if (("A" in t) == True) or (("B" in t) == True) or (("C" in t) == True):
            telefonoTr = telefonoTr + "2"
        elif (("D" in t) == True) or (("E" in t) == True) or (("F" in t) == True):
            telefonoTr = telefonoTr + "3"
        elif (("G" in t) == True) or (("H" in t) == True) or (("I" in t) == True):
            telefonoTr = telefonoTr + "4"
        elif (("J" in t) == True) or (("K" in t) == True) or (("L" in t) == True):
            telefonoTr = telefonoTr + "5"
        elif (("M" in t) == True) or (("N" in t) == True) or (("O" in t) == True):
            telefonoTr = telefonoTr + "6"
        elif (("P" in t) == True) or (("Q" in t) == True) or (("R" in t) == True) or (("S" in t) == True):
            telefonoTr = telefonoTr + "7"
        elif (("T" in t) == True) or (("U" in t) == True) or (("V" in t) == True):
            telefonoTr = telefonoTr + "8"
        elif (("W" in t) == True) or (("X" in t) == True) or (("Y" in t) == True) or (("Z" in t) == True):
            telefonoTr = telefonoTr + "9"
        elif (("-" in t) == True):
            telefonoTr = telefonoTr + "-"
    return telefonoTr


def formarNombreUsuario(nombre, apellido, matricula):
    n = nombre[:3]
    a = apellido[:3]
    m = matricula[4:]
    nf = n.lower()
    af = a.lower()
    nombreU = nf+af+m
    return nombreU

def esCorrecto(nom,apellidoP,apellidoM):
    nomf = nom[:1]
    apellidoF1= apellidoP[:1]
    apellidoF2 = apellidoM[:1]
    prim2 = nomf[1+1:]
    seg2 = apellidoP[1+1:]
    ter2 = apellidoM[1+1:]
    if nomf.isupper() and prim2.islower() and apellidoF1.isupper() and seg2.islower() and apellidoF2.isupper() and ter2.islower():
        return True
    else:
        return False

def main():
    opc = -1
    while opc != 6:
        print("¿Que deseas hacer?")
        print("1.- Combinar letras")
        print("2.- Encontrar vocales")
        print("3.- Formar nombre de usuario")
        print("4.- Comprobar si las mayúsculas están bien aplicadas")
        print("5.- Traucir telefóno")
        print("6.- Salir")
        opc = float(input("¿Que deseas hacer? "))
        if opc == 1:
            cadena = input("Escribe tu frase: ")
            Mym = combinarLetras(cadena)
            print(Mym)
            input("Pulsa cualquier tecla para continuar...")
        if opc == 2:
            cadena = input("Escribe una palabra: ")
            qwerty = contieneLasVocales(cadena)
            print(qwerty)
            input("Pulsa cualquier tecla para continuar...")
        if opc == 3:
            nombre = input("Escribe tu nombre: ")
            apellido = input("Escribe tu apellido paterno: ")
            matricula = input("Escribe tu matricula sin A0")
            usuario = formarNombreUsuario(nombre,apellido,matricula)
            print(usuario)
            input("Pulsa cualquier tecla para continuar...")
        if opc == 4:
            nom = input("Teclea tu nombre: ")
            apellidoP = input("Teclea tu apellido paterno: ")
            apellidoM = input("Teclea tu apellido materno: ")
            qw = esCorrecto(nom,apellidoP,apellidoM)
            print(qw)
            input("Pulsa cualquier tecla para continuar...")
        if opc == 5:
            tel = input("Escribe el número en formato (01800-XXX-XXXX): ")
            tra = traducirTelefono(tel)
            print(tra)
            input("Pulsa cualquier tecla para continuar...")
        if opc == 6:
            print("Hasta luego!")
        else:
            print("La opción no es válida")
            input("Pulsa cualquier tecla para continuar...")
main()