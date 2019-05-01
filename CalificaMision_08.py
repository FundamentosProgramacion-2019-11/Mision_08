# Autor: Rosalía Serrano Herrera
# Califica las funciones de cadenas

def combinarLetras(cadenaCombinados):
    combinada = ""
    contador = 1

    for palabra in cadenaCombinados:
        if contador == 1:
            letra = palabra.upper()
            combinada = combinada + letra
            contador = - contador
        else:
            letra = palabra.lower()
            combinada = combinada + letra
            contador = - contador

    return combinada


def contieneLasVocales(cadenaVocales):
    palabra = cadenaVocales.lower()
    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"

    if a in palabra and e in palabra and i in palabra and o in palabra and u in palabra:
        return True
    else:
        return False


def formarNombreUsuario(nombre, apellido, matricula):
    nombreMinus = nombre.lower()
    apellidoMinus = apellido.lower()
    strMatricula = str(matricula)
    usuarioNombre = nombreMinus[:3:]
    usuarioApellido = apellidoMinus[:3:]
    usuarioMatricula = strMatricula[4:]
    formato = usuarioNombre + usuarioApellido + usuarioMatricula

    return formato


def esCorrecto(nombrePersona):
    nombre = nombrePersona.split()

    for palabra in nombre:
        for primera in palabra[0:1]:
            primera.isupper()

    for palabra in nombre:
        for restantes in palabra[1:]:
            restantes.islower()

    if primera.isupper() and restantes.islower():
        return True
    else:
        return False


def traducirTelefono(numeroTelefonico):
    numeroEscrito = numeroTelefonico[5:]
    dos = ["A", "B", "C"]
    tres = ["D", "E", "F"]
    cuatro = ["G", "H", "I"]
    cinco = ["J", "K", "L"]
    seis = ["M", "N", "O"]
    siete = ["P", "Q", "R", "S"]
    ocho = ["T", "U", "V"]
    nueve = ["W", "X", "Y", "Z"]
    guion = ["-"]
    numeroNuevo = "01800" + ""

    for numero in numeroEscrito:
        for letra in dos:
            if letra in numero:
                numeroNuevo += "2"
        for letra in tres:
            if letra in numero:
                numeroNuevo += "3"
        for letra in cuatro:
            if letra in numero:
                numeroNuevo += "4"
        for letra in cinco:
            if letra in numero:
                numeroNuevo += "5"
        for letra in seis:
            if letra in numero:
                numeroNuevo += "6"
        for letra in siete:
            if letra in numero:
                numeroNuevo += "7"
        for letra in ocho:
            if letra in numero:
                numeroNuevo += "8"
        for letra in nueve:
            if letra in numero:
                numeroNuevo += "9"
        for letra in guion:
            if letra in numero:
                numeroNuevo += "-"

    return numeroNuevo

# AQUI agregas tus funciones





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


