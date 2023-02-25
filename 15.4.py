# 15.4 Генератор безопасных паролей

from random import shuffle

digits = '0123456789'
lowers = 'abcdefghijklmnopqrstuvwxyz'
uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '#$%&*+-=?@^_'
chars = ''


# проверка на натуральное число
def check_int(value):
    while not value.isdigit():
        value = input('Необходимо ввести целое число: ')
    return int(value)


# проверка на да/нет
def check_yn(value):
    while value not in ('ynдн'):
        value = input('Если да - введите y или д, если нет - введите n или н: ')
    return True if value in ('yд') else False


# ввод
amount = check_int(input('Введите количество паролей для генерации: '))
length = check_int(input('Введите длину пароля: '))
digit = check_yn(input('Включать ли цифры 0123456789? (д/н): '))
upper = check_yn(input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (д/н): '))
lower = check_yn(input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (д/н): '))
symbol = check_yn(input('Включать ли символы !#$%&*+-=?@^_? (д/н): '))
similar_symbols = check_yn(input('Исключать ли неоднозначные символы il1Lo0O? (д/н): '))

# формирование строки с символами, из которых будет собран пароль
chars += digits if digit else ''
chars += uppers if upper else ''
chars += lowers if lower else ''
chars += symbols if symbol else ''
if similar_symbols:
    chars = [i for i in chars if i not in 'il1Lo0O']
else:
    chars = list(chars)

# генерация паролей с помощью shuffle
for _ in range(amount):
    shuffle(chars)
    print(''.join(chars[:length]))
