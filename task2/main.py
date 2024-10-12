import re
from typing import Callable

def generator_numbers(text: str):
    """
    Генератор для виділення дійсних чисел з тексту.
    
    :param text: Вхідний текст для аналізу.
    :yield: Дійсні числа, знайдені у тексті.
    """

    # Шаблон для знаходження дійсних чисел, які відокремлені пробілами
    pattern = r'(?<= )\d+\.\d+(?= )'
    matches = re.findall(pattern, text)
    for match in matches:
        yield float(match)


def sum_profit(text: str, func: Callable) -> float:
    """
    Функція для обчислення загальної суми дійсних чисел.
    
    :param text: Вхідний текст для аналізу.
    :param func: Функція-генератор, що видає дійсні числа.
    :return: Загальна сума дійсних чисел.
    """
    return sum(func(text))

# Приклад використання

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")