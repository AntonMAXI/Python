print('Вас приветствует игра "Исключение букв"')
name = input('Введите свое имя :')
age = int(input('Введите свой возраст :'))
male = input('Введите ваш пол :')
name_pet = input('Введите имя своего питомца :')
gamer = bool(input('Любите ли вы играть?  Да/Нет :'))
if age < 18:
    print('Вы еще молодой, для этих игр =D!')
elif age > 90:
    print('Возможно Вас утомит эта игра')
    choice_pl = input('Все равно хотите поиграть? Да/Нет :').upper()
    if choice_pl == 'ДА':
        choice_pl2 = input('Вы уверены? Да/Нет :').upper()
        if choice_pl2 == 'ДА':
            print('Хорошо тогда начнем игру.')
        else:
            print('Пока ' + name)
    elif choice_pl == 'НЕТ':
        print('Пока ' + name)
else:
    print('Привет ' + name)
    print('Я могу назвать буквы алфавита, которых нет в твоем имени :')
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    list_name = list(name)
    i = 0
    while int(i) < len(alphabet):
        for item in list_name:
            if item in alphabet:
                alphabet.remove(item)
                i += 1
            else:
                i += 1
    print('Буквы алфавита, которых нет в твоем имени :')
    print(alphabet)
