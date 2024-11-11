import pandas as pd
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import Frame, LEFT
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_thong_ke_tab(notebook, app):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="THỐNG KÊ", padding=(10, 10))

    # Đọc dữ liệu từ file CSV
    customers_df, products_df, orders_df = load_data()

    if customers_df is None or products_df is None or orders_df is None:
        print("Lỗi: Không thể tải dữ liệu từ các file CSV.")
        return

    # Tạo khung cho biểu đồ
    chart_frame = Frame(tab)
    chart_frame.pack(fill='both', expand=True)

    # Tạo khung con để đặt biểu đồ cạnh nhau
    left_frame = Frame(chart_frame)
    left_frame.pack(side=LEFT, fill='both', expand=True, padx=5, pady=5)
    right_frame = Frame(chart_frame)
    right_frame.pack(side=LEFT, fill='both', expand=True, padx=5, pady=5)

    # Vẽ các biểu đồ ban đầu
    plot_product_count_by_category(products_df, left_frame)
    plot_payment_methods(orders_df, right_frame)

def load_data():
    """Hàm để tải dữ liệu từ các file CSV."""
    try:
        customers_df = pd.read_csv('customers.csv', encoding='utf-8-sig')
        products_df = pd.read_csv('products.csv', encoding='utf-8-sig')
        orders_df = pd.read_csv('orders.csv', encoding='utf-8-sig')
        return customers_df, products_df, orders_df
    except FileNotFoundError as e:
        print(f"Không tìm thấy file: {e}")
        return None, None, None
def plot_product_count_by_category(products_df, frame):
    # Kiểm tra xem cột 'Nhóm Sản Phẩm' có trong dữ liệu không
    if 'Nhóm Sản Phẩm' not in products_df.columns:
        print("Lỗi: Cột 'Nhóm Sản Phẩm' không có trong dữ liệu sản phẩm.")
        return

    # Tính số lượng sản phẩm theo từng nhóm
    product_counts = products_df['Nhóm Sản Phẩm'].value_counts()

    # Tạo biểu đồ kích thước nhỏ hơn để phù hợp với giao diện
    fig, ax = plt.subplots(figsize=(3, 2))
    product_counts.plot(kind='bar', ax=ax, color='#5bc0de')  # Vẽ biểu đồ cột với màu xanh nhạt

    # Thiết lập tiêu đề và nhãn trục
    ax.set_title("Số lượng sản phẩm theo nhóm")
    ax.set_xlabel("Nhóm Sản Phẩm")
    ax.set_ylabel("Số lượng")

    # Chuyển biểu đồ thành canvas để hiển thị trên giao diện Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

    # Đóng biểu đồ để giải phóng bộ nhớ
    plt.close(fig)

def plot_payment_methods(orders_df, frame):
    # Kiểm tra xem cột 'Phương Thức Thanh Toán' có trong dữ liệu không
    if 'Phương Thức Thanh Toán' not in orders_df.columns:
        print("Lỗi: Cột 'Phương Thức Thanh Toán' không có trong dữ liệu đơn hàng.")
        return

    # Tính tỷ lệ các phương thức thanh toán
    payment_counts = orders_df['Phương Thức Thanh Toán'].value_counts()

    # Tạo biểu đồ tròn với kích thước nhỏ hơn để phù hợp với giao diện
    fig, ax = plt.subplots(figsize=(3, 2))
    payment_counts.plot(
        kind='pie', 
        autopct='%1.1f%%',  # Hiển thị phần trăm
        startangle=140,     # Góc bắt đầu của biểu đồ tròn
        ax=ax, 
        colors=['#5bc0de', '#20c997', '#B1C6B4']
    )

    # Xóa nhãn trục Y và thiết lập tiêu đề
    ax.set_ylabel('')
    ax.set_title("Tỉ lệ phương thức thanh toán")

    # Chuyển biểu đồ thành canvas để hiển thị trên giao diện Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

    # Đóng biểu đồ để giải phóng bộ nhớ
    plt.close(fig)

