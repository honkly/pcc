try:
	with open('alice.txt') as file_object:
		alice_text = file_object.read()

except FileNotFoundError:
	print("File not found!")

else:
	print(alice_text.lower().count('the'))

