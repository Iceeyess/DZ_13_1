class Category:
    """Класс для характеристики и действий над категориями товаров"""
    name: str
    description: str
    goods: list
    total_category_count: int  # общее количество категории
    total_unique_product: int  # общее количество уникальный товаров

    goods = list()
    total_category_count = 0
    total_unique_product = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        Category.total_category_count += 1

    def __repr__(self):
        return f"{self.name}"


class Product:
    """Класс для характеристик и действий над свойствами товаров"""
    name: str
    description: str
    price: float
    remaining_quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.remaining_quantity = quantity
        if self.verify_product_instance(): # Только если не ЭК в списке Category.goods идет добавление
            Category.total_unique_product += 1
            Category.goods.append(self)

    def verify_product_instance(self):
        """Метод для определения, есть ли данный ЭК в списке Category.goods."""
        flag = True  # Переменная с булевым значением, чтобы понять, есть ли данный ЭК в Category.goods или нет.
        for category_ in Category.goods:
            if self.name in category_.__dict__.values():
                flag = False
                return flag
        return flag

    def __repr__(self):
        return f"{self.name}"

