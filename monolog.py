from sys import argv

script, filename = argv

text = f'''
У вас есть этот файл под названия {filename}?
Тогда погнали
'''
print(text)

my_file = open(filename, 'w+', encoding='utf-8')

user_text = input('Введите тескт:>> ')

my_file.write(user_text)
my_file.read()
my_file.close()
