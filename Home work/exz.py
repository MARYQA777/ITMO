import re

# Регулярное выражение
pattern = r'\d{1,2}\s[А-Я][а-я]+\s\d{4}'

# Пример использования
date_string = "12 Августа 2023"
match = re.match(pattern, date_string)

if match:
    print("Дата соответствует формату")
else:
    print("Дата не соответствует формату")