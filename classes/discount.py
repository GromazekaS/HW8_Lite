class Discount:
    """
    Класс Discount

    Этот класс представляет скидку в интернет-магазине.

    Атрибуты:
        description: Описание скидки.
        discount_percent: Процент скидки.

    Методы:
        apply_discount: Статический метод для применения скидки к цене.
        __str__ и __repr__: Возвращают удобочитаемую информацию о скидке.
    """
    def __init__(self, description: str, discount_percent: float):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(price: float, discount_percent: float) -> float:
        """
        Применяет скидку к цене и возвращает новую цену.
        """
        return price * (1 - discount_percent / 100)

    def __str__(self):
        return f"Скидка ({self.description}, {self.discount_percent}%)"

    def __repr__(self):
        return f"Discount(description='{self.description}', discount_percent={self.discount_percent})"