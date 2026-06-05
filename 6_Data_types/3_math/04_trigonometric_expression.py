#               Тригонометрическое выражение.
# Напишите программу, вычисляющую значение тригонометрического выражения
# sin(x) + cos(x) + tan^2(x) по заданному числу градусов x.

from math import sin, cos, tan, radians

x = radians(float(input()))

# Альтернатива функции radians()
# R = x * pi / 180 -- формула для перевода градусов в радианы.

trigonometric_expression = sin(x) + cos(x) + pow(tan(x), 2)

print(trigonometric_expression)
