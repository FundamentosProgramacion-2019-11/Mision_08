def combinarLetras(cadena):
    totalCaracteres=len(cadena)
    resultado=""

    for i in range(0,totalCaracteres):
        caracter = cadena[i]
        if i%2==0:
            caracterMayuscula = caracter.upper()
            resultado=resultado+caracterMayuscula
        else:
            caracterMinuscula=caracter.lower()
            resultado=resultado+caracterMinuscula
    return resultado


def contieneLasVocales(cadena):
    nuevaCadena=len(cadena)
    acumulador=0
    acumuladorA=0
    acumuladorE=0
    acumuladorI=0
    acumuladorO=0
    acumuladorU=0
    for i in range(0,nuevaCadena):
        caracter= cadena[i]
        if caracter in ["a","e","i","o","u","A","E","I","O","U"]:
            if caracter in ["a","A"]:
                acumuladorA+=1
            if acumuladorA>=1:
                acumuladorA=1

            if caracter in ["e","E"]:
                acumuladorE+=1
            if acumuladorE>=1:
                acumuladorE=1
            if caracter in ["o","O"]:
                acumuladorO+=1
            if acumuladorO>=1:
                acumuladorO=1
            if caracter in ["i","I"]:
                acumuladorI+=1
            if acumuladorI>=1:
                acumuladorI=1
            if caracter in ["u","U"]:
                acumuladorU+=1
            if acumuladorU>=1:
                acumuladorU=1
                acumulador=acumuladorU+acumuladorI+acumuladorA+acumuladorO+acumuladorE

    if acumulador==5:
        return True
    else:
        return False


def formarNombreUsuario(nombre,apellidoPaterno,matricula):
    matriculaEnCadena=str(matricula)
    cantidadDeNumerosEnLaMatricula=len(matriculaEnCadena)
    cantidadDeNumerosRestatantesMatricula= cantidadDeNumerosEnLaMatricula-3
    nuevaCadenaNombre=nombre.lower()
    nuevaCadenaApellido=apellidoPaterno.lower()
    letrasSeleccionadadDelNombre=nuevaCadenaNombre[0:3]
    letrasSeleccionadasDelApellido=nuevaCadenaApellido[0:3]
    numerosSeleccionados=matriculaEnCadena[cantidadDeNumerosRestatantesMatricula:cantidadDeNumerosEnLaMatricula]
    resultado=letrasSeleccionadadDelNombre+letrasSeleccionadasDelApellido+numerosSeleccionados
    return resultado

def esCorrecto(cadena):
    nuevacadena=cadena.split()
    numeroDePalabras=len(nuevacadena)
    nombre1=nuevacadena[0]
    separacionNombre1=nombre1[0]
    restanteDelNombre1=nombre1[1:]

    apellido1=nuevacadena[1]
    separacionNombre2=apellido1[0]
    restanteDelNombre2=apellido1[1:]

    apellido2=nuevacadena[2]
    separacionNombre3=apellido2[0]
    restanteDelNombre3=apellido2[1:]
    if separacionNombre1.isupper() and restanteDelNombre1.islower() and separacionNombre2.isupper() and restanteDelNombre2.islower() and separacionNombre3.isupper() and restanteDelNombre3.islower():
        return True
    else:
        return False


def traucirTelefono(cadena):
    totalDeCaracteres=len(cadena)
    acumularTelefono=""
    for i in range (0,totalDeCaracteres):
        caracter=cadena[i]
        if caracter in ["0", "1", "2","3","4","5","6","7","8","9","-"]:
            acumularTelefono=acumularTelefono+caracter
        else:
            if caracter in ["A", "B", "C"]:
                acumularTelefono = acumularTelefono+"2"
            if caracter in ["D", "E", "F"]:
                acumularTelefono = acumularTelefono + "3"
            if caracter in ["G", "H", "I"]:
                acumularTelefono = acumularTelefono+"4"
            if caracter in ["J", "K", "L"]:
                acumularTelefono = acumularTelefono + "5"
            if caracter in ["M", "N", "O"]:
                acumularTelefono = acumularTelefono + "6"
            if caracter in ["P", "Q", "R", "S"]:
                acumularTelefono = acumularTelefono+"7"
            if caracter in ["T","U","V"]:
                acumularTelefono = acumularTelefono+"8"
            if caracter in ["W","X","Y","Z"]:
                acumularTelefono = acumularTelefono+"9"
    return acumularTelefono


def main():
    print(combinarLetras("la niña del vestido azul"))
    print(contieneLasVocales("amigos"))
    print(formarNombreUsuario("YANABANY", "castro",1725302519390))
    print(esCorrecto("Itzel Castro Becerril "))
    print(traucirTelefono("01800-HOLA-MUNDO"))



main()
