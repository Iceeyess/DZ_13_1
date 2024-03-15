from src.utils import Category
from src.utils import Product
import pytest


@pytest.fixture
def prod_instances():
    p1 = Product('Сачок для чистки бассейна Bestway',
                 'Универсальный сачок Bestway 58635 предназначен для сбора мусора со дна и поверхности бассейна.', 766,
                 10)
    p2 = Product('ASUS Материнская плата PRIME B450M-A II DDR4', 'Материнская плата ', 7498, 5)
    p3 = Product('Пальто Nike', 'Цвет идеально сочетает в себе функциональность, комфорт и стильный дизайн.', 5980, 3)
    p4 = Product('ASUS Материнская плата PRIME B450M-A II DDR4', 'Материнская плата ', 7498, 5)
    return p1, p2, p3, p4


@pytest.fixture
def category_instances():
    c1 = Category('Одежда', 'Nike, Zinger, PALMARY LEADING')
    c2 = Category('Электроника', 'Asus, Acer, Apple, Dell')
    c3 = Category('Дом и сад', 'Best way, Intex, Huter')
    return c1, c2, c3


def test_init(prod_instances, category_instances):
    list_prod = ['Сачок для чистки бассейна Bestway', 'ASUS Материнская плата PRIME B450M-A II DDR4', 'Пальто Nike']
    for index in range(len(category_instances)):
        assert Category.goods[index].name == list_prod[index]
    assert len(prod_instances) == 4
    assert len(Category.goods) == 3 # Проверка на неуникальность, т.к. выше 4 ЭК
    assert len(category_instances) == 3
    assert prod_instances[0].name == 'Сачок для чистки бассейна Bestway'
    assert prod_instances[0].description == 'Универсальный сачок Bestway 58635 предназначен для сбора мусора со дна и поверхности бассейна.'
    assert prod_instances[0].price == 766
    assert prod_instances[0].remaining_quantity == 10

