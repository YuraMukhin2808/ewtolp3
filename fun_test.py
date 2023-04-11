print("Привет! Давайте сложим и умножим треоуголник!")
def trilog_s(a, b, c):
    s = a + b + c
    return s

def trilog_p(a, b, c):
    p = a * b * c
    return p

v = trilog_s(
        int(input("Введите Первый Число:>> ")),
        int(input("Введите Второй Число:>> ")),
        int(input("Введите Трейти Число:>> "))
        )
d = trilog_p(
        int(input("Введите Первый Число:>> ")),
        int(input("Введите Второй Число:>> ")),
        int(input("Введите Трейти Число:>> "))
        )

print(f"Ответ: S: {v}, P: {d}")
