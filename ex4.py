# Присваем Cаrs на целый число 100
cars = 100
# Присваем Space_In_A_Car с плывающий число 4.0 или целый число 4
space_in_a_car = 4
# Присваем Drivers на целый число 30
drivers = 30
# Присваем Passengers целый число 90
passengers = 90
# Присваем Cars_Not_Driven на Cars и Drivers, 100 - 4 = 96
cars_not_driven = cars - drivers
# Присваем Cars_Driven на Drivers
cars_driven = drivers
# Присваем Carpool_Capacity на Cars_Driven и Space_In_A_Car, 30 * 4 = 120
carpool_capacity = cars_driven * space_in_a_car
# Присваем Average_Passengers_Per_Car на Passengers и Cars_Driven, 90 / 30 = 3.0
average_passengers_per_car = passengers / cars_driven

#Результат:
print("В наличии", cars, "автомобилей.")
print("И только", drivers, "водителей вышли на работу.")
print("Получается, что", cars_not_driven, "машин пустуют.")
print("Мы можем превезти сегодня", carpool_capacity, "человек.")
print("Сегодня нужно отвезти", passengers, "человек.")
print("В каждой машине будет примерно", average_passengers_per_car, "человек.")