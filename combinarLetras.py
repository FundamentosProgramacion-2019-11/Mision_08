#Autor: Ivana Olvera Mérida
#Escribe la función combinarLetras, que recibe como parámetro una cadena
#y regresa una nueva alternando mayúsculas y minúsculas.

def combinarLetras(parametro):
    cadena = ""

    for k in range(len(parametro)): # k -> 1,2,3,4,5,6,7,8,9
        if k%2 == 0:
            cadena += parametro[k].upper()
        else:
            cadena += parametro[k].lower()

        return cadena


def main():
    combinacion = combinarLetras("Hola Mundo")
    print(combinacion)
main()

