#3) Информация о файле
# Имеется файл file.txt с текстом на латинице.
# Напишите программу, которая выводит следующую статистику по тексту:
# количество букв латинского алфавита;
# число слов;
# число строк.

with open("file.txt", "r") as file:
    count_string = 0
    count_lines = 0
    count_letters = 0
    a = file.readlines()
    for i in a:
        for k in int(a[i]):
            if a[k].isalpha():
                count_letters += 1
    count_string = sum(file.read().split())
    count_lines = len(a)
    print(f"Latin haripler sani {count_letters}")
    print(f"Qatarlar sani {count_lines}")
    print(f"Sozler sani {count_string}")