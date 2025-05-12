# 🛒 Inventory Management System (OOP Based - Python)

This is a Python-based Inventory Management System built using **Object-Oriented Programming (OOP)** principles. The system allows you to manage different types of products such as **Electronics**, **Grocery**, and **Clothing** with features like product addition, selling, restocking, and file persistence using **JSON**.

---

## 📦 Features

- Add new products (Electronics, Grocery, Clothing)
- Sell and restock products
- Search products by name or type
- Save inventory to a JSON file
- Load inventory from a JSON file
- Check grocery expiry
- Command Line Interface (CLI)

---

## 🧠 OOP Concepts Used

- Abstract Base Classes (`abc.ABC`)
- Inheritance and Polymorphism
- Encapsulation (`_protected` attributes)
- Custom class methods (`to_dict`, `__str__`)

---

## 🛍️ Product Types

### 1. Electronics
- Attributes: `product_id`, `name`, `price`, `quantity_in_stock`, `warranty_years`, `brand`

### 2. Grocery
- Attributes: `product_id`, `name`, `price`, `quantity_in_stock`, `expiry_date`
- Method: `is_expired()` to check if item is expired

### 3. Clothing
- Attributes: `product_id`, `name`, `price`, `quantity_in_stock`, `size`, `material`

---

## 🖥️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/inventory-management-system.git
   cd inventory-management-system
