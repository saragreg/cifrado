from string import ascii_lowercase
import operator
from collections import Counter
import string

texto = open('texto1.txt', 'r')
mensaje = texto.read()
mensaje = mensaje.replace('v', '0')
msj = mensaje.lower()
a = [' ', ',', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '/n']
length = len(msj)
print(length)
for c in a:
    length = length - msj.count(c)  # Se calcula las letras que hay sin contar comas, puntos, espacios y números
Alphabet = ascii_lowercase
FrecT = []
Frec = [['e', 16.78, 100], ['a', 11.96, 100], ['o', 8.69, 100], ['l', 8.37, 100], ['s', 7.88, 100], ['n', 7.01, 100],
        ['d', 6.87, 100], ['r', 4.94, 100], ['u', 4.80, 100], ['i', 4.15, 100], ['t', 3.31, 100], ['c', 2.92, 100],
        ['p', 2.776, 100], ['m', 2.12, 100], ['y', 1.54, 100], ['q', 1.53, 100], ['b', 0.92, 100], ['h', 0.89, 100],
        ['g', 0.73, 100], ['f', 0.52, 100], ['v', 0.39, 100], ['j', 0.30, 100], ['ñ', 0.29, 100], ['z', 0.15, 100],
        ['x', 0.06, 100], ['k', 0, 100], ['w', 0, 100]]
usados = []
for letra in Alphabet:  # recorremos todo el alfabeto
    i = msj.count(letra)  # se cuenta cuantas veces aparece en el texto
    por = [letra, (i / length) * 100]  # se calcula la frecuencia y se guarda [letra, frecuencia]
    FrecT.append(por)  # se añade al array
print(length)
i = 0

for letra in Frec:  # se recorre el array de frecuencias inicial
    for letraB in FrecT:  # se recorre el array de frecuencias creadas
        if letraB[0] not in usados:  # si no esta usada (la de frecuencias creadas)
            print(letraB[0],
                  abs(letra[1] - letraB[1]))  # imprime la letra y la diferencia con cada una de las frecuencias
            if letra[2] > abs(letra[1] - letraB[
                1]):  # si la diferencia de la letra (de frecuencias inicial) es mayor que la calculada
                cambio = letraB[0]  # cambio = esa letra (creada)
                letra[2] = abs(letra[1] - letraB[1])  # se actualiza la diferencia en el array de frecuencias inicial
                print(cambio)
    msj = msj.replace(cambio, letra[
        0].upper())  # se reemplaza la letra de cambio por la letra de la frecuencia inicial y se pone en mayúscula para evitar errores
    usados.append(cambio)  # se añade el cambio al array de usados
    print(cambio, letra[0])  # se imprime el cambio

msj = msj.replace('P', 's')  # se ajustan manualmente las letras incorrectas
msj = msj.replace('T', 'm')
msj = msj.replace('K', 'r')
msj = msj.replace('S', 'n')
msj = msj.replace('N', 'l')
msj = msj.replace('C', 'p')
msj = msj.replace('B', 'q')
msj = msj.replace('H', 'j')
msj = msj.replace('V', 'x')
msj = msj.replace('Y', 'b')
msj = msj.replace('R', 'c')
msj = msj.replace('I', 't')
msj = msj.replace('L', 'i')
msj = msj.replace('M', 'f')
msj = msj.replace('J', 'z')
msj = msj.replace('F', 'h')
msj = msj.replace('0', 'v')

print(msj.upper())
