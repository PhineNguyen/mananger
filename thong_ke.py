import pandas as pd
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import Frame, LEFT
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_thong_ke_tab(notebook, app):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="THỐNG KÊ", padding=(20,20))
    
    try:
        # Đọc dữ liệu từ các file CSV
        customers_df = pd.read_csv('customers.csv', encoding='utf-8-sig')
        products_df = pd.read_csv('products.csv', encoding='utf-8-sig')
        orders_df = pd.read_csv('orders.csv', encoding='utf-8-sig')
    except FileNotFoundError as e:
        print(f"Không tìm thấy file: {e}")
        return

    # Khung chứa biểu đồ
    chart_frame = Frame(tab)
    chart_frame.pack(fill='both', expand=True)

    # Tạo hai khung con để đặt biểu đồ ngang hàng
    left_frame = Frame(chart_frame)
    left_frame.pack(side=LEFT, fill='both', expand=True, padx=5, pady=5)

    right_frame = Frame(chart_frame)
    right_frame.pack(side=LEFT, fill='both', expand=True, padx=5, pady=5)

    # Hàm để cập nhật biểu đồ khi kích thước thay đổi
    def update_charts(event=None):
        for widget in left_frame.winfo_children():
            widget.destroy()  # Xóa các widget cũ trong khung trái
        for widget in right_frame.winfo_children():
            widget.destroy()  # Xóa các widget cũ trong khung phải

        width, height = left_frame.winfo_width(), left_frame.winfo_height()

        # Vẽ lại các biểu đồ với kích thước mới
        plot_product_count_by_category(left_frame, width, height)
        plot_payment_methods(right_frame, width, height)

    # Biểu đồ thống kê số lượng sản phẩm theo nhóm
    def plot_product_count_by_category(frame, width, height):
        product_counts = products_df['Nhóm Sản Phẩm'].value_counts()
        # Tăng chiều cao bằng cách nhân hệ số vào height (chẳng hạn tăng gấp đôi)
        fig, ax = plt.subplots(figsize=(width / 100, height / 150), constrained_layout=True)  # Sử dụng constrained_layout=True
        product_counts.plot(kind='bar', ax=ax, color='#5bc0de')
        ax.set_title("Số lượng sản phẩm theo nhóm")
        ax.set_xlabel("Nhóm Sản Phẩm")
        ax.set_ylabel("Số lượng")
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        plt.close(fig)  # Đóng biểu đồ sau khi vẽ

    # Biểu đồ phương thức thanh toán phổ biến
    def plot_payment_methods(frame, width, height):
        payment_counts = orders_df['Phương Thức Thanh Toán'].value_counts()
        fig, ax = plt.subplots(figsize=(width / 100, height / 200), constrained_layout=True)  # Sử dụng constrained_layout=True
        payment_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, ax=ax, colors=['#5bc0de', '#20c997', '#B1C6B4'])
        ax.set_ylabel('')
        ax.set_title("Tỉ lệ phương thức thanh toán")
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        plt.close(fig)  # Đóng biểu đồ sau khi vẽ

    # Gọi update_charts khi cửa sổ thay đổi kích thước
    chart_frame.bind("<Configure>", update_charts)

    # Vẽ các biểu đồ ban đầu
    update_charts()
