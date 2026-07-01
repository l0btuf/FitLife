import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stdin.reconfigure(encoding="utf-8")

# Проект FitLife - MVP версия 2.0

print("Цифровой фитнес-трекер приветствует вас")

# 1. Знакомство
user_name = input("Как я могу к вам обращаться? ")

# 2. Запуск цикла для проверки ввода возраста
while True:
    try:
        user_age = int(input("Сколько вам лет? "))
        break
    except ValueError:
        print("Пожалуйста, введите ваш возраст цифрами.\n")

# 3. Сбор данных
user_weight = float(input("Какой у вас вес (кг)? Например: 75.5 "))
user_height = float(input("Какой у вас рост (м)? Например: 1.8 "))

# 4. Расчет индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# 5. Расчет нормы воды
water_per_kg = 30
liter_per_ml = 1000
water_needed = user_weight * water_per_kg / liter_per_ml

# 6. Вывод красивого результата
print(f"Отчет для пользователя: {user_name} ({user_age} г.)\n")
print(f"Ваш Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_needed:.1f} л. в день\n")
print("Расчет окончен. Будьте здоровы!")
