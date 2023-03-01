#4) Запрещенные слова
# Напишите программу, которая получает на вход строку
# с названием текстового файла, и выводит на экран содержимое
# этого файла, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове).
# Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt.
# Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова,
# где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра:
# если файл forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
# Формат ввода
# Строка текста с именем существующего текстового файла, в котором необходимо заменить запрещенные слова звездочками.

file1 = open("file.txt", "r").read().split()
file2 = open("forbidden_words.txt", "r").read().split()
for i in file1:
    if i in file2:
        file1.insert(i.index(), "*"*len(i))
print(file1)