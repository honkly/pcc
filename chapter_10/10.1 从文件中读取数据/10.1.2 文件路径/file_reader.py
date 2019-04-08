#with open('C:/Users/knight.li/Desktop/Coding/pcc/chapter_10/10.1 从文件中读取数据/10.1.2 文件路径/text_files/pi_digits.txt') as file_object:
with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
