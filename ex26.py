from sys import argv

print("Сколько вам лет?:>>", end=' ')
age = input()
print("Какого вы роста?:>>", end=' ')
height = input()
print("Сколько вы весите?:>>", end=' ')
weight = input()

print(f"Итак, вам{age} лет, ваш рост - {height} и ваш вес - {weight}.")

script, filename = argv

txt = open(filename, "w+", encoding="utf-8")

print(f"Вот ваш файл {filename}.")
print(txt.read())
txt.close()
print("Снова укажите имя файла:")
file_again = input(":>> ")

n = open(file_again, "w+", encoding="utf-8")

print(n.read())
print('Давайте попрактикуемся!')
print('Вы должны знать об управляющих последовательностях с символом \\, которые \n управляют переносом строк и \t отступами.')
n.close()
poem = """
\tДля счастья
мне совсем немного надо.
Хочу тебя \n я нежно обнимать.
Хочу всегда
я быть с тобою рядом
\tи никогда не отпускать!
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"Здесь должна быть пятерка: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# помните, что это еще один способ форматирования строки
print("Начиная с: {}".format(start_point))
# так же, как со строкой f""
print(f"У нас есть {beans} бобов, {jars} банок и {crates} ящиков.")

start_point = start_point / 10
print(start_point)
