import pandas as pd
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_thong_ke_tab(notebook, app):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Thống Kê")
    
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

    # Biểu đồ thống kê số lượng sản phẩm theo nhóm
    def plot_product_count_by_category():
        product_counts = products_df['Nhóm Sản Phẩm'].value_counts()
        fig, ax = plt.subplots(figsize=(6, 4))
        product_counts.plot(kind='bar', ax=ax, color='#5bc0de')
        ax.set_title("Số lượng sản phẩm theo nhóm")
        ax.set_xlabel("Nhóm Sản Phẩm")
        ax.set_ylabel("Số lượng")
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    # Biểu đồ giá trị đơn hàng trung bình
    def plot_average_order_value():
        avg_order_value = orders_df['Tổng Giá Trị Đơn Hàng'].mean()
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(['Trung bình giá trị đơn hàng'], [avg_order_value], color='#20c997')
        ax.set_title("Giá trị đơn hàng trung bình")
        ax.set_ylabel("VND")
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    # Biểu đồ phương thức thanh toán phổ biến
    def plot_payment_methods():
        payment_counts = orders_df['Phương Thức Thanh Toán'].value_counts()
        fig, ax = plt.subplots(figsize=(6, 4))
        payment_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, ax=ax, colors=['#5bc0de', '#20c997', '#B1C6B4'])
        ax.set_ylabel('')
        ax.set_title("Tỉ lệ phương thức thanh toán")
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    # Vẽ các biểu đồ
    plot_product_count_by_category()
    #plot_average_order_value()
    plot_payment_methods()
    


