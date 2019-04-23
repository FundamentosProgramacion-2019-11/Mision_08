#Autor: Ivana Olvera Mérida
#Escribe la función formarNombreUsuario, que recibe tres parámetros:
#nombre, apellido paterno y matrícula numérica entera (7 dígitos).

def formarNombreUsuario(nombre, apellido, matricula):
    a = nombre
    nom = a[0:3] #Toma los primeros 3 elementos de la cadena: 0,1,2,3 (3-1)
    b = apellido
    ap = b[0:3] #Toma los primeros 3 elementos de la cadena

    d = str(matricula)
    mat = d[4:]

    cadenaUsuario = nom.lower() + ap.lower()+ mat

    print(cadenaUsuario)

def main():
    nombre = input("Introduce tu nombre: ")
    apellido = input("Introduce tu apellido paterno: ")
    matricula = input("Introduce tu matricula (7 dígitos únicamente): ")

    formarNombreUsuario(nombre, apellido, matricula)

main()

