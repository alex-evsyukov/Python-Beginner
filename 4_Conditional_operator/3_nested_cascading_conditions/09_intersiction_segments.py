#           Пересечение отрезков 🌶️🌶️
# На числовой прямой даны два отрезка: [a1; b1] и [a2; b2]. Напишите программу, которая находит их пересечение.

a1, b1 = int(input()), int(input())
a2, b2 = int(input()), int(input())

if a1 < b1 < a2 < b2 or a2 < b2 < a1 < b1:
    print('пустое множество')
elif a1 < b1 == a2 < b2:
    print(a2)
elif a2 < b2 == a1 < b1:
    print(a1)
elif a1 < a2 < b1 < b2:
    print(a2, b1)
elif a2 < a1 < b2 < b1:
    print(a1, b2)
elif a1 == a2 < b1 < b2:
    print(a1, b1)
elif a1 == a2 < b2 < b1:
    print(a1, b2)
elif a2 < a1 < b1 < b2:
    print(a1, b1)
elif a1 < a2 < b2 < b1:
    print(a2, b2)
elif a2 < a1 < b1 == b2:
    print(a1, b1)
elif a1 < a2 < b1 == b2:
    print(a2, b2)
elif a1 == a2 < b1 == b2:
    print(a1, b1)
