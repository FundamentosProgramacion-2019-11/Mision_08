#Autor: Ivana Olvera Mérida
#Escribe la función esCorrecto, que recibe como parámetro una cadena que representa el nombre de
#una persona. Regresa True si las reglas de mayúsculas están bien aplicadas, False en otro caso.

def esCorrecto(nombreCompleto):
    nombreApellidos = nombreCompleto.split() #La función split se encarga de separar los elementos de la cadena('Ivana', 'Olvera', 'Mérida')
    nombre = nombreApellidos[0] #Ivana
    apellidoP = nombreApellidos[1] #Olvera
    apellidoM = nombreApellidos[2] #Mérida
    contadorNombre = 0

    if nombre[0].isupper() and nombre[1:].islower(): #El nombre debe cumplir con la primera letra en mayúcula y el resto de las letras en minúsculas
        contadorNombre += 1
    if apellidoP[0].isupper() and apellidoP[1:].islower():
        contadorNombre += 1
    if apellidoM[0].isupper() and apellidoM[1:].islower():
        contadorNombre += 1
        return True
    else:
        return False

def main():
    correcto = esCorrecto("Ivana Olvera Mérida")
    print(correcto)
    #Prueba con: esCorrecto("ivana OLVera MéRiDA")

main()

