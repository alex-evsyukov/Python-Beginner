#                           Количество дней 📅
# Дан порядковый номер месяца (1, 2, ..., 12).
# Напишите программу, которая выводит на экран количество дней в этом месяце.
# Принять, что год является невисокосным.

month_number = int(input())
if 1 <= month_number <= 12:
    if month_number == 2:
        print(28)
    elif month_number == 4 or month_number == 6 or month_number == 9 or month_number == 11:
        print(30)
    else:
        print(31)
