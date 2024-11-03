import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from don_hang import sample_data  # Giả sử sample_data đã được cập nhật để chứa thông tin cần thiết

def create_thong_ke_tab(notebook):
    frame_thong_ke = ttk.Frame(notebook)
    notebook.add(frame_thong_ke, text="THỐNG KÊ")

    title_label = ttk.Label(
        frame_thong_ke, 
        text="Quản Lý Thống Kê", 
        bootstyle="primary-inverse", 
        font=("Helvetica", 18, "bold")
    )
    title_label.pack(pady=20)

    stats_frame = ttk.Frame(frame_thong_ke, padding=20, bootstyle="info")
    stats_frame.pack(padx=20, pady=10, fill=X)

    # Tính toán tổng tiền thu được
    total_revenue = sum(int(order[6].replace('.', '').replace(',', '')) * int(order[5]) for order in sample_data)

    # Hiển thị thông tin
    ttk.Label(
        stats_frame, 
        text="Tổng số tiền đã thu:", 
        font=("Helvetica", 12), 
        bootstyle="info"
    ).grid(row=0, column=0, sticky=W, padx=5, pady=5)
    ttk.Label(
        stats_frame, 
        text=f"{total_revenue:,} VND", 
        font=("Helvetica", 12, "bold"), 
        bootstyle="success"
    ).grid(row=0, column=1, sticky=W, padx=5, pady=5)

    # Hiển thị tên khách hàng và mã đơn hàng
    ttk.Label(stats_frame, text="Danh sách đơn hàng:", font=("Helvetica", 12, "bold")).grid(row=1, column=0, sticky=W, padx=5, pady=10, columnspan=2)

    for i, order in enumerate(sample_data, start=2):  # Bắt đầu từ hàng thứ 2
        customer_name = order[1]  # Tên khách hàng
        order_id = order[0]       # Mã đơn hàng
        ttk.Label(stats_frame, text=f"Khách hàng: {customer_name}, Mã đơn hàng: {order_id}", font=("Helvetica", 12)).grid(row=i, column=0, sticky=W, padx=5, pady=5)

    ttk.Label(frame_thong_ke, text="").pack(pady=10)
