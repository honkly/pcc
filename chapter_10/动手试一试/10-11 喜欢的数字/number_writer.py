import json

number = input("Please input number that your favorite!")

filename = 'numbers.json'

with open(filename, 'w') as file_object:
    json.dump(number, file_object)
