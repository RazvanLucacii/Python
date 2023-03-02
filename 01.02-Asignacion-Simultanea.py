#############################################################
# Declaracion de Variables                                  #
#############################################################
#                                                           #
# Sintaxis: [Nombre de la variable] = [Valor inicial]       #
#                                                           #
# Ejemplos:                                                 #
#   numero = 20                                             #
#   saludo = "Hola Mundo !!!"                               #
#                                                           #
#############################################################

#Cambiar los valores de a y b. Intento 1.

a = 5
b = 10

a = b
b = a

print("Intento 1. Forma incorrecta.")
print(a)
print(b)
print("")

#Cambiar loos valores de a y b. Intento 2.

a = 5
b = 10

temp = a
a = b
b = temp

print("Intento 2. Forma correcta.")
print(a)
print(b)
print("")

#Cambiar loos valores de a y b. Intento 3.

a = 5
b = 10

a,b = b,a

print("Intento 3. Forma correcta segun Python.")
print(a)
print(b)
print("")

