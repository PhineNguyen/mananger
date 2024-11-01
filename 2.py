import sqlite3

# Khởi tạo database và tạo bảng nếu chưa tồn tại
def initialize_database():
    conn = sqlite3.connect('shop_database.db')
    cursor = conn.cursor()
    
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

# Thêm đơn hàng vào bảng Orders
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

# Chạy chương trình
if __name__ == "__main__":
    initialize_database()
    
    while True:
        print("\nChọn một trong các lựa chọn sau:")
        print("1. Nhập thông tin khách hàng")
        print("2. Thêm đơn hàng cho khách hàng")
        print("3. Thoát")
        
        choice = input("Lựa chọn của bạn: ")
        
        if choice == "1":
            while True:
                print("\nNhập thông tin khách hàng (nhấn '1' để dừng):")
                name = input("Nhập tên khách hàng: ")
                if name == "1":
                    break
                phone = input("Nhập Số Điện Thoại: ")
                email = input("Nhập email: ")
                address = input("Nhập địa chỉ: ")
                
                add_customer(name, phone, email, address)
        
        elif choice == "2":
            while True:
                print("\nNhập thông tin đơn hàng (nhấn '1' để dừng):")
                customer_id = input("Nhập ID khách hàng cho đơn hàng: ")
                if customer_id == "1":
                    break
                order_date = input("Nhập ngày đặt hàng (VD: 2024-10-30): ")
                total_amount = float(input("Nhập tổng số tiền: "))
                status = input("Nhập trạng thái đơn hàng (Pending/Completed): ")
                
                add_order(int(customer_id), order_date, total_amount, status)
        
        elif choice == "3":
            print("Thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
