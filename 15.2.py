# 15.2 Числовая угадайка
# сравнение введенного числа с загаданным числом

from random import *


def is_valid(str_input):
    return str_input.isdigit() and 1 <= int(str_input) <= 100


def is_valid_num():
    while True:
        num_inout = input()
        if is_valid(num_inout):
            return int(num_inout)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')


def compare_num():
    while True:
        n = is_valid_num()
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            break


num = randint(1, 100)

print('Добро пожаловать в числовую угадайку')
print('Введите число от 1 до 100: ')
compare_num()
