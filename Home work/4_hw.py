# class Rectangle:
#     def _init_(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# # Создаем три объекта класса Rectangle
# rect1 = Rectangle(4, 5)
# rect2 = Rectangle(2, 7)
# rect3 = Rectangle(6, 3)
#
# # Выводим результаты для каждого прямоугольника
# print(f"Прямоугольник 1: ширина={rect1.width}, высота={rect1.height}")
# print(f"Площадь: {rect1.area()}")
# print(f"Периметр: {rect1.perimeter()}")
#
# print("\nПрямоугольник 2: ширина={rect2.width}, высота={rect2.height}")
# print(f"Площадь: {rect2.area()}"
# print(f"Периметр: {rect2.perimeter()}")
#
# print("\nПрямоугольник 3: ширина={rect3.width}, высота={rect3.height}")
# print(f"Площадь: {rect3.area()}")
# print(f"Периметр: {rect3.perimeter()}")



# class Math:
#     def _init_(self, a, b):
#         self.a = a
#         self.b = b
#
#     def addition(self):
#         print(f"Сложение: {self.a} + {self.b} = {self.a + self.b}")
#
#     def multiplication(self):
#         print(f"Умножение: {self.a} * {self.b} = {self.a * self.b}")
#
#     def division(self):
#         if self.b != 0:
#             print(f"Деление: {self.a} / {self.b} = {self.a / self.b}")
#         else:
#             print("Ошибка: деление на ноль!")
#
#     def subtraction(self):
#         print(f"Вычитание: {self.a} - {self.b} = {self.a - self.b}")
# calculator = Math(10, 5)
# методы
# calculator.addition()
# calculator.multiplication()
# calculator.division()
# calculator.subtraction()

#
# class SidebarButton:
#     def _init_(self, text):
#         self.text = text
#         self.type = 'Кнопка'
#         self.locator = ''
#
#     def click(self):
#         return f'Клик по кнопке {self.text}'
#
#
# # Создаем объекты для кнопок второго уровня
# buttons = [
#     SidebarButton('Text Box'),
#     SidebarButton('Check Box'),
#     SidebarButton('Radio Button'),
#     SidebarButton('Web Tables'),
#     SidebarButton('Buttons'),
#     SidebarButton('Links'),
#     SidebarButton('Broken Links Images'),
#     SidebarButton('Upload and Download'),
#     SidebarButton('Dynamic Properties')
# ]
#
# # Выводим текст каждой кнопки
# print('Тексты кнопок:')
# for button in buttons:
#     print(button.text)
#
# # Вызываем клик для каждой кнопки
# print('\nРезультаты клика по кнопкам:')
# for button in buttons:
#     print(button.click())


class SidebarButton:
    def _init_(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.text}"


# Создаем объекты для кнопок второго уровня
# Теперь мы передаем текст каждой кнопки в конструктор
buttons = [
    SidebarButton("Text Box"),
    SidebarButton("Check Box"),
    SidebarButton("Radio Button"),
    SidebarButton("Web Tables"),
    SidebarButton("Buttons"),
    SidebarButton("Links"),
    SidebarButton("Broken Links Images"),
    SidebarButton("Upload and Download"),
    SidebarButton("Dynamic Properties")
]
# Выводим текст каждой кнопки
print("Тексты кнопок:")
for button in buttons:
    print(button.text)

# Вызываем клик для каждой кнопки
print("\nРезультаты клика по кнопкам:")
for button in buttons:
    print(button.click())










