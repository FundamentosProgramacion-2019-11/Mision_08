#Bernardo Mondragon Ramírez
# Lee diferentes acciones con cadenas


def combinarLetras(letras):
    c = ""
    contador = 1
    for l in letras:
        if contador == 0:
            l = l.lower()
        elif contador == 1:
            l = l.upper()
        c = c + l
        contador = - contador
    print(c)



def contieneLasVocales(l):

    l = l.lower()

    a = l.find("a")
    e = l.find("e")
    i = l.find("i")
    o = l.find("o")
    u = l.find("u")

    if (a != -1) and (e != -1) and (i != -1) and (o != -1) and (u != -1):
        print (True, "contiene todas las vocales")
    else:
        print (False, " no tiene todas las vocales")

def formarNombreUsuario(n, a, m):
    n = n.lower()
    a = a.lower()
    m = str(m)
    nUsuario = n[0:3] + a[0:3] + m[4:]
    print("Tu monbre de usuarios es es:", nUsuario)



def esCorrecto(ncompleto):
    n = ncompleto.split()
    for letra in n:
        min = letra[1:]
        may = letra[:1]
        if may.isupper() and min.islower():
            print(True)
        else:
            print(False, "no todas empiezan con mayusculas")


def traducirTelefono(telefono):
    contador=""
    telefono = telefono.upper()
    for t in telefono:
        if t == "a" or t == "b" or t == "b":
            contador = contador + "2"
        elif t == "d" or t == "e" or t == "f":
            contador = contador + "3"
        elif t == "g" or t == "h" or t == "i":
            contador = contador + "4"
        elif t == "j" or t == "k" or t == "l":
            contador = contador + "5"
        elif t == "m" or t == "n" or t == "o":
            contador = contador + "6"
        elif t == "p" or t == "q" or t == "r" or t == "s":
            contador = contador + "7"
        elif t == "t" or t == "u" or t == "v":
            contador = contador + "8"
        elif t == "w" or t == "x" or t == "y" or t == "z":
            contador = contador + "9"

    print("01-800-",contador)



def main():
    letras=str(input("Escribe una frase: "))
    combinarLetras(letras)
    contieneLasVocales(letras)
    print()
    nombre = input("Teclea tu nombre: ")
    apellido = input(("Teclea tu primer apellido: "))
    matricula= str(input("Teclea tu matricula A0"))
    formarNombreUsuario(nombre, apellido, matricula)
    print()
    nombreCompleto=str(input("Teclea tu nombre completo para probar la regla: "))
    esCorrecto(nombreCompleto)
    print()
    telefono=str(input("Teclea  01-800-XXX-XXXX: 01-800"))
    traducirTelefono(telefono)



main()