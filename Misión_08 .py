# Usuario: Luis Renteria
# Misión 8

def combinarLetras(cadena):
    cadenaFinal=''
    for i in range(len(cadena)):
        if i%2==0:
            cadenaFinal+=cadena[i].upper()
        else:
            cadenaFinal+=cadena[i].lower()
    return cadenaFinal

def contieneLasVocales(cadena):
    vocales=['a','e','i','o','u']
    vocalesLeidas=[]
    for letra in cadena:
        if letra.lower() in vocales and not letra.lower() in vocalesLeidas:
            vocalesLeidas.append(letra)
    if len(vocalesLeidas)==5:
        return True
    else:
        return False

def formarNombreUsuario(nombre,apellidoPat, matriculaNum):
    if len(nombre)<3 or len(apellidoPat)<3 or len(str(matriculaNum))<7:
        return 'Datos incorrectos!!'
    userName=''
    userName+=nombre[:3]+apellidoPat[:3]+str(matriculaNum)[-3:]
    return userName.lower()

def esCorrecto(cadena):
    listaNombre=cadena.split()
    checkPalabra=[]
    for palabra in listaNombre:
        if palabra[0]==palabra[0].upper() and palabra[1:]==palabra[1:].lower():
            checkPalabra.append(True)
        else:
            return False
    return True

def traducirTelefono(cadena):
    cadenaFinal=''
    for caracter in cadena:
        if caracter.lower() in ['a','b','c']:
            cadenaFinal+='2'
        elif caracter.lower() in ['d','e','f']:
            cadenaFinal+='3'
        elif caracter.lower() in ['g','h','i']:
            cadenaFinal+='4'
        elif caracter.lower() in ['j','k','l']:
            cadenaFinal+='5'
        elif caracter.lower() in ['m','n','o']:
            cadenaFinal+='6'
        elif caracter.lower() in ['p','q','r','s']:
            cadenaFinal+='7'
        elif caracter.lower() in ['t','u','v']:
            cadenaFinal+='8'
        elif caracter.lower() in ['x','w','y','z']:
            cadenaFinal+='9'
        else:
            cadenaFinal+=caracter
    return cadenaFinal

def esValido(cadena):
    if len(cadena)<8 or cadena[0].isdigit():
        return False
    mayus=0
    minus=0
    especial=0
    digits=0
    for caracter in cadena:
        if caracter.isalpha() and caracter==caracter.upper():
            mayus+=1
        elif caracter.isalpha() and  caracter==caracter.lower():
            minus+=1
        elif not caracter.isalpha() and not caracter.isdigit():
            especial+=1
        elif caracter.isdigit():
            digits+=1
    if mayus==0 or minus==0 or especial==0 or digits==0:
        return False
    for i in range(len(cadena)):
        if i<len(cadena)-1 and cadena[i].isdigit():
            if int(cadena[i])+1==int(cadena[i+1]):
                return False
    return True
    
def mainPruebas():
    print('--------combinarLetras("Hola mundo")--------')
    print(combinarLetras('Hola mundo'))
    print('--------contieneLasVocales("Monterrey")--------')
    print(contieneLasVocales('Monterrey'))
    print('--------contieneLasVocales("Abuelito")--------')
    print(contieneLasVocales('Abuelito'))
    print('--------formarNombreUsuario("Roberto","Martínez",12345678)--------')
    print(formarNombreUsuario('Roberto','Martínez',12345678))
    print('--------esCorrecto("Roberto Martínez Román")--------')
    print(esCorrecto('Roberto Martínez Román'))
    print('--------esCorrecto("roberto MARtinez RoMan")--------')
    print(esCorrecto('roberto MARtinez RoMan'))
    print('--------traducirTelefono("01800-VOY-BIEN")--------')
    print(traducirTelefono('01800-VOY-BIEN'))
    print('--------esValido("Abcd-7635")--------')
    print(esValido('Abcd-7635'))
    print('--------esValido("abcd1936")--------')
    print(esValido('abcd1936'))

mainPruebas()
