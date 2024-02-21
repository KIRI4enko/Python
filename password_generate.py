'''
Генератор пароля
Password generate
'''


def generate_password(len):
    from random import choice
    az = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    az += [i.upper() for i in az] + [str(a) for a in range(10)]
    return ''.join([choice(az) for _ in range(len)])


print(generate_password(int(input('Введите длину пароля: '))))
