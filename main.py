from time import sleep


def read_file(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        for i in file:
            a = i.split()
    if 'ошибка' in a:
        print('Ошибка')
        sleep(2)
        exit()
    if 'функция' in a:
        with open(r'D:\Python\xak_24.11.22\py\test.py', 'w', encoding='UTF-8') as test:
            if '+' in a or 'плюс' in a:
                test.write(f'def I0():\n')
                test.write(f'    print({a[1]} + {a[3]})')
                test.write('\n')
                test.write(f'I0()')

            elif 'сумма' in a:
                test.write(f'def I0():\n')
                test.write(f'    print({a[2]} + {a[3]})')
                test.write('\n')
                test.write(f'I0()')

            elif '-' in a or 'минус' in a:
                test.write(f'def I0():\n')
                test.write(f'    print({a[1]} - {a[3]})')
                test.write('\n')
                test.write(f'I0()')

            elif 'разность' in a:
                test.write(f'def I0():\n')
                test.write(f'    print({a[2]} - {a[3]})')
                test.write('\n')
                test.write(f'I0()')

            elif 'поделить' == a[1] or 'разделить' == a[1] or 'делить' == a[1]:
                test.write(f'def I0():\n')
                test.write(f'    print({a[2]} / {a[4]})')
                test.write('\n')
                test.write(f'I0()')

            elif '/' in a:
                test.write(f'def I0():\n')
                test.write(f'    print({a[1]} / {a[3]})')
                test.write('\n')
                test.write(f'I0()')

            elif 'поделить' in a or 'разделить' in a or 'делить' in a:
                test.write(f'def I0():\n')
                test.write(f'    print({a[1]} / {a[4]})')
                test.write('\n')
                test.write(f'I0()')

            elif 'умножить' == a[1]:
                test.write(f'def I0():\n')
                test.write(f'    print({a[2]} * {a[4]})')
                test.write('\n')
                test.write(f'I0()')

            elif '*' in a:
                test.write(f'def I0():\n')
                test.write(f'    print({a[1]} * {a[3]})')
                test.write('\n')
                test.write(f'I0()')

            elif 'умножить' in a:
                test.write(f'def I0():\n')
                test.write(f'    print({a[1]} * {a[4]})')
                test.write('\n')
                test.write(f'I0()')

            elif 'x' == a[2] or 'х' == a[2] or 'X' in a or 'Х' in a:
                test.write(f'def I0():\n')
                test.write(f'    print({a[1]} * {a[3]})')
                test.write('\n')
                test.write(f'I0()')

            elif 'квадрате' in a:
                test.write(f'def I0():\n')
                test.write(f'    print({a[1]} ** 2)')
                test.write('\n')
                test.write(f'I0()')

            elif 'степени' in a:
                test.write(f'def I0():\n')
                test.write(f'    print({a[1]} ** {a[4]})')
                test.write('\n')
                test.write(f'I0()')

            elif 'корень' in a and 'из' in a:
                test.write(f'import math')
                test.write('\n')
                test.write(f'def I0():\n')
                test.write(f'    print(math.sqrt({a[3]}))')
                test.write('\n')
                test.write(f'I0()')

            elif 'корень' in a:
                test.write(f'import math')
                test.write('\n')
                test.write(f'def I0():\n')
                test.write(f'    print(math.sqrt({a[2]}))')
                test.write('\n')
                test.write(f'I0()')

    elif 'вывести' in a or 'посчитать' in a or 'вычислить' in a or 'посчитай' in a or \
            'вычисли' in a or 'выведи' in a or 'рассчитай' in a or 'рассчитать' in a:
        with open(r'D:\Python\xak_24.11.22\py\test.py', 'w', encoding='UTF-8') as test:
            if '+' in a or 'плюс' in a:
                test.write(f'print({a[1]} + {a[3]})')
                test.write('\n')

            elif 'сумма' in a:
                test.write(f'print({a[2]} + {a[3]})')
                test.write('\n')

            elif '-' in a or 'минус' in a:
                test.write(f'print({a[1]} - {a[3]})')
                test.write('\n')

            elif 'разность' in a:
                test.write(f'print({a[2]} - {a[3]})')
                test.write('\n')

            elif 'поделить' == a[1] or 'разделить' == a[1] or 'делить' == a[1]:
                test.write(f'print({a[2]} / {a[4]})')
                test.write('\n')

            elif '/' in a:
                test.write(f'print({a[1]} / {a[3]})')
                test.write('\n')

            elif 'поделить' in a or 'разделить' in a or 'делить' in a:
                test.write(f'print({a[1]} / {a[4]})')
                test.write('\n')

            elif 'умножить' == a[1]:
                test.write(f'print({a[2]} * {a[4]})')
                test.write('\n')

            elif '*' in a:
                test.write(f'print({a[1]} * {a[3]})')
                test.write('\n')

            elif 'умножить' in a:
                test.write(f'print({a[1]} * {a[4]})')
                test.write('\n')

            elif 'x' == a[2] or 'х' == a[2] or 'X' in a or 'Х' in a:
                test.write(f'print({a[1]} * {a[3]})')
                test.write('\n')

            elif 'квадрате' in a:
                test.write(f'print({a[1]} ** 2)')
                test.write('\n')

            elif 'степени' in a:
                test.write(f'print({a[1]} ** {a[4]})')
                test.write('\n')

            elif 'корень' in a:
                test.write(f'import math')
                test.write('\n')
                test.write(f'print(math.sqrt({a[3]}))')
                test.write('\n')


def main():
    read_file(r'D:\Python\xak_24.11.22\message.txt')


if __name__ == '__main__':
    main()
