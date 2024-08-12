from classes.order import Order


class Customer:
    """
    Класс Customer

    Этот класс представляет клиента интернет-магазина.

    Атрибуты:
        name: Имя клиента.
        orders: Список заказов клиента.

    Методы:
        add_order: Добавляет заказ к списку заказов клиента.
        get_total_orders: Возвращает общее количество заказов клиента.
        get_total_spent: Возвращает общую сумму, потраченную клиентом на все заказы.
        __str__ и __repr__: Возвращают удобочитаемую информацию о клиенте.
    """
    def __init__(self, name: str):
        self.name = name
        self.orders = []

    def add_order(self, order: Order):
        self.orders.append(order)

    def get_total_orders(self):
        return len(self.orders)

    def get_total_spent(self):
        return sum(order.total_price() for order in self.orders)

    def __str__(self):
        return f"Клиент (Имя={self.name}, Заказы={self.get_total_orders()}, Сумма= ${self.get_total_spent()})"
