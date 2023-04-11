# Создаем основной функции две переменые 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"У нас есть {cheese_count}, сырков!")
    print(f"У нас есть {boxes_of_crackers} пачек чипсов!")
    print("Этого достаточно для вечеринки!")
    print("Погнали!\n")
# Вывод Первый: присваем две числа 
print("Мы можем непорсредственно передать числа функции:")
cheese_and_crackers(20, 30)


# Создаем переменые с числам
print("Или, мы можем использовать переменые из нашего сценария:")
amount_of_cheese = 10
amount_of_crackers = 50
# Вывод Второй: вывод с созданым переменый
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Вывод Третий: сложения двух чисел на функции
print("Мы даже можем выполнять вычисления внутри функции:")
cheese_and_crackers(10 + 20, 5 + 6)

# Вывод Четвертый: вывод перемен и сложения числа
print("И обЪединять переменые вычисления внутри функции:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
