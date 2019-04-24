# Autor: Juan Carlos Flores García A01376511. Grupo 02.

# Programa que muestra un menu con 3 opciones: Calcular residuo y cociente de divisiones, encontrar el número mayor de
# una serie de números y salir del menu.


# Esta función calcula el residuo y cociente de una división y luego lo imprime.
def probarDivisiones(dividendo, divisor):
    residuo = dividendo
    cociente = 0
    while (divisor <= residuo):
        residuo -= divisor
        cociente += 1

    print(dividendo, "/", divisor, "=", cociente, ", sobra", residuo)


# Esta función encuentra el mayor de una serie de números y después imprime ese número.
def encontrarMayor():
    serieNumerica = 0
    numeroMayor = 0
    while (serieNumerica != -1):
        serieNumerica = int(input("Teclea un número [-1 para salir]: "))
        if serieNumerica < -1:
            print("No hay valor mayor")
        elif serieNumerica > numeroMayor:
            numeroMayor = serieNumerica
    if numeroMayor == 0:
        print("No hay valor mayor")
    else:
        print("El mayor es", numeroMayor)


# Esta función imprime las opciones del menu para elegir la opción deseada.
def leerOpcionMenu():
    print("Misión 07. Ciclos while")
    print("Autor: Juan Carlos Flores García")
    print("Matrícula: A01376511")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    return opcion


# Función principal que se encarga de mostrar el menu y llamar al resto de las funciones.
def main():
    opcion = leerOpcionMenu()
    while opcion != 3:
        if opcion == 1:
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            probarDivisiones(dividendo, divisor)
        elif opcion == 2:
            print("Teclea una serie de números para encontrar el mayor.")
            encontrarMayor()
        elif opcion >= 0 or opcion < 3:
            print("ERROR, teclea 1, 2 o 3")
        opcion = leerOpcionMenu()
    print("Gracias por usar este programa, regresa pronto.")


# Llamada a la función principal.
main()
