# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:45:06 2021

@author: Osnaider Carbonell
"""


"""
1. Tres personas deciden invertir su dinero para fundar una empresa.
Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
que cada quien invierte con respecto a la cantidad total invertida.
"""
inversion1 = float(input('Digité su inversión: $'))
inversion2 = float(input('Digité su inversión: $'))
inversion3 = float(input('Digité su inversión: $'))
total_inversion = (inversion1 + inversion2 + inversion3)
porcentaje_inversion1 = (inversion1 / total_inversion) * 100
porcentaje_inversion2 = (inversion2 / total_inversion) * 100
porcentaje_inversion3 = (inversion3 / total_inversion) * 100
print(f'El porcentaje para la persona 1 es de: {porcentaje_inversion1}%')
print(f'El porcentaje para la persona 2 es de: {porcentaje_inversion2}%')
print(f'El porcentaje para la persona 3 es de: {porcentaje_inversion3}%')


"""
2. Una empresa paga a sus empleados además del sueldo base una
bonificación especial de $80.000 por cada hijo. Realice un programa
en Java que determine el monto de la bonificación y el monto total a
pagar al trabajador.
"""
sueldo_base = float(input('Digité su sueldo base: $'))
numero_hijos = int(input('Digité el numero de hijo que usted tiene: '))
bonificacion = numero_hijos * 80000
monto_total = bonificacion + sueldo_base
print(f'El monto de su bonificación es: ${bonificacion:,}')
print(f'Su monto total es: ${monto_total:,}')


"""
3. Un banco da a sus ahorradores un interes de 1.5% sobre el monto
ahorrado. Teniendo como dato de entrada el saldo inicial del
ahorrador determine el saldo final.
"""
saldo_inicial = float(input('Digité el saldo inicial del ahorrador: $'))
numero_meses = int(input('Digité el número de meses: '))
monto = (saldo_inicial * numero_meses * 0.015)
saldo_final = (saldo_inicial + monto)
print(f'El saldo final es de: {saldo_final}')


"""
4. Una inmobiliria vende terrenos a $80.000 el metro cuadrado. El
cliente debe dar una cuota inicial del 35% y el resto lo paga en 12
cuotas. Determine el valor a pagar por cuota inicial y el monto de
cada cuota.
"""
metros_cuadrados = float(input('Digité la cantidad de metros cuadrados: '))
cuota_inicial = 0.35
terreno = metros_cuadrados * 80000
monto_cuota = (terreno - cuota_inicial) / 12
print(f'El valor de monto de cada cuota es de: ${monto_cuota:,}')
print(f'El valor de su terreno es de: ${terreno:,}')


"""
5. Una empresa le hace los siguientes descuentos sobre el sueldo base
a sus trabajadores: 1% por ley de politica pública, 4% por seguro
social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un
programa en Java que determine el monto de cada descuento y el
monto total a pagar al trabajador
"""
sueldo_base = float(input('Digité el sueldo base de sus trabajadores: $'))
politica_publica = (sueldo_base * 0.01)
seguro_social = (sueldo_base * 0.04)
seguro_forzoso = (sueldo_base * 0.005)
caja_ahorro = (sueldo_base * 0.05)
monto_total = (sueldo_base - politica_publica - seguro_social
               - seguro_forzoso - caja_ahorro)
print(f'El Monto a descontar por ley de politica es de: ${politica_publica:,}')
print(f'El Monto a descontar de seguro social es de: ${seguro_social:,}')
print(f'El Monto a descontar de seguro forzoso es de: ${seguro_forzoso:,}')
print(f'El Monto a descontar por caja de ahorro es de: ${caja_ahorro:,}')
print(f'El Monto a pagar a los trabajadores es de: ${monto_total:,}')


"""
6. El periódico el Informador cobra por un aviso clasificado un monto
que depende del número de palabras, tamaño en cetímetros y
número de colores. Cada palabra tiene un costo de $20.000, cada
centímetro tiene un costo de $15.000 y cada color tiene un costo de
$25.000. Realice un algoritmo que determine el monto a pagar por un
aviso clasificado.
"""
total_palabras = int(input('Digité el número total de palabras: '))
cm = float(input('Digité el número total de cetímetros: '))
total_colores = int(input('Digité el número total de colores: '))
valor_palabras = (total_palabras * 20000)
valor_cm = (cm * 15000)
valor_colores = (total_colores * 25000)
monto = (valor_palabras + valor_cm + valor_colores)
print(f'El monto total es de: ${monto:,}')


"""
7. Una empresa paga a sus empleados un bono por antigüedad que
consiste en $100.000 por el primer año laboral y $120.000 por cada
año siguiente. Realice un programa en Java que determine el monto
del bono a pagar a un trabajador que tiene varios años en la empresa.
"""
cantidad_anos = int(input('Digité la cantidad de años en la empresa: '))
if cantidad_anos > 1:
    bono = (cantidad_anos * 120000)
    print(f'Su bono es de: ${bono:,}')
else:
    bono = (cantidad_anos * 100000)
    print(f'El monto de su bono es de: ${bono:,}')


"""
8. Una Universidad le paga a sus profesores $20.000 la hora y le hace
un descuento del 5% por concepto de caja de ahorro. Determine el
monto del descuento y el monto total a pagar al profesor.
"""
num_horas_trabajadas = int(input('Digité el número de horas trabajadas: '))
valor_hora = 20000
desc_caja_ahorro = 0.05
monto_descuento = (num_horas_trabajadas * valor_hora) * desc_caja_ahorro
monto_total = (num_horas_trabajadas * valor_hora) - monto_descuento
print(f'El descuento por concepto de caja de ahorros es de: {monto_descuento}')
print(f'Su sueldo final es de: ${monto_total:,}')


"""
9. Un centro de comunicaciones alquilan tarjetas para realizar llamadas
y cobran el monto consumido de la tarjeta mas un recargo del 20%.
Teniendo como dato de entrada el monto inicial y el monto final de la
tarjeta, determine el costo de la llamada.
"""
monto_inicial = float(input('Digité el monto inicial: $'))
monto_final = float(input('Digité el monto final: $'))
costo_llamada = (monto_inicial - monto_final) * 0.2
print(f'El costo de la llamada es de: ${costo_llamada:,}')


"""
10. En una fototienda cobran por el revelado de un rollo $1.500 por cada
foto. Realice un programa en Java que determine el monto a pagar
por un revelado completo sabiendo que adiconalmente le cobran el
IVA (16%).
"""
cant_fotos = int(input('Digité la cantidad de Fotos que contien su rollo: '))
valor_fotos = 1500
iva = 0.16
costo_fotos = (cant_fotos * valor_fotos)
costo_final = ((costo_fotos * iva) + costo_fotos)
print(f'El valor a pagar es de: ${costo_final:,}')


"""
11. En un hospital existen tres áreas: Ginecología, Pediatría y
Traumatología. El presupuesto anual del hospital se reparte
conforme a la siguiente tabla: [Ginecología: 40%, Traumatología 30%,
Pediatría 30%]. Obtener la cantidad de dinero que recibirá cada área,
para cualquier monto presupuestal.
"""
presupuesto_anual = float(input('Digité el presupuesto anual: $'))
presupuesto_ginecologia = (presupuesto_anual * 0.40)
presupuesto_traumatologia = (presupuesto_anual * 0.30)
presupuesto_pediatria = (presupuesto_anual * 0.30)
print(f'Ginecología Recibirá: ${presupuesto_ginecologia:,}')
print(f'Traumatología Recibirá: ${presupuesto_traumatologia:,}')
print(f'Pediatría Recibirá: ${presupuesto_pediatria:,}')


"""
12. Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
que consiste en dejar gratis el alquiler de una película. Realice un
programa en Java que teniendo como dato de entrada el total de
películas alquiladas, y el número de días de alquiler, determine el
monto a pagar.
"""
cantidad_peliculas = int(input('Digité la cantidad de peliculas a alquilar: '))
cantidad_dias = int(input('Digité la cantidad de dias a alquilar: '))
DVD = 1500
monto = (cantidad_peliculas * cantidad_dias * DVD)
print(f'El monto a pagar es de: ${monto:,}')


"""
13. Una Agencia de viajes cobra por un Tour a Cartagena $25.000
diarios por persona. Realice un programa en Java que determine el
monto a pagar por una familia que desee realizar dicho Tour
sabiendo que también cobran el 12% de IVA.
"""
cant_personas = int(input('Digité la cantidad de personas: '))
valor_personas = 1500
iva = 0.12
costo_personas = (cant_personas * valor_personas)
costo_final = ((costo_personas * iva) + costo_personas)
print(f'El valor a pagar es de: ${costo_final:,}')


"""
14. Un Hotel 5 Estrellas de Santa Marta tiene una promoción para sus
clientes. Cobra por una habitación $100.000 el primer día y por el
resto $200.000 por día. Realice un programa en Java que determine
el valor total a pagar por la habitación si la estadía fue de varios
días.
"""
cantidad_dias = int(input('Digité la cantidad de dias a hospedarse: '))
if cantidad_dias == 1:
    valor_dia = (cantidad_dias * 100000)
    print(f'El valor de la habitación es de: ${valor_dia:,}')
else:
    valor_dia = (cantidad_dias * 200000)
    print(f'El valor de la habitación es de: ${valor_dia:,}')


"""
15. El banco del Pueblo da microcréditos a empresarios para ser
cancelados en un lapso de 2 años (24 meses). Al monto del
préstamo se le cobra un interés del 24%. El empresario debe pagar
la mitad del préstamo en 4 cuotas especiales y la otra mitad en 20
cuotas ordinarias. Realice un algoritmo que teniendo como dato de
entrada el monto del préstamo, determine el monto total a pagar por
el préstamo, el monto de las cuotas especiales y el monto de las
cuotas ordinarias.
"""
monto_prestamo = float(input('Digité el monto de prestamo: $'))
monto_total = (monto_prestamo * 0.24) + monto_prestamo
cuotas_especiales = monto_total / 4
cuotas_ordinarias = monto_total / 20
print(f'El monto total a pagar es de: ${monto_total:,}')
print(f'El monto de coutas especiales (4) es de: ${cuotas_especiales:,}')
print(f'El monto de coutas ordinarias (20) es de: ${cuotas_ordinarias:,}')
