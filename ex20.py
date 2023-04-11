from sys import argv
# Импортураем sys с функций argv и делаем перемену имя скрипта (script) и имя файла (input_file) 
script, input_file = argv
# Первая функций читает файл
def print_all(f):
    print(f.read())
# Вторая функций проматовает на начальный строкой
def rewind(f):
    f.seek(0)
# Трейти функций читает по одной строку
def print_a_line(line_count, f):
    print(line_count, f.readline())
# Открываем существующий файл
current_file = open(input_file, encoding='utf-8')
# Первый Вывод print_all
print("Первый делом выведем этот файл целиком:\n")

print_all(current_file)
# Второй Вывод rewind
print("Теперь отмотаем назад, словоно это кассета")

rewind(current_file)
# Трейти Вывод print_a_line, при этом перемена current_line плюсоем ради того чтобы файл мог читать по одному строку
print("Выведем три строки:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
