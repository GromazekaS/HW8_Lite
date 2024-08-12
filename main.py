from classes.product import Product
from classes.order import Order
from classes.customer import Customer
from classes.discount import Discount

# Создаем продукты
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)
product3 = Product("Headphones", 100)

# Создаем скидки
seasonal_discount = Discount("Seasonal Sale", 10)
promo_discount = Discount("Promo Code", 15)

# Рассчитываем цену с учетом скидки
discounted_price = Discount.apply_discount(product1.price, seasonal_discount.discount_percent)
print(f"Сниженная цена на {product1.name} по сезонной скидке: ${discounted_price}")  # Вывод: 900.0

# Создаем заказы
order1 = Order([product1])
order2 = Order([product2, product3])

# Применяем скидку на второй заказ
order2_discounted_price = sum(Discount.apply_discount(product.price, promo_discount.discount_percent) for product in order2.products)
print(f"Сумма заказа с промокодом: ${order2_discounted_price}")  # Вывод: 510.0

# Создаем клиента
customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Добавляем заказы клиентам
customer1.add_order(order1)
customer2.add_order(order2)

# Выводим общее количество заказов и сумму, потраченную каждым клиентом
print(f"{customer1.name} сделал {customer1.get_total_orders()} заказов на сумму ${customer1.get_total_spent():.2f}")  # Вывод: 1000.0
print(f"{customer2.name} сделал {customer2.get_total_orders()} заказов на сумму ${customer2.get_total_spent():.2f}")  # Вывод: 600.0

# Выводим информацию о клиентах и их заказах
print(customer1)  # Вывод: Клиент (Имя=Alice, Заказы=1, Сумма=1000)
print(customer2)  # Вывод: Клиент (Имя=Bob, Заказы=1, Сумма=600)

# Выводим информацию о заказах
print(order1)  # Вывод: Заказ (Общая цена = 1000)
print(order2)  # Вывод: Заказ (Общая цена = 600)

