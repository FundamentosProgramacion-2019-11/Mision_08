#Autor David Yair Fernández Salas
#A01747088
#Este programa realiza difernetes funciones de cadenas regresando valores que los problemas piden para cada función


"""Esta es una función cuyo objetivo es que el usuario introduzca una cadena, y le devuelva la misma cadena, pero
con letras en mayusculas y minusculas. La función usa "len" que sirve para que cuente cuantos caracteres tiene el
código y usa un ciclo para que se guarde cada caracter e imprima un resultado, tambien se uso "upper" que es para
hacer más grandes las palabras que uno desea y un lower para que las letras disminuyan su tamaño"""
def combinarLetra(palabras):
    letras = len(palabras)
    nuevaCadena = ""
    for letra in range(letras):
        mayuscula = (palabras[letra].upper())
        minuscula = (palabras[letra].lower())
        if (letra%2==0):
            nuevaCadena+=mayuscula
        else:
            nuevaCadena+=minuscula
    return nuevaCadena




"""Esta función, realiza mediante un ciclo for la tarea de buscar con un contador si es que la palabra que introduce 
el usuario contiene todas las vocales (a,e,i,o,u) y regresa true si es que lo cumple y si no regresa es el caso regresa
False"""
def contieneVocales(pregunta2):
    vocales= ["a","e","i","o","u"]
    cadenaBien=""
    for i in pregunta2:
        if i in vocales:
            cadenaBien+=i
    contA=0
    contE=0
    contI=0
    contO=0
    contU=0
    for y in cadenaBien:
        if y== vocales[0]:
            contA+=1
        if y== vocales[1]:
            contE+=1
        if y== vocales[2]:
            contI+=1
        if y== vocales[3]:
            contO+=1
        if y== vocales[4]:
            contU+=1
    if contA*contE*contI*contO*contU !=0:
        return True
    else:
        return False#Multiplica todos los corredores y si alguno da 0 , regresa False


"""esta función recibe tanto el nombre, como el apellido y la matricula que el usuario quiere introducir
se uso los operadores de slice que lo que hacen es que cortan cada cadena en los caracteres que uno desea para que 
a a la hora de imprimir solo aparezcan éstos  """
def formarNombreUsuario(nombre,apellido,matricula):
    nombreCortado=slice(3) # se uso slice para indicar le a pycharm y a la función que solo quiero usar esos caracteres
    apellidoCortado= slice(3) # y lo corte hasta los primeros 3 caracteres
    nombrebien=(nombre[nombreCortado]+apellido[apellidoCortado]+matricula[0:3])
    print(nombrebien)
#se usó este formato pues esta usando los parametros que el usuario ingreso y se puso en[]las variables quese cortaron
#para poder guardalos todos en una variable con + y imprimir esa variable


"""esta función toma los parametros de nombre,apellidoPaterno y apellidoMaterno que el usuario ingresa y usando los 
operadores """
def esCorrecto(nombre1):
    partesnombre= nombre1.split () # te regresa el nombre en formato de lista,toma como referencia los espacios entre
    # palabras para separarlas
    correcto= 0 #contador de inicial mayuscula
    tamanoNombre=len(partesnombre) #Deteceta la cant de palabras del nombre(excepto la ñ)
    for i in range(0,tamanoNombre): #Recorre el rango de o al num de letras de la palabra
        for j in partesnombre[i]:#recorre las letras de la palabra
            for x in range(0,len(partesnombre[i])): #Recorre el rango de 0 al num de letras de la palabra
                if j.isupper()==True: #como es lista,cada nombre y apellido tiene un lugar ordenado en esa lista y siempre...
                    correcto+=1#Si es mayuscula , la suma al contador
                if x!=0:##como queremos que solo la primera se mayuscula este "if detectasi alguna de las demas es mayuscula y si lo es...
                    if j.isupper()==True:##... le resta al contador
                        correcto-=1
    if correcto == tamanoNombre:## el numero de mayusculas iniciales tienen que ser igual que el numero de palabras que tenga el nombre
        return True
    else:
        return False


"""Esta función realiza la traducción de numeros a letras mediante el uso de contadores y se uso if para cada condicón y 
 poder dar con el numero que buscamos """
def traducirTelefono(numeroTelefono):
    contador=" "
    for letra in range(len(numeroTelefono)):
        if letra== "A" or "B" or "C":
            contador+= "2"
        if letra=="D" or "E" or "F":
            contador+="3"
        if letra=="G" or "H" or"I":
            contador+="4"
        if letra =="J" or "K" or "L":
            contador+="5"
        if letra=="M" or "N" or "O":
            contador+="6"
        if letra =="P" or "Q" or "R" or "S":
            contador+="7"
        if letra =="T" or "U" or "V":
            contador+="8"
        if letra=="W" or "X" or "Y" or "Z":
            contador+="9"
        else:
            pass
    return("01800"+contador)


"""Esta función es la principal y de aqui salen los paramateros para que se puedan realizar todas las opercaiones """
def main():
    palabras = str(input("Dime tu palabra: "))
    combinarLetra(palabras)
    nuevaCadena=combinarLetra(palabras)
    print(nuevaCadena)
    pregunta2= input("Dime tu palabra: ")
    vocales=contieneVocales(pregunta2)
    print(vocales)
    nombre = str(input("Dime tu nombre: "))
    apellido = str(input("Dime tu apellido: "))
    matricula = (input("Dime tu matricula sin el a0 (solo los 7 digitos): "))
    formarNombreUsuario(nombre,apellido,matricula)
    nombre1 = str(input("Dime tu nombre completo con apellidos(Paterno y Materno): "))
    nombreCorrecto=esCorrecto(nombre1)
    print(nombreCorrecto)
    numeroTelefono=(input("Dime tu numero: "))
    convertir=traducirTelefono(numeroTelefono)
    print(convertir)


main()