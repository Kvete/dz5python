"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем.Об окончании ввода данных свидетельствует пустая строка.
"""
my_f = open('file1.txt', 'w', encoding='utf8')
while True:
    input_str = input('give me str ')
    if input_str != '':
        my_f.write(input_str + "\n")
    else:
        break
my_f.close()
