#José Isidro Sánchez Vázquez A01748144
#Tarea sobre el uso de cadenas

def combinarLetras(cadena):
    NuevaCadena=""
    par=1
    for Ncadena in cadena:
        impar=1
        if(par == 1 and impar ==1):
            NuevaCadena += str(Ncadena.upper())
            par = 2
            impar=0
        if(par == 2 and impar ==1):
            NuevaCadena += str(Ncadena.lower())
            par = 1
            impar = 0
    return result

def contieneLasVocales(cadena):
    a = 0
    i = 0
    u = 0
    e = 0
    o = 0
    for x in cadena:
        if(x == "a"):
            a=1
        elif (x == "a"):
            i = 1
        elif (x == "a"):
            u = 1
        elif (x == "a"):
            e = 1
        elif (x == "a"):
            o = 1
    if((a+i+u+e+o)==5): #La condicion hace la suma de todos los datos y si la suma es 5 es por que todas las bocales se encuentran
        return True
    return False

def formarNombreUsuario(nombre, apellido, matricula):
    usuario=""
    usuario+=nombre[0:3]
    usuario += apellido[0:3]
    usuario += matricula[-3:]
    return usuario

def esCorrecto(nombre):
    dividir = nombre.split()
    first = dividir[0]
    second = dividir[1]
    third = dividir[2]
    if(first[0].isupper()):
        if(first[1:].islower()):
            if(second[0].isupper()):
                if (second[1:].islower()):
                    if (third[0].isupper()):
                        if (third[1:].islower()):
                            return True


    return False

def traducirTelefono(telefono):
    dividir = telefono[6:]
    codedPhone="01800-"
    for x in dividir:
        if(x=="A" or x=="B" or x=="C"):
            codedPhone+="2"
        elif (x == "D" or x == "E" or x == "F"):
            codedPhone += "3"
        elif (x == "G" or x == "H" or x == "I"):
            codedPhone += "4"
        elif (x == "J" or x == "K" or x == "L"):
            codedPhone += "5"
        elif (x == "M" or x == "N" or x == "O"):
            codedPhone += "6"
        elif (x == "P" or x == "Q" or x == "R" or x=="S"):
            codedPhone += "7"
        elif (x == "S" or x == "T" or x == "V"):
            codedPhone += "8"
        elif (x == "W" or x == "X" or x == "Y" or x=="Z"):
            codedPhone += "9"
        elif(x=="-"):
            codedPhone +="-"
    return codedPhone



def main():
    print("Menu")
    print("1.-Funcion convinar letras")
    print("2.-Contiene vocales")
    print("3.-Formar nombre de usuario")
    print("4.-funcion es correcto")
    print("5.-Traducir telefono")
    print("7.-Terminar")
    numElegido= int(input("Que funcion quieres usar: "))
    if numElegido==1:
        cadena = input("Escribe la cadena: ")
        nuevaCadena = combinarLetras(cadena)
        print(nuevaCadena)
    elif numElegido ==2:
        cadena = input("Escribe la cadena: ")
        cadenaNueva=contieneLasVocales(cadena)
        print(cadenaNueva)
    elif numElegido ==3:
        nombre = input("Teclea tu nombre: ")
        apellido = input("Teclea tu apellido: ")
        matricula = input("Teclea la matricula: ")
        NombreUsuario=formarNombreUsuario(nombre,apellido,matricula)
        print(NombreUsuario)
    elif numElegido ==4:
        nombre = input("Teclea tu nombre: ")
        correcto = esCorrecto(nombre)
        print(correcto)
    elif numElegido ==5:
        telefono= input("Teclea el telefono")
        traducirTelefono(telefono)
    elif numElegido ==7:
        print("gracias vuelva pronto")


main()