class Currency:
    def abbreviation(self):
        return "Currency abbreviations"

class Dollar(Currency):
    def abbreviation(self):
        return "USD/$"

class Ruble(Currency):
    def abbreviation(self):
        return "RUB/P"

def test_currency():
    currency = Currency()
    dollar = Dollar()
    ruble = Ruble()
    
    print("Currency:", currency.abbreviation())
    print("Dollar:", dollar.abbreviation())
    print("Ruble:", ruble.abbreviation())

if __name__ == "__main__":
    test_currency()
