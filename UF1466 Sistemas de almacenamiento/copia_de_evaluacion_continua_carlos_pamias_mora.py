# -*- coding: utf-8 -*-
"""Copia de Evaluacion continua Carlos Pamias Mora.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RL1pdN_ZwkOAqlQdeuo5qCcikBJZvzBt

## Pregunta 1
"""

celsius = float(input('Introduzca la temperatura en grados Celsius:'))
fahrenheit = ((celsius * (9/5)) + 32)
print(f'La conversion de los grados celsius introducidos: {celsius} es: {fahrenheit} en grados fahrenheit')



"""## Pregunta 2"""

letras = 0
valor = input('Introduzca una frase: ')
palabras = valor.split()
contador = len(palabras)
for a in valor:
    if a != ' ':
        letras +=1
print(f'La frase introducida tiene {letras} letras y {contador} palabras')

"""## Pregunta 3"""

peso = float(input('Introduzca su peso en Kg: '))
altura = float(input('Introduzca su altura en metros: '))
IMC = (peso / (altura**2))
texto = f'Su IMC indica que tiene '
if IMC < 18.5:
    texto += 'Bajo peso'
elif IMC >= 18.5 and IMC < 25:
     texto += 'Peso normal.'
elif IMC >= 25 and IMC < 30:
     texto += 'Sobrepeso.'
else:
     texto += 'Obesidad'
print(texto)

"""## pregunta 4

"""

tabla = []
palabras= ""
while palabras != '**':
    palabras = input('Introduzca palabras, para terminar pulse "**": ')
    if palabras != '**':
       tabla.append(palabras)


tabla.sort()
print(tabla)

"""## Pregunta 5"""

diasTrabajados = int(input('Introduce el total de dias trabajados: '))
anyos = diasTrabajados // 365
diasTrabajados %= 365
mes = diasTrabajados // 30
dias = diasTrabajados % 30
print(f'Has trabajado {anyos} años, {mes} meses y {dias} en tu vida laboral')