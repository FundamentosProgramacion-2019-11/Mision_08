#Martha Margarita Dorantes Cordero
# cadenas 


def combinarLetras(cadena) :
	cadena = cadena.lower()
	resultado = ""
	x = True
	for s in cadena:
		if x == True :
			resultado += s.upper()
			x = False
		else :
			resultado += s
			x = True
	return resultado


def contieneLasVocales(cadena) :
	cadena = cadena.lower()
	if "a" in cadena and "e" in cadena and "i" in cadena and "o" in cadena and "u" in cadena :
		return True
	else :
		return False


def formarNombreUsuario(nombre, paterno, matricula) :
	nombre = nombre.lower()
	paterno = paterno.lower()
	matricula = str(matricula)
	resultado = nombre[:3] + paterno[:3] + matricula[(len(matricula) - 3):]
	return resultado


def esCorrecto(nombreCompleto) :
	cadenaCorrecta = nombreCompleto.title()
	if nombreCompleto == cadenaCorrecta :
		return True
	else :
		return False


def traducirTelefono(numeroTelefono) :
	numeroTraducido = numeroTelefono.upper()
	for s in numeroTraducido:
		if s == 'A' or s == 'B' or s == 'C' :
			numeroTraducido = numeroTraducido.replace(s, '2')
		if s == 'D' or s == 'E' or s == 'F' :
			numeroTraducido = numeroTraducido.replace(s, '3')
		if s == 'G' or s == 'H' or s == 'I' :
			numeroTraducido = numeroTraducido.replace(s, '4')
		if s == 'J' or s == 'K' or s == 'L' :
			numeroTraducido = numeroTraducido.replace(s, '5')
		if s == 'M' or s == 'N' or s == 'O' :
			numeroTraducido = numeroTraducido.replace(s, '6')
		if s == 'P' or s == 'Q' or s == 'R' or s == 'S' :
			numeroTraducido = numeroTraducido.replace(s, '7')
		if s == 'T' or s == 'U' or s == 'V' :
			numeroTraducido = numeroTraducido.replace(s, '8')
		if s == 'W' or s == 'X' or s == 'Y' or s == 'Z' :
			numeroTraducido = numeroTraducido.replace(s, '9')
	return numeroTraducido


"""
print(
	combinarLetras("Esta cadena"),
	contieneLasVocales("Abuelito"),
	formarNombreUsuario("Emmanuel","Saenz",12345678),
	esCorrecto("Emmanel Nz Rangel"),
	traducirTelefono("01800-VOY-BIEN"))
"""
