#David Yair Fernández Salas
#A01747088
#Este programa realiza difernetes funciones de cadenas regresando valores que los problemas piden para cada función

"""Esta es una función cuyo objetivo es que el usuario introduzca una cadena, y le devuelva la misma cadena, pero
con letras en mayusculas y minusculas. La función usa "len" que sirve para que cuente cuantos caracteres tiene el
código y usa un ciclo para que se guarde cada caracter e imprima un resultado, tambien se uso "upper" que es para
hacer más grandes las palabras que uno desea y un lower para que las letras disminuyan su tamaño"""
def combinarLetras(cadena):
    letras = len(cadena)
    nuevaCadena = ""
    for letra in range(letras):
        mayuscula = (cadena[letra].upper())
        minuscula = (cadena[letra].lower())
        if (letra%2==0):
            nuevaCadena+=mayuscula
        else:
            nuevaCadena+=minuscula
    return nuevaCadena


"""Esta función, realiza mediante un ciclo for la tarea de buscar con un contador si es que la palabra que introduce 
el usuario contiene todas las vocales (a,e,i,o,u) y regresa true si es que lo cumple y si no regresa es el caso regresa
False"""
def contieneLasVocales(cadena):
    vocales= ["a","e","i","o","u","A","E","I","O","U"]
    cadenaBien=""
    for i in cadena:
        if i in vocales:
            cadenaBien+=i
    conta=0
    conte=0
    conti=0
    conto=0
    contu=0
    contA=0
    contE=0
    contI=0
    contO=0
    contU=0
    for y in cadenaBien:
        if y== vocales[0]:
            conta+=1
        if y== vocales[1]:
            conte+=1
        if y== vocales[2]:
            conti+=1
        if y== vocales[3]:
            conto+=1
        if y== vocales[4]:
            contu+=1
        if y== vocales[5]:
            contA+=1
        if y== vocales[6]:
            contE+=1
        if y == vocales[7]:
            contI += 1
        if y == vocales[8]:
            contO += 1
        if y == vocales[9]:
            contU += 1
    if conta*conte*conti*conto*contu !=0:
        return True
    elif contA*contE*contI+contO*contU !=0:
        return True
    else:
        return False#Multiplica todos los corredores y si alguno da 0 , regresa False


"""esta función recibe tanto el nombre, como el apellido y la matricula que el usuario quiere introducir
se uso los operadores de slice que lo que hacen es que cortan cada cadena en los caracteres que uno desea para que 
a a la hora de imprimir solo aparezcan éstos  """
def formarNombreUsuario(nombre, apellido, matricula):
    nombreCortado=slice(3) # se uso slice para indicar le a pycharm y a la función que solo quiero usar esos caracteres
    apellidoCortado= slice(3) # y lo corte hasta los primeros 3 caracteres
    matriculabien=str(matricula)
    nombrebien=(nombre[nombreCortado].lower()+apellido[apellidoCortado].lower()+matriculabien[4:])
    return (nombrebien)
#se usó este formato pues esta usando los parametros que el usuario ingreso y se puso en[]las variables quese cortaron
#para poder guardalos todos en una variable con + y imprimir esa variable


"""esta función toma los parametros de nombre,apellidoPaterno y apellidoMaterno que el usuario ingresa y usando los 
operadores """
def esCorrecto(cadena):
    partesnombre= cadena.split () # te regresa el nombre en formato de lista,toma como referencia los espacios entre
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
def traducirTelefono(cadena):
    contador=""
    numero = cadena
    for letra in numero:
        if letra in "-0123456789":
            contador+=letra
        elif letra in "ABC":
            contador+="2"
        elif letra in "DEF":
            contador+="3"
        elif letra in "GHI":
            contador+="4"
        elif letra in "JKL":
            contador += "5"
        elif letra in "MNO":
            contador+="6"
        elif letra in "PQRS":
            contador += "7"
        elif letra in "TUV":
            contador+="8"
        elif letra in "WXYZ":
            contador+="9"
        elif letra in "abc":
            contador += "2"
        elif letra in "def":
            contador += "3"
        elif letra in "ghi":
            contador += "4"
        elif letra in "jkl":
            contador += "5"
        elif letra in "mno":
            contador += "6"
        elif letra in "pqrs":
            contador += "7"
        elif letra in "tuv":
            contador += "8"
        elif letra in "wxyz":
            contador += "9"
    return contador


"""Esta función es la principal y de aqui salen los paramateros para que se puedan realizar todas las operaciones """
def main():
    cadena = str(input("Dime tu palabra: "))
    combinarLetras(cadena)
    nuevaCadena=combinarLetras(cadena)
    print(nuevaCadena)
    cadena= input("Dime tu palabra: ")
    vocales=contieneLasVocales(cadena)
    print(vocales)
    nombre = str(input("Dime tu nombre: "))
    apellido = str(input("Dime tu apellido: "))
    matricula = (input("Dime tu matricula sin el a0 (solo los 7 digitos): "))
    nombrebien=formarNombreUsuario(nombre,apellido,matricula)
    print(nombrebien)
    cadena = str(input("Dime tu nombre completo con apellidos(Paterno y Materno): "))
    nombreCorrecto=esCorrecto(cadena)
    print(nombreCorrecto)
    cadena=(input("Dime tu numero: "))
    convertir=traducirTelefono(cadena)
    print(convertir)

main()