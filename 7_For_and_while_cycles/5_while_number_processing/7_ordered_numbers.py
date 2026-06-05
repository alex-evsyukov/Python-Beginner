#               Упорядоченные цифры 🌶️
# Дано натуральное число.
# Напишите программу, которая определяет,
# является ли последовательность его цифр при просмотре справа налево
# упорядоченной по не убыванию.

n = int(input())
flag = True
while n > 9:
    current_digit = n % 10
    previous_digit = n % 100 // 10
    if previous_digit < current_digit:
        flag = False
    n //= 10
if flag:
    print('YES')
else:
    print('NO')