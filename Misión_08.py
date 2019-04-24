#Autor: Diego Raul Elizalde Uriarte
#Mision 08







def combinarLetras(cadena):
    acumulador = ""
    for i in range(len(cadena)):
        letra = cadena[i]
        if i == 0 or i % 2 == 0:
            acumulador += letra.upper()
        else:
            acumulador += letra.lower()
    return acumulador



def contieneLasVocales(cadena):
     if cadena.find("a") != -1 or cadena.find("A") != -1:
         if cadena.find("e") != -1 or cadena.find("E") != -1:
             if cadena.find("i") != -1 or cadena.find("I") != -1:
                 if cadena.find ("o") != -1 or cadena.find("O") != -1:
                     if cadena.find ("u") != -1 or cadena.find("U") != -1:
                         return True
     else:
         return False



def formarNombreUsuario(Nombre, Apellido, Matricula):
    nombre = Nombre[0:3:1]
    apellido = Apellido[0:3:1]
    matricula = Matricula[len(Matricula)-3:len(Matricula):1]
    NombreUsuario = nombre + apellido + matricula
    UsuarioMinusculas = NombreUsuario.lower()
    return UsuarioMinusculas




def esCorrecto(NombrePersona):
    lista = NombrePersona.split()
    lista1 = lista[0]
    lista2 = lista[1]
    lista3 = lista[2]
    if lista1[0].isupper() and lista2[0].isupper() and lista3[0].isupper():
        if lista1[1:len(lista1):1].islower() and lista2[1:len(lista2):1].islower() and lista1[1:len(lista1):1].islower():
            return True
        else:
            return False
    else:
        return False


def traducirTelefono(cadena):
    cadena1 = cadena.replace("A", "2")
    cadena2 = cadena1.replace("B", "2")
    cadena3 = cadena2.replace("C", "2")
    cadena4 = cadena3.replace("D", "3")
    cadena5 = cadena4.replace("E", "3")
    cadena6 = cadena5.replace("F", "3")
    cadena7 = cadena6.replace("G", "4")
    cadena8 = cadena7.replace("H", "4")
    cadena9 = cadena8.replace("I", "4")
    cadena10 = cadena9.replace("J", "5")
    cadena11 = cadena10.replace("K", "5")
    cadena12 = cadena11.replace("L", "5")
    cadena13 = cadena12.replace("M", "6")
    cadena14 = cadena13.replace("N", "6")
    cadena15 = cadena14.replace("O", "6")
    cadena16 = cadena15.replace("P", "7")
    cadena17 = cadena16.replace("Q", "7")
    cadena18 = cadena17.replace("R", "7")
    cadena19 = cadena18.replace("S", "7")
    cadena20 = cadena19.replace("T", "8")
    cadena21 = cadena20.replace("U", "8")
    cadena22 = cadena21.replace("V", "8")
    cadena23 = cadena22.replace("W", "9")
    cadena24 = cadena23.replace("X", "9")
    cadena25 = cadena24.replace("Y", "9")
    cadena26 = cadena25.replace("Z", "9")

    return cadena26


def esValido(Password):
    minusculas = []
    mayusculas = []
    contador = 0
    if len(Password) >=8:
        i = 0
        for letra in Password:
            if letra.isupper():
                mayusculas.append(i)

            elif letra.islower():
                minusculas.append(i)

            i += 1

        if mayusculas != [] and minusculas !=[]:
            if Password.isalnum() == False:
                if any(i.isdigit() for i in Password):
                    if Password[0].isalpha():
                        for character in Password:
                            if character.isdigit() :

                                t = Password.find(character)

                                z = t+1

                                g = int(character)



                                if Password[z].isdigit() and z <= len(Password):
                                    h = int(Password[z])


                                    if h-g == 1:

                                        return False



                                    else:

                                        return True



                                else:
                                    return True


                        return False













                    else:
                        return(False)
                else:
                    return(False)

            else:
                return(False)
        else:
            return(False)

    return False


def main():
    combinarLetras("Hola Mundo")
    print(combinarLetras("Hola Mundo"))
    contieneLasVocales("Abuelito")
    print(contieneLasVocales("Abuelito"))
    Nombre = "Diego"
    Apellido = "Elizalde"
    Matricula = int("12345678")
    formarNombreUsuario(Nombre, Apellido, str(Matricula))
    print(formarNombreUsuario(Nombre, Apellido, str(Matricula)))
    NombrePersona = "Diego Elizalde Uriarte"
    esCorrecto(NombrePersona)
    print(esCorrecto(NombrePersona))
    traducirTelefono("01800-VOY-BIEN" )
    print(traducirTelefono("01800-VOY-BIEN"))
    Password = input("Password: ")
    esValido(Password)
    print(esValido(Password))










main()