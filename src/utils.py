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
    __price: float
    remaining_quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.remaining_quantity = quantity

    def verify_product_instance(self):
        """Метод для определения, есть ли данный ЭК в списке Category.__goods."""

    def __repr__(self):
        """Хранит в списках шаблон по заданию 13.2 - Задача 2"""
        return f"{self.name}, {self.price} руб. Остаток: {self.remaining_quantity} шт."

    def __str__(self):
        """Для корректного отображения в диалоговом окне для пользователя в методе price.setter"""
        return f"{self.name}, {self.price} руб. Остаток: {self.remaining_quantity} шт."
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, old_new_instances):
        old_value, new_value = old_new_instances
        if new_value.price <= 0:
            print(f"Введена некорректная цена. Проверьте цену.")
        else:
            if old_value.price > new_value.price:
                print('Данные уже введенного продукта: ', old_value)
                print('Данные нового продукта: ', new_value)
                feedback = input(f"Вы уверены, что хотите понизить цену?\n (Введите 'y', если да, 'n' если нет.\n").lower()
                if feedback == 'y':
                    self.__price = new_value.price
                else:
                    self.__price = old_value.price
            else:
                self.__price = new_value.price

    @classmethod
    def add_product(cls, name, description, price, quantity):
        """Возвращает новый товар по 13.2 - задание 3 и 3*, если такого нет, иначе изменяет остатки и цену"""
        new_product = cls(name, description, price, quantity)
        for category_ in Category.goods:
            if new_product.name in category_.__dict__.values():
                category_.price = (category_, new_product)
                category_.__dict__['remaining_quantity'] += new_product.remaining_quantity
                return new_product
        Category.total_unique_product += 1
        Category.add_product(new_product)

