            # Арифметические строки 🌶️.
# Вводятся 3 строки в случайном порядке.
# Напишите программу, которая выясняет, можно ли из длин этих строк
# построить арифметическую прогрессию.

len1, len2, len3 = len(input()), len(input()), len(input())

a = min(len1, len2, len3)
c = max(len1, len2, len3)
avg = len1 + len2 + len3 - a - c

print(a, avg, c)

if avg - a == c - avg:
    print("YES")
else:
    print("NO")









