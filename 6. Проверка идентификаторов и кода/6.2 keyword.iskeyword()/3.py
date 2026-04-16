import keyword


s = input()

print(keyword.iskeyword(s.lower()) or keyword.iskeyword(s.title()))
