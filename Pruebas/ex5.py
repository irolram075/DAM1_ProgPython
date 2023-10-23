"""
<<<<<<< HEAD
Crea un algoritmo en pseudocódigo y pásalo también a un programa en Python que pida los días totales 
trabajados en la vida laboral y te transforme esos días a años, meses y días.

Para este programa vamos a considerar que todos los años tienen 365 días y todos los meses 30 días.
=======
Crea un algoritmo en pseudocódigo y pásalo también a un programa en Python que pida los días totales trabajados en la vida laboral y te transforme esos días a años, meses y días.

Para este programa vamos a considerar que todos los años tienen 360 días y todos los meses 30 días.
>>>>>>> a5242033c3c148990c3d612e94184b0a7e7efe75

Debe cumplir lo siguiente:

- La palabra año, mes y día irá en plural o singular dependiendo de su cantidad.

<<<<<<< HEAD
- No puede introducir un valor negativo para los días. Si lo hace, debéis dar un mensaje de error y volver
 a pedir los días trabajados hasta que introduzca un número positivo (el 0 también es válido).
=======
- No puede introducir un valor negativo para los días. Si lo hace, debéis dar un mensaje de error y volver a pedir los días trabajados hasta que introduzca un número positivo (el 0 también es válido).
>>>>>>> a5242033c3c148990c3d612e94184b0a7e7efe75

Ejemplo 1:

> Introduzca los días trabajados: 1347
<<<<<<< HEAD
> Ha cotizado 3 años, 8 meses y 12 días.
=======
> Ha cotizado 3 años, 8 meses y 27 días.
>>>>>>> a5242033c3c148990c3d612e94184b0a7e7efe75

Ejemplo 2:

> Introduzca los días trabajados: 31
> Ha cotizado 0 años, 1 mes y 1 día.

Ejemplo 3:

> Introduzca los días trabajados: -230
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: -33
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: 0
> Ha cotizado 0 años, 0 meses y 0 días.


Inicio
<<<<<<< HEAD
año = diast / 365
mes = diast // 365
dia = diast % 365
Escribe "Introduzca los días trabajados: "
Lee diast

mientras (diast< 0) hacer
    Escribir "Error"


Si(diast >= 0) entonces
    Escribir "Ha cotizado " año, + "años" + mes, + "meses" + dia +"días"
    
=======
>>>>>>> a5242033c3c148990c3d612e94184b0a7e7efe75

    
Fin
"""
<<<<<<< HEAD
=======
import datetime

fecha = int(input("Cuantos dias has trabajado en tu vida hulio: "))

dias_cotizados = datetime.datetime(fecha)
hoy = datetime.datetime.now()


>>>>>>> a5242033c3c148990c3d612e94184b0a7e7efe75
