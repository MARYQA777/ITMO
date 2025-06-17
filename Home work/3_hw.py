def find_max(num1: float, num2: float) -> None:
    """
    Функция находит и выводит максимальное из двух чисел

    :param num1: первое число
    :param num2: второе число
    :return: None (выводит результат в консоль)
    """
    # Сравниваем числа с помощью условного оператора
    if num1 > num2:
        max_num = num1
    else:
        max_num = num2
print(f'Наибольшее число: {'max_num'}')

find_max(5, 15)

#     # Пример использования функции
#     find_max(7, 5)  # Выведет: Наибольшее число: 7
#     find_max(-1, -3)  # Выведет: Наибольшее число: -1
#
def find_max_simple(num1: float, num2: float) -> None:
        max_num = max(num1, num2)
        print(f"Наибольшее число: {max_num}")
find_max_simple(5, 15)


# def check_difference(num1, num2):
#     # Используем abs() для получения абсолютного значения разности
#     if abs(num1 - num2) == 135:
#         print("yes")
#     else:
#         print("No")
# check_difference(10, 145) # выведет yes

# Пример использования:
# check_difference(200, 65)  # выведет yes
# check_difference(100, 150) # выведет No


#
# def get_season(month):
#     if month in [12, 1, 2]:
#         return "зима"
#     elif month in [3, 4, 5]:
#         return "весна"
#     elif month in [6, 7, 8]:
#         return "лето"
#     elif month in [9, 10, 11]:
#         return "осень"
#     else:
#         return "Некорректный номер месяца"
#
# print(get_season(2))

# print(get_season(5))  # выведет "весна"
# print(get_season(8))  # выведет "лето"
# print(get_season(11)) # выведет "осень"
# print(get_season(13)) # выведет "Некорректный номер месяца"
#
#
#
# def check_numbers(a, b, c):
#         if a > 10 and b > 10 and c > 10:
#             print("yes")
#         else:
#             print("no")
# check_numbers(11, 12, 13)
#
#
# # Пример использования:
# # check_numbers(10, 15, 20) # выведет no
# # check_numbers(5, 15, 20) # выведет no

# def count_positives(numbers):
#     count = 0
#     for num in numbers:
#         if num > 0:
#             count += 1
#     return count
#
# print(count_positives([1, -2, 3, -4, 5]))


# def count_positives_filter(numbers):
#     return len(list(filter(lambda x: x > 0, numbers)))
#
# print(count_positives_filter([1, -2, 3, -4, 5]))


def count_positives_generator(numbers):
    return sum(1 for num in numbers if num > 0)

print(count_positives_generator([1, -2, 3, -4, 5]))




































