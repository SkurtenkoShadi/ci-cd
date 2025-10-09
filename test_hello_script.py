import pytest
import hello_script

class TestGreet:
    """Тесты для функции greet"""
    
    def test_greet_default(self):
        """Тест приветствия по умолчанию"""
        assert hello_script.greet() == "Hello, World!"
    
    def test_greet_with_name(self):
        """Тест приветствия с именем"""
        assert hello_script.greet("Alice") == "Hello, Alice!"
        assert hello_script.greet("Bob") == "Hello, Bob!"


class TestSumNumbers:
    """Тесты для функции sum_numbers"""
    
    def test_sum_three_numbers(self):
        """Тест суммирования трех чисел"""
        assert hello_script.sum_numbers(1, 2, 3) == 6
        assert hello_script.sum_numbers(0, 0, 0) == 0
        assert hello_script.sum_numbers(-1, 1, 0) == 1
    
    def test_sum_two_numbers_default(self):
        """Тест суммирования с значением по умолчанию"""
        assert hello_script.sum_numbers(5, 5) == 10
        assert hello_script.sum_numbers(10, 20) == 30
    
    def test_sum_with_floats(self):
        """Тест суммирования дробных чисел"""
        assert hello_script.sum_numbers(1.5, 2.5, 1.0) == 5.0
    
    def test_sum_type_error(self):
        """Тест ошибки типа данных"""
        with pytest.raises(TypeError):
            hello_script.sum_numbers("1", 2, 3)
        
        with pytest.raises(TypeError):
            hello_script.sum_numbers(1, "2", 3)


class TestIsEven:
    """Тесты для функции is_even"""
    
    def test_even_numbers(self):
        """Тест четных чисел"""
        assert hello_script.is_even(2) == True
        assert hello_script.is_even(0) == True
        assert hello_script.is_even(-4) == True
    
    def test_odd_numbers(self):
        """Тест нечетных чисел"""
        assert hello_script.is_even(1) == False
        assert hello_script.is_even(7) == False
        assert hello_script.is_even(-3) == False
    
    def test_is_even_type_error(self):
        """Тест ошибки типа данных"""
        with pytest.raises(TypeError):
            hello_script.is_even("2")
        
        with pytest.raises(TypeError):
            hello_script.is_even(2.5)


class TestProcessNumbers:
    """Тесты для функции process_numbers"""
    
    def test_process_normal_list(self):
        """Тест обработки обычного списка"""
        numbers = [1, 2, 3, 4, 5, 6]
        result = hello_script.process_numbers(numbers)
        
        expected_evens = [2, 4, 6]
        expected_sum = 21
        
        assert result['even_numbers'] == expected_evens
        assert result['total_sum'] == expected_sum
        assert result['count_evens'] == 3
    
    def test_process_empty_list(self):
        """Тест обработки пустого списка"""
        result = hello_script.process_numbers([])
        
        assert result['even_numbers'] == []
        assert result['total_sum'] == 0
        assert result['count_evens'] == 0
    
    def test_process_only_odds(self):
        """Тест обработки списка только с нечетными числами"""
        numbers = [1, 3, 5, 7]
        result = hello_script.process_numbers(numbers)
        
        assert result['even_numbers'] == []
        assert result['total_sum'] == 16
        assert result['count_evens'] == 0
    
    def test_process_type_error(self):
        """Тест ошибки типа данных"""
        with pytest.raises(TypeError):
            hello_script.process_numbers("not a list")
        
        with pytest.raises(TypeError):
            hello_script.process_numbers(123)


def test_main_function(capsys):
    """Тест что основная функция выполняется без ошибок"""
    hello_script.main()
    
    # Проверяем что функция что-то выводит
    captured = capsys.readouterr()
    assert "Hello" in captured.out
    assert "Sum" in captured.out
