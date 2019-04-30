#Autor: Ivana Olvera Mérida
#Misión 08: Cadenas

#1
def combinarLetras(parametro):
    cadena = ""

    for k in range(0, len(parametro),1): # k -> 1,2,3,4,5,6,7,8,9
        if k%2 == 0:
            cadena += parametro[k].upper()
        else:
            cadena += parametro[k].lower()

    return cadena


#2
def contieneLasVocales(cadena):
    copiaVocal = cadena.upper() #Utilizar una copia para identificar si se recibió una vocal en mayúscula

    contadorVocales = 0

    if copiaVocal.count('A')>=1: #Si se cuenta la vocal una o más veces dentro de una palabra
        contadorVocales += 1
    if copiaVocal.count('E') >= 1:
        contadorVocales += 1
    if copiaVocal.count('I') >= 1:
        contadorVocales += 1
    if copiaVocal.count('O') >= 1:
        contadorVocales += 1
    if copiaVocal.count('U') >= 1:
        contadorVocales += 1

    if contadorVocales == 5:
        return True
    else:
        return False


#3
def formarNombreUsuario(nombre, apellido, matricula):
    a = nombre
    nom = a[0:3] #Toma los primeros 3 elementos de la cadena: 0,1,2,3 (3-1)
    b = apellido
    ap = b[0:3] #Toma los primeros 3 elementos de la cadena

    d = str(matricula)
    mat = d[4:]

    cadenaUsuario = nom.lower() + ap.lower()+ mat
    return cadenaUsuario


#4
def esCorrecto(nombreCompleto):
    nombreApellidos = nombreCompleto.split() #La función split se encarga de separar los elementos de la cadena('Ivana', 'Olvera', 'Mérida')
    nombre = nombreApellidos[0] #Ivana
    apellidoP = nombreApellidos[1] #Olvera
    apellidoM = nombreApellidos[2] #Mérida
    contadorNombre = 0

    if nombre[0].isupper() and nombre[1:].islower(): #El nombre debe cumplir con la primera letra en mayúcula y el resto de las letras en minúsculas
        contadorNombre += 1
    if apellidoP[0].isupper() and apellidoP[1:].islower():
        contadorNombre += 1
    if apellidoM[0].isupper() and apellidoM[1:].islower():
        contadorNombre += 1
        return True
    else:
        return False


#5
def traducirTelefono(telefono):
    numero = ""
    telefono = telefono.upper()
    numInicio = "01800"

    for n in telefono:
        if n == "-":
            numero = numero + "-"
        if n == "A" or n == "B" or n == "C":
            numero = numero + "2"
        if n == "D" or n == "E"  or n == "F":
            numero = numero + "3"
        if n == "G" or n == "H" or n == "I":
            numero = numero + "4"
        if n == "J" or n == "K" or n == "L":
            numero = numero + "5"
        if n == "M" or n == "N" or n == "O":
            numero = numero + "6"
        if n == "P" or n == "Q" or n == "R" or n == "S":
            numero = numero + "7"
        if n == "T" or n == "U" or n == "V":
            numero = numero + "8"
        if n == "W" or n == "X" or n == "Y" or n == "Z":
            numero = numero + "9"

    numFinal = numInicio + numero
    return numFinal


def main():
    combinacion = combinarLetras("Hola Mundo")
    print(combinacion)

    todasLasVocales = contieneLasVocales("abuelito")
    print(todasLasVocales)

    usuario = formarNombreUsuario("Ivana", "Olvera", "1746744")
    print(usuario)

    correcto = esCorrecto("Ivana Olvera Mérida")
    print(correcto)

    traducirTelefono("01800-VOY-BIEN")

main()