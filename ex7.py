﻿# 1, 5 и 6 просто выводим текст, нечего особеного 
print("У мэри был маленький барашек.")
# Выводим сообщения в конце добавлаем слово "снег" функций .format()
print("Его шерсть была белой как {}.".format("снег"))
print("И всюду, куда Мэри шла,")
print("Маленкий барашек всегда следовал за ней.")
# Выводим точки умножаем на 10, результат: ..........
print("." * 10)
# Создаю переменый end1-8 по одной буквы
end1 = "Б"
end2 = "а"
end3 = "д"
end4 = "д"
end5 = "и"
end6 = "Г"
end7 = "а"
end8 = "й"
# Выводим Результат в конце функций end делаем пробел, не убираете запятою выводит ошибка SystamError
# Результат: Бадди Гай
print(end1 + end2 + end3 + end4 + end5, end=' ')
print(end6 + end7 + end8)