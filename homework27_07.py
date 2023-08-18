#Завдання 1  .
#def my_text():
#   text=("""Don't compare yourself with anyone in this world…
#   if you do so, you are insulting yourself.
#    Bill Gates""")
#   return text

#Завдання 2
#Розв'язок задачі:
# def numeri_pari(number_one,number_two):
#     new_list = []
#     for item in range(number_one,number_two + 1):
#         if item % 2 == 0 and item != number_one and item != number_two  :
#             new_list.append(item)
#     return new_list

#Завдання 3
#Розв'язок задачі:
# def risposta(user_data):
#     if user_data.upper() == "ТАК":
#         return "Квадрат заповнений"
#     else:
#         return "Квадрат пустий"





#Завдання 4
#Розв'язок задачі:
# def numero_minimale():
#      min_numero = 1000000
#      for item in user_list:
#          if item < min_numero :
#              min_numero = item
#      return min_numero

#Завдання 5
#Розв'язок задачі:

# def multiplicazione():
#     result = 1
#     for item in (new_list):
#         result *= item
#     return result

#Завдання 6

# def conta_numeri():
#     result = len(number_one)
#     return result

#Завдання 7
#Хід розв'язку:
# Паліндром — це число, у якого перша частина цифр рівноцінна другій дзеркально відображеній частині цифр.
# Умова 1: Отже число паліндром повинне бути із парною кількістю символів
# Умова 2: ділим число на 2 рівні частини(за кількістю символів)зберігаючи порядковість,при чому
# 1 частина повинна дорівнювати другій частині в оберненій порядковості.
# Числа які будуть задовільняти дані 2 умови будуть паліндромами.

# def polindrom():
#     half_number = quantity_symbols // 2
#     first_half = user_number[:half_number]
#     second_half = user_number[half_number:]
#     reversed_second_half = second_half[::-1]
#     if quantity_symbols % 2 == 0 and first_half == reversed_second_half:
#         result = print(f"{user_number} is polindrom")
#     else:
#         result = print(f"{user_number} is not polindrom")
#     return result










if __name__ == "__main__":
    print("Zdorov")

#Завдання 1
#Напишіть функцію, яка відобразить на екрані такий форматований текст:
#"Don't compare yourself with anyone in this world…
#if you do so, you are insulting yourself."
#Bill Gates

#Розв'язок задачі:
#   print(my_text())

#Завдання 2
#Напишіть функцію, яка приймає два числа як параметр і відображає всі парні числа між ними.

#Дані від користувача:
# number_one = int(input("Введіть перше число:"))
# number_two = int(input("Введіть друге число:"))
#
# print(numeri_pari(number_one,number_two))

#Завдання 3
#Напишіть функцію, яка відображає порожній або заповнений квадрат з певного символу.
#Функція приймає як параметри довжину сторони квадрата, символ і змінну логічного типу:

    #якщо вона дорівнює True, квадрат заповнений;
    #якщо — False, квадрат порожній.

#Дані від користувача:
# user_data = input("Напишіть чи квадрат заповнений (ТАК,НІ):")
# print(risposta(user_data))

#Завдання 4
#Напишіть функцію, яка повертає мінімальне з п'яти чисел. Числа передаються як параметри.

#Дані від користувача:
# user_list = [7,67576,31,48,900]
# print(numero_minimale())

#Завдання 5
#Напишіть функцію, яка повертає добуток чисел у вказаному діапазоні.
#Межі діапазону передаються як параметри.
#Якщо межі діапазону переплутані (наприклад, 5 — верхня межа, 25 — нижня межа), їх треба поміняти місцями.

#Дані від користувача:
# number_one = int(input("Введіть нижнє число діапазону:"))
# number_two = int(input("Введіть верхнє число діапазону:"))
#
# bigger_number = max(number_one,number_two)
# smaller_number = min(number_two,number_one)
#
# new_list = []
# for item in range(smaller_number,bigger_number + 1):
#     new_list.append(item)
# print(multiplicazione())

#Завдання 6
#Напишіть функцію, яка рахує кількість цифр у числі. Число передається як параметр.
#З функції потрібно повернути отриману кількість цифр. Наприклад, якщо передали 3456, кількість цифр буде 4.

#Дані від користувача:
# number_one = input("Введіть число:")
# print(conta_numeri())

#Завдання 7
#Напишіть функцію, яка перевіряє, чи є число паліндромом.
#Число передається як параметр. Якщо число є паліндромом, потрібно повернути з функції true, якщо ні — false.
#Паліндром — це число, у якого перша частина цифр рівноцінна другій дзеркально відображеній частині цифр.
#Наприклад, 123321 — паліндром (перша частина – 123, друга частина – 321, повернувши яку отримаємо 123).
#546645 — паліндром, а 421987 — не паліндром.

#Дані від користувача:
# user_number = input("Введіть число:")
# quantity_symbols = len(user_number)
# print(polindrom())