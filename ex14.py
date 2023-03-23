from sys import argv
import time
script, user_name, user_famile, first, second = argv
prompt = ':>> '
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(f"Привет, {user_name} {user_famile}, {first} я - сценарий {script}.")
print(f"Сейчас время {current_time}")
print("Я хочу задать тебе несколько  вопросов.")
print(f"Я тебе наврлюсь, {user_name}?")
likes = input(prompt)

print(f"Где ты живешь, {user_name}?")
lives = input(prompt)

print("На каком компьютере ты работаешь?")
computer = input(prompt)

print(f"""
Итак, ты ответил {likes} на вопрос, наврлюсь ли тебе.
Ты живешь {lives}. Не представлю, где это.
Ты {first} раз запуcкал этот код.
И у тебя есть компьютер {computer}. Прекрасно!
Не правди секунд {second}.
""")
