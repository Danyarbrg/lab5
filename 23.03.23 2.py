alp = {
    "авеинорст": 1,
    "дклмпу": 2,
    "бгёья": 3,
    "йы": 4,
    "жзхцч": 5,
    "шэю": 8,
    "фщъ": 10
}

word = input("Введите слово: ")
count = 0
for i in word:
    for key, value in alp.items():
        if i in key:
            count += int(value)

print(key, count)

