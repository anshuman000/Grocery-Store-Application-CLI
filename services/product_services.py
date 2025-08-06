from factories.product_factory import ProductFactory
from models.product import Product
def list_all_product():
    products = ProductFactory.list_all_product()
    for product in products:
        print_product(product)

def get_product():
    product = ProductFactory.get_product()
    print_product(product)

def add_product():
    name = input("Product Name.")
    desc = input("Description")
    price = input("Enter price.")
    image = input("Add image.")
    print_product(ProductFactory.add_product(name, desc, price, image))

def update_product():
    prod_id, name = input("Enter product id and product name.")
    print_product(ProductFactory.update_product(name, prod_id))

def update_product_stock():
    stock = input("Enter quantity.")
    prod_id = input("Enter product id.")
    ProductFactory.update_product(stock, prod_id)

def remove_product():
    prod_id = input("Enter product id.")
    ProductFactory.remove_product(prod_id)

    #edhjsfysgiy

def print_product(product):
    for key, value in product.to_dict().items():
        print(f"{key.capitalize()} : {value}")