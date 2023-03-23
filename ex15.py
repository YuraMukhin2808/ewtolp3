from sys import argv
# 1 строки импортируем sys из функций argv и делаем перемен script и filename ложим на argv
script, filename = argv
# Делаем переменую txt и функций open открываем filename или ex15_sample.txt (Правки на автор: перед открытие файла, нужный вести функций кодировка encoding выдилить перемный utf8 чтобы все работал, без него выводит ошибка)
txt = open(filename, encoding="utf8")
# Выводим ex15_sample.txt на экран
print(f"Содержимое файла {filename}")
print(txt.read())
txt.close() # Закрываем файл.
# Через пользутелский ввода выводит тоже файл ex15_sample.txt
print("Снова введите имя файла:")
file_again = input(":>> ")
# СамоПовтор
txt_again = open(file_again, encoding="utf8")

print(txt_again.read())
txt_again.close()
