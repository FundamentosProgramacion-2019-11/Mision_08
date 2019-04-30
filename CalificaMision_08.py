#Autor: José Luis Macías Vázquez, Grupo 03
# 1. Escribir una cadena y regresa la cadena alternando mayúsculas y minúsculas, la primera letra de la cadena que regresa
# siempre es mayúscula 2. Pide una cadena y entrega la verdadeo o falso según tenga todas las vocales o no.

# AQUI agregas tus funciones


def combinarLetras(palabras):
    acumulador = ""

    contador = 1

    palabras = palabras.lower()

    for idx in palabras:

        if contador == 1:

            idx = idx.upper()

        elif contador % 2 == 0:

            idx = idx.lower()

        acumulador = acumulador + idx

        contador = - contador

    return (acumulador)


def contieneLasVocales(cadena):
    i = cadena.lower()

    if (("a" in i) == True) and (("e" in i) == True) and (("i" in i) == True) and (("o" in i) == True) and (
            ("u" in i) == True):

        return True

    else:

        return False


def formarNombreUsuario(nombre, apellidoPaterno, matriculaNumerica):
    nombreVar = nombre.lower()

    apellidoVar = apellidoPaterno.lower()

    matriculaVar = str(matriculaNumerica)

    nombreUsuario = nombreVar[:3] + apellidoVar[:3] + matriculaVar[-3:]

    return (nombreUsuario)


print(formarNombreUsuario("José", "Macías", 1655713))


def esCorrecto(cadena):
    reglasCorrectas = cadena.title()

    if cadena == reglasCorrectas:

        return True

    else:

        return False


def traducirTelefono(numeroTel):
    idx = "01800-"

    for i in numeroTel[6:]:

        if i == "A" or i == "B" or i == "C":

            idx += "2"

        elif i == "D" or i == "E" or i == "F":

            idx += "3"

        elif i == "G" or i == "H" or i == "I":

            idx += "4"

        elif i == "J" or i == "K" or i == "L":

            idx += "5"

        elif i == "M" or i == "N" or i == "O":

            idx += "6"

        elif i == "P" or i == "Q" or i == "R" or i == "S":

            idx += "7"

        elif i == "T" or i == "U" or i == "V":

            idx += "8"

        elif i == "W" or i == "X" or i == "Y" or i == "Z":

            idx += "9"

        else:

            idx += "-"

    numeroTel = numeroTel.upper()

    return idx


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


