import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def create_don_hang_tab(notebook):
    # Create frame for "Đơn Hàng" tab
    frame_don_hang = ttk.Frame(notebook)
    notebook.add(frame_don_hang, text="ĐƠN HÀNG")
    
    # Components in "Đơn Hàng" tab
    search_entry = ttk.Entry(frame_don_hang, bootstyle="secondary", width=30)
    search_entry.insert(0, "tìm kiếm theo sản phẩm")
    search_entry.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    add_order_button = ttk.Button(frame_don_hang, text="thêm đơn", bootstyle="secondary")
    add_order_button.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    latest_button = ttk.Button(frame_don_hang, text="Mới nhất", bootstyle="secondary")
    latest_button.grid(row=0, column=2, padx=5, pady=5, sticky=W)

    # Headers for the order list
    headers = ["Mã", "Tên sản phẩm", "ngày", "Tên khách hàng", "SDT", "Số lượng", "Thành tiền", ""]
    for i, header in enumerate(headers):
        ttk.Label(frame_don_hang, text=header, bootstyle="secondary").grid(row=1, column=i, padx=5, pady=5)

    # Sample order data
    order_data = [["123", "dép lào", "1/11/2024", "tùy", "0123", "2", "100.000"]]
    for row_index, row_data in enumerate(order_data, start=2):
        for col_index, item in enumerate(row_data):
            ttk.Label(frame_don_hang, text=item, bootstyle="secondary").grid(row=row_index, column=col_index, padx=5, pady=2)
        
        # Delete button
        delete_button = ttk.Button(frame_don_hang, text="nút xóa", bootstyle="danger")
        delete_button.grid(row=row_index, column=len(headers)-1, padx=5, pady=2)
