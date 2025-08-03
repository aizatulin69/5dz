from collections import OrderedDict

# Глобальний словник для зберігання чисел Фібоначчі
fibonacci_numbs = {1: 0, 2: 1}

# Функція для обчислення та кешування чисел Фібоначчі 
def caching_fibonacci(number):
    global fibonacci_numbs  # Працюємо з глобальним словником

    def fibonacci(n):
        fibonacci_num_1 = 0
        fibonacci_num_2 = 1

        # Перевірка на коректне число
        if n <= 0 or not isinstance(n, int):
            print('Only positive int numbers')
        
        # Якщо число вже є в словнику — просто виводимо
        elif len(fibonacci_numbs) >= n:
            print(fibonacci_numbs[n - 1])
        
        else:
            # Обчислюємо числа Фібоначчі до потрібного індексу
            for _ in range(n - 2):
                fibonacci_num_2 = fibonacci_num_2 + fibonacci_num_1
                fibonacci_num_1 = fibonacci_num_2 - fibonacci_num_1
                fibonacci_numbs.update({(_ + 3): fibonacci_num_2})  # додаємо нове число в словник

            # Виводимо результат
            fibonacci_num = fibonacci_num_2
            print(f"{n} fibanacci number is: {fibonacci_num}")

    fibonacci(number)
    return fibonacci_numbs  # Повертаємо оновлений словник

# Головний цикл взаємодії з користувачем
while True:
    input_num = input('Enter int number >>> ')
    if input_num.isdigit():
        caching_fibonacci(int(input_num))  # виклик функції для числа
    elif input_num == "show all":
        print(fibonacci_numbs)  # показ усіх збережених чисел
    elif input_num == 'end':
        break  