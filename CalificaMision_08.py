#Autor: Karla Ximena Rueda Ruiz
#Probando misión 8


# AQUI agregas tus funciones

def combinarLetras(entrada):

    resultado=""
    n=0
    for letra in entrada:
        if n%2==0:
            resultado+=letra.upper()
        else:
            resultado+=letra.lower()
        n += 1

    return resultado

print(combinarLetras("Hola"))


def contieneLasVocales(S):

    sMayus=S.lower()

    if "a" in sMayus and"e" in sMayus and "i" in sMayus and "o" in sMayus and "u" in sMayus:

            return True
    else:
            return False

print(contieneLasVocales("Ximena"))


def formarNombreUsuario(nombre,apellido,matr):
    nom=nombre.lower()
    ape=apellido.lower()
    matricula=str(matr)
    usuario=nom[:3]+ape[:3]+matricula[-3:]
    return(usuario)

print(formarNombreUsuario("Karla","Rueda",1745943))

def esCorrecto(cadena):

    palabras=cadena.split()
    nombre=palabras[0]
    resto=nombre[1:]
    letra=nombre[0]
    if letra.isupper()==True:

        if resto.islower()==True:
            apellidop = palabras[1]
            restop = apellidop[1:]
            letraP = apellidop[0]


            if letraP.isupper()==True:

                if restop.islower()==True:
                    apellidom = palabras[2]
                    restom = apellidom[1:]
                    letraM = apellidom[0]
                    if letraM.isupper()==True:
                        if restom.islower()==True:
                            return True

                        else:
                            return False

                    else:
                        return False

                else:
                    return False
            else:
                return False

        else:
            return False
    else:
        return False

print(esCorrecto("Karla Rueda Ruiz"))

def traducirTelefono(telefono):

    resultado="01800-"
    cadena=telefono[6:]

    for letra in cadena:

        if letra =="A" or letra=="B" or letra=="C":
            resultado+="2"
        if letra =="D" or letra=="E" or letra=="F":
            resultado+="3"
        if letra == "G" or letra == "H" or letra == "I":
            resultado += "4"
        if letra == "J" or letra == "K" or letra == "L":
            resultado += "5"
        if letra == "M" or letra == "N" or letra == "O":
            resultado += "6"
        if letra == "P" or letra == "Q" or letra == "R" or letra == "S":
            resultado += "7"
        if letra == "T" or letra == "U" or letra == "V":
            resultado += "8"
        if letra == "W" or letra == "X" or letra == "Y" or letra == "Z":
            resultado += "9"
        if letra == "-" :
            resultado += "-"

    return resultado

print(traducirTelefono("01800-VOY-BIEN"))



# NO MODIFIQUES EL CODIGO QUE SIGUE
def main():

    HP_MAXIMO = 1250
    hp = 1250

    print("\n\n----------------\n## Calificando Misión 8\n----------------")
    print("\nCalificación inicial:", hp,"HP\n\n")

    print("### 1. Prueba función combinarLetras(cadena)")

    try:

        pruebas = [ ("Hola Mundo", "HoLa mUnDo"), ("rObErtoMtzRoman", "RoBeRtOmTzRoMaN"), ("PRUEBA-  5","PrUeBa-  5") ]
        for a, b in pruebas:    # prueba, correcto
            print("\n- Prueba con:", a)
            r = combinarLetras(a)
            print("combinarLetras('", a, "'), regresa la cadena: '", r, "'", sep="")
            if r == b:
                print("✅ Resultado correcto")
            else:
                print("❌ Incorrecto, debería regresar: '", b, "'", sep="")
                print("Pierdes 80 hp")
                hp -= 80

            if r == None:
                print("La función NO ESTA REGRESANDO el resultado, VERIFICA que usas return.")
    # Errores
    except NameError as e:
        print("Error, la función combinarLetras(cadena), o alguna variable, no existe. ", e)
        print("Pierdes 250 hp")
        hp -= 250
    except TypeError as e:
        print("Error, falta el parámetro de la función combinarLetras(cadena). ", e)
        print("Pierdes 250 hp")
        hp -= 250
    except IndexError as e:
        print("Revisa los índices en el recorrido de la cadena. ", e)
        print("Pierdes 250 hp")
        hp -= 250

    #-----------------------------------------------------

    print("\n\n### 2. Prueba función contieneLasVocales(cadena)")

    try:

        pruebas = [ ("Aguascalientes", False), ("ABUELITO", True), ("aaaaeeeeuuu", False), ("aeioeeioaex", False) ]
        for a, b in pruebas:
            print("\n- Prueba con:", a)
            r = contieneLasVocales(a)
            print("contieneLasVocales('", a, "'), regresa: ", r, " ", type(r), sep="")
            if r == b:
                print("✅ Resultado correcto")
            else:
                print("❌ Incorrecto, debería regresar:", b, type(b))
                print("Pierdes 50 hp")
                hp -= 50

            if r == None:
                print("La función NO ESTA REGRESANDO un resultado, VERIFICA que usas return.")

    # Errores
    except NameError as e:
        print("Error, la función contieneLasVocales(cadena) no existe. ", e)
        print("Pierdes 200 hp")
        hp -= 200
    except TypeError as e:
        print("Error, falta el parámetro de la función contieneLasVocales(cadena). ", e)
        print("Pierdes 200 hp")
        hp -= 200
    except IndexError as e:
        print("Revisa los índices en el recorrido de la cadena. ", e)
        print("Pierdes 200 hp")
        hp -= 200
    except ValueError as e:
        print("Alguna función no puede aplicarse. ", e)
        print("Pierdes 200 hp")
        hp -= 200


    # -----------------------------------------------------

    print("\n\n### 3. Prueba función formarNombreUsuario(nombre, apellido, matricula)")

    try:

        pruebas = [ (("Roberto", "Martinez", 1234567), "robmar567"), (("john", "DOE", 1029384), "johdoe384"), (("aNa", "deAcaracatamboDeLasTunas", 1476300), "anadea300") ]
        for a, b in pruebas:
            print("\n- Prueba con:", a)
            nombre, apellido, matricula = a
            r = formarNombreUsuario(nombre, apellido, matricula)
            print("formarNombreUsuario", a, ", regresa: ", r, sep="")
            if r == b:
                print("✅ Resultado correcto")
            else:
                print("❌ Incorrecto, debería regresar:", b)
                print("Pierdes 80 hp")
                hp -= 65

            if r == None:
                print("La función NO ESTA REGRESANDO un resultado, VERIFICA que usas return.")

    # Errores
    except NameError as e:
        print("Error, la función formarNombreUsuario(nombre, apellido, matricula) no existe. ", e)
        print("Pierdes 200 hp")
        hp -= 200
    except TypeError as e:
        print("Error, falta el parámetro de la función formarNombreUsuario(nombre, apellido, matricula). ", e)
        print("La matrícula debe ser numérica, posiblemente enviaste una cadena.")
        print("Pierdes 200 hp")
        hp -= 200
    except IndexError as e:
        print("Revisa los índices en el recorrido de la lista. ", e)
        print("Pierdes 200 hp")
        hp -= 200
    except AttributeError as e:
        print("Estás usando el parámetro matrícula como cadena, pero debe ser numérico. ", e)
        print("Pierdes 200 hp")
        hp -= 200


    # -----------------------------------------------------

    print("\n\n### 4. Prueba función esCorrecto(cadena)")

    try:

        pruebas = [ ("Roberto Martínez Román", True), ("AnA López ALVAREZ", False), ("Edgar Aguilar casaS", False) ]
        for a, b in pruebas:
            print("\n- Prueba con: '%s'" % (a))
            r = esCorrecto(a)
            print("esCorrecto('%s')" % (a), "regresa:", r, type(r))
            if r == b:
                print("✅ Resultado correcto")
            else:
                print("❌ Incorrecto, debería regresar:", b, type(b))
                print("Pierdes 100 hp")
                hp -= 100

            if r == None:
                print("La función NO ESTA REGRESANDO un resultado, VERIFICA que usas return.")

    # Errores
    except NameError as e:
        print("Error, la función esCorrecto(cadena) no existe. ", e)
        print("Pierdes 300 hp")
        hp -= 300
    except TypeError as e:
        print("Error, falta el parámetro de la función esCorrecto(cadena). ", e)
        print("Pierdes 300 hp")
        hp -= 300
    except IndexError as e:
        print("Revisa los índices en el recorrido de la cadena. ", e)
        print("Pierdes 300 hp")
        hp -= 300


    # -----------------------------------------------------

    print("\n\n### 5. Prueba función traducirTelefono(cadena)")

    try:
        pruebas = [ ("01800-VOY-BIEN", "01800-869-2436"), ("01800-MAS-TELE", "01800-627-8353"), ("01800-ABA-MONO", "01800-222-6666") ]
        for a, b in pruebas:
            print("\n- Prueba con:", a)
            r = traducirTelefono(a)
            print("traducirTelefono('",a,"'), regresa: ", r, sep="")
            if r == b:
                print("✅ Resultado correcto")
            else:
                print("❌ Incorrecto, debería regresar:", b)
                print("Pierdes 100 hp")
                hp -= 100

            if r == None:
                print("La función NO ESTA REGRESANDO un resultado, VERIFICA que usas return.")

    # Errores
    except NameError as e:
        print("Error, la función traducirTelefono(cadena) no existe. ", e)
        print("Pierdes 300 hp")
        hp -= 300
    except TypeError as e:
        print("Error, falta el parámetro de la función traducirTelefono(cadena). ", e)
        print("Pierdes 300 hp")
        hp -= 300
    except IndexError as e:
        print("Revisa los índices en el recorrido de la cadena. ", e)
        print("Pierdes 300 hp")
        hp -= 300



    # -----------------------------------------------------

    print("\n\n### 6. Prueba función esValido(password) - EXTRA")

    hpExtra = 300

    try:
        pruebas = [ ("Abcd-7635", True), ("abc936", False), ("4829-584", False), ("Wxyz-12345", False), ("$$Lxg-iwyl365", False) ]
        for a, b in pruebas:
            print("\n- Prueba con:", a)
            r = esValido(a)
            print("esValido('",a,"'), regresa: ", r, sep="")
            if r == b:
                print("✅ Resultado correcto")
            else:
                print("❌ Incorrecto, debería regresar:", b)
                hpExtra = 0


    # Errores
    except NameError as e:
        print("Error, la función esValido(password) no existe. ", e)
        print("No hay extra :(")
        hpExtra = 0
    except TypeError as e:
        print("Error, falta el parámetro de la función esValido(password). ", e)
        print("No hay extra :(")
        hpExtra = 0
    except IndexError as e:
        print("Revisa los índices en el recorrido de la cadena. ", e)
        print("No hay extra :(")
        hpExtra = 0
    except ValueError as e:
        print("Revisa el tipo de dato que usas en las operaciones/conversiones. ", e)
        print("No hay extra :(")
        hpExtra = 0

    # -----------------------------------------------------


    print("\n---- Fin de la evaluacion ----")
    print("\n### Has ganado %d/%d HP." % (hp, HP_MAXIMO))
    if hp==1250:
        print("\n### ¡FELICIDADES!, cumpliste la misión de forma EXCELENTE. 🤓")

    if hpExtra > 0:
        print("\n#### ¡FELICIDADES!, ganaste 300 HP adicionales.🤓")
        print("### Tu calificación ahora es: %d" % (hp + hpExtra))
    else:
        print("#### HP extra: %d" % (hpExtra))

    # end of main method


main()


