print('Я могу назвать буквы алфавита, которых нет в твоем имени :')
alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
print(alphabet)
name = input('Введите свое имя :')
list_name = list(name)
print(list_name)
i = 0
while int(i) < len(alphabet):
    for item in list_name:
        if item in alphabet:
            alphabet.remove(item)
            i += 1
        else:
            i += 1

print(i)
print(alphabet, end=' ')