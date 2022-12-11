"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
и выводить ее на экран.
"""
my_sum = 0
my_f = open('file5.txt', 'w', encoding='utf-8')
elements = [5, 3, 7, 9, 1, 2, 13]
for el in elements:
    my_f.write(str(el) + ' ')
my_f.close()
my_f2 = open('file5.txt', 'r', encoding='utf-8')
content = my_f2.readlines()
my_f2.close()
print(content[0])
elements_input = content[0].split()
for el in elements_input:
    my_sum += int(el)
print(my_sum)
