#Autor: Eric Andrés Jardón Chao
#Misión 08. Cadenas. Colección de funciones para 6 propósitos diferentes usando cadenas.
# La función principal recibe parámetros y las corre. Imprime resultados True o False.

def main(): #recibe los parámetros necesarios para las funciones
    cadena=input("Teclea la cadena a combinar: ")
    print(combinarLetras(cadena))
    vocales=input("Teclea la cadena para evaluar sus vocales: ")
    print(contieneLasVocales(vocales))
    correrParte3() #corre una función que recibe los tres parámetros necesarios para la siguiente función
    nombre=input("Checar mayúsculas. Teclea un nombre y dos apellidos: ")
    print(esCorrecto(nombre))
    telefono=input("Teclea un teléfono en el formato 01800-XXX-XXXX: ")
    print(traducirTelefono(telefono))
    passw=input("Teclea tu contraseña para validar: ")
    print(esValido(passw))


#FUNCIÓN 1
def combinarLetras(cadena):
    nueva="" #acumulador de cadena
    x=1
    for i in cadena: #para cada caracter de la cadena lo toma y lo convierte en mayúscula o minúscula según sea el caso.
        if x==1: #primer carácter será mayúscula
            caracter=i.upper()
        elif x==-1:
            caracter=i.lower() #se alterna con minúsculas
        nueva=nueva+caracter #el carácter modificado se añade a la nueva cadena.
        x=-x #Al final de cada paso cambia el valor de x. De esta forma alternamos para cada caracter mayúscula y minúscula.
    return nueva


#FUNCIÓN 2
def contieneLasVocales(cadena):
    minusculas=cadena.lower() #transforma todo a minúsculas para que no haya problema
    return('a' in minusculas and 'e' in minusculas and 'i' in minusculas and 'o' in minusculas and 'u' in minusculas)
#Devuelve el resultado booleano de evaluar si a, e, i, o, y u están dentro de la cadena ingresada.


#FUNCIÓN 3 (dos funciones)
def correrParte3(): #recibe los parámetros que se pasan a la función formarNombreUsuario
    print("Formación de un usuario.")
    nombre=input("Teclea el nombre: ")
    paterno=input("Teclea el apellido paterno: ")
    matricula=input("Teclea la matrícula sin A0")
    print(formarNombreUsuario(nombre,paterno,matricula))


def formarNombreUsuario(n,a,m):
    usuario="" #Acumulador de cadena
    p1=n[:3] #Toma los caracteres desde el inicio hasta el tercer caracter del nombre
    p2=a[:3] #Toma los caracteres desde el inicio hasta el tercer caracter del apellido
    inicioMatricula=m[:4] #Toma los 4 primeros caracteres de la matrícula
    divisor=int(inicioMatricula+'000') #Suma tres ceros al inicio de la matrícula y lo convierte en un número entero
    finMat=int(m)%(divisor) #módulo de la matrícula entre el inicio de la matrícula con tres ceros, nos devuelve los últimos 3 dígitos (el residuo).
    #Para arreglar el problema si el usuario tiene una matrícula con un 0 en el quinto y/o sexto caracter:
    p3=("%03d") %finMat #formateamos la cadena para que despliegue 3 cifras siempre.
    usuario=p1.lower()+p2.lower()+p3 #suma las subcadenas en orden: nombre, apellido y matrícula.
    return(usuario)


#FUNCIÓN 4
def esCorrecto(nombre):
    lista=nombre.split() #Divide la cadena en tres elementos: nombre, apellido 1 y apellido 2.
    correctos=0 #Número de elementos correctamente escritos.
    for palabra in lista: #Lee cada elemento (palabra) de la lista.
        resto=palabra[1:] #Quita la primer letra de cada palabra.
        if palabra[0].isupper() and resto.islower(): #Si la primer letra es mayúscula y el resto de la palabra está en minúscula, se suma 1 al número de elementos correctos
            correctos+=1
    return correctos == 3 #Se asume que sólo hay tres palabras en la cadena. Si hay 3 palabras correctas, toda la cadena es correcta.


#FUNCIÓN 5
def traducirTelefono(number): #Asumimos que el usuario ingresa el número en el formato correcto siempre; no hay necesidad de probar
    alfaAnum = {} #Creación de un diccionario que transforma alfabético a número
    alfaAnum['A'] = '2'
    alfaAnum['B'] = '2'
    alfaAnum['C'] = '2'
    alfaAnum['F']='3'
    alfaAnum['D'] = '3'
    alfaAnum['E'] = '3'
    alfaAnum['G']='4'
    alfaAnum['H'] = '4'
    alfaAnum['I'] = '4'
    alfaAnum['J']='5'
    alfaAnum['K'] = '5'
    alfaAnum['L'] = '5'
    alfaAnum['M']='6'
    alfaAnum['N'] = '6'
    alfaAnum['O'] = '6'
    alfaAnum['P'] = '7'
    alfaAnum['Q'] = '7'
    alfaAnum['R'] = '7'
    alfaAnum['S'] = '7'
    alfaAnum['T'] = '8'
    alfaAnum['U'] = '8'
    alfaAnum['V'] = '8'
    alfaAnum['W'] = '9'
    alfaAnum['X'] = '9'
    alfaAnum['Y'] = '9'
    alfaAnum['Z'] = '9'
    lista=number.split('-') #Separa el número ingresado en 3 elementos: 1800, primer palabra y segunda palabra
    palabra1="" #acumuladores de cadenas para cada palabra
    palabra2=""
    for letra in lista[1]: #Cada letra de la primer palabra
        digit=alfaAnum[letra] #La traduce según el diccionario
        palabra1=palabra1+digit
    for letra2 in lista[2]: #Cada letra de la segunda palabra
        digit = alfaAnum[letra2] #Traduce según el diccionario
        palabra2 = palabra2 + digit
    traducido=lista[0]+"-"+palabra1+"-"+palabra2 #imprime el 01800, la primer palabra en números y la segunda palabra en números, separadas por un guión.
    return traducido


#FUNCIÓN EXTRA
def esValido(passw): #La contraseña ingresada debe cumplir con todos los requisitos para que la función devuelva True
    #Asignamos valores default para cada requisito (Falso) y si cumple con el requisito cambia a True
    #Debe tener 8 caracteres o más
    length=False
    #Debe tener 1 mayúscula y una minúscula al menos
    caps=0 #En este caso usamos un contador para validar que cumple: debemos sumar 2.
    #Debe tener un carácter especial (no es número ni letra)
    special=False
    #Debe contener al menos un dígito
    hayDigito=False
    #Debe comenzar con una letra
    inicio=False
    #No debe contener números consecutivos
    consecutivos=False
    if len(passw)>=8: #Si la longitud es igual o mayor a 8, cumple
        length=True
    for caracter in passw: #Lee cada caracter de la contraseña. A la primer mayúscula que encuentre, suma 1 y rompe el ciclo.
        if caracter.isupper():
            caps+=1
            break
    for caracter in passw: #Lee cada caracter de la contraseña. A la primer minúscula que encuentre, suma 1 y rompe el ciclo.
        if caracter.islower():
            caps+=1
     #Si la contraseña contiene al menos una mayúscula y una minúscula, ya sumamos 2 en el contados 'caps'.
            break
    for caracter in passw: #Lee cada caracter. Si hay alguno que no sea ni letra ni número, cumple con la condición y  rompe el ciclo.
        if not caracter.isalnum():
            special=True
            break
    for caracter in passw: #Lee cada caracter. Si hay alguno que sea numérico, cumple con la condición y rompe el ciclo.
        if caracter.isdigit():
            hayDigito=True
            break
    if passw[0].isalpha(): #Si el primer caracter es alfabético, cumple con la condición.
        inicio=True
    for n in range(0,len(passw)-1): #Para todos los caracteres excepto el último para que no haya error de parseo de string.
        if passw[n].isdigit() and passw[n+1].isdigit(): #Si el caracter y su consecutivo son numéricos, evalúa la siguiente condición.
            if int(passw[n+1]) == (int(passw[n])+1): #Si el carácter consecutivo en entero es equivalente al carácter anterior en entero más uno, son números consecutivos y entonces reprueba.
                consecutivos=True #Entonces hay números consecutivos y rompe con el ciclo.
                break
#caps debe ser 2, consecutivos debe ser falso y el resto deben ser verdaderos.
    if length and caps == 2 and special and hayDigito and inicio and not consecutivos:
        return True
    else:
        return False


main()