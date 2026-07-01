import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stdin.reconfigure(encoding="utf-8")

# Проект FitLife - MVP версия 1.0

print("Цифровой фитнес-трекер приветствует тебя")

# 1. Знакомство
user_name = input("Как я могу к тебе обращаться? ")
user_age = int(input("Сколько вам лет? "))

# 2. Сбор данных
user_weight = float(input("Какой у вас вес (кг)? Например: 75.5 "))
user_height = float(input("Какой у вас рост (м)? Например: 1.8 "))

# 3. Расчет индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# Переименовано строго по TODO задания: water_needed вместо water_liters
water_needed = user_weight * 30 / 1000

# 4. Вывод красивого результата
print()
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_needed:.1f} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
