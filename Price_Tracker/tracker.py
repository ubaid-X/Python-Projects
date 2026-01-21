# tracker.py
from typing import List, Dict
from storage import load_products, save_products
from config import Price_Drop_Threshold

def update_products(new_products: List[Dict]) -> None:
    """
    Update the stored products with new product data.
    If a product's price has dropped by more than the defined threshold,
    it will be updated in the storage.
    """
    old_products = {p['id']: p for p in load_products()}
    update = []
    for product in new_products:
        old_price = old_products.get(product['id'], {}).get('price')
        product['old_price'] = old_price
        update.append(product)
    save_products(update)

def get_price_drops() -> List[Dict]:
    products = load_products()
    drops = []
    for product in products:
        old = product.get('old_price')
        new = product['price']
        if old is not None and new < old - Price_Drop_Threshold:
            drops.append(product)
    return drops

def list_products() -> List[Dict]:
    return load_products()

# search products by category names
def search_category(category_name: str) -> List[Dict]:
    data = load_products()
    products = []
    for product in data:
        if product['category'].lower() == category_name.lower():
            products.append(product)
    return products

# search products by names/ titles
def search_name(product_name: str) -> List[Dict]:
    data = load_products()
    products = []
    for product in data:
        if product['title'].lower() == product_name.lower():
            products.append(product)
    return products
