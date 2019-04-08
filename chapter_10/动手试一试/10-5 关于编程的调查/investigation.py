filename = 'reasons.txt'

while True:
	name = input("Why do you like programming?\n")
	with open(filename,'a') as file_object:
		file_object.write(name + '\n')