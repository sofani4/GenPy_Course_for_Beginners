# алгоритмом Цезаря для en и ru с проверками на ввод числа

chars_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def check_int_1and2(value):
    while not value.isdigit() or not (int(value) == 1 or int(value) == 2):
        value = input('Необходимо ввести число 1 или 2: ')
    return int(value)


def check_int(value):
    while not value.isdigit():
        value = input('Необходимо ввести натуральное число: ')
    return int(value)


cipher = check_int_1and2(input('Что необходимо сделать? шифровать == 1, дешифровать == 2: '))
lang = check_int_1and2(input('Какой язык? английский == 1, русский == 2: '))
step = check_int(input('Укажите шаг сдвига (целое число): '))
text = input('Введите текст: ')


# Определяем шаг для шифрования/дешифрования
if cipher == 2: step *= -1
# Определяем язык
alphabet = chars_en if lang == 1 else chars_ru

# Шифруем
for i in text:
    if i.upper() in alphabet:
        tmp = alphabet[(alphabet.find(i.upper()) + step) % len(alphabet)]
        print(tmp.lower() if i.islower() else tmp, end='')
    else:
        print(i, end='')
