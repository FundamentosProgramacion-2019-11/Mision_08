#Roberto Castro Barrios A01748559
#Descripción: Programa con diferentes funciones para cadenas

def combinarLetras(cadena):
    n = len(cadena)
    alternar = ""
    for i in range((n)):
        if i%2==0:
            alternar += cadena[i].upper()
        else:
            alternar += cadena[i].lower()
    return alternar

def contieneLasVocales (cadena):
    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"
    if a in cadena and e in cadena and i in cadena and o in cadena and u in cadena:
        return True
    else:
        return False

def esCorrecto(cadena):
    original = cadena
    cadenaMayusculaInicial = cadena.title()
    if cadenaMayusculaInicial == original:
        return True
    else:
        return False

def formarNombreUsuario (nombre, apellidoP, matricula):
    pass