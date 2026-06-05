#                   Сортировка трёх 🔀🌶️.
# Напишите программу, которая упорядочивает три числа от большего к меньшему.

a, b, c = int(input()), int(input()), int(input())

total = a + b + c

print(max(a, b, c))
print(total - max(a, b, c) - min(a, b, c))
print(min(a, b, c))
