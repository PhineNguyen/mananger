import pandas as pd
import random
from faker import Faker

fake = Faker()

# Hàm tạo dữ liệu khách hàng
def generate_customers_data(num_customers):
    customers_data = {
        "ID Khách Hàng": list(range(1, num_customers + 1)),
        "Tên Khách Hàng": [fake.name() for _ in range(num_customers)],
        "Địa Chỉ": [fake.address().replace("\n", ", ") for _ in range(num_customers)],
        "Số Điện Thoại": [fake.phone_number() for _ in range(num_customers)],
        "Email": [fake.email() for _ in range(num_customers)],
        "Lịch Sử Mua Hàng": [", ".join([f"Đơn hàng {random.randint(1, 50)}" for _ in range(random.randint(1, 3))]) for _ in range(num_customers)]
    }
    return pd.DataFrame(customers_data)

# Hàm tạo dữ liệu sản phẩm
def generate_products_data(num_products):
    products_data = {
        "ID Sản Phẩm": list(range(101, 101 + num_products)),
        "Tên Sản Phẩm": [fake.word().capitalize() for _ in range(num_products)],
        "Giá": [random.randint(100000, 1000000) for _ in range(num_products)],
        "Số Lượng Tồn Kho": [random.randint(1, 100) for _ in range(num_products)],
        "Mô Tả": [fake.sentence() for _ in range(num_products)],
        "Nhóm Sản Phẩm": [random.choice(["Quần áo", "Giày dép", "Phụ kiện", "Đồ gia dụng", "Đồng hồ"]) for _ in range(num_products)]
    }
    return pd.DataFrame(products_data)

# Hàm tạo dữ liệu đơn hàng
def generate_orders_data(num_orders, num_customers, num_products):
    orders_data = {
        "ID Đơn Hàng": list(range(201, 201 + num_orders)),
        "ID Khách Hàng": [random.randint(1, num_customers) for _ in range(num_orders)],
        "Ngày Đặt Hàng": [fake.date_this_year() for _ in range(num_orders)],
        "Danh Sách Sản Phẩm": [", ".join([str(random.randint(101, 100 + num_products)) for _ in range(random.randint(1, 3))]) for _ in range(num_orders)],
        "Tổng Giá Trị Đơn Hàng": [random.randint(200000, 2000000) for _ in range(num_orders)],
        "Trạng Thái Đơn Hàng": [random.choice(["Đang xử lý", "Đã giao", "Đã hủy"]) for _ in range(num_orders)],
        "Phương Thức Thanh Toán": [random.choice(["Tiền mặt", "Chuyển khoản", "Thẻ tín dụng"]) for _ in range(num_orders)]
    }
    return pd.DataFrame(orders_data)

# Số lượng dữ liệu muốn tạo
num_customers = 50
num_products = 50
num_orders = 50

# Tạo DataFrame cho từng loại dữ liệu
customers_df = generate_customers_data(num_customers)
products_df = generate_products_data(num_products)
orders_df = generate_orders_data(num_orders, num_customers, num_products)

# Lưu dữ liệu vào các file CSV
customers_df.to_csv('customers.csv', index=False, encoding='utf-8-sig')
products_df.to_csv('products.csv', index=False, encoding='utf-8-sig')
orders_df.to_csv('orders.csv', index=False, encoding='utf-8-sig')

print("Dữ liệu đã được lưu vào các file CSV!")
