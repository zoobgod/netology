
# Решение без ввода данных со стороны пользователя и без использования функций
# year = 2020

# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print("Високосный год")
# else:
#     print("Обычный год")

# Решение с вводом данных со стороны пользователя
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return "Високосный год"
    else:
        return "Обычный год"
    
year = int(input("Введите год: "))
result = is_leap_year(year)
print(result)