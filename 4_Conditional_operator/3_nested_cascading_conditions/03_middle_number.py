#                                       Серединное число
# Даны три различных целых числа. Напишите программу, которая находит серединное значение из этих чисел.

n1, n2, n3 = int(input()), int(input()), int(input())

if n1 < n2 < n3 or n1 > n2 > n3:
    print(n2)
elif n2 < n1 < n3 or n2 > n1 > n3:
    print(n1)
elif n1 < n3 < n2 or n1 > n3 > n2:
    print(n3)