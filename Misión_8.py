#Rafael ROMERO bello
#A01747730
#mision8 fecha: 29/04/2019

def combinarLetras(L):
    totalC=len(L)
    r=''
    for i in range(0, totalC):
        c=L[i]
        if i%2==0:
            cMayus=c.upper()
            r=r+cMayus
        else:
            cMinus=c.lower()
            r=r+cMinus
    return r


def esCorrecto(nombre):
    a=nombre.split()
    p1=a[0]
    p2=a[1]
    p3=a[2]
    p1s=p1[1:]
    p2s=p2[1:]
    p3s=p3[1:]
    if p1[0].isupper() and p1s.islower() and p2[0].isupper() and p2s.islower() and p3[0].isupper() and p3s.islower():
        a='true'
    else:
        a='false'
    return a


def formarNombreUsuario(nombre, apellido, matricula):
    minusNombre=nombre.lower()
    minusapellido=apellido.lower()
    newnombre = minusNombre[:3]
    newapellido = minusapellido[:3]
    newM = str(matricula)
    newmatricula1 = len(newM)
    newmatricula1 -= 3
    matriculanew = newM[newmatricula1:]
    resultado=newnombre+newapellido+matriculanew

    return resultado


def contieneLasVocales(cadena):
    newcadena=cadena.lower()
    if 'a' in newcadena and 'e' in newcadena and 'i' in newcadena and 'o' in newcadena and 'u' in newcadena:
        a='true'
    else:
        a='false'
    return a

def traducirTelefono(num):
    n1 = num.replace("A", "2")
    n2 = n1.replace("B", "2")
    n3 = n2.replace("C", "2")
    n4 = n3.replace("D", "3")
    n5 = n4.replace("E", "3")
    n6 = n5.replace("F", "3")
    n7 = n6.replace("G", "4")
    n8 = n7.replace("H", "4")
    n9 = n8.replace("I", "4")
    n10 = n9.replace("J", "5")
    n11 = n10.replace("K", "5")
    n12 = n11.replace("L", "5")
    n13 = n12.replace("M", "6")
    n14 = n13.replace("N", "6")
    n15 = n14.replace("O", "6")
    n16 = n15.replace("P", "7")
    n17 = n16.replace("Q", "7")
    n18 = n17.replace("R", "7")
    n19 = n18.replace("S", "7")
    n20 = n19.replace("T", "8")
    n21 = n20.replace("U", "8")
    n22 = n21.replace("V", "8")
    n23 = n22.replace("W", "9")
    n24 = n23.replace("X", "9")
    n25 = n24.replace("Y", "9")
    n23 = n25.replace("Z", "9")
    return n23


def main():
    print(combinarLetras('Hola Mundo'))
    print(esCorrecto('Roberto Martinez Roman'))
    print(formarNombreUsuario('Roberto', 'Martinez', 12345678))
    print(traducirTelefono('1800-VOY-BIEN'))
    print(contieneLasVocales('Abuelito'))

main()