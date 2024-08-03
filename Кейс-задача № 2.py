# Определяем базовый класс
class Currency:
    def abbreviation(self):
        return "Currency abbreviations"

# Определяем производный класс
class Dollar(Currency):
    def abbreviation(self):
        return "USD/$"

# Определяем еще один производный класс
class Ruble(Currency):
    def abbreviation(self):
        return "RUB/P"

# Функция для тестирования
def test_currency():
    # Создаем объекты базового и производных классов
    currency = Currency()
    dollar = Dollar()
    ruble = Ruble()
    
    # Выводим результаты вызова методов speak
    print("Currency:", currency.abbreviation())
    print("Dollar:", dollar.abbreviation())
    print("Ruble:", ruble.abbreviation())

# Запускаем тестирование
if __name__ == "__main__":
    test_currency()