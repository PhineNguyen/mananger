import pandas as pd

# Dữ liệu khách hàng
customers_data = {
    "ID Khách Hàng": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Tên Khách Hàng": [
        "Nguyễn Văn A", "Trần Thị B", "Lê Văn C", "Phạm Thị D", "Nguyễn Văn E",
        "Trần Văn F", "Lê Thị G", "Phạm Văn H", "Nguyễn Thị I", "Trần Văn J"
    ],
    "Địa Chỉ": [
        "123 Đường 1, Quận 1, TP.HCM", "456 Đường 2, Quận 2, TP.HCM",
        "789 Đường 3, Quận 3, TP.HCM", "101 Đường 4, Quận 4, TP.HCM",
        "112 Đường 5, Quận 5, TP.HCM", "131 Đường 6, Quận 6, TP.HCM",
        "415 Đường 7, Quận 7, TP.HCM", "161 Đường 8, Quận 8, TP.HCM",
        "718 Đường 9, Quận 9, TP.HCM", "192 Đường 10, Quận 10, TP.HCM"
    ],
    "Số Điện Thoại": [
        "0123456789", "0987654321", "0912345678", "0901234567",
        "0934567890", "0945678901", "0956789012", "0967890123",
        "0978901234", "0989012345"
    ],
    "Email": [
        "a@example.com", "b@example.com", "c@example.com", "d@example.com",
        "e@example.com", "f@example.com", "g@example.com", "h@example.com",
        "i@example.com", "j@example.com"
    ],
    "Lịch Sử Mua Hàng": [
        "Đơn hàng 1, Đơn hàng 2", "Đơn hàng 3", "Đơn hàng 4, Đơn hàng 5",
        "Đơn hàng 6", "Đơn hàng 7", "Đơn hàng 8, Đơn hàng 9", "Đơn hàng 10",
        "Đơn hàng 11", "Đơn hàng 12, Đơn hàng 13", "Đơn hàng 14"
    ]
}

# Dữ liệu sản phẩm
products_data = {
    "ID Sản Phẩm": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Tên Sản Phẩm": [
        "Áo thun", "Quần jean", "Giày thể thao", "Balo", "Nón",
        "Kính mát", "Thắt lưng", "Đồng hồ", "Ví da", "Giày sandal"
    ],
    "Giá": [200000, 300000, 500000, 150000, 100000, 250000, 350000, 400000, 300000, 450000],
    "Số Lượng Tồn Kho": [50, 30, 20, 40, 10, 25, 35, 15, 60, 5],
    "Mô Tả": [
        "Áo thun cotton", "Quần jean màu xanh", "Giày thể thao màu trắng", "Balo du lịch",
        "Nón thời trang", "Kính mát chống UV", "Thắt lưng da", "Đồng hồ thông minh",
        "Ví da nam", "Giày sandal nữ"
    ],
    "Nhóm Sản Phẩm": [
        "Quần áo", "Quần áo", "Giày dép", "Đồ gia dụng", "Phụ kiện",
        "Phụ kiện", "Phụ kiện", "Đồng hồ", "Phụ kiện", "Giày dép"
    ]
}

# Dữ liệu đơn hàng
orders_data = {
    "ID Đơn Hàng": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    "ID Khách Hàng": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Ngày Đặt Hàng": [
        "2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04",
        "2024-01-05", "2024-01-06", "2024-01-07", "2024-01-08",
        "2024-01-09", "2024-01-10"
    ],
    "Danh Sách Sản Phẩm": [
        "101, 102", "103", "104, 105", "106", "107, 108",
        "109", "110", "101, 106", "102, 104", "105, 109"
    ],
    "Tổng Giá Trị Đơn Hàng": [
        500000, 500000, 800000, 250000, 600000,
        350000, 300000, 450000, 650000, 800000
    ],
    "Trạng Thái Đơn Hàng": [
        "Đang xử lý", "Đã giao", "Đã hủy", "Đang xử lý", "Đã giao",
        "Đã hủy", "Đang xử lý", "Đã giao", "Đang xử lý", "Đã giao"
    ],
    "Phương Thức Thanh Toán": [
        "Tiền mặt", "Chuyển khoản", "Thẻ tín dụng", "Tiền mặt", "Chuyển khoản",
        "Tiền mặt", "Thẻ tín dụng", "Tiền mặt", "Chuyển khoản", "Thẻ tín dụng"
    ]
}

# Tạo DataFrame cho từng loại dữ liệu
customers_df = pd.DataFrame(customers_data)
products_df = pd.DataFrame(products_data)
orders_df = pd.DataFrame(orders_data)

# Lưu dữ liệu vào các file CSV
customers_df.to_csv('customers.csv', index=False, encoding='utf-8-sig')
products_df.to_csv('products.csv', index=False, encoding='utf-8-sig')
orders_df.to_csv('orders.csv', index=False, encoding='utf-8-sig')

print("Dữ liệu đã được lưu vào các file CSV!")
