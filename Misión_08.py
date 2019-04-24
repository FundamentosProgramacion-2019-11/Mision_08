def combinarLetras (cadena):
    minMay=""
    for letra in range (len(cadena)):
        if letra%2 !=0:
            minMay+= cadena[letra].lower()
        else:
            minMay+= cadena[letra].upper()
    return minMay

def contieneLasVocales(cadena2):
    if ("a"or "A") and ("e"or"E") and ("i"or"I") and ("o"or"O") and ("u"or"U") in cadena2:
        return True
    else:
        return False

def formarnombreUsuario(nombre,apellidoPaterno,matricula):
    nombre3= nombre[0:3]
    apellido3= apellidoPaterno[0:3]
    if len(matricula) == 7:
        matstr= str(matricula)
        matricula3= matstr[-3:]
        return (nombre3 + apellido3 + matricula3)
    else:
        return "introduce matricula de 7 digitos"

def esCorrecto (cadena3):
    cadenastr= cadena3.split()
    print (cadenastr)
    for letra in cadenastr:
        mayus= letra[0:1]
        minus=  letra[1:]
        if mayus.isupper() and minus.islower:
            return True
        else:
            return False

def traducirTelefono(numeroTelefono):
    digito=""
    for numero in (numeroTelefono):
        if numero == "1":
            digito +="1"
        elif numero == "A" or numero=="B"or numero== "C":
            digito +=  "2"
        elif numero == "D" or numero=="E" or numero=="F":
            digito +=  "3"
        elif numero == "G" or numero== "H" or numero== "I":
            digito += "4"
        elif numero == numero=="J" or numero=="K"or numero=="L":
            digito +=  "5"
        elif numero == "M" or numero=="N"or numero=="O":
            digito +=  "6"
        elif numero == "P" or numero=="Q"or numero=="R" or numero=="S":
            digito +=  "7"
        elif numero == "T"or numero== "U" or numero=="V":
            digito +=  "8"
        elif numero == "W" or numero== "X" or numero=="Y" or numero=="Z":
            digito +=  "9"
        else:
            digito +=  "-"
        formato= "01800"+digito
        return formato


def main():
    cadena= input("Escribe algo: ")
    combinacion= combinarLetras(cadena)
    print(combinacion)
    cadena2=input("Escribe una palabra: ")
    abecedario= contieneLasVocales(cadena2)
    print(abecedario)
    nombre= input("Dame tu nombre: ")
    apellidoPaterno= input ("Dame tu apellido paterno: ")
    matricula= input("Matricula numerica de 7 digitos: ")
    nomUsuario=formarnombreUsuario(nombre,apellidoPaterno,matricula)
    print(nomUsuario)
    cadena3=input ("Dame un nombre competo: ")
    nombreCorrecto= esCorrecto(cadena3)
    print (nombreCorrecto)
    numeroTelefono= input("introduce siglas del numero \"01800-\"")
    telefono= traducirTelefono(numeroTelefono)
    print(telefono)

main()