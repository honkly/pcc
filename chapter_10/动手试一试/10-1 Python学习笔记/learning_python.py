print("第一次打印时读取整个文件:")
with open('learning_python.txt') as file_object:
	print(file_object.read())

print("第二次打印时遍历文件对象:")
with open('learning_python.txt') as file_object:
	for line in file_object:
		print(line.strip())

print("第三次打印时将各行存储在一个列表中， 再在with 代码块外打印它们")
with open('learning_python.txt') as file_object:
	words_list = file_object.readlines()

for word in words_list:
	print(word.strip())