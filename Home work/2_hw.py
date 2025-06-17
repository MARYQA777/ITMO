def task_1() -> None:
    # Создаем переменные разных типов
    number_int: int = 42
    number_float: float = 3.14
    text_str: str = "Жизнь прекрасна"
    my_list: list = [1, 2,"три", 4, 5.0]
    is_true: bool = True

    # Выводим типы данных
    print(f"Тип number_int: {type(number_int)}")
    print(f"Тип number_float: {type(number_float)}")
    print(f"Тип text_str: {type(text_str)}")
    print(f"Тип my_list: {type(my_list)}")
    print(f"Тип is_true: {type(is_true)}")

    # Вызываем функцию
    task_1()


def task_2() -> None:
    # Создаем список
    a = [1, 2, 3, 5, 8, 13, 21]

    # Выводим первые 3 значения
    print(a[:3])


# Вызываем функцию
task_2()


def task_3(number: float) -> float:
    """
    Функция возводит число в квадрат

    :param number: число для возведения в квадрат
    :type number: float
    :return: квадрат числа
    :rtype: float
    """
    return number ** 2


# Вызов функции с выводом результата
result = task_3(5)
print(f"Квадрат числа равен: {result}")
