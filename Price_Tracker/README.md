# Price Tracker (CLI-Based)

A simple, educational Python project that fetches products data from **DummyJSON** and provides a command-line interface (CLI) to list products, update data, detect price drops, and search by name or category.
Built for developers who want to learn how to structure a Python CLI application using asynchronous HTTP requests and modular code design.

---

## Features

* Fetches products from: `https://dummyjson.com/products`
* Stores data locally in `data/products.json`
* Supports the following CLI commands:

  * **list** – Show all stored products
  * **update** – Fetch and update the latest product data
  * **drop** – Show products whose price has dropped
  * **search by name** – Find products by title keyword
  * **search by category** – Filter products by category

---

## Technologies Used

* **Python 3.8+**
* **asyncio** – For asynchronous operations
* **httpx** – For async HTTP requests
* **json** – For reading/writing data
* **typing (List, Dict)** – For type annotations
* **pathlib.Path** – For platform-independent file paths

---

## Project Structure

```
Price_Tracker/
│
├── main.py         # Entry point for CLI
├── cli.py          # Handles CLI commands and arguments
├── tracker.py      # Business logic for tracking and comparing prices
├── storage.py      # Handles JSON read/write operations
├── api.py          # Fetches data from DummyJSON API
├── config.py       # API URLs, file paths, configuration
│
└── data/
    └── products.json   # Local product data (auto-created if missing)
```

---

## Installation

Install required modules:

```bash
pip install httpx
```

(Optional)

```bash
pip install requests
```

---

## Usage

Run the CLI:

```bash
python main.py
```

---

### 1. List Products

write => list

Displays all saved products with id, name, price, and category.

---

### 2. Update Products (Fetch Latest Data)

write => update

Fetches latest products from the API and saves them to `data/products.json`.

---

### 3. Show Price Drops

write => drops

Compares old and new prices and shows products where the price has decreased.

---

### 4. Search Products by Name

write => search by name

---

### 5. Search Products by Category

write => search by category

---

## Example Output (List Command)

```
ID   Title             Price    Category
--   ----------------  -------  -------------
1    iPhone 9          549      smartphones
2    Samsung A52       399      smartphones
3    Perfume Oil       13       fragrances
```

---

## Purpose of This Project

This project is built **purely for practice** to help developers understand:

* Async HTTP calls with `httpx`
* Data storage using JSON
* Building a structured CLI with multiple commands
* Modular Python file organization

---

