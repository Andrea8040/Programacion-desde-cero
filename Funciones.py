"""
una funcion se crea con la palabra def + Nombre terminado en (), si vamos a enviarle algun parametro,
 esos parametros se ponen dentro del parentesis separados por coma ,


Print: Imprime por terminal
Return: Nos retorna una cadena de texto

FEJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 *
"""

def funcion_a()->None:
    print("Funcion sin parámetros ni retorno")
def  retornar_saludo():
    return  "mi primer retorno impreso por consola"
saludo = retornar_saludo()
print(retornar_saludo())

# Con argumentos
def with_return(name, apellido):
    print (f"{name}, {apellido}")
with_return("Imprima", "cadena")

# Con argumentos predeterminado
def default_arg_saludo(name="Predeterminado"):
    print(f"este valor es, {name}")

default_arg_saludo("predeterminado 1")
default_arg_saludo()

"""DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos."""

def print_numeros(text1, text2)-> int:
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(text1 + text2)
        elif i % 3 == 0:
            print(text1)
        elif i % 5 == 0:
            print(text2)


print_numeros("Texto 1","Texto 2")













