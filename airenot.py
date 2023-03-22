from sys import argv

name_script, script = argv
vod = ":>>"
text = f"""
Здравствутйе, меня зовут {script}.
И я модель {name_script}.
Сегодня я буду выпонлять ваши коммандый.
Вы должный записать четыре комманд.
Готовый? Тогда ПОЕХАЛИ!
"""
print(text)
print("Введите первый комманд")
com1 = input(vod)
print("Введите второй комманд")
com2 = input(vod)
print("Введите трейти комманд")
com3 = input(vod)
print('Введите четвертый комманд')
com4 = input(vod)

prontent = f'''
И так вы хотите:
{com1},
{com2},
{com3},
{com4}.
Выполним скоро времений, а пока до свиданий.
'''
print(prontent)
