import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def create_don_hang_tab(notebook):
    # Create frame for "Đơn Hàng" tab
    frame_don_hang = ttk.Frame(notebook)
    notebook.add(frame_don_hang, text="ĐƠN HÀNG")
    
    # Search bar and action buttons
    search_entry = ttk.Entry(frame_don_hang, bootstyle="secondary", width=30)
    search_entry.insert(0, "tìm kiếm theo sản phẩm")
    search_entry.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    add_order_button = ttk.Button(frame_don_hang, text="thêm đơn", bootstyle="secondary")
    add_order_button.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    latest_button = ttk.Button(frame_don_hang, text="Mới nhất", bootstyle="secondary")
    latest_button.grid(row=0, column=2, padx=5, pady=5, sticky=W)

    # Headers for the order list (no data rows)
    headers = ["Mã", "Tên sản phẩm", "ngày", "Tên khách hàng", "SDT", "Số lượng", "Thành tiền", ""]
    for i, header in enumerate(headers):
        ttk.Label(frame_don_hang, text=header, bootstyle="secondary").grid(row=1, column=i, padx=5, pady=5)

    # No sample data rows; the table is empty
