"""Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a 
aplicar y calcule e imprima por pantalla el precio final del artículo.
"""

num1 = input("Precio primer producto: ")
print(num1)
num2 = input("Precio segundo producto: ") 
print(num2)
iva = 0.21
suma = num1 + num2
print("La suma de " + num1 + " + " + num2 + " es igual a " + suma)