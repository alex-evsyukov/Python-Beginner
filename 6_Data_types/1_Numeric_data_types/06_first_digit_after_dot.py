# Дано положительное действительное число.
# Выведите его первую цифру после десятичной точки.

number = float(input())

number = number * 10
digit_after_dot = int(number % 10)

print(digit_after_dot)