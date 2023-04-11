from sys import argv
script, filename = argv
my_file = open(filename, 'w+', encoding="utf-8"); user = input(":>> "); my_file.write(user); print(my_file.read()); my_file.close()
