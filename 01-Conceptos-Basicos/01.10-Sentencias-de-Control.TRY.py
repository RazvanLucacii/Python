import sys

num1 = 0
num2 = 100

try:
    num3 = num1 / num2
    print(f"Resultado: {num3}")
    f = open('myfile.txt')
except Exception as err:
    print("Se ha producido un error")
    print(err)
    print(type(err))
finally:
    print("Bloque FINALLY")

print("FIN")