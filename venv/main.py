#import random
#from random import randint
# Тут я создавал симуляцию БД ID клиентов
from collections import Counter
#i = 0
#a = []
#b = 0
#while i < 101:
#    b = randint(1000,10000000)
#    a.append(b)
#    b = 0
#    i += 1
#with open("db.txt","w") as out:
#   for i in a:
#      print(i,file=out)


def nol(a): #первая функция для ID с 0
    sum = 0

    while (a != 0):
        sum = sum + a % 10
        a = a // 10
    group_number_o.append(sum)
    return a

def ne_nol(a):
    sum = 0
    if len(n_first_id) < 1:
        n_first_id.append(a) #насколько я понял надо записать первый ID, который начинается не с 0(но могу ошибаться))
    while (a != 0):
        sum = sum + a % 10
        a = a // 10
    group_number.append(sum)

    return a

id_client = []
group_number_o = []
group_number = []
n_first_id = []

data_id = open("db.txt", "r") #пробегаем по файлу
for line in data_id:
    id_client.append(line.strip())
for n_customers in id_client:
    first =  int(str(n_customers)[0])
    if len(str(n_customers)) > 7 or len(str(n_customers)) < 5: # проверка на правильность ID(5-7 символов)
        print("Error!")
    else:
        if first == 0:
            nol(int(n_customers))
        else:
            ne_nol(int(n_customers))

c_1 = Counter(group_number_o)

c_2 = Counter(group_number)
print('''
Для ID с начальным символом 0: 

Номер группы - кол-во клиентов в ней''')
for i in c_1:
    print(str(i) + " - " + str(c_1[i]))


print('''
Для ID с начальным произвольным символом: 
''')

print("Первый такой ID: " + str(n_first_id[0]))

print('''
Номер группы - кол-во клиентов в ней''')
for i in c_2:
    print(str(i) + " - " + str(c_2[i]))