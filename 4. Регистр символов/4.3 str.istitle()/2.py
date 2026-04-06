s = input()

print(s.startswith(("ООО ", "ИП ")) and s[s.find(" "):].istitle())
