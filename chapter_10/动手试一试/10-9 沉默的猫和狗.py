try:
	with open('cats.txt') as file_object:
		cat_list = file_object.readlines()
	with open('dogs.txt') as file_object:
		dog_list = file_object.readlines()

except FileNotFoundError:
	pass

else:
	for cat in cat_list:
		print(cat.strip())

	for dog in dog_list:
		print(dog.strip())

