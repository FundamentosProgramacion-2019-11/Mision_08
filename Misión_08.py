#Autor: Karla Ximena Rueda Ruiz
#Códigos correspondientes a los programas de la Misión 8

entrada=[]
salida = []
def combinarLetras(entrada):
    salida = []
    for(i) in range (0,len(entrada)):
        if (i%2 == 0):
            salida.append(entrada[i].upper())
        else:
            salida.append(entrada[i].lower())
    return (salida)
print(combinarLetras("Hola"))


lista=[]
a = 0
def contieneLasVocales(lista):
    a = 0
    voc=["a","e","i","o","u"]
    for (low)in range(0,len(voc)):
        if (voc[low]in lista):
            a = a + 1
    if a == 5:
            return True
    else:
            return False

print(contieneLasVocales("Ximena"))


def formarNombreUsuario(nombre,apellido,matr):
    nom=nombre.lower()
    ape=apellido.lower()
    matricula=str(matr)
    usuario=nom[:3]+ape[:3]+matricula[-3:]
    return(usuario)

print(formarNombreUsuario("Karla","Rueda",1745943))

def esCorrecto(cadena):

    palabras=cadena.split()
    nombre=palabras[0]
    resto=nombre[1:]
    letra=nombre[0]
    if letra.isupper()==True:

        if resto.islower()==True:
            apellidop = palabras[1]
            restop = apellidop[1:]
            letraP = apellidop[0]


            if letraP.isupper()==True:

                if restop.islower()==True:
                    apellidom = palabras[2]
                    restom = apellidom[1:]
                    letraM = apellidom[0]
                    if letraM.isupper()==True:
                        if restom.islower()==True:
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

print(esCorrecto("Karla Rueda Ruiz"))

def traducirTelefono(t):
    print(t)
    t = list(t)
    i = 6
    while i >= 6 and i <= 13:
        L = t[i]
        if L == "A" or L == "B" or L == "C":
            t[i] = "2"
        elif L == "D" or L == "E" or L == "F":
            t[i] = "3"
        elif L == "G" or L == "H" or L == "I":
            t[i] = "4"
        elif L == "J" or L == "K" or L == "L":
            t[i] = "5"
        elif L == "M" or L == "N" or L == "O":
            t[i] = "6"
        elif L == "P" or L == "Q" or L == "R" or L == "S":
            t[i] = "7"
        elif L == "T" or L == "U" or L == "V":
            t[i] = "8"
        elif L == "W" or L == "X" or L == "Y" or L == "Z":
            t[i] = "9"

        i += 1

    print("".join(t))


t = "01800-VOY-BIEN"
traducirTelefono(t)

