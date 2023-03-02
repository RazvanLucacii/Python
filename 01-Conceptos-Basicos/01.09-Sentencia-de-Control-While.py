valor = 0
while (valor < 5):
    valor = valor + 1                       # equivalente a valor += 1
    if(valor == 2):
        break
    print(f"El valor es {valor}.")
print("")

citricos = ["naranja", "limon", "pomelo", "lima", "mandarina"]
posicion = 0

while (posicion < len(citricos)):
    print(f"{posicion}: {citricos[posicion]}")
    posicion += 1
else:
    print("Else del while")

print("Fin del WHILE")

