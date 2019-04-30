#Autor Sofía Trujillo Vargas
#Aqui utilizaremos diferentes funciones para strings para resolver diferentes funciones

def combinarLetras(palabra):
    cnt = ""
    tot = 0
    for letra in palabra:
        if tot == 0:
            cnt = cnt + letra.upper()
            tot = 1
        elif tot == 1:
            cnt = cnt + letra.lower()
            tot = 0
    return cnt

def contieneLasVocales(vocal):
    vocal1 = vocal.lower()
    if (("a" in vocal1) == True) and (("e" in vocal1) == True) and (("i" in vocal1) == True) and (
            ("o" in vocal1) == True) and (("u" in vocal1) == True):
        return True
    else:
        return False

def formarNombreUsuario(nombre,apellido,matricula):
    nom = nombre
    ape = apellido
    mat = str(matricula)
    mat1 = mat[4:]
    ape1 = ape[:3]
    nom2 = nom[:3]
    ape2 = ape1.lower()
    nomb = nom2.lower()
    nuevo = nomb + ape2 + mat1
    return (nuevo)

def esCorrecto(nombrec):
    nombrecom= nombrec.title()
    if nombrec == nombrecom:
        return True
    else:
        return False

def traducirTelefono(llamar):
    tel = llamar[6:]
    base = "01800"
    for num in tel:
        for num in llamar:
            if (("A" in num) == True) or (("B" in num) == True) or (("C" in num) == True):
                base = base + "2"
            elif (("D" in num) == True) or (("E" in num) == True) or (("F" in num) == True):
                base = base + "3"
            elif (("G" in num) == True) or (("H" in num) == True) or (("I" in num) == True):
                base = base + "4"
            elif (("J" in num) == True) or (("K" in num) == True) or (("L" in num) == True):
                base = base + "5"
            elif (("M" in num) == True) or (("N" in num) == True) or (("O" in num) == True):
                base = base + "6"
            elif (("P" in num) == True) or (("Q" in num) == True) or (("R" in num) == True) or (("S" in num) == True):
                base = base + "7"
            elif (("T" in num) == True) or (("U" in num) == True) or (("V" in num) == True):
                base = base + "8"
            elif (("W" in num) == True) or (("X" in num) == True) or (("Y" in num) == True) or (("Z" in num) == True):
                base = base + "9"
            elif (("-" in num) == True):
                base = base + "-"
        return base


def main():
    opcion = -1
    while opcion != 6:
        print("""Menú.
        1. Combinar las letras
        2. Ver si una palabra tiene todas las vocales
        3. Te dare una opción de nombre de usuario
        4. Tu nombre esta escrito de manera correcta
        5. Te dare el número del teléfono
        6. Salir""")
        opcion = float(input("¿Que quieres hacer? "))
        if opcion == 1:
            word = input("Dime la palabra que te gustaría intercalar: ")
            inter = combinarLetras(word)
            print(inter)
        if opcion == 2:
            palabra = input("Dime la palabra que quieres que quieres saber si tiene todas las vocales: ")
            print(contieneLasVocales(palabra))
        if opcion == 3:
            nombre = input("Dame tu nombre: ")
            apellido = input("Dame tu apellido: ")
            matricula = input("Dame tu matrícula (Completa con el A0) : ")
            print(formarNombreUsuario(nombre, apellido, matricula))
        if opcion == 4:
            nombrec = input("Dame tu nombre completo: ")
            completo = esCorrecto(nombrec)
            print(completo)
        if opcion == 5:
            men = input("Teléfonno: ")
            print(traducirTelefono(men))

main()
