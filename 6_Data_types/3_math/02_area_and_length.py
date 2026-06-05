#                            Площадь и длина.
# Напишите программу, определяющую площадь круга и длину окружности по
# заданному радиусу R.

from math import pow, pi
radius = float(input())

area = pi * pow(radius, 2) # площадь круга
length = 2 * pi * radius   # длина окружности

print(area)
print(length)