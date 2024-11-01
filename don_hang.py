import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def create_don_hang_tab(notebook):
    # Tạo frame cho tab "Đơn Hàng"
    frame_don_hang = ttk.Frame(notebook)
    notebook.add(frame_don_hang, text="ĐƠN HÀNG")

    # Thanh tìm kiếm và các nút chức năng
    search_entry = ttk.Entry(frame_don_hang, bootstyle="secondary", width=30)
    search_entry.insert(0, "tìm kiếm theo sản phẩm")
    search_entry.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    add_order_button = ttk.Button(frame_don_hang, text="Thêm đơn", bootstyle="secondary")
    add_order_button.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    latest_button = ttk.Button(frame_don_hang, text="Mới nhất", bootstyle="secondary")
    latest_button.grid(row=0, column=2, padx=5, pady=5, sticky=W)

    # Tạo bảng với các cột phù hợp
    columns = ["Mã", "Tên sản phẩm", "ngày", "Tên khách hàng", "SDT", "Số lượng", "Thành tiền"]

    # Tạo Treeview cho bảng đơn hàng
    order_table = ttk.Treeview(frame_don_hang, columns=columns, show="headings", bootstyle="secondary")
    order_table.grid(row=2, column=0, columnspan=len(columns), padx=5, pady=5, sticky="nsew")

    # Đặt tiêu đề cho các cột
    for col in columns:
        order_table.heading(col, text=col)
        order_table.column(col, width=100)  # Điều chỉnh độ rộng cột nếu cần

    # Thêm một số hàng mẫu vào bảng
    sample_data = [
        ("123", "Dép lào", "1/11/2024", "Túy", "0123", "2", "100.000"),
        ("124", "Áo thun", "2/11/2024", "Minh", "0456", "1", "150.000"),
        ("125", "Nón bảo hiểm", "3/11/2024", "Hùng", "0789", "3", "300.000")
    ]

    for row in sample_data:
        order_table.insert("", "end", values=row)

    # Tạo layout co giãn khi thay đổi kích thước cửa sổ
    frame_don_hang.grid_rowconfigure(2, weight=1)
    frame_don_hang.grid_columnconfigure(0, weight=1)
