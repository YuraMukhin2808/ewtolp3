# Создаюм переменый formatter строкой четырек фигурный скобки 
formatter = "{} {} {} {}"
# Все выводы водится переменый с формативный функций format: 4) Целый число, 5) Строка, 6) Логическая тип, 7) Показ повтор 4 раз в одной строкой, 8) Стих виде списка (но все равно виде одной строкой).
print(formatter.format(1, 2, 3, 4))
print(formatter.format("раз", "два", "три", "четыре"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Спят в конюше пони,",
    "начал пес дремать",
    "только мальчик Джонни",
    "не ложится спать!"
))
