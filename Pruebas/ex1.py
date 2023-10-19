"""
Escribe un algoritmo en pseudocódigo que lea un número y te diga si es par o impar.
El número no puede ser negativo ni mayor de 10, en tal caso solo mostrará un mensaje de error.
"""

"""
Inicio
    Escribe "Dame un número: "
    Leer num

    Mientras (num < 0 o > 10) hacer
        Escribe "Error "
    Si(num mod 2 = 0) entonces
        Escribe "El numero es par"
        Sino
        Escribe "El numero es impar"        


Fin
"""
num = int(input("Dame un numero: "))
print (num)
while num < 0 or num > 10:
    print("ERROR")
input("Introduce el numero de nuevo: ")
if num % 2 == 0:
    print ("El numero es par")
else:
    print ("El numero es impar")
