s = input()

if s.endswith("?"):
    print("Вопросительное предложение")
elif s.endswith("!"):
    print("Восклицательное предложение")
else:
    print("Обычное предложение")
