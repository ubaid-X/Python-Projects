# cli.py: control loop to show data on terminal
import asyncio
from api import fetch_data
from tracker import update_products, get_price_drops, list_products, search_category, search_name


def print_products(products):
    """ This function is printing all the products"""
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product['title']} | "
              f"price: ${product['price']} | "
              f"category: {product['category']}")


async def update_command():
    print("Fetching latest product data...")
    new_products = await fetch_data()
    update_products(new_products)
    print("Product data updated.")


def drop_command():
    drops = get_price_drops()
    if not drops:
        print("No price drops detected.")
        return
    print("Price drops detected:")
    for product in drops:
        print(
            f"- {product['title']}: "
            f"old price: ${product['old_price']} -> "
            f"new price: ${product['price']}"
            )


def start_cli():
    """ This function is to show menu and for terminal user Interface"""
    print("Welcome to the Product Tracker CLI")
    while (command := input(
        "\nEnter a command (list, update, drops, search by category,search by name, exit): "
            ).strip().lower()):
        match command:
            case "list":
                products = list_products()
                if not products:
                    print("No products stored yet.")
                else:
                    print_products(products)
            case "update":
                asyncio.run(update_command())
            case "drops":
                drop_command()
            case "search by category":
                category = input("Enter a Category of Products: ")
                searched_products = search_category(category)
                if not searched_products:
                    print(f"No products found in category '{category}'.")
                else:
                    print_products(searched_products)
            case "search by name":
                name = input("Enter Product name: ")
                products = search_name(name)
                if not products:
                    print(f"No products found with name '{name}'.")
                else:
                    print_products(products)
            case "exit":
                print("Thank you for using the Software. Goodbye!")
                break
            case _:
                print("Invalid command. please Try Again")
