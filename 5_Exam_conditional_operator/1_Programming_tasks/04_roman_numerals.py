#                                   Римские цифры.
# Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру.
# Если число находится вне диапазона [1;10], то программа должна вывести текст «ошибка» (без кавычек).

numeral = int(input())

if 1 <= numeral <= 10:
    if numeral == 1:
        print('I')
    elif numeral == 2:
        print('II')
    elif numeral == 3:
        print('III')
    elif numeral == 4:
        print('IV')
    elif numeral == 5:
        print('V')
    elif numeral == 6:
        print('VI')
    elif numeral == 7:
        print('VII')
    elif numeral == 8:
        print('VIII')
    elif numeral == 9:
        print('IX')
    elif numeral == 10:
        print('X')
else:
    print('ошибка')
