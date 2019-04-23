#Autor: Ivana Olvera Mérida
#Escribe la función traducirTelefono, que recibe como parámetro un número de teléfono en el formato "01800-XXX-XXXX"
#y regresa una cadena del número de teléfono con los dígitos correspondientes.

def traducirTelefono(telefono):
    numero = ""
    telefono = telefono.upper()

    for n in telefono:
        if n == "-":
            numero = numero + "-"
        if n == "A" or n == "B" or n == "C":
            numero = numero + "2"
        if n == "D" or n == "E"  or n == "F":
            numero = numero + "3"
        if n == "G" or n == "H" or n == "I":
            numero = numero + "4"
        if n == "J" or n == "K" or n == "L":
            numero = numero + "5"
        if n == "M" or n == "N" or n == "O":
            numero = numero + "6"
        if n == "P" or n == "Q" or n == "R" or n == "S":
            numero = numero + "7"
        if n == "T" or n == "U" or n == "V":
            numero = numero + "8"
        if n == "W" or n == "X" or n == "Y" or n == "Z":
            numero = numero + "9"

    print("01800", numero)



def main():
    traducirTelefono("01800-VOY-BIEN")

main()

