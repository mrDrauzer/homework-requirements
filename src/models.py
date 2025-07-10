class Product:
    """Класс для представления товара"""

    total_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.total_products += 1


class Category:
    """Класс для представления категории товаров"""

    total_categories = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.total_categories += 1

    def add_product(self, product):
        """Добавить товар в категорию"""
        self.products.append(product)
