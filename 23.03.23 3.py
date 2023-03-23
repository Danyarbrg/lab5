std_dict = dict.fromkeys(['Иванов', 'Сидоров', 'Семенов', 'Черный', 'Белый'])
lng_dict = dict.fromkeys(['Английский', 'Китайский', 'Французский', 'Русский'])
final_dict = dict.fromkeys(['Иванов', 'Сидоров', 'Семенов', 'Черный', 'Белый'])

from random import randint

count = 0
for i in lng_dict:
    count += 1
    key, value = i, count
    lng_dict.update({key: value})
print(lng_dict)


for i in std_dict:
    str_num = ''
    lst = []
    quan = randint(1,4)
    print(i, 'знает ', quan, 'язык/a/ов')
    while True:
        if len(set(lst)) == quan: break
        num = randint(1,4)
        lst.append(num)
        str_num += str(num)
        final_dict.update({i: set(lst)})

print(final_dict)


for key, val in final_dict.items():
    if 2 in val:
        print(key)




