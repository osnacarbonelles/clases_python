# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:56:33 2021

@author: Osnaider Carbonell
"""

print('Hello word!')

a = 5
print(a)

# Suma
a = 5
b = 2
c = a + b
print(c)

# Resta
a = 5
b = 2
c = a - b
print(c)

numero = int(input('Digite un numero: '))
cuadrado = numero ** 2
print(f'El numero {numero} al cuadrado es {cuadrado}')

valor_producto = float(input('Digite el valor del producto: $'))
descuento = valor_producto * 0.20
valor_total = valor_producto - descuento
valor_ahorrado = valor_producto - valor_total
print(f'El valor del producto es: ${valor_producto:,}')
print(f'El valor del producto con descuento es: ${valor_total:,}')
print(f'El valor ahorrado es: ${valor_ahorrado:,}')

edad = int(input('Digite su edad: '))
if (edad >= 18):
    print('Usted es mayor de 18 años')
else:
    print('Usted es menor de 18 años')

numero = int(input('Digite un numero: '))
if numero < 0:
    print(f'El numero {numero} es Negativo')
elif numero > 0:
    print(f'El numero {numero} es Positivo')
else:
    print(f'El numero {numero} es igual a cero')

    