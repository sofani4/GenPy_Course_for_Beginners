# 14.1.4 Звездный треугольник 🌶️
# вывести равнобедренный треугольник с основанием == 15 и высотой == 8

def draw_triangle():
    space = 7
    for i in range(1, 16, 2):
        print(' ' * space + '*' * i)
        space -= 1
# Тестирование
# draw_triangle()


# 14.1.7 Число словами 🌶️
def number_to_words(n):
    dig = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    dec = ['',  'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
           'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    teen = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
            'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    x = ''
    if 10 < n < 20:
        x += teen[n % 10]
    else:
        x += dec[n // 10] + ' ' + dig[n % 10]
    return x.lstrip()
# Тестирование
# print(number_to_words(7))
# print(number_to_words(85))

# 14.1.9 Магические даты
# день, умноженный на месяц, равен числу образованному последними двумя цифрами года.
def is_magic(date):
    # return int(date[0:2]) * int(date[3:5]) == int(date[-2:]) # v1
    d, m, g = map(int, date.split('.'))
    return d * m == g % 100
# Тестирование 14.1.9
# print(is_magic('10.06.1960'))
# print(is_magic('11.06.1960'))


# 14.1.10 Панграммы
def is_pangram(text):
    return len(set(text.lower().replace(' ', ''))) == 26
# Тестирование 14.1.10
# print(is_pangram('Jackdaws love my big sphinx of quartz'))
# print(is_pangram('The jay pig fox zebra and my wolves quack'))
# print(is_pangram('Hello world'))
