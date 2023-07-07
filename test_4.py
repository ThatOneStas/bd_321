# ---- Завдання перше 1 ----

# Num_1 = int(input('Введіть перше число: '))
# Num_2 = int(input('Введіть друге число: '))
# Num_3 = int(input('Введіть третє число: '))
# Cond_1 = input('Введіть "сума" для суми або "добуток" для добутку: ')
# if Cond_1.lower() == 'сума':
#     print(f"Сума: {Num_1 + Num_2 + Num_3}")
# elif Cond_1.lower() == 'добуток':
#     print(f"Сума: {Num_1 * Num_2 * Num_3}")
# else:
#     print('Something went wrong.')

# ---- Завдання друге 2 ----

# Num_1_2 = int(input('Введіть перше число: '))
# Num_2_2 = int(input('Введіть друге число: '))
# Num_3_2 = int(input('Введіть третє число: '))
# Cond_1_2 = input('Введіть - "мін" для мін. значення,\n"макс" для макс. значення,\n"середнє" для середнього ариф. : ')
# if Cond_1_2.lower() == 'мін':
#     print(f"Найменше число: {min(Num_1_2, Num_2_2, Num_3_2)}")
# elif Cond_1_2.lower() == 'макс':
#     print(f"Найбільше число: {max(Num_1_2, Num_2_2, Num_3_2)}")
# elif Cond_1_2.lower() == 'середнє':
#     print(f"Середнє арифметичне: {(Num_1_2 + Num_2_2 + Num_3_2) / 3}")
# else:
#     print('Something went wrong.')

# ---- Завдання третє 3 ----

Metres = int(input('Введіть к-сть метрів для обчислення: '))
Cond_1_3 = input('Введіть:\n"Милі" щоб перевести метри у милі,\n"Дюйми" щоб перевести метри у дюйми,\n"Ярди" щоб перевести метри у ярди. ')
if Cond_1_3.lower() == 'милі':
    print(f"{Metres} м. - {round(Metres * 0.0006, 2)} миль.")
elif Cond_1_3.lower() == 'дюйми':
    print(f"{Metres} м. - {round(Metres * 39.37, 2)} дюймів.")
elif Cond_1_3.lower() == 'ярди':
    print(f"{Metres} м. - {round(Metres * 1.0936, 2)} ярд.")
else:
    print('Something went wrong.')