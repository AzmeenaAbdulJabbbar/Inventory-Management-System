from abc import ABC ,abstractmethod
from datetime import datetime
import json

class Product (ABC):
    def __init__(self, _product_id,_name,_price,_quantity_in_stock):
        self._product_id= _product_id
        self._name = _name
        self._price = _price
        self._quantity_in_stock = _quantity_in_stock
    @abstractmethod
    def __str__(self):
        pass

    def restock(self,amount):
        self._quantity_in_stock += amount
    def sell(self , quantity):
        if self._quantity_in_stock >= quantity:
            self._quantity_in_stock -= quantity
        else:
            raise ValueError("Not enough stock available.") 
    def get_total_value (self):
           return (self._price * self._quantity_in_stock)
class Electronics(Product):
    def __init__ (self, _product_id,_name,_price,_quantity_in_stock, warranty_years, brand):
        super().__init__ (_product_id,_name,_price,_quantity_in_stock)
        self.warranty_years = warranty_years
        self.brand = brand
    def __str__(self):
     return f"Electronics (ID: {self._product_id}) - {self._name}, Brand: {self.brand}, Price: {self._price}, Stock: {self._quantity_in_stock}, Warranty: {self.warranty_years} years"

    def to_dict(self):
        return{
                "type": "Electronics",
                "product_id": self._product_id,
                "name": self._name,
                "price": self._price,
                "quantity_in_stock": self._quantity_in_stock,
                "warranty_years": self.warranty_years,
                "brand": self.brand
        }

class Grocery(Product):
    def __init__(self,_product_id,_name,_price,_quantity_in_stock,expiry_date):
        super().__init__(_product_id,_name,_price,_quantity_in_stock)
        self.expiry_date = datetime.strptime(expiry_date,"%Y-%m-%d")

    def __str__(self):
        return f"Grocery (ID: {self._product_id}) - {self._name}, Price: {self._price}, Stock: {self._quantity_in_stock}, Expiry: {self.expiry_date.strftime('%Y-%m-%d')}"
    def is_expired(self):
        return datetime.now() > self.expiry_date
    def to_dict(self):
        return {
                "type": "Grocery",
                "product_id": self._product_id,
                "name": self._name,
                "price": self._price,
                "quantity_in_stock": self._quantity_in_stock,
                "expiry_date": self.expiry_date.strftime("%Y-%m-%d")
       }

class clothing (Product):
    def __init__(self,_product_id,_name,_price,_quantity_in_stock, size, material):
        super().__init__(_product_id,_name,_price,_quantity_in_stock)
        self.size = size
        self.material = material
    def __str__(self):
        return f"Clothing (ID: {self._product_id}) - {self._name}, Size: {self.size}, Material: {self.material}, Price: {self._price}, Stock: {self._quantity_in_stock}"
    def to_dict(self):
         return {
            "type": "Clothing",
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "quantity_in_stock": self._quantity_in_stock,
            "size": self.size,
            "material": self.material
    }

    
class Inventory ():
    def __init__(self):
        self._products = {}

    def add_product(self, product: Product):
        if product._product_id in self._products:
            raise ValueError("Product with this ID already exists.")
        self._products[product._product_id] = product

    def remove_product(self, product_id):
        if product_id in self._products:
            del self._products[product_id]
        else:
            raise ValueError("Product not found.")

    def search_by_name(self, name):
        return [product for product in self._products.values() if name.lower() in product._name.lower()]
    def search_by_type(self, product_type):
        return [product for product in self._products.values() if isinstance(product, product_type)]
    def list_all_products(self):
        return [str(product) for product in self._products.values()]
    def sell_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id].sell(quantity)
        else:
            raise ValueError("Product not found.")
    def restock_product(self, product_id, amount):
        if product_id in self._products:
            self._products[product_id].restock(amount)
        else:
            raise ValueError("Product not found.")
    def save_to_file(self, filename):
        with open(filename, "w") as f:
             json.dump([product.to_dict() for product in self._products.values()], f, indent=4)
    def load_from_file(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            for item in data:
                p_type = item["type"]
                if p_type == "Electronics":
                     product = Electronics(item["product_id"], item["name"], item["price"], item["quantity_in_stock"], item["warranty_years"], item["brand"])
                elif p_type == "Grocery":
                    product = Grocery(item["product_id"], item["name"], item["price"], item["quantity_in_stock"], item["expiry_date"])
                elif p_type == "Clothing":
                     product = clothing(item["product_id"], item["name"], item["price"], item["quantity_in_stock"], item     ["size"], item["material"])
                else:
                 continue
                self._products[product._product_id] = product  
def main():
    inventory = Inventory()
    
    while True:
        print("\n1. Add Product")
        print("2. Sell Product")
        print("3. Search/View Product")
        print("4. Save Inventory")
        print("5. Load Inventory")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            # Example of adding a product
            p_type = input("Enter product type (Electronics/Grocery/Clothing): ")
            if p_type.lower() == 'electronics':
                _id = input("Enter product ID: ")
                name = input("Enter product name: ")
                price = float(input("Enter price: "))
                stock = int(input("Enter stock quantity: "))
                warranty = int(input("Enter warranty years: "))
                brand = input("Enter brand: ")
                product = Electronics(_id, name, price, stock, warranty, brand)
            elif p_type.lower() == 'grocery':
                _id = input("Enter product ID: ")
                name = input("Enter product name: ")
                price = float(input("Enter price: "))
                stock = int(input("Enter stock quantity: "))
                expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
                product = Grocery(_id, name, price, stock, expiry_date)
            elif p_type.lower() == 'clothing':
                _id = input("Enter product ID: ")
                name = input("Enter product name: ")
                price = float(input("Enter price: "))
                stock = int(input("Enter stock quantity: "))
                size = input("Enter size: ")
                material = input("Enter material: ")
                product = clothing(_id, name, price, stock, size, material)
            else:
                print("Invalid product type")
                continue

            inventory.add_product(product)
            print(f"Product {name} added successfully.")
        
        elif choice == '2':
            # Selling a product
            product_id = input("Enter product ID to sell: ")
            quantity = int(input("Enter quantity to sell: "))
            try:
                inventory.sell_product(product_id, quantity)
                print("Product sold successfully.")
            except ValueError as e:
                print(e)
        
        elif choice == '3':
            # Searching for products
            name = input("Enter product name to search: ")
            products = inventory.search_by_name(name)
            if products:
                for product in products:
                    print(product)
            else:
                print("No products found.")
        
        elif choice == '4':
            # Save inventory
            filename = input("Enter file name to save inventory: ")
            inventory.save_to_file(filename)
            print("Inventory saved successfully.")
        
        elif choice == '5':
            # Load inventory
            filename = input("Enter file name to load inventory: ")
            try:
                inventory.load_from_file(filename)
                print("Inventory loaded successfully.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()


    


