import math
num_1 = input("Введите число:")
print(type(num_1))
max = 0
i = 0
while i < len(num_1):
    if str(max) < num_1[i]:
        max = num_1[i]
        i+=1
    else:
        i+=1
print("Максимальная цифра в числе", max)


num_1 = input("Введите первое число")
num_2 = input("Введите второе число")
num_1, num_2 = num_2, num_1
print("Число один равно:", num_1)
print("Число два равно:", num_2)


print("Напишите программу, вычисляющую корни квадратного уравнения вида \n 4ax² + bx + c = 0.")
print("Решение:")
a = int(input("Введите значение a"))
b = int(input("Введите значение b"))
c = int(input("Введите значение c"))
print("Находим дискриминант по формуле d = b**2 - 4ac :")
d = b**2 - 4 * a * c
print(d)
if d > 0:
    print("d > 0, корней будет два")
    print("Находим корни квадратного уравнения:")
    print("Найдем x1 = (-b + math.sqrt(d))/ 2 * a:")
    x1 = (-b + math.sqrt(d))/ 2 * a
    print("x1 =",x1)
    print("Найдем x2 = (-b - math.sqrt(d))/ 2 * a:")
    x2 = (-b - math.sqrt(d)) / 2 * a
    print("x2 =",x2)
elif d < 0:
    print("d < 0, корней нет")
else:
    print("d = 0, есть ровно один корень")
    print("Находим корень квадратного уравнения:")
    print("Найдем x1 = (-b + math.sqrt(d))/ 2 * a:")
    x1 = (-b + math.sqrt(d))/ 2 * a
    print("x1 =",x1)






