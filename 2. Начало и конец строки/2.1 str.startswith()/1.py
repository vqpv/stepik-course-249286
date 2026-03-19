s = input()

vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]

print(s.split("\\\\")[2].lower().startswith(tuple(vowels)))
