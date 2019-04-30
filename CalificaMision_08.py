# AQUI agregas tus funciones



def combinarLetras(cadena):
    result=""
    x=1
    for c in cadena:
        y=1
        if(x == 1 and y==1):
            result += str(c.upper())
            x = 2
            y=0
        if(x == 2 and y==1):
            result += str(c.lower())
            x = 1
            y = 0
    return result

def contieneLasVocales(cadena):
    a = 0
    i = 0
    u = 0
    e = 0
    o = 0
    for c in cadena:
        if (c == "a" or c=="A"):
            a = 1
        if (c == "i" or c=="I"):
            i = 1
        if (c == "u" or c=="U"):
            u = 1
        if (c == "e" or c=="E"):
            e = 1
        if (c == "o" or c=="O"):
            o = 1
    if(a==1 and a==i and i==u and u==e and e==o):
        return True
    return False

def formarNombreUsuario(nombre, apellido, matricula):
    username=""
    username+=nombre[0:3]
    username += apellido[0:3]

    username += str(matricula)[-3:]
    return username.lower()

def esCorrecto(nombre):
    roto = nombre.split()
    first = roto[0]
    second = roto[1]
    third = roto[2]
    if(first[0].isupper()):
        if(first[1:].islower()):
            if(second[0].isupper()):
                if (second[1:].islower()):
                    if (third[0].isupper()):
                        if (third[1:].islower()):
                            return True
    return False

def traducirTelefono(telefono):
    roto = telefono[6:]
    codedPhone="01800-"
    for c in roto:
        if(c=="A" or c=="B" or c=="C"):
            codedPhone+="2"
        elif (c == "D" or c == "E" or c == "F"):
            codedPhone += "3"
        elif (c == "G" or c == "H" or c == "I"):
            codedPhone += "4"
        elif (c == "J" or c == "K" or c == "L"):
            codedPhone += "5"
        elif (c == "M" or c == "N" or c == "O"):
            codedPhone += "6"
        elif (c == "P" or c == "Q" or c == "R" or c=="S"):
            codedPhone += "7"
        elif (c == "S" or c == "T" or c == "V"):
            codedPhone += "8"
        elif (c == "W" or c == "X" or c == "Y" or c=="Z"):
            codedPhone += "9"
        elif(c=="-"):
            codedPhone +="-"
    return codedPhone


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


