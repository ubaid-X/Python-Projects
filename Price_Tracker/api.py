import httpx
from config import API_URL
from typing import List, Dict


async def fetch_data() -> List[Dict]:
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL)
        response.raise_for_status()
        data = response.json()
        products = data.get("products", [])
        normalized_product = []
        for product in products:
            normalized_product.append({
                "id": product["id"],
                "title": product["title"],
                "price": product["price"],
                "category": product["category"],
            })
        return normalized_product
