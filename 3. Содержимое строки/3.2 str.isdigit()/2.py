s = input()

if s.isdigit() or (s.startswith(("+", "-")) and s[1:].isdigit()):
    print(int(s) * -1)
else:
    print("Строка не является целым числом")
