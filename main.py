from src.funcs import get_json_file
from src.utils import Product, Category
import os

product_instance_list, category_instance_list = [], []


path_ = os.path.join('src', 'products.json')
json_file = get_json_file(path_)

for key in json_file:
    value = dict()
    if isinstance(key['products'], list):
        for product_keys in key['products']:
            Product.add_product(product_keys['name'], product_keys['description'], product_keys['price'], product_keys['quantity'])
    category_instance_list.append(Category(key['name'], key['description']))

print(Category.goods)