#Bernardo Mondragon Ramírez
# Lee diferentes acciones con cadenas

def combinarLetras (x): #correcto checar
    Contador=""
    for l in range (len(x)):
        if l%2 !=0:

            Contador += x[l].lower()
        else:
            Contador += x[l].upper()

    return Contador



def contieneLasVocales(p): #Correcto
    v = p.lower()

    if "a" in v and "e" in v and "i" in v and "o" in v and "u" in v:
        return True
    elif "A" in v and "E" in v and "I" in v and "O" in v and "U" in v:
        print("contiene todas las vocales")
        return True

    else:
        print("hacen falta vocales")
        return False



def formarNombreUsuario(n, a, m): #correcto
    n = n.lower()
    a = a.lower()
    m = str(m)
    nUsuario = n[0:3] + a[0:3] + m[4:]
    print("tu nombre usuario es:")
    return nUsuario




def esCorrecto(ncompleto): #correcto
    n = ncompleto.split()
    for letra in n:
        min = letra[1:]
        may = letra[:1]
    if may.isupper() or min.islower():
        return True
    else:
        return False




def main():

    cadena= input("Escribe una frase: ")
    print(combinarLetras(cadena))
    print()

    p = input("Escribe un apalabra: ")
    print(contieneLasVocales(p))
    print()

    nombre = input("Teclea tu nombre: ")
    apellido = input(("Teclea tu primer apellido: "))
    matricula= str(input("Teclea tu matricula A0"))
    print(formarNombreUsuario(nombre, apellido, matricula))
    print()

    nombreCompleto=str(input("Teclea tu nombre completo para probar la regla: "))
    print(esCorrecto(nombreCompleto))
    print()






main()