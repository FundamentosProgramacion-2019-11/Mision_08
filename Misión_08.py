#Autor: Alan Giovanni Rodriguez Camacho
#Descripcion: MISION 8

def combinarLetras(cadena):
    cadenita = len(cadena)
    acumulador = ""
    for mod in range (cadenita):
        if (mod %2 == 0):
            par = cadena[mod].upper()
            acumulador = acumulador + par
        elif (mod %2 != 0):
            impar = cadena[mod].lower()
            acumulador = acumulador + impar
    return acumulador


def contieneLasVocales(cadenaa):
    cadenaa = cadenaa.lower()
    if "a" in cadenaa and "e" in cadenaa and "i" in cadenaa and "o" in cadenaa and "u" in cadenaa or "A" in cadenaa and "E" in cadenaa and "I" in cadenaa and "O" in cadenaa and "U" in cadenaa:
        return True
    else:
        return False


def formarNombreUsuario(nombre,apellidoPaterno,matricula):
    nombre = nombre.lower()[:3]
    apellidoPaterno =apellidoPaterno.lower()[:3]
    matricula = str(matricula)
    matriculaa = matricula[4:]
    usuario = nombre+apellidoPaterno+matriculaa
    return usuario


def esCorrecto(cadenaaa):
    if cadenaaa.istitle():
        return True
    else:
        return False


def traducirTelefono(telefono):






def main():
    cadena = input("Inserte una cadena:")
    print(combinarLetras(cadena))

    palabra=input("Inserte una palabra: ")
    print(contieneLasVocales(palabra))

    nombre = input("Inserte su nombre: ")
    apellidoPaterno = input("Inserte su apellido Paterno: ")
    matricula = int(input("Inserte su matricula de 7 digitos sin el A0: "))
    print(formarNombreUsuario(nombre,apellidoPaterno,matricula))

    nombree = input("Inserte su nombre con sus 2 apellidos: ")
    print(esCorrecto(nombree))

    telefono= input("Inserte su numero en formato '01800-XXX-XXXX': ")
    print(traducirTelefono(telefono))



main()