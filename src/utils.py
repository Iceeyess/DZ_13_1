class Category:
    """Класс для характеристики и действий над категориями товаров"""
    name: str
    description: str
    __goods: list
    total_category_count: int  # общее количество категории
    total_unique_product: int  # общее количество уникальный товаров

    __goods = list()
    total_category_count = 0
    total_unique_product = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        Category.total_category_count += 1

    def __repr__(self):
        return f"{self.name}"

    @classmethod
    @property
    def goods(cls):
        return cls.__goods

    @classmethod
    def add_product(cls, product):
        """Метод добавляет экземпляр класса в список Category.__goods"""
        cls.__goods.append(product)


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

    def verify_product_instance(self):
        """Метод для определения, есть ли данный ЭК в списке Category.__goods."""

    def __repr__(self):
        """Хранит в списках шаблон по заданию 13.2 - Задача 2"""
        return f"{self.name}, {self.price} руб. Остаток: {self.remaining_quantity} шт."

    @classmethod
    def add_product(cls, name, description, price, quantity):
        """Возвращает новый товар по 13.2 - задание 3 и 3*, если такого нет, иначе изменяет остатки и цену"""
        new_product = cls(name, description, price, quantity)
        for category_ in Category.goods:
            if new_product.name in category_.__dict__.values():
                category_.__dict__['remaining_quantity'] += new_product.remaining_quantity
                category_.__dict__['price'] = max(category_.__dict__['price'], new_product.price)
                return new_product
        Category.total_unique_product += 1
        Category.add_product(new_product)

