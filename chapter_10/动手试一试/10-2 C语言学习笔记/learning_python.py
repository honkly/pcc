words = "I really like dogs"
print(words.replace('dog', 'cat'))

with open('learning_python.txt') as file_object:
	message = file_object.read()
	message = message.replace('Python', 'C++')
	print(message)