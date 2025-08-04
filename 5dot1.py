from collections import OrderedDict

# Функція для обчислення та кешування чисел Фібоначчі 
def caching_fibonacci():
    # Глобальний словник для зберігання чисел Фібоначчі
    fibonacci_numbs = {1: 0, 2: 1}

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
            for _ in range(n - 1):
                fibonacci_num_2 = fibonacci_num_2 + fibonacci_num_1
                fibonacci_num_1 = fibonacci_num_2 - fibonacci_num_1
                fibonacci_numbs.update({(_ + 3): fibonacci_num_2})  # додаємо нове число в словник

            # Виводимо результат
            fibonacci_num = fibonacci_num_2
            print(f"{n} fibanacci number is: {fibonacci_num}")

    # Головний цикл взаємодії з користувачем
    while True:
        number = input('Enter int number >>> ')
        if number.isdigit():
            fibonacci(int(number))  # виклик функції для числа
        elif number == "show all":
            print(fibonacci_numbs)  # показ усіх збережених чисел
        elif number == 'end':
            break 

    return fibonacci_numbs  # Повертаємо оновлений словник

caching_fibonacci()
