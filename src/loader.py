import json
from .models import Product, Category


def load_data_from_json(filename):
    """
    Загружает категории и товары из JSON-файла.

    Args:
        filename (str): Путь к JSON-файлу

    Returns:
        list: Список объектов Category с товарами
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    categories = []
    for cat_data in data['categories']:
        products = []
        for prod_data in cat_data['products']:
            product = Product(
                name=prod_data['name'],
                description=prod_data['description'],
                price=prod_data['price'],
                quantity=prod_data['quantity']
            )
            products.append(product)

        category = Category(
            name=cat_data['name'],
            description=cat_data['description'],
            products=products
        )
        categories.append(category)

    return categories
