"""
this is a exersize for the practis lenguage python whit logict programing

 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

"""

print("************Welcome FiZZ BuZZ************")

for index in range(1, 101) :

    es_multiplo_tres = index % 3 == 0
    es_multiplo_cinco = index % 5 == 0

    if es_multiplo_tres and es_multiplo_cinco :
        print('FiZZ-BUZZ')
    elif es_multiplo_tres:
        print("FiZZ")
    elif es_multiplo_cinco:
        print("BuZZ")
    else:
        print(index)


print("************End FiZZ BuZZ************")

# Otra forma de hacerlo mas corto y legible
for index in range(1, 101) :
    output = ''
    if index % 3 == 0:
        output += 'FiZZ'
    if index % 5 == 0:
        output += 'BuZZ'
    print( output if output else index)