"""
Escribe un algoritmo en pseudocódigo que lea un número y te diga si es par o impar.
El número no puede ser negativo ni mayor de 10, en tal caso solo mostrará un mensaje de error.
"""

"""
Inicio
<<<<<<< HEAD
    Escribe "Dame un número entre 0 y 10: "
    Leer num

    Mientras (num < 0, o > 10) hacer 
        Escribe " Error, dame un número entre 0 y 10 "

    Si (num / 2  ) entonces 
        Escribe "num es un número par "

    Sino
        Escribe "num es un número impar "   



Fin
"""
=======
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
>>>>>>> a5242033c3c148990c3d612e94184b0a7e7efe75
