"""
#OPERADORES ARITMETICOS
Suma +
Resta -
Multimplicacion *
Division /
Modulo %
Exponente **
Division entera //

OPERADORES LOGICOS
Operadores de Igualdad ==
Operadores de Igualdad !=
Mayor > Mayor que =>
menor < Menor que <=
and &&  or  not  !=
+= x  Le suma el valor de la X Esto nos funciona para todas las operaciones (+ - * /)
"""

 #Crea un programa que imprima por consola todos los números comprendidos
 #entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.


a = 5
b = 3
print(f"la suma de 5+3 : {a+b}")
print(f"la resta de 5-3 : {a-b}")
print(f"la multiplicacion de 5*3 : {a*b}")
print(f"la division de 5/3 : {a/b}")
print(f"El modulo de 5%3 : {a%b}")
print(f"El exponente de 5**3 : {a**b}")
print(f"el 5 es mayor que 3: {a > b}")
print(f"el 5 es menor que 3: {a < b}")

for i in range(10, 56):
    if i != 16:
        if i % 3 != 0:
            print(i)


