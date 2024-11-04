import sqlite3
import random

# Kết nối đến cơ sở dữ liệu (nếu file không tồn tại, nó sẽ được tạo)
conn = sqlite3.connect('store_management.db')
cursor = conn.cursor()

# Tạo bảng khách hàng
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    phone TEXT,
    email TEXT,
    purchase_history TEXT
)
''')

# Tạo bảng sản phẩm
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    stock_quantity INTEGER,
    description TEXT,
    category TEXT
)
''')

# Tạo bảng đơn hàng
cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    product_list TEXT,
    total_value REAL,
    order_status TEXT,
    payment_method TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
)
''')

# Dữ liệu mẫu cho khách hàng
customers_data = [
    (i, f"Khách hàng {i}", f"{random.randint(1, 100)} Đường {random.randint(1, 20)}, Quận {random.randint(1, 12)}, TP.HCM",
     f"09{random.randint(10000000, 99999999)}", f"khach{i}@example.com", f"Đơn hàng {random.randint(1, 20)}")
    for i in range(1, 11)
]

# Dữ liệu mẫu cho sản phẩm
products_data = [
    (i, f"Sản phẩm {i}", random.uniform(10000, 100000), random.randint(1, 50),
     f"Mô tả sản phẩm {i}: màu sắc, kích thước, chất liệu.", random.choice(["Quần áo", "Giày dép", "Đồ gia dụng"]))
    for i in range(1, 11)
]

# Dữ liệu mẫu cho đơn hàng
orders_data = [
    (i, random.randint(1, 10), f"2024-11-{random.randint(1, 30)}", 
     f"[Sản phẩm {random.randint(1, 10)}, Sản phẩm {random.randint(1, 10)}]", 
     random.uniform(10000, 300000), random.choice(["Đang xử lý", "Đã giao", "Đã hủy"]),
     random.choice(["Tiền mặt", "Chuyển khoản", "Thẻ tín dụng"]))
    for i in range(1, 11)
]

# Thêm dữ liệu vào bảng
cursor.executemany('INSERT INTO Customers VALUES (?, ?, ?, ?, ?, ?)', customers_data)
cursor.executemany('INSERT INTO Products VALUES (?, ?, ?, ?, ?, ?)', products_data)
cursor.executemany('INSERT INTO Orders VALUES (?, ?, ?, ?, ?, ?, ?)', orders_data)

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

print("Dữ liệu mẫu đã được lưu vào file store_management.db.")
