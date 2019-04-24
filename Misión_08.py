#Autor: César Guzmán Guadarrama
#Misión 08



def combinarLetras(cadena):
    contador = ""
    for x in range(len(cadena)):
        numLetra = cadena[x]
        if x == 0 or x % 2 == 0:
            contador += numLetra.upper()
        else:
            contador += numLetra.lower()
    print(contador)




def traducirTelefono(numero):
    numero1 = numero.replace("A", "2")
    numero2 = numero1.replace("B", "2")
    numero3 = numero2.replace("C", "2")
    numero4 = numero3.replace("D", "3")
    numero5 = numero4.replace("E", "3")
    numero6 = numero5.replace("F", "3")
    numero7 = numero6.replace("G", "4")
    numero8 = numero7.replace("H", "4")
    numero9 = numero8.replace("I", "4")
    numero10 = numero9.replace("J", "5")
    numero11 = numero10.replace("K", "5")
    numero12 = numero11.replace("L", "5")
    numero13 = numero12.replace("M", "6")
    numero14 = numero13.replace("N", "6")
    numero15 = numero14.replace("O", "6")
    numero16 = numero15.replace("P", "7")
    numero17 = numero16.replace("Q", "7")
    numero18 = numero17.replace("R", "7")
    numero19 = numero18.replace("S", "7")
    numero20 = numero19.replace("T", "8")
    numero21 = numero20.replace("U", "8")
    numero22 = numero21.replace("V", "8")
    numero23 = numero22.replace("W", "9")
    numero24 = numero23.replace("X", "9")
    numero25 = numero24.replace("Y", "9")
    numero26 = numero25.replace("Z", "9")

    return numero26



def esCorrecto(cadena2):
    cadena3 = cadena2
    cadena4 = cadena2.title()
    if cadena4 == cadena2:
        return "True"
    else:
        return "False"



def formarNombreUsuario(nombre, apellido, matricula):
    nombre2 = nombre[:3:]
    apellido2 = apellido[0:3:]
    matricula2 = matricula[5:len(matricula):]
    usuario = nombre2 + apellido2 + matricula2
    usuario2 = usuario.lower()
    return usuario2




def contieneLasVocales(cadena):

    cadena2 = cadena.lower()

    if "a" in cadena2 and "e" in cadena2 and "i" in cadena2 and "o" in cadena2 and "u" in cadena2:
        return "True"
    else:
        return "False"


def esValido(password):
    if len(password) >= 8:
        for x in password:
            if x.isupper():
                for x in password:
                    if x.lower():
                        for x in password:
                            if not x.isalnum():
                                for x in password:
                                    if x.isdigit():
                                        if password[0].isalpha():
                                            return True



def main():
    nombre = "Roberto"
    apellido = "Martínez"
    matricula = "12345678"
    password = "Abcd-123"
    combinarLetras("Cesar Guzman")
    print(contieneLasVocales("Abuelito"))
    print(formarNombreUsuario(nombre, apellido, matricula))
    print(esCorrecto("Cesar GUzMaN Guadarrama"))
    print(traducirTelefono("01800-VOY-BIEN"))
    print(esValido(password))



main()