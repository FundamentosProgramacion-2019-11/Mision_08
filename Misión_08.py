#Autor: Santiago España Vázquez - A01748311
#Misión 08 Cadenas

def combinarLetras(cadena):
    result=""
    x=1
    for c in cadena:
        y=1
        if(x == 1 and y==1):
            result += str(c.upper())
            x = 2
            y=0
        if(x == 2 and y==1):
            result += str(c.lower())
            x = 1
            y = 0
    return result

def contieneLasVocales(cadena):
    a = 0
    i = 0
    u = 0
    e = 0
    o = 0
    for c in cadena:
        if(c == "a"):
            a=1
        if (c == "a"):
            i = 1
        if (c == "a"):
            u = 1
        if (c == "a"):
            e = 1
        if (c == "a"):
            o = 1
    if((a+i+u+e+o)==5):
        return True
    return False

def formarNombreUsuario(nombre, apellido, matricula):
    username=""
    username+=nombre[0:3]
    username += apellido[0:3]
    username += matricula[-3:]
    return username

def esCorrecto(nombre):
    roto = nombre.split()
    first = roto[0]
    second = roto[1]
    third = roto[2]
    if(first[0].isupper()):
        if(first[1:].islower()):
            if(second[0].isupper()):
                if (second[1:].islower()):
                    if (third[0].isupper()):
                        if (third[1:].islower()):
                            return True


    return False

def traducirTelefono(telefono):
    roto = telefono[6:]
    codedPhone="01800-"
    for c in roto:
        if(c=="A" or c=="B" or c=="C"):
            codedPhone+="2"
        elif (c == "D" or c == "E" or c == "F"):
            codedPhone += "3"
        elif (c == "G" or c == "H" or c == "I"):
            codedPhone += "4"
        elif (c == "J" or c == "K" or c == "L"):
            codedPhone += "5"
        elif (c == "M" or c == "N" or c == "O"):
            codedPhone += "6"
        elif (c == "P" or c == "Q" or c == "R" or c=="S"):
            codedPhone += "7"
        elif (c == "S" or c == "T" or c == "V"):
            codedPhone += "8"
        elif (c == "W" or c == "X" or c == "Y" or c=="Z"):
            codedPhone += "9"
        elif(c=="-"):
            codedPhone +="-"
    return codedPhone