s = input()

if s.isalnum() and len(s) >= 8 and not (s.lower().startswith(("qwerty", "123")) or s.lower().endswith(("890", "word"))):
    print("Пароль принят")
else:
    print("Пароль не принят")
