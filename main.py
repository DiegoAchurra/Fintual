from datetime import datetime
from typing import List, Dict
from enum import Enum

# Constantes
DAYS_IN_YEAR = 365.25


class StockType(Enum):
    COMMON = "Common"
    PREFERRED = "Preferred"


class Stock:
    def __init__(self, symbol: str, prices: Dict[datetime, float], stock_type: StockType = StockType.COMMON):
        self.symbol: str = symbol
        self.prices: Dict[datetime, float] = prices
        self.stock_type: StockType = stock_type

    def price(self, date: datetime) -> float:
        try:
            return self.prices[date]
        except KeyError:
            raise ValueError(f"Precio de {self.symbol} el día {date} no pude ser encontrado")


class Portfolio:
    def __init__(self):
        self.stocks: List[Stock] = []

    def add_stock(self, stock: Stock):
        self.stocks.append(stock)

    def _total_value_on_date(self, date: datetime) -> float:
        try:
            return sum(stock.price(date) for stock in self.stocks)
        except ValueError as e:
            print(f"Error al calcular el valor total el día {date}: {e}")
            return 0.0

    def profit(self, start_date: datetime, end_date: datetime) -> float:
        start_value = self._total_value_on_date(start_date)
        end_value = self._total_value_on_date(end_date)
        return end_value - start_value

    def annualized_return(self, start_date: datetime, end_date: datetime) -> float:
        start_value = self._total_value_on_date(start_date)
        
        if start_value == 0:
            raise ValueError("El valor inicial no puede ser cero al calcular el rendimiento anualizado")

        profit = self.profit(start_date, end_date)
        years = (end_date - start_date).days / DAYS_IN_YEAR

        return ((profit / start_value) + 1) ** (1 / years) - 1


# Ejemplos de Uso
if __name__ == "__main__":
    
    stock1 = Stock("AAPL", {
        datetime(2023, 1, 1): 150.0,
        datetime(2024, 1, 1): 160.0,
    })

    stock2 = Stock("GOOGL", {
        datetime(2023, 1, 1): 100.0,
        datetime(2024, 1, 1): 120.0,
    })

    portfolio = Portfolio()
    portfolio.add_stock(stock1)
    portfolio.add_stock(stock2)

    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 1, 1)

    print("Ganancia:", portfolio.profit(start_date, end_date))
    print("Retorno Anualizado:", portfolio.annualized_return(start_date, end_date))
