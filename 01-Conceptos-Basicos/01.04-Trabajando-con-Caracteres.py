#####################################################################
# Trabajando con Cadenas de Texto                                   #
#####################################################################

cadena = "Hola Mundo !!!"

# Mostrar caractéres de posiones o rangos
print(cadena)
print(cadena[2])
print(cadena[2:])
print(cadena[:6])
print(cadena[2:6])
print(cadena[-2])

print(f"Número de caractéres: {len(cadena)}")

# Funciones de objetos de tipo STR
print(cadena.lower())
print(cadena.upper())
print(cadena.capitalize())
print(cadena.replace("o", "0"))
print(cadena.isdigit())
print("57".isdigit())
print(cadena.count("o"))

#####################################################################
# Formateando Cadenas y Número                                      #
#####################################################################

mensaje = "Mundo"

print("Hola " + mensaje + " !!!")
print("Hola {} !!!".format(mensaje))
print("Hola {s} !!!".format(s=mensaje))
print("Hola {mensaje} !!!")
print(f"Hola {mensaje} !!!")


resultado = "Hola {s} !!!".format(s=mensaje)
print(resultado)

numero = 10 / 3
print(numero)
print("Numero: {n}".format(n=numero))
print("Numero: {n:1.2f}".format(n=numero))