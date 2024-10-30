import sqlite3
import tkinter as tk
from tkinter import filedialog

# Kết nối đến database và tạo bảng nếu chưa tồn tại
def initialize_database():
    conn = sqlite3.connect('shop_database.db')
    cursor = conn.cursor()
    
    # Xóa bảng cũ nếu có và tạo lại
    cursor.execute("DROP TABLE IF EXISTS Customers")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            phone TEXT,
            email TEXT,
            address TEXT
        )
    ''')
    
    # Tạo bảng Orders với khóa ngoại tham chiếu đến Customers
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS Orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            order_date TEXT,
            total_amount REAL,
            status TEXT,
            FOREIGN KEY (customer_id) REFERENCES Customers (customer_id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database và bảng đã được khởi tạo thành công.")

# Thêm khách hàng vào bảng Customers
def add_customer(name, phone, email, address):
    conn = sqlite3.connect('shop_database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO Customers (name, phone, email, address) 
        VALUES (?, ?, ?, ?)
    ''', (name, phone, email, address))
    
    conn.commit()
    conn.close()
    print("Khách hàng đã được thêm thành công.")

# Thêm đơn hàng cho khách hàng vào bảng Orders
def add_order(customer_id, order_date, total_amount, status):
    conn = sqlite3.connect('shop_database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO Orders (customer_id, order_date, total_amount, status) 
        VALUES (?, ?, ?, ?)
    ''', (customer_id, order_date, total_amount, status))
    
    conn.commit()
    conn.close()
    print("Đơn hàng đã được thêm thành công.")

# Lấy danh sách khách hàng
def get_customers():
    conn = sqlite3.connect('shop_database.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM Customers')
    customers = cursor.fetchall()
    
    conn.close()
    return customers

# Chạy chương trình mẫu
if __name__ == "__main__":
    # Khởi tạo database và bảng
    initialize_database()
    
    # Thêm khách hàng
    add_customer(
        name="Nguyen Van A",
        phone="0123456789",
        email="nguyenvana@example.com",
        address="123 Đường ABC, Hà Nội"
    )
    
    # Thêm đơn hàng cho khách hàng
    add_order(
        customer_id=1,  # ID của khách hàng
        order_date="2024-10-30",
        total_amount=1500000,
        status="Pending"
    )
    
    # Lấy danh sách khách hàng và in ra
    customers = get_customers()
    print("Danh sách khách hàng:")
    for customer in customers:
        print(customer)
