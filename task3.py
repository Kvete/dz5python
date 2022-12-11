"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет
оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
my_f = open('file3.txt', 'r', encoding='utf8')
content = my_f.readlines()
my_f.close()
print(content)
salary = []
surname = []
for el in content:
    surname.append(el[:el.find(' ')])
    salary.append(float(el[el.find(' ') + 1:el.find('\n')]))
print(salary)
print(surname)
sum = 0
for i in range(len(salary)):
    sum += salary[i]
    if salary[i] < 20000:
        print(f'{surname[i]} зарабатывает {salary[i]}')
print(f'average={sum / len(salary)}')
