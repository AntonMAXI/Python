x = 15
y = 0
while y < x:
    print(y)
    y+=1
for l in range(x) :
    print(l)

num_1 = input("Введите первое число")
num_2 = input("Введите второе число")
num_dop = num_2
num_2 = num_1
num_1 = num_dop
print(num_1)
print(num_2)

age = input("Укажите ваш возраст")
if int(age) > 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
