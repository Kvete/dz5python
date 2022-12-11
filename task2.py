"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
my_f = open('file2.txt', encoding='utf-8')
content = my_f.readlines()
my_f.close()
print(content)
print(f'количество строк={len(content)}')
for el in content:
    if el == '\n' or el == '':
        print(f'количество слов в {content.index(el) + 1} '
              f'строке={0}')
    else:
        print(f'количество слов в {content.index(el) + 1} '
              f'строке={el.count(" ") + 1}')
