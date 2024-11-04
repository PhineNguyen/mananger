import pandas as pd

# Đường dẫn đến các file CSV
customer_file = 'customers.csv'
product_file = 'products.csv'
order_file = 'orders.csv'

def add_customer(customer_id, name, address, phone, email, purchase_history):
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(customer_file)

    # Thêm khách hàng mới
    new_customer = {
        "ID Khách Hàng": customer_id,
        "Tên Khách Hàng": name,
        "Địa Chỉ": address,
        "Số Điện Thoại": phone,
        "Email": email,
        "Lịch Sử Mua Hàng": purchase_history
    }

    df = df.append(new_customer, ignore_index=True)
    df.to_csv(customer_file, index=False, encoding='utf-8-sig')
    print("Đã thêm khách hàng mới!")

def update_customer(customer_id, **kwargs):
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(customer_file)

    # Tìm khách hàng và cập nhật thông tin
    if customer_id in df["ID Khách Hàng"].values:
        for key, value in kwargs.items():
            if key in df.columns:
                df.loc[df["ID Khách Hàng"] == customer_id, key] = value
        df.to_csv(customer_file, index=False, encoding='utf-8-sig')
        print(f"Đã cập nhật thông tin khách hàng với ID {customer_id}!")
    else:
        print("Không tìm thấy khách hàng với ID này.")

def delete_customer(customer_id):
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(customer_file)

    # Xóa khách hàng
    if customer_id in df["ID Khách Hàng"].values:
        df = df[df["ID Khách Hàng"] != customer_id]
        df.to_csv(customer_file, index=False, encoding='utf-8-sig')
        print(f"Đã xóa khách hàng với ID {customer_id}!")
    else:
        print("Không tìm thấy khách hàng với ID này.")

# Ví dụ sử dụng:
# Thêm một khách hàng mới
add_customer(11, "Nguyễn Văn K", "233 Đường 11, Quận 11, TP.HCM", "0912345670", "k@example.com", "Đơn hàng 15")

# Cập nhật thông tin của khách hàng có ID 1
update_customer(1, Tên_Khách_Hàng="Nguyễn Văn A mới", Email="a_moi@example.com")

# Xóa khách hàng có ID 2
delete_customer(2)
