#           Одинаковые цифры
# Дано натуральное число.
# Напишите программу, которая определяет, состоит ли указанное число из
# одинаковых цифр.

n = int(input())
flag = True

while n > 9:
    last_digit = n % 10
    previous_digit = n % 100 // 10
    if last_digit != previous_digit:
        flag = False
    n //= 10

if flag:
    print('YES')
else:
    print('NO')