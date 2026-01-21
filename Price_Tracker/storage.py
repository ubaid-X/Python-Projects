import json
from typing import List, Dict
from config import Product_FIle


def load_products() -> List[Dict]:
    """Load products from a JSON file."""
    if not Product_FIle.exists():
        return []
    else:
        with open(Product_FIle, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data


def save_products(products: List[Dict]) -> None:
    """Save products to a JSON file."""
    with open(Product_FIle, 'w', encoding='utf-8') as file:
        json.dump(products, file, indent=4)
