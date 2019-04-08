filename = 'guest_book.txt'

while True:
	name = input("Please input your name:\n")
	print("Hello! " + name)
	with open(filename,'a') as file_object:
		file_object.write(name + '\n')