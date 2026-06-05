# Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя – и выводит фразу:
# Hello <введённое имя> <введённая фамилия>! You have just delved into Python

name1, name2 = input(), input()
print("Hello", name1, name2 + "!", "You have just delved into Python")