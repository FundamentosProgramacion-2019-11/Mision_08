#Autor: Michel Antoine Dionne Gutierrez A0174863, Grupo: 03
#Tarea Cadenas

def combinarLetras(cadena):
    resultado = " "
    for x in range(len(cadena)):
        caracter = cadena[x]
        if x == 0 or x % 2 == 0:
            resultado = resultado + caracter.upper()
        else:
            resultado = resultado + caracter.lower()
    return resultado

def contieneLasVocales(cadena):
    cadenaMayus = cadena.upper()
    a = cadenaMayus.count("A")
    e = cadenaMayus.count("E")
    i = cadenaMayus.count("I")
    o = cadenaMayus.count("O")
    u = cadenaMayus.count("U")
    if a==1 and e==1 and i==1 and o==1 and u==1:
        return True
    else:
        return False
    
def formarNombreUsuario(nombre, apellido, matricula):
    strmatricula = str(matricula)
    nombreUno = nombre.lower()
    apellidoUno = apellido.lower()
    usuario = nombreUno[0:3:1]+apellidoUno[0:3:1]+strmatricula[4:len(strmatricula):1]
    return usuario

def esCorrecto(nomCompleto):
    correcto = nomCompleto.title()
    if nomCompleto == correcto:
        return True
    else:
        return False

def traducirTelefono(tel):
    uno = tel.replace("A", "2")
    dos = uno.replace("B","2")
    tres = dos.replace("C","2")
    cuatro = tres.replace("D","3")
    cinco = cuatro.replace("E", "3")
    seis = cinco.replace("F", "3")
    siete = seis.replace("G", "4")
    ocho = siete.replace("H","4")
    nueve = ocho.replace("I","4")
    diez = nueve.replace("J","5")
    once = diez.replace("K","5")
    doce = once.replace("L","5")
    trece = doce.replace("M","6")
    catorce = trece.replace("N","6")
    quince = catorce.replace("O","6")
    diezseis = quince.replace("P","7")
    diezsiete = diezseis.replace("Q","7")
    diezocho = diezsiete.replace("R","7")
    dieznueve = diezocho.replace("S","7")
    veinte = dieznueve.replace("T","8")
    veinteuno = veinte.replace("U","8")
    veintedos = veinteuno.replace("V","8")
    veintetres = veintedos.replace("W","9")
    veintecuatro = veintetres.replace("X","9")
    veintecinco = veintecuatro.replace("Y","9")
    veinteseis = veintecinco.replace("Z","9")
    return veinteseis

def main():
    a = combinarLetras("Hola Mundo")
    b = contieneLasVocales("Abuelito")
    #nombre = str(input("Dame tu nombre"))
    #apellido = str(input("Dame tu apellido"))
    #matricula = int(input("Dame tu matricula"))
    c = formarNombreUsuario("Michel", "Dionne", "1748632")
    print(a)
    print(b)
    print(c)
    #nomCompleto = str(input("Pon tu nombre completo"))
    d = esCorrecto("Michel Antoine Dionne Gutierrez")
    print(d)
    #tel = str(input("Dame el numero de telefono"))
    e = traducirTelefono("01800-VOY-BIEN")
    print(e)

main()
