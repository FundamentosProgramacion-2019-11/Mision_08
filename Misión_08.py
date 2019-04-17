#Autor: Ruth Salmun Nehmad, A01379037

def combinarLetras(cadena):
    acumulador = ""
    cont = 1
    for n in cadena:
        if cont == 1:
            n = n.upper()
        elif cont == 0:
            n = n.lower()
        acumulador = acumulador + n
        cont =- cont
    print(acumulador)

def contieneLasVocales(cadena):
    letra = cadena.lower()
    a = "a" or "á"
    e = "e" or "é"
    i = "i" or "í"
    o = "o" or "ó"
    u = "u" or "ú"
    if a in letra and e in letra and i in letra and o in letra and u in letra:
        print("True")
        return True
    else:
        print("False")
        return False

def formarNombreUsuario(nombre, apellido, matricula):
    nombre = nombre.lower()
    apellido = apellido.lower()
    matricula = str(matricula)
    nueva = nombre[0:3] + apellido[0:3] + matricula[4:8]
    print("Tu nombre de usuario es: ", nueva)

def esCorrecto(ncompleto):
    nombre = ncompleto.split()
    for palabra in nombre:
        min = palabra[1:]
        may = palabra[0:1]
        if may.isupper() and min.islower():
            print("Correcto")
            return True
        else:
            print("Incorrecto")
            return False

def traducirTelefono(cel):
    cel = cel.lower()
    numero = ""
    for n in cel:
        if n == "a" or n == "b" or n == "c":
            numero = numero + "2"
        if n == "d" or n == "e" or n == "f":
            numero = numero + "3"
        if n == "g" or n == "h" or n == "i":
            numero = numero + "4"
        if n == "j" or n == "k" or n == "l":
            numero = numero + "5"
        if n == "m" or n == "n" or n == "o":
            numero = numero + "6"
        if n == "p" or n == "q" or n == "r" or n == "s":
            numero = numero + "7"
        if n == "t" or n == "u" or n == "v":
            numero = numero + "8"
        if n == "w" or n == "x" or n == "y" or n == "z":
            numero = numero + "9"
        if n == "-":
            numero = numero + "-"
    print("01800-", numero)

def main():
    cadena = str(input("Teclea una frase: "))
    nombre = str(input("Teclea tu nombre: "))
    apellido = str(input("Teclea tu apellido: "))
    matricula = int(input("Teclea tu matrícula: A0"))
    ncompleto = str(input("Escribe tu nombre y tus dos apellidos: "))
    cel = str(input("Traduce tu teléfono (01800-XXX-XXXX): 01800-"))
    combinarLetras(cadena)
    contieneLasVocales(cadena)
    formarNombreUsuario(nombre, apellido, matricula)
    esCorrecto(ncompleto)
    traducirTelefono(cel)

main()