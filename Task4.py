# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def kordinants(x, y):
    for i in range(1):
            if s1 < 1 or s1 > 4:
                print('Такой плоскости нет')
    for i in range(10):
            if s1 == 1:
                print(f'x = {i}', end = ', ')
                print(f'y = {i}', end = '\n')
            elif s1 == 2:
                print(f'x = {i}', end = ', ')
                print(f'y = {-i}', end = '\n')
            elif s1 == 3:
                print(f'x = {-i}', end = ', ')
                print(f'y = {-i}', end = '\n')
            elif s1 == 4:
                print(f'x = {-i}', end = ', ')
                print(f'y = {i}', end = '\n')

s1 = int(input("Введите номер поскости: \n № = "))
x = 0; y = 0
kordinants(x, y)