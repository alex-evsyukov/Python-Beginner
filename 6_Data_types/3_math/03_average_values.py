#                   Средние значения.
# На вход программе подаются два положительных действительных числа
# a и b, каждое на отдельной строке.
# Программа должна вывести
# 4 числа (каждое на отдельной строке) –
# среднее арифметическое,
# геометрическое,
# гармоническое и квадратичное.

from math import sqrt

a, b = float(input()), float(input())

arithmetic_mean = (a + b) / 2                      # среднее арифметическое чисел a и b
geometric_mean = sqrt(a * b)                       # среднее геометрического чисел a и b
harmonic_mean = (2 * a * b) / (a + b)              # среднее гармонического чисел a и b
quadratic_mean = sqrt((pow(a, 2) + pow(b, 2)) / 2) # среднее квадратичного чисел a и b

print(arithmetic_mean)
print(geometric_mean)
print(harmonic_mean)
print(quadratic_mean)
