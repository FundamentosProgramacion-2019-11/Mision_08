#Victor Ivan Morales Ramos A01377601

#Primera funcion

def combinarLetras(entrada):
    resultado = ""
    longitud = len(entrada)
    for letra in range(longitud):
        if letra%2 !=0:
            resultado += entrada[letra].lower()
        else:
            resultado += entrada[letra].upper()
    return resultado

def contieneLasVocales(entrada):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for vocal in entrada:
        if vocal == "a" or "A" or "á" or "Á":   ###
            a += 1                                #
        if vocal == "e" or "E" or "é" or "É":     #
            e += 1                                #
        if vocal == "i" or "I" or "í" or "Í":      ##Evalua la existencia de los digitos mencionados
            i += 1                                 ##
        if vocal == "o" or "O" or "ó" or "Ó":     #
            o += 1                                #
        if vocal == "u" or "U" or "ú" or "Ú":     #
            u += 1                              ###
    if a >= 1 and e >= 1 and i >= 1 and o >= 1 and u >= 1:
        return "True"
    else:
        return "False"

def formarNombreUsuario(nombre, apellidop, m):

    nombre = nombre.lower() #Pasa a minusculas
    apellidop = apellidop.lower() #pasa a minusculas
    nombreu = nombre[0:3]          #Agarra las letras en el intervalo
    apellidopu = apellidop[0:3]    #Agarra las letras en el intervalo
    mu = m[4:8]                    #Agarra los numeros en el intervalo

    nombrefinal = print(nombreu + apellidopu + mu)  #Muestra el resultado
    return nombrefinal

def esCorrecto(nombre, a1, a2):
    mayusculas = 0
    minusculas = 0

    n1 = nombre[0:1]
    a1l = a1[0:1]
    a2l = a2[0:1]

    if n1.isupper():
        mayusculas +=1
    if a1l.isupper():
        mayusculas += 1
    if a2l.isupper():
        mayusculas += 1
    else:
        minusculas += 1

    if minusculas >= 1:
        print("FALSE")
    else:
        print("TRUE")

def traducirTelefono(numeroin):
    digito = ""
    frase = numeroin[6::]
    for no in frase:
        if no == "1":
            digito += 1
        if (no == "A") or (no == "B") or (no == "C"):
            digito += 2
        if (no == "D")or (no == "E") or (no == "F"):
            digito += 3
        if (no == "G") or (no == "H") or (no == "I"):
            digito += 4
        if (no == "J") or (no == "K") or (no == "L"):
            digito += 5
        if (no == "M") or (no == "N") or (no == "O"):
            digito += 6
        if (no == "P") or (no == "Q") or (no == "R") or (no == "S"):
            digito += 7
        if (no == "T") or (no == "U") or (no == "V"):
            digito += 8
        if (no == "W") or (no == "X") or (no == "Y") or (no == "Z"):
            digito += 9
        else:
            digito += "-"
    return "01800-" + digito



def main():
    #---------------------------------------------#
    #FUNCION 1:                                   #
    p = input("inserta una oracion: ")            #
    r = combinarLetras(p)                         #
    print(r)                                      #
    #---------------------------------------------#
    #FUNCION 2:                                     #
    letra = input("Dime una palabra: ")             #
    vof = contieneLasVocales(letra)                 #
    print(vof)                                      #
    #-----------------------------------------------#
    #FUNCION 3:                                             #
    name = input("Dime tu nombre: ")                        #
    surname = input("Dime tu Apellido Paterno: ")           #
    matricula = input("Escribe tu matricula: A0")           #
    fname = formarNombreUsuario(name, surname, matricula)   #
    print(fname)                                            #
    #-------------------------------------------------------#
    #FUNCION 4:                                         #
    name0 = input("Dime tu nombre: ")                   #
    surname0 = input("Dime tu primer apellido: ")       #
    surname01 = input("Dime tu psegundo apellido: ")    #
    tof = esCorrecto(name0, surname0, surname01)        #
    print(tof)                                          #
    #---------------------------------------------------#
    #FUNCION 5:
    noin = input("Dime una frase en formato 01800-XXX-XXXX: ")
    termina = traducirTelefono(noin)
    print(termina)

main()