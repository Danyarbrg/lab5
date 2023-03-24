from random import randint
def str():
    print('--------------------------------------------------------------------------------')


#1
lst = [randint(0,15) for i in range(10)]
number = int(input('Введите число на проверку: '))
if number in lst:
    print('Поздравляю, вы угадали число!', '\n', lst)
else:
    print('Нет такого числа :( ', '\n', lst)
str()


#2
set_lst = []
for i in lst:
    count = 0
    for j in lst:
        if i == j:
            count += 1
            if count >= 2:
                set_lst.append(i)
print(set(set_lst))
str()

#3
days = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
num = int(input('Сколько выходных вы хотите? '))

counter = 0
days_off = []
for i in range(num):
    counter -= 1
    days_off.append(days[counter])
print('Ваши выходные дни: ',  days_off[::-1])

work_days = []
for i in range(7 - num):
    work_days.append(days[i])
print('Ваши рабочие дни: ', work_days)
str()


#4
stud_1 = ['Черный', 'Белый', 'Красный', 'Синий', 'Оранжевый', 'Фиолетовый', 'Зеленый', 'Желтый', 'Коричневый', 'Голубой']
stud_2 = ['Иванов', 'Сидоров', 'Федорков', 'Бляхов', 'Кузнецов', 'Молодцов', 'Холодцов', 'Зинченко', 'Вафелькин', 'Госдумов']
stud_3 = []

quant_stud = []
while True:
    if len(quant_stud) == 5: break
    i = randint(0,9)
    if i not in quant_stud:
        quant_stud.append(i)

stud_3 = [stud_1[i] for i in quant_stud] + [stud_2[i] for i in quant_stud]

count_ivanov = 0
for i in stud_3:
    if i == 'Иванов':
        count_ivanov += 1

print(f'Исходные две группы:\n {stud_1}\n{stud_2}\nНовая группа по алфавиту:\n{sorted(stud_3)}\nКолличество детей в новой группе: {len(stud_3)}')
if 'Иванов' in stud_3:
    print(f'Иванов встречается {count_ivanov} раз')
else:
    print('Иванова нет в новой группе')