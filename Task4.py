# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


n = int(input('Введите n: '))

if n>4 or n<1: print("Пожалуйста, в диапазоне 1 - 4")
elif n==1: print("X > 0; Y > 0")
elif n==2: print("X < 0; Y > 0")
elif n==3: print("X < 0; Y < 0")
else: print("X > 0; Y < 0")
