#Autor: Ivana Olvera Mérida
#Escribe la función contieneLasVocales, que recibe como parámetro una cadena
#y regresa True si la cadena contiene TODAS las vocales, False en otro caso.

def contieneLasVocales(cadena):
    copiaVocal = cadena.upper() #Utilizar una copia para identificar si se recibió una vocal en mayúscula

    contadorVocales = 0

    if copiaVocal.count('A')>=1: #Si se cuenta la vocal una o más veces dentro de una palabra
        contadorVocales += 1
    if copiaVocal.count('E') >= 1:
        contadorVocales += 1
    if copiaVocal.count('I') >= 1:
        contadorVocales += 1
    if copiaVocal.count('O') >= 1:
        contadorVocales += 1
    if copiaVocal.count('U') >= 1:
        contadorVocales += 1

    if contadorVocales == 5:
        return True
    else:
        return False

def main():
    todasLasVocales = contieneLasVocales("abuelito")
    print(todasLasVocales)
main()