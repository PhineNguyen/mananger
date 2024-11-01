import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from don_hang import sample_data  # Import dữ liệu mẫu từ don_hang

def create_thong_ke_tab(notebook):
    # Tạo frame cho tab "Thống Kê"
    frame_thong_ke = ttk.Frame(notebook)
    notebook.add(frame_thong_ke, text="THỐNG KÊ")

    # Tiêu đề chính cho tab "Thống Kê"
    title_label = ttk.Label(
        frame_thong_ke, 
        text="Quản Lý Thống Kê", 
        bootstyle="primary-inverse", 
        font=("Helvetica", 18, "bold")
    )
    title_label.pack(pady=20)

    # Tạo frame phụ để nhóm các thông tin thống kê
    stats_frame = ttk.Frame(frame_thong_ke, padding=20, bootstyle="info")
    stats_frame.pack(padx=20, pady=10, fill=X)

    # Tính toán các thống kê dựa trên sample_data
    total_orders = len(sample_data)  # Tổng số đơn hàng
    total_revenue = sum(int(order[6].replace('.', '').replace(',', '')) for order in sample_data)  # Tổng doanh thu
    total_quantity = sum(int(order[5]) for order in sample_data)  # Tổng số lượng sản phẩm bán ra

    # Tạo nhãn và biểu tượng cho mỗi thống kê
    ttk.Label(
        stats_frame, 
        text="Tổng số đơn hàng:", 
        font=("Helvetica", 12), 
        bootstyle="info"
    ).grid(row=0, column=0, sticky=W, padx=5, pady=5)
    ttk.Label(
        stats_frame, 
        text=total_orders, 
        font=("Helvetica", 12, "bold"),
        bootstyle="success"
    ).grid(row=0, column=1, sticky=W, padx=5, pady=5)

    ttk.Label(
        stats_frame, 
        text="Tổng doanh thu:", 
        font=("Helvetica", 12), 
        bootstyle="info"
    ).grid(row=1, column=0, sticky=W, padx=5, pady=5)
    ttk.Label(
        stats_frame, 
        text=f"{total_revenue:,} VND", 
        font=("Helvetica", 12, "bold"), 
        bootstyle="success"
    ).grid(row=1, column=1, sticky=W, padx=5, pady=5)

    ttk.Label(
        stats_frame, 
        text="Tổng số lượng sản phẩm đã bán:", 
        font=("Helvetica", 12), 
        bootstyle="info"
    ).grid(row=2, column=0, sticky=W, padx=5, pady=5)
    ttk.Label(
        stats_frame, 
        text=total_quantity, 
        font=("Helvetica", 12, "bold"), 
        bootstyle="success"
    ).grid(row=2, column=1, sticky=W, padx=5, pady=5)

    # Khoảng trống cuối tab để cân bằng giao diện
    ttk.Label(frame_thong_ke, text="").pack(pady=10)
