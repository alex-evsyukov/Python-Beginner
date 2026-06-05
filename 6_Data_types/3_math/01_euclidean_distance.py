#                       Евклидово расстояние 📏.
# Напишите программу, определяющую евклидово расстояние между двумя точками, координаты которых заданы.

from math import sqrt, pow

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

euc_distance = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) # Евклидово расстояние. (формула)

print(euc_distance)