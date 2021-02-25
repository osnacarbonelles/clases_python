# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 14:27:31 2021

@author: Osnaider Carbonell
"""

"""
1. Hacer un algoritmo que calcule el total a pagar por la compra de
camisas. Si se compran tres camisas o mas se aplica un descuento
del 30% sobre el total de la compra y si son menos de tres camisas
un descuento del 10%.
"""
precio = float(input('Digité el precio de la camisa: $'))
cant_camisas = int(input('Digité la cantidad de camisas a comprar: '))
total = cant_camisas * precio
if (cant_camisas >= 3):
    descuento1 = total * 0.30
    Valor_total1 = total - descuento1
    print(f'El total a pagar es: ${Valor_total1:,}')
else:
    descuento2 = total * 0.10
    Valor_total2 = total - descuento1
    print(f'El total a pagar es: ${Valor_total2:,}')


"""
2. En un supermercado se hace una promoción, mediante la cual el
cliente obtiene un descuento dependiendo de un número que se
escoge al azar. Si el número escogido es menor que 74 el descuento
es del 15% sobre el total de la compra, si es mayor o igual a 74 el
descuento es del 20%. Obtener cuanto dinero se le descuenta.
"""
compra = float(input('Digité el total de su compra: $'))
numero = int(input('Digité un numero para participar en el descuento: '))
if (numero < 74):
    descuento1 = compra * 0.15
    Valor_total1 = compra - descuento1
    print(f'Su descuento fue de: ${descuento1:,}')
    print(f'El total a pagar es: ${Valor_total1:,}')
else:
    descuento2 = compra * 0.20
    Valor_total2 = compra - descuento2
    print(f'Su descuento fue de: ${descuento2:,}')
    print(f'El total a pagar es: ${Valor_total2:,}')


"""
3. Una compañía de seguros está abriendo un departamento de
finanzas y estableció un programa para captar clientes, que conssite
en lo siguiente: Si el monto por el que se efectúa la fianza es menor
que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
es mayor que $50.000 la cuota a pagar será el 2% del monto. La
afianzadora desea determinar cual será la cuota que debe pagar al
cliente.
"""
monto_fianza = float(input('Digité su monto de fianza: $'))
if (monto_fianza < 50000):
    couta_pagar = monto_fianza * 0.03
    print(f'La cuato que el cliente debe pagar es: ${couta_pagar:,}')
else:
    couta_pagar = monto_fianza * 0.02
    print(f'La cuato que el cliente debe pagar es: ${couta_pagar:,}')


"""
4. Una fábrica ha sido sometida a un programa de control de
contaminación para lo cual se efectúa una revisión de los puntos de
contaminación generados por la fábrica. El programa de control de
contaminación consiste en medir los puntos que emite la fábrica en
cinco días de una semana y si el promedio es superior a los 170
puntos entonces tendrá la sanción de parar su producción por una
semana y una multa del 50% de las ganancias diarias cuando no se
detiene la producción. Si el promedio obtenido de puntos es de 170 o
menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
desea saber cuanto dinero perderá después de ser sometido a la
revisión.
"""
puntos1 = int(input('Digité la cantidad de puntos del primer dia: '))
puntos2 = int(input('Digité la cantidad de puntos del segundo dia: '))
puntos3 = int(input('Digité la cantidad de puntos del tercer dia: '))
puntos4 = int(input('Digité la cantidad de puntos del cuarto dia: '))
puntos5 = int(input('Digité la cantidad de puntos del quinto dia: '))
ganancias1 = int(input('Digité las ganancias del primer dia: $'))
ganancias2 = int(input('Digité las ganancias del segundo dia: $'))
ganancias3 = int(input('Digité las ganancias del tercer dia: $'))
ganancias4 = int(input('Digité las ganancias del cuarto dia: $'))
ganancias5 = int(input('Digité las ganancias del quinto dia: $'))
promedio_puntos = (puntos1 + puntos2 + puntos3 + puntos4 + puntos5) / 5
ganancia_total = ganancias1 + ganancias2 + ganancias3 + ganancias4 + ganancias5
if (promedio_puntos > 170):
    multa = ganancia_total * 0.50
    print(f'La multa por contaminación es de: ${multa:,}')
else:
    multa = 0
    print(f'No tuvo multa por contaminación')
print(f'El promedio de puntos por revision fue de: {promedio_puntos}')
print(f'La ganancia total de la semana es de: ${ganancia_total:,}')


"""
5. Una persona se encuentra con un problema de comprar un automóvil
o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
mientras el automóvil se devalúa, con el terreno sucede lo contrario.
Esta persona comprará el automóvil si al cabo de tres años la
devaluación de este no es mayor que la mitad del incremento del
valor del terreno. Ayúdale a esta pesona a determinar si debe o no
comprar el automóvil.
"""
precio = float(input('Digite el precio del del terreno o del automovil: $'))
incremento_anual = float(input('Digite el incremento anual del terreno: '))
decremento_anual = float(input('Digite el devaluación anual del automovil: '))
incremento = (((precio * incremento_anual) / 100) * 3) / 2
decremento = ((precio * decremento_anual) / 100) * 3
print(f'La mitad del incremento del terreno en 3 años es: ${incremento:,}')
print(f'La devaluacion del automovil en 3 años es: ${decremento:,}')
if (decremento < incremento):
    print('Te conviene comprar el Automovil')
else:
    print('Te conviene comprar el terreno')


"""
6. En una fábrica de computadoras se planea ofrecer a los clientes un
descuento que dependerá del número de computadoreas que
compre. Si las computadoras son menos de cinco se les dará un 10%
de descuento sobre el total de la compra; si el número de
computadoras es mayor o igual a cinco pero menos de diez se le
otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
precio de cada computadora es de $11.000.
"""
num_computadoras = int(input('Digite el numero de computadoras compradas: '))
total_computadoras = num_computadoras * 11000
if (num_computadoras < 5):
    descuento = total_computadoras * 0.10
elif (num_computadoras < 10):
    descuento = total_computadoras * 0.20
else:
    descuento = total_computadoras * 0.40
total = total_computadoras - descuento
print(f'El descuento aplicado es de: ${descuento:,}')
print(f'El total a pagar por las {num_computadoras} computadoras')
print(f'compradas es de: ${total:,}')


"""
7. Un proveedor de estéreos ofrece un descuento del 10% sobre el
precio sin IVA, de algún aparato si este cuesta $2000 o más. Además,
independientemente de esto, ofrece un 5% de descuento si la marca
es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente
cualquiera por la compra de su aparato. IVA es del 16%.
"""
precio = float(input('Digite el precio del aparato: '))
marca = input('Digite la marca del aparato: ')
porcentaje = float(input('Digite el porcentaje de IVA: '))
if marca == 'NOSY' and precio >= 2000:
    descuento = precio * 0.15
elif precio >= 2000:
    descuento = precio * 0.10
total = precio - descuento
iva = (total * porcentaje) / 100
valor_total = total + iva
print(f'El total a pagar es: ${precio:,}')
print(f'El descuento aplicado es: ${descuento:,}')
print(f'El IVA aplicado es; ${iva:,}')
print(f'El total a pagar ya on IVA incluido es: ${valor_total:,}')


"""
8. Una empresa quiere hacer una compra de varias piezas de la misma
clase a una fábrica de refacciones. La empresa, dependiendo del
monto total de la compra, decidirá que hacer para pagar al fabricante.
Si el monto total de la compra excede de $500.000 la empresa tendrá
la capacidad de invertir de su propio dinero un 55% del monto de la
compra, pedir prestado al banco un 30% y el resto lo pagará
solicitando un crédito al fabricante. Si el monto total de la compra no
excede de $500.00 la empresa tendrá capacidad de invertir de su
propio dinero un 70% y el restante 30% lo pagará solicitando crédito
al fabricante. El fabricante cobra por concepto de interes un 20%
sobre la cantidad que se le pague a crédito. Obtener la cantidad a
inverir, valor del préstamo, valor del crédito y los intereses.
"""
num_piezas = int(input('Digite el numero de piezas: '))
valor_piezas = float(input('Digite el costo de la pieza: $'))
total = num_piezas * valor_piezas
if (total > 50000):
    inversion = total * 0.55
    banco = total * 0.30
    credito = total * 0.15
else:
    inversion = total * 0.70
    banco = 0
    credito = total * 0.30
interes = credito * 0.20
print(f'La inversion es de: ${inversion:,}')
print(f'El prestamo del banco es de: ${banco:,}')
print(f'El credito a pagar es por: ${credito:,}')
print(f'El interes por el credito es: ${interes:,}')


"""
9. Leer 2 números; si son iguales que lo multiplique, si el primero es
mayor que el segundo que los reste y sino que los sume.
"""
numero1 = int(input('Digite un numero: '))
numero2 = int(input('Digite otro numero: '))
if (numero1 == numero2):
    multiplicacion = numero1 * numero2
    print(f'{numero1} x {numero2} = {multiplicacion}')
elif (numero1 > numero2):
    resta = numero1 - numero2
    print(f'{numero1} - {numero2} = {resta}')
else:
    suma = numero1 + numero2
    print(f'{numero1} + {numero2} = {suma}')


"""
10. Leer tres números diferentes e imprimir el número mayor de los
tres.
"""
numero1 = int(input('Digite un numero: '))
numero2 = int(input('Digite otro numero: '))
numero3 = int(input('Digite otro numero: '))
if (numero1 > numero2) and (numero1 > numero3):
    print(f'El numero mayor es: {numero1}')
elif (numero2 > numero1) and (numero2 > numero3):
    print(f'El numero mayor es: {numero2}')
else:
    print(f'El numero mayor es: {numero3}')
