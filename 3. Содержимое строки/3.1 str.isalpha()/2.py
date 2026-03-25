s = input()

if s.startswith("/"):
    if s[1:].isalpha():
        print("Команда принята:", s[1:])
    else:
        print("Ошибка: недопустимая команда")
else:
    print("Обычное сообщение")
