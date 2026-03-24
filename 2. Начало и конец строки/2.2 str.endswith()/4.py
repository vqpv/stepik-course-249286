s_1 = input()
s_2 = input()

if s_1.lower().endswith(tuple(s_2.split(", "))):
    print("Файл допустимого формата")
else:
    print("Недопустимый формат файла")
