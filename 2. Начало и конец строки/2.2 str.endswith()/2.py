s = input()

if s.startswith("https://") and s.endswith((".ru", ".com", ".org")):
    print("Это корректный веб-адрес")
else:
    print("Некорректный адрес")
