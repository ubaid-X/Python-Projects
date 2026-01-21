from pathlib import Path
Base_Dir = Path(__file__).resolve().parent
Data_Dir = Base_Dir / "data"
Data_Dir.mkdir(exist_ok=True)

Product_FIle = Data_Dir / "products.json"

API_URL = "https://dummyjson.com/products"

Price_Drop_Threshold = 0.0   # Notify if the price drops below this value
