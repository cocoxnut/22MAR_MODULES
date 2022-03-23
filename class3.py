names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
group1 = []
from random import choice as ch
for i in names:
    i = ch(names)
    if len(group1) <= int(len(names) / 4):
        group1.append(i)
print(group1)

