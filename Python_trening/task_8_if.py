num = 3
if num >= 0:

    print('Число больше либо равно 0')

else:
    print('число отрицательное')


def task_yes_no(str1, str2):
    if str_1 in str_2:
        print('ДА')
        print('НЕТ')


permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print ('Печать запрещена')


def student_rank(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
        print("Вы бакалавр")
    elif year_of_study in pange(5, 7):
        print("Вы магистр")
    elif 7 <= year_of_study in pange <= 9:
        print("Вы аспирант")
    else:
        print("Введите корректный год обучения")

    student_rank (5)


a=5

if a > 100 or a < -100:
    print('+')
else:
    print('-')

























