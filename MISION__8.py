#Autor: Andrea Romo Ortega, A01375591
#Misión 8 segundo intento

#tengo un dilema, el programa aquí solo funciona con print y en el de la tarea solo funciona con return asi que pondré dos veces mi código para
#que vea que si funciona, y abajo el que tiene los prints. :D

def combinarLetras(cadena):

    mayusculas = letra.upper()
    minusculas = letra.lower()
    combina = ""

    for letra in range (0, len(cadena[1::1]), 3):
        combina = combina + mayusculas[letra] + minusculas[letra + 1]

    return (combina)


def contieneLasVocales(cadena):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    laVocalA =["A", "a"]
    laVocalE =["E","e"]
    laVocalI =["I","i"]
    laVocalO =["O","o"]
    laVocalU =["U","u"]

    for letra in cadena:
        for aVocal in laVocalA:
            if aVocal in letra:
                a+=1
        for eVocal in laVocalE:
            if eVocal in letra:
                e+=1
        for iVocal in laVocalI:
            if iVocal in letra:
                i+=1
        for oVocal in laVocalO:
            if oVocal in letra:
                o+=1
        for uVocal in laVocalU:
            if uVocal in letra:
                u+=1

    if a>=1 and e>=1 and i>=1 and o>=1 and u>=1:
        print(True)
        return True
    else:
        print ("Error")
        return False


def formarNombreUsuario(nombre, apellido, matricula):
    nombre = nombre.lower()
    apellido = apellido.lower()
    matricula = str(matricula)
    n= nombre[:3:]
    a= apellido[:3:]
    m = matricula[4:]
    usuario= n+a+m
    return(usuario)


def esCorrecto(cadena):
    nombre= cadena.split()
    for palabra in nombre:
        for letra in palabra[0]:
            if letra.islower():
                print(False)
                return False
        for letra in palabra[1::]:
            if letra.isupper():
                print(False)
                return False
    print(True)
    return True


def traducirTelefono( numero):
    numeros = str( numero)
    letras = numeros.upper()
    guion = ["-", "_", " "]
    n2= ["A","B","C"]
    n3=["D","E","F"]
    n4=["G","H","I"]
    n5=["J","K","L"]
    n6=["M","N","O"]
    n7=["P","Q","R","S"]
    n8=["T","U","V"]
    n9=["W","X","Y","Z"]
    nCompleto= numeros[:5:]
    for letra in letras:
        for numeros in n2:
            if numeros in letra:
                nCompleto+="2"
        for numeros in n3:
            if numeros in letra:
                nCompleto+="3"
        for numeros in n4:
            if numeros in letra:
                nCompleto+="4"
        for numeros in n5:
            if numeros in letra:
                nCompleto+="5"
        for numeros in n6:
            if numeros in letra:
                nCompleto+="6"
        for numeros in n7:
            if numeros in letra:
                nCompleto+="7"
        for numeros in n8:
            if numeros in letra:
                nCompleto+="8"
        for numeros in n9:
            if numeros in letra:
                nCompleto+="9"
        for numeros in guion:
            if numeros in letra:
                nCompleto += "-"
    return (nCompleto)








#este es el de los prints, este no va en su codigo....





def combinarLetras(cadena):

    mayusculas = cadena.upper()
    minusculas = cadena.lower()
    combina = ""


    for letra in range(0, len(cadena[1::1]), 2):
        combina = combina + mayusculas[letra] + minusculas[letra+1 ]
    print (combina)


def contieneLasVocales(cadena):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    laVocalA =["A", "a"]
    laVocalE =["E","e"]
    laVocalI =["I","i"]
    laVocalO =["O","o"]
    laVocalU =["U","u"]

    for letra in cadena:
        for aVocal in laVocalA:
            if aVocal in letra:
                a+=1
        for eVocal in laVocalE:
            if eVocal in letra:
                e+=1
        for iVocal in laVocalI:
            if iVocal in letra:
                i+=1
        for oVocal in laVocalO:
            if oVocal in letra:
                o+=1
        for uVocal in laVocalU:
            if uVocal in letra:
                u+=1

    if a>=1 and e>=1 and i>=1 and o>=1 and u>=1:
        print(True)
        return True
    else:
        print ("Error")
        return False


def formarNombreUsuario(nombre, apellido, matricula):
    nombre = nombre.lower()
    apellido = apellido.lower()
    matricula = str(matricula)
    n= nombre[:3:]
    a= apellido[:3:]
    m = matricula[4:]
    usuario= n+a+m
    print(usuario)


def esCorrecto(cadena):
    nombre= cadena.split()
    for palabra in nombre:
        for letra in palabra[0]:
            if letra.islower():
                print(False)
                return False
        for letra in palabra[1::]:
            if letra.isupper():
                print(False)
                return False
    print(True)
    return True


def traducirTelefono( numero):
    numeros = str( numero)
    letras = numeros.upper()
    guion = ["-", "_", " "]
    n2= ["A","B","C"]
    n3=["D","E","F"]
    n4=["G","H","I"]
    n5=["J","K","L"]
    n6=["M","N","O"]
    n7=["P","Q","R","S"]
    n8=["T","U","V"]
    n9=["W","X","Y","Z"]
    nCompleto= numeros[:5:]
    for letra in letras:
        for numeros in n2:
            if numeros in letra:
                nCompleto+="2"
        for numeros in n3:
            if numeros in letra:
                nCompleto+="3"
        for numeros in n4:
            if numeros in letra:
                nCompleto+="4"
        for numeros in n5:
            if numeros in letra:
                nCompleto+="5"
        for numeros in n6:
            if numeros in letra:
                nCompleto+="6"
        for numeros in n7:
            if numeros in letra:
                nCompleto+="7"
        for numeros in n8:
            if numeros in letra:
                nCompleto+="8"
        for numeros in n9:
            if numeros in letra:
                nCompleto+="9"
        for numeros in guion:
            if numeros in letra:
                nCompleto += "-"
    print (nCompleto)




def main():
    combinarLetras("hola mundo")
    combinarLetras("robertomtzroman ")
    contieneLasVocales("Abuelito")
    formarNombreUsuario("Andrea", "Romo", 1375591)
    formarNombreUsuario("Roberto", "Martinez", 1234567)
    esCorrecto("Andrea Romo Ortega")
    traducirTelefono("01800-VOY-BIEN")



main()