"""Конвертер одиниць виміру."""


def km_to_miles(km: float) -> float:
    """Переводить кілометри в милі."""
    return km * 0.621371


def miles_to_km(miles: float) -> float:
    """Переводить милі в кілометри."""
    return miles / 0.621371


def celsius_to_fahrenheit(celsius: float) -> float:
    """Переводить градуси Цельсія в Фаренгейта."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Переводить градуси Фаренгейта в Цельсія."""
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    print(f"10 км = {km_to_miles(10):.2f} миль")
    print(f"100 °C = {celsius_to_fahrenheit(100):.1f} °F")
    print(f"10 миль = {miles_to_km(10):.2f} км")
    print(f"212 °F = {fahrenheit_to_celsius(212):.1f} °C")
