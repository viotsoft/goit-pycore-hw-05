def caching_fibbonacci():
    # Створюємо порожній словник для кешу
    cache = {}

    # Внутрішня функція для обчислення Фібоначчі
    def fibonacci(n):
        # Базові випадки
        if n <=0:
            return 0
        elif n == 1:
            return 1
        
        # Перевіряємо, чи вже обчислено число Фібоначчі для n
        if n in cache:
            return cache[n]
        
        # Обчислюємо n-те число Фібоначчі і зберігаємо в кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci


# Приклад використання:
fib = caching_fibbonacci()

print(fib(10))
print(fib(15))

