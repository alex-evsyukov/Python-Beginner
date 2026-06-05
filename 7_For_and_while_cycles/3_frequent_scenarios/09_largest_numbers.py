#               Наибольшие числа 🌶️🌶️
# На вход программе подаются натуральное число n (n >= 2), а затем n
# различных натуральных чисел последовательности, каждое на отдельной строке.
# Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

n = int(input())
largest_1 = 0
largest_2 = 0

for _ in range(n):
    n = int(input())
    if n > largest_1:
        largest_2, largest_1 = largest_1, n
    elif n > largest_2:
        largest_2 = n

print(largest_1)
print(largest_2)
