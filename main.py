# Задача:
# Написать программу, которая:
# 1. Создает с помощью генератора списков список случайных целых чисел от -50 до 50 размером 25 элементов.
# 2. Находит количество положительных, отрицательных и нулевых элементов в списке.
# 3. Выводит значения и их количество (положительных, отрицательных и нулевых) вместе с процентом от общего количества.
# 4. Выводит самое большое и самое маленькое значение в списке.

import random  # Импортируем модуль random для работы с генерацией случайных чисел
numbers = [random.randint(-50, 50) for _ in range(25)] # Генерируем список из 25 случайных чисел в диапазоне от -50 до 50
positive_count = 0 # Инициализируем счетчики для положительных элементов
negative_count = 0 # Инициализируем счетчики для отрицательных элементов
zero_count = 0 # Инициализируем счетчики для нулевых элементов
for number in numbers: # Проходим по каждому элементу списка
    if number > 0:  # Если число положительное
        positive_count += 1
    elif number < 0:  # Если число отрицательное
        negative_count += 1
    else:  # Если число равно нулю
        zero_count += 1
total_count = len(numbers) # Подсчитываем общее количество элементов
positive_percentage = (positive_count / total_count) * 100 # Вычисляем проценты для положитнльного элемента
negative_percentage = (negative_count / total_count) * 100 # Вычисляем проценты для отрицательного элемента
zero_percentage = (zero_count / total_count) * 100 # Вычисляем проценты для нулевого элемента
max_value = max(numbers) # Находим максимальное значение в списке
min_value = min(numbers) # Находим максимальное значение в списке
print("Список случайных чисел:", numbers) # Выводим сгенерированный список
print(f"Положительных чисел: {positive_count} ({positive_percentage:.2f}%)") # Выводим количество и процентное соотношение положительных чисел
print(f"Отрицательных чисел: {negative_count} ({negative_percentage:.2f}%)") # Выводим количество и процентное соотношение отрицательных чисел
print(f"Нулевых значений: {zero_count} ({zero_percentage:.2f}%)") # Выводим количество и процентное соотношение нулевых чисел
print(f"Самое большое значение в списке: {max_value}") # Выводим максимальное значение в списке
print(f"Самое маленькое значение в списке: {min_value}") # Выводим минимальное значение в списке