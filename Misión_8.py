# Autor: Victor Manuel Cerón Navarrete
# Descripción: Misión 8 Cadena

def combinarLetras(cadena):
    palabra = "" # funciona de acomulador
    posicionLetra = 1 # Se sumará y restará a si mismo dependiendo de si su posición da 1 o 0
    for n in cadena:
        if posicionLetra == 1: #Da la primera posición como 1, lo que hace que sea mayuscula

            n = n.upper()

        elif posicionLetra == 0:

            n = n.lower()


        palabra = palabra + n # escribe la letra
        posicionLetra =- posicionLetra # Convierte la posicionLetra a 0
    print(palabra)

def contieneLasVocales(palabra):
    letraA = 0
    letraE = 0
    letraI = 0
    letraO = 0
    letraU = 0

    for i in palabra:
        if i == "a" or i == "A":
            letraA= letraA + 1
        elif i == "e" or i == "E":
            letraE = letraE + 1
        elif i == "i" or i == "I":
            letraI= letraI + 1
        elif i == "o" or i == "O":
            letraO= letraO + 1
        elif i == "u" or i == "U":
            letraU= letraU + 1

    if letraA >= 1 and letraE >= 1 and letraI >= 1 and letraO >= 1 and letraU >= 1:
        print("Tiene todas las vocales" )
    else:
        print("no tiene todas las vocales")

def formarNombreUsuario(nombreUsuario, apellidoUsuario, matriculaUsuario):
    nombreUsuario = nombreUsuario.lower()  #El nombre y apellido los hace todos minúscula
    apellidoUsuario = apellidoUsuario.lower()
    matriculaUsuario = str(matriculaUsuario)
    print("Tu usuario es:", nombreUsuario[0:3], apellidoUsuario[0:3], matriculaUsuario[6:9])

def esCorrecto(persona):
    nombre = persona.split()
    for x in nombre:
        for y in x[0]:  #y es la primera letra
            if y.islower():
                print("False. Las mayúsculas están mal posicionadas")
                return False


    print("True. Tus mayúsculas estan bien posicionadas.")
    return True


#def traducirTelefono(telefono):
    telefono=str(telefono)

    numerodos = A or a or B or b or C or c
    numerotres = D or d or E or e or F or f
    numerocuatro = G or g or H or h or I or i
    numerocinco = J or j or K or k or L or l
    numeroseis = M or m or N or n or O or o
    numerosiete = P or p or Q or q or R or r or S or s
    numeroocho = T or t or U or u or V or v
    numeronueve = W or w or X or x or Y or y or Z or z

    #No pude prof, perdon :(



def main():
    cadena = str(input("Teclea tu frase: "))
    palabra = str(input("Teclea tu palabra o frase y te diré si contiene todas las vocales: "))
    nombreUsuario = str(input("Escribe tu primer nombre: "))
    apellidoUsuario = str(input("Escribe tu apellido paterno: "))
    matriculaUsuario = str(input("Teclea tu matrícula: "))
    persona = str(input("Teclea un nombre y dos apellidos. Te diré si tus mayúsculas están bien posicionadas: "))
    combinarLetras(cadena)
    contieneLasVocales(palabra)
    formarNombreUsuario(nombreUsuario, apellidoUsuario, matriculaUsuario)
    esCorrecto(persona)
    #traducirTelefono()






main()