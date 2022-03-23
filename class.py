list_names = ['Asel', 'Adilet', 'Ilyas', 'Danislan']
command1 = []
command2 = []
from random import choice as ch
'''for x  in range(len(list_names)):
	if x <= 2:
		print(command1.append(ch(x))
	if x > 2:
		print(command2.append(ch(x))
'''
for name in list_names:
	name = ch(list_names)
	if len(command1) <= int(len(list_names) / 2):
		command1.append(name)
		list_names.remove(name)
	else:
		command2.append(name)
		list_names.remove(name)
print(command1)
print(command2)
print(list_names)
