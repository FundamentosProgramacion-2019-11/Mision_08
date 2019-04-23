#María Angélica Hernández Parada A01169796
#Cadenas


#RECIBE UNA CADENA Y REGRESA UNA NUEVA ALTERANDO CON MINUSCULAS Y MAYUSCULAS
def combinarLetras(letras):
    cadena = ""  #en esta parte se acumula la cadena
    cont = 1
    for n in letras: #revisa la posición de las letras y las cambia a mayor o menor
        if cont == 1:
            n = n.upper()
        elif cont == 0:
            n = n.lower()
        cadena = cadena + n #se guarda en una nueva cadena
        cont = - cont
    print(cadena)


#RECIBE UNA CADENA Y REGRESA VERDADERO O FALSO SI TIENE TODAS LAS VOCALES
def contieneLasVocales(letras):
    #Con el lower me cambia todas las letras a minusculas y hace una nueva cadena
    letras = letras.lower()
    #Con el find regresa el índice del caracter c, -1 si no lo encuentra.
    a = letras.find("a")
    e = letras.find("e")
    i = letras.find("i")
    o = letras.find("o")
    u = letras.find("u")

    if (a != -1) and (e != -1) and (i != -1) and (o != -1) and (u != -1):
        print (True)
    else:
        print (False)


#RECIBE NOMBRE, APELLIDO Y MATRICULA Y REGRESA UN NOMBRE DE USUARIO FORMADO DE LOS TRES PRIMEROS CARACTERES DE ESTOS TRES
def formarNombreUsuario(nombre, apellido, matricula):
    nombre=nombre.lower()
    apellido=apellido.lower()
    usuario = nombre[:3] + apellido[:3] + matricula[4:8]
    print("Usuario: ", usuario)


#RECIBE UNA CADENA QUE REPRESENTA EL NOMBRE DE UNA PERSONA, REGRESA TRUE SI LAS REGLAS DE MAYUSCULAS ESTAN BIEN APLICADAS Y FALSE EN OTRO CASO
def esCorrecto(nombreCompleto):
    nombre = nombreCompleto.split()
    for cadena in nombre:
        minuscula = cadena[1:]
        mayuscula = cadena[0:1]
    if mayuscula.isupper() and minuscula.islower():
        print(True)
    else:
        print(False)


#RECIBE UN PARAMETRO DE NUMERO DE TELEFONO EN EL FORMATO "01800-XXX-XXXX" Y REGRESA UNA CADENA DE NUMERO TELEONICO CON DIGITOS CORRESPONDIENTES
def traducirTelefono(telefono):
    n = ""
    numero = telefono.upper()

    for c in numero:
        if c == " ":
            n = n + "-"
        elif c == "A" or c == "B" or c == "C":
            n = n + "2"
        elif c == "D" or c == "E" or c == "F":
            n = n + "3"
        elif c == "G" or c == "H" or c == "I":
            n = n + "4"
        elif c == "J" or c == "K" or c == "L":
            n = n + "5"
        elif c == "M" or c == "N" or c == "O":
            n = n + "6"
        elif c == "P" or c == "Q" or c == "R" or c == "S":
            n = n + "7"
        elif c == "T" or c == "U" or c == "V":
            n = n + "8"
        elif c == "W" or c == "X" or c == "Y" or c == "Z":
            n = n + "9"

    numero = "01800-" + n
    print (numero)


def main():
    letras=str(input("Escribe una frase: "))
    combinarLetras(letras)
    contieneLasVocales(letras)
    nombre = input("Teclea tu primer nombre: ")
    apellido = input(("Teclea tu apellido paterno: "))
    matricula= str(input("Teclea tu matricula numerica entera (7 digitos): "))
    formarNombreUsuario(nombre, apellido, matricula)
    nombreCompleto=str(input("Teclea tu nombre y tus dos apellidos "))
    esCorrecto(nombreCompleto)
    telefono=str(input("Teclea teléfono que empiece con 01-800-XXX-XXXX. ejemplo (01800-VOY-BIEN) y traducirlo a numeros: "))
    traducirTelefono(telefono)



main()