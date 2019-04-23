#Autor: Luis Alberto Zepeda Hernandez, A01328616
#Descripción Mision 08



#Esta funcion untercala las letras dentro de una cadena, entre mayuscúlas y minuscúlas.
def combinarLetras(cadena):
    cont = ""
    for letra in range(len(cadena)):
        if letra %2 == 0:
            mayusculas = cadena[letra].upper()
            cont += mayusculas 

        else:
            minusculas = cadena[letra].lower()
            cont += minusculas

    return cont


#Esta funcion verfica si una cadena contiene las vocales dentro de esta. Regresa true si todas las vocales forman parte. False si no.
def contieneLasVocales(cadena):
    cadena = cadena.lower()
    if "a" and "e" and "i" and "o" and "u" in cadena:
        return True

    else:
        return False


#Esta funcion crea un user name con el nombre, apellido y matricula.
def formarNombreUsuario(nombre,apellidoPaterno,matricula):
    nombre = nombre.lower()
    apellidoPaterno = apellidoPaterno.lower()
    cadenaMatricula = str(matricula)

    return nombre[:3:] + apellidoPaterno[:3:] + cadenaMatricula[-3::]


#Funcion para comprobar si hay mayúscula después de un espacio en un nombre sencillo.
def esCorrecto(nombre):
    nombreSeparado = nombre.split()
    for letra in nombreSeparado:
        mayusc = letra[:1:]
        minusc = letra[1::]
    if mayusc.isupper() and minusc.islower():
        return True
    else:
        return False


#Esta funcion traduce un número telefoníco con letras dentro de este a numeros.
def traducirTelefono(telefono):
    cont =""

    for numero in telefono:
        if numero == "A" or numero == "B" or numero == "C":
            cont = cont + "2"
        elif numero == "D" or numero == "E" or numero == "F":
            cont = cont + "3"
        elif numero == "G" or numero == "H" or numero == "I":
            cont = cont + "4"
        elif numero == "J" or numero == "K" or numero == "L":
            cont = cont + "5"
        elif numero == "M" or numero == "N" or numero == "O":
            cont = cont + "6"
        elif numero == "P" or numero == "Q" or numero == "R" or numero == "S":
            cont = cont + "7"
        elif numero == "T" or numero == "U" or numero == "V" :
            cont = cont + "8"
        elif numero == "W" or numero == "X" or numero == "Y" or numero == "Z":
            cont = cont + "9"
        elif numero == "-":
            cont = cont +"-"

    return "01800"+cont


#Esta función se encarga de llamar e imprimir lo que hacen las funciones
def main():
    print(combinarLetras("hola mundo"))

    print(contieneLasVocales("abuelito"))

    print(formarNombreUsuario("Luis","Zepeda",1328616))

    print(esCorrecto("Luis Alberto zepeda"))

    print(traducirTelefono("01800-VOY-BIEN"))

    
main()