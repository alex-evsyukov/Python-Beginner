# Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

city1, city2, city3 = input(), input(), input()

min_city_len = min(len(city1), len(city2), len(city3))
max_city_len = max(len(city1), len(city2), len(city3))

# Для самых маленьких
if len(city1) == min_city_len:
    print(city1)
elif len(city2) == min_city_len:
    print(city2)
else:
    print(city3)

# Для самых больших
if len(city1) == max_city_len:
    print(city1)
elif len(city2) == max_city_len:
    print(city2)
else:
    print(city3)
