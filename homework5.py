#1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.

with open('test1.txt', 'w', encoding = 'utf-8') as file1:
  data = 0
  while data != '':
    data = input('Введите строку с данными (для завершения оставьте строку пустой): ')
    print(data, file = file1)



#2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open('test2.txt', 'r', encoding = 'utf-8') as file2:
  data = file2.readlines()
  for i, line in enumerate(data, 1):
    word = len(line.split())
    print(f'{i}ая строка содержит {word} слов(а)')


#3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.

#Пример файла:
#Иванов 23543.12
#Петров 13749.32

total_zp = 0
num_worker = 0

with open('test3.txt', 'r', encoding = 'utf-8') as file3:
  for line in file3:
    zp = int(line.split()[1])
    worker = line.split()[0]
    total_zp = total_zp + zp
    num_worker = num_worker + 1
    if zp < 20000:
      print(worker)

average_zp = total_zp / num_worker
print(average_zp)   



#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.



sl = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('test4_new.txt', 'w', encoding = 'utf-8') as file4_new:
  with open('test4.txt', 'r', encoding = 'utf-8') as file4:
    for line in file4:
      file4_new.writelines([line.replace(line.split()[0], sl[line.split()[0]])])
  



#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

with open('test5.txt', 'w', encoding = 'utf-8') as file5:
  num = [randint(1, 25) for _ in range(50)]
  file5.write(' '.join(map(str, num)))

print('Сумма чисел: ', sum(num))
