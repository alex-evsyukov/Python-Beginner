#                   Асимптотическое приближение 📉
# На вход программе подаётся натуральное число n.
# Напишите программу, которая вычисляет значение выражения
#  (1 + 1/2 + 1/3 + ... + 1/n) - ln(n)

from math import log

n = int(input())
total = 0
for i in range(2, n + 1):
    total += 1 / i
result = (1 + total) - log(n)
print(result)