#Autor: Andrea Romo Ortega, A01375591
#Misión 8

def combinarLetras(cadena):

    mayusculas = cadena.upper()
    minusculas = cadena.lower()
    combina = ""

    for letra in range(0, len (cadena), 2):
        combina = combina + mayusculas[letra]+ minusculas[letra +1]

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
        print(nCompleto)



# Ejercicio EXTRA
def esValido(contrasena):
    reglasOK = 0
    letraMayus = 0
    letraMinus = 0
    digito = 0
    # 8 caracteres o más
    if len(contrasena) >= 8:
        reglasOK += 1

    # al menos un carácter especial
    if not contrasena.isalnum(): #un guion  es especial
        reglasOK += 1 #num

    # al menos una mayúscula y una minúscula
    # al menos 1 dígito
    for letra in contrasena:
        if letra.isupper(): # revisa mayuscula
            letraMayus += 1
        elif letra.islower():# revisa minuscula
            letraMinus += 1
        elif letra.isnumeric(): #revisa numero
            digito += 1
    if letraMayus >= 1 and letraMinus >= 1 and digito >= 1: #revisa que haya uno de cada uno
        reglasOK += 2

    # comienza con una letra
    for caracter in contrasena[0]:
        if not caracter.isnumeric(): #deja pasar las que empiezan con letra
            reglasOK += 1

    # no dígitos consecutivos
    noConsecutivo = 0
    contrasenaSeparada = ""
    for caracter in contrasena:
        if caracter.isnumeric():
            while noConsecutivo == 0: # checa que los numeros no sean en cadena
                noConsecutivo += 1
                contrasenaSeparada = contrasena.split(caracter)

    # comprueba que la cadena tenga solo numeros
    soloNum = ""
    for caracter in contrasenaSeparada[1]:
        if caracter.isnumeric(): # en esta parte hace el chequeo
            soloNum += caracter

    # Obtiene el par de números consecutivos
    segundoNumero = soloNum[0]
    numeroAntecesor = str(int(segundoNumero) - 1)
    numerosConsecutivos = numeroAntecesor + segundoNumero  #rompe cadena de numeros seguidos
    if not numerosConsecutivos in contrasena:
        reglasOK += 1

    # Comprueba que todas las reglas se cumplan
    if reglasOK == 6:
        print(True)
        return True
    else:
        print(False)
        return False


def main():
    combinarLetras("la vida es bella")
    contieneLasVocales("Abuelito")
    formarNombreUsuario("Andrea", "Romo", 1375591)
    esCorrecto("Andrea Romo Ortega")
    traducirTelefono("01800-VOY-BIEN")
    esValido("Afew-58Gm")


main()