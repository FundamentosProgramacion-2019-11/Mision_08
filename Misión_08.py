def combinarLetras (cadena):
    minMay=""
    for letra in range (len(cadena)):
        if letra%2 !=0:
            minMay+= cadena[letra].lower()
        else:
            minMay+= cadena[letra].upper()
    return minMay

def contieneLasVocales(cadena2):
    if ("a" or "A") in cadena2:
        if("e" or "E")in cadena2:
            if("i" or "I")in cadena2:
                if("o" or "O") in cadena2:
                    if("u" or "U") in cadena2:
                        return True
    return False


def formarNombreUsuario(nombre,apellido,matricula):
    minusculas= nombre.lower()
    minusculasApe= apellido.lower()
    nombre3= minusculas[0:3]
    apellido3= minusculasApe[0:3]
    matstr = str(matricula)
    if len(matstr) == 7:
        matricula3= matstr[-3:]
        return (nombre3 + apellido3 + matricula3)
    else:
        return "introduce matricula de 7 digitos"

def esCorrecto (cadena3):
    cadenastr= cadena3.split()
    palabra= cadenastr[0]
    palabra2= cadenastr[1]
    palabra3= cadenastr[2]
    if palabra[0].isupper() and palabra[1:].islower():
        if palabra2[0].isupper() and palabra2[1:].islower():
            if palabra3[0].isupper() and palabra3[1:].islower():
                return  True

    return False

def traducirTelefono(numeroTelefono):
    digito=""
    mensaje= numeroTelefono[6::]
    for numero in mensaje:
        if numero == "1":
            digito +="1"
        elif (numero == "A") or (numero == "B") or (numero== "C"):
            digito +=  "2"
        elif (numero == "D" )or (numero == "E") or (numero=="F"):
            digito +=  "3"
        elif (numero == "G") or (numero == "H") or (numero== "I"):
            digito += "4"
        elif (numero == "J") or (numero == "K") or (numero=="L"):
            digito +=  "5"
        elif (numero == "M") or (numero == "N") or (numero=="O"):
            digito +=  "6"
        elif (numero == "P") or (numero == "Q") or (numero=="R") or (numero=="S"):
            digito +=  "7"
        elif (numero == "T") or (numero == "U") or (numero=="V"):
            digito +=  "8"
        elif (numero == "W") or (numero == "X") or (numero=="Y") or (numero=="Z"):
            digito +=  "9"
        else:
            digito += "-"
    return "01800-"+digito


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