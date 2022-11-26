from time import sleep


# JavaScript
def read_file(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        for i in file:
            a = i.split()
    if 'ошибка' in a:
        print('Ошибка')
        sleep(2)
        exit()
    if 'функция' in a:
        with open(r'D:\Python\xak_24.11.22\js\test.js', 'w', encoding='UTF-8') as test:
            if '+' in a or 'плюс' in a:
                test.write(f'function I0({a[1]}, {a[3]})\n')
                test.write('{\n')
                test.write(f'   console.log({a[1]} + {a[3]});')
                test.write('\n}\n')
                
            elif 'сумма' in a:
                test.write(f'function I0({a[2]}, {a[3]})\n')
                test.write('{\n')
                test.write(f'   console.log({a[2]} + {a[3]});')
                test.write('\n}\n')
                
            elif '-' in a or 'минус' in a:
                test.write(f'function I0({a[1]}, {a[3]})\n')
                test.write('{\n')
                test.write(f'   console.log({a[1]} - {a[3]});')
                test.write('\n}\n')
                
            elif 'разность' in a:
                test.write(f'function I0({a[2]}, {a[3]})\n')
                test.write('{\n')
                test.write(f'   console.log({a[2]} - {a[3]});')
                test.write('\n}\n')
                
            elif 'поделить' == a[1] or 'разделить' == a[1] or 'делить' == a[1]:
                test.write(f'function I0({a[2]}, {a[4]})\n')
                test.write('{\n')
                test.write(f'   console.log({a[2]} / {a[4]});')
                test.write('\n}\n')
                
            elif '/' in a:
                test.write(f'function I0({a[1]}, {a[3]})\n')
                test.write('{\n')
                test.write(f'   console.log({a[1]} / {a[3]});')
                test.write('\n}\n')
                
            elif 'поделить' in a or 'разделить' in a or 'делить' in a:
                test.write(f'function I0({a[1]}, {a[4]})\n')
                test.write('{\n')
                test.write(f'   console.log({a[1]} / {a[4]});')
                test.write('\n}\n')
                
            elif 'умножить' == a[1]:
                test.write(f'function I0({a[2]}, {a[4]})\n')
                test.write('{\n')
                test.write(f'   console.log({a[2]} * {a[4]});')
                test.write('\n}\n')
                
            elif '*' in a:
                test.write(f'function I0({a[1]}, {a[3]})\n')
                test.write('{\n')
                test.write(f'   console.log({a[1]} * {a[3]});')
                test.write('\n}\n')
                
            elif 'умножить' in a:
                test.write(f'function I0({a[1]}, {a[4]})\n')
                test.write('{\n')
                test.write(f'   console.log({a[1]} * {a[4]});')
                test.write('\n}\n')
                
            elif 'x' == a[2] or 'х' == a[2]:
                test.write(f'function I0({a[1]}, {a[3]})\n')
                test.write('{\n')
                test.write(f'   console.log({a[1]} * {a[3]});')
                test.write('\n}\n')
                
            elif 'степени' in a:
                test.write(f'function I0({a[1]}, {a[4]})\n')
                test.write('{\n')
                test.write(f'    console.log(Math.pow({a[1]},{a[4]}))')
                test.write('\n}\n')
                
            elif 'корень' in a and 'из' in a:
                test.write(f'function I0({a[3]})\n')
                test.write('{\n')
                test.write(f'    console.log(Math.sqrt({a[3]}))')
                test.write('\n}\n')
                
            elif 'корень' in a:
                test.write(f'function I0({a[2]})\n')
                test.write('{\n')
                test.write(f'    console.log(Math.sqrt({a[2]}))')
                test.write('\n}\n')
                
    elif 'вывести' in a or 'посчитать' in a or 'вычислить' in a or 'посчитай' in a or \
             'вычисли' in a or 'выведи' in a or 'рассчитай' in a or 'рассчитать' in a:
        with open(r'D:\Python\xak_24.11.22\js\test.js', 'w', encoding='UTF-8') as test:
            if '+' in a or 'плюс' in a:
                test.write(f'console.log({a[1]} + {a[3]});')
                
            elif 'сумма' in a:
                test.write(f'console.log({a[2]} + {a[3]});')
                
            elif '-' in a or 'минус' in a:
                test.write(f'console.log({a[1]} - {a[3]});')
                
            elif 'разность' in a:
                test.write(f'console.log({a[2]} - {a[3]});')
                
            elif 'поделить' == a[1] or 'разделить' == a[1] or 'делить' == a[1]:
                test.write(f'console.log({a[2]} / {a[4]});')
                
            elif '/' in a:
                test.write(f'console.log({a[1]} / {a[3]});')
                
            elif 'поделить' in a or 'разделить' in a or 'делить' in a:
                test.write(f'console.log({a[1]} / {a[4]});')
                
            elif 'умножить' == a[1]:
                test.write(f'console.log({a[2]} * {a[4]});')
                
            elif '*' in a:
                test.write(f'console.log({a[1]} * {a[3]});')
                
            elif 'умножить' in a:
                test.write(f'console.log({a[1]} * {a[4]});')
                
            elif 'x' == a[2] or 'х' == a[2]:
                test.write(f'console.log({a[1]} * {a[3]});')
                
            elif 'степени' in a:
                test.write(f'console.log(Math.pow({a[1]},{a[4]}))')
                
            elif 'корень' in a and 'из' in a:
                test.write(f'console.log(Math.sqrt({a[3]}))')
                
            elif 'корень' in a:
                test.write(f'console.log(Math.sqrt({a[2]}))')
                


def main():
    read_file(r'D:\Python\xak_24.11.22\message.txt')


if __name__ == '__main__':
    main()
