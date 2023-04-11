from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Копиравание данных из файла {from_file} в файл {to_file}")

# Можете следующие две строки кода разместить в одну?
in_file = open(from_file, encoding="utf-8")
indata = in_file.read()

print(f"Исходный файл имеет размер {len(indata)} байт")

text = f"""
Целый файл существует? {exists(to_file)}
Готов, нажмите клавишу Enter для продолжения или CTRL+C для отмены.
"""
input(':>> ')

print("Начинаем копирование...")
out_file = open(to_file, 'w')
out_file.write(indata)
print("Копиравание завершено.")
print("Отлично, все сделано.")

out_file.close()
in_file.close()
