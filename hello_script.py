def greet(name="World"):
    """Возвращает приветствие"""
    return f"Hello, {name}!"

def sum_numbers(a, b, c=0):
    """Суммирует числа с проверкой типов"""
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("All arguments must be numbers")
    return a + b + c

def is_even(number):
    """Проверяет, является ли число четным"""
    if not isinstance(number, int):
        raise TypeError("Number must be integer")
    return number % 2 == 0

def process_numbers(numbers):
    """Обрабатывает список чисел: возвращает четные и их сумму"""
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    even_numbers = [n for n in numbers if is_even(n)]
    total_sum = sum(numbers)
    
    return {
        'even_numbers': even_numbers,
        'total_sum': total_sum,
        'count_evens': len(even_numbers)
    }

def main():
    """Основная функция для демонстрации"""
    print(greet("GitHub Actions"))
    print(greet())
    
    # Демонстрация sum_numbers
    result1 = sum_numbers(5, 3, 7)
    print(f"Sum 1: {result1}")
    
    result2 = sum_numbers(10, 20)  # с значением по умолчанию
    print(f"Sum 2: {result2}")
    
    # Демонстрация is_even
    print(f"Is 4 even? {is_even(4)}")
    print(f"Is 7 even? {is_even(7)}")
    
    # Демонстрация process_numbers
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    processed = process_numbers(numbers_list)
    print(f"Processed: {processed}")

if __name__ == "__main__":
    main()
