# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kcRcLyCpzTzh2oKYcVTzGXNlRueHbO6k
"""

MasaPelota = 0.05
TiempoGolpe = 0.2

print("Vas a golpear una pelota(que esta en reposo) con una palo de golf por 0.2s, ingresa la fuerza con la que quieres que se golpee la pelota, la pelota pesa 0.05g")

Fuerza = float(input("Ingresa la Fuerza: "))
"""
Para esta parte use la formula Fuerza * delta_tiempo = masa * velocidadfinal - masa*velocidadinicial. del tema Impulso

y por que esta en reposo la velocidad inicial es 0 entonces todo esta parte (masa*velocidadinicial) es igual a 0

luego de esa formula despejamos velocidadfinal = masa * fuerza / delta_tiempo

"""

VelocidadPelotaf = (Fuerza * TiempoGolpe) / MasaPelota

print("La velocidad de la pelota es: ", VelocidadPelotaf)

print("La pelota va a colisionar con una caja, despuès de la colisión se van a unir la pelota y la caja, ingresa la masa de la caja para que al final alcancen una altura superior o igual a 12 cm")

MasaCaja = float(input("Ingresa la masa de la caja en (KG): "))


"""
Para esta parte use la formula del tema choques: masa1 * velocidad1inicial + masa2 * velocidad2inicial  = masa1 * velocidad1final + masa2 * velocidad2final

Y debido a que la caja esta en reposo esta parte de aqui es 0 :masa2 * velocidad2inicial

y en esta parte masa1 * velocidad1final + masa2 * velocidad2final: las velocidades son las mismas, entonces las juntamos en una y queda asi la formula:

masa1 * velocidad1inicial = (masa1  + masa2) velocidadConjunto

y de esta formula despejamos la velocidad en Conjunto: velocidadConjunto = masa1 * velocidad1inicial/ (masa1  + masa2)


"""

VelocidadConjunto = (VelocidadPelotaf * MasaPelota) / (MasaCaja + MasaPelota)

print("La velocidad de la pelota y la caja unida es de conjunto es: ", VelocidadConjunto , "m/s")

"""
Para esta parte usa la formula: 1/2*(m1+m2)VelocidadConjunto^2 = (m1+m2)*g*h

de ahi despeje la altura(nota las masas se cancelan )

quedando altura = (VelocidadConjunto^2) / (2 * 9.8)


"""

altura = (VelocidadConjunto ** 2) / (2 * 9.8)

altura = altura * 100

altura = int(altura)

print("La altura de la caja es: ", altura, "cm")

if (altura >= 12):
    print("Ganaste")
else:
    print("Perdiste")