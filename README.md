# Fintual

Este es un sistema simple de gestión de portafolios en Python que permite rastrear las ganancias y el retorno anualizado de una colección de acciones durante un período especificado.

## Características

- **Clase Portfolio**: Administra una colección de acciones y calcula las ganancias y el retorno anualizado entre dos fechas.
- **Clase Stock**: Representa acciones individuales con precios históricos.
- **Manejo de Errores**: Maneja casos en los que faltan precios o las fechas son inválidas.
- **Cálculo de Retorno Anualizado**: Proporciona una opción para calcular el retorno anualizado del portafolio.

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/DiegoAchurra/Fintual.git
cd Fintual
```

## Uso

### 1. Clase Stock

La clase `Stock` contiene un símbolo, datos de precios y el tipo de cada acción. Los precios están almacenados en un diccionario donde las claves son fechas y los valores son los precios.

#### Ejemplo:

```python
from datetime import datetime
from stock import Stock, StockType

# Crear acción con símbolo, precios históricos y tipo
stock1 = Stock("AAPL", {
    datetime(2023, 1, 1): 150.0,
    datetime(2024, 1, 1): 160.0,
}, StockType.COMMON)
```

### 2. Clase Portfolio

La clase `Portfolio` contiene una colección de acciones y proporciona métodos para calcular las ganancias y el retorno anualizado en un período dado.

#### Métodos

- **add_stock(stock: Stock)**: Agrega una acción al portafolio.
- **profit(start_date: datetime, end_date: datetime)**: Calcula las ganancias entre dos fechas.
- **annualized_return(start_date: datetime, end_date: datetime)**: Calcula el retorno anualizado para el rango de fechas especificado.

#### Ejemplo:

```python
from datetime import datetime
from portfolio import Portfolio

# Inicializar portafolio
portfolio = Portfolio()
portfolio.add_stock(stock1)

# Definir fechas
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 1, 1)

# Calcular ganancias y retorno anualizado
print("Ganancia:", portfolio.profit(start_date, end_date))
print("Retorno Anualizado:", portfolio.annualized_return(start_date, end_date))
```

## Manejo de Errores

- El portafolio mostrará un mensaje de error si falta el precio de una acción en una fecha especificada.
- El método `annualized_return` lanzará un `ValueError` si el valor inicial es cero para evitar una división por cero.

## Constantes y Enums

- **DAYS_IN_YEAR**: Usado para calcular el retorno anualizado de manera precisa.
- **StockType Enum**: Define tipos de acciones, permitiendo una extensión futura.

## Ejecutar el Ejemplo

Para ejecutar el ejemplo incluido en el código:

```bash
python main.py
```
