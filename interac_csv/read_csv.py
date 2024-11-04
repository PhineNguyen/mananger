import pandas as pd

def read_and_print_csv(file_path):
    # Đọc file CSV
    try:
        df = pd.read_csv(file_path)
        
        # In dữ liệu ra bảng
        print(f"Dữ liệu trong file: {file_path}")
        print(df)
        print("\n")  # Thêm dòng trống để phân cách
    except FileNotFoundError:
        print(f"File {file_path} không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Đường dẫn đến các file CSV
customer_file = 'customers.csv'
product_file = 'products.csv'
order_file = 'orders.csv'

# Gọi hàm để đọc và in dữ liệu từ các file CSV
read_and_print_csv(customer_file)
read_and_print_csv(product_file)
read_and_print_csv(order_file)
