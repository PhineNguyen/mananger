import pandas as pd
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import Frame, LEFT, TOP, BOTH, X, Y
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_thong_ke_tab(notebook, app):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="THỐNG KÊ", padding=(10, 10))

    # Đọc dữ liệu từ file CSV
    customers_df, products_df, orders_df = load_data()

    if customers_df is None or products_df is None or orders_df is None:
        print("Lỗi: Không thể tải dữ liệu từ các file CSV.")
        return

    # Tạo khung chính chứa 4 hcn
    main_frame = Frame(tab)
    main_frame.pack(fill=BOTH, expand=True)

    # Tạo khung trên và dưới
    top_frame = Frame(main_frame)
    top_frame.pack(fill=BOTH, expand=True)
    
    bottom_frame = Frame(main_frame)
    bottom_frame.pack(fill=BOTH, expand=True)

    # Tạo Combobox để chọn biểu đồ
    chart_choice = ttk.Combobox(top_frame, values=["Số lượng sản phẩm theo nhóm", "Tỉ lệ phương thức thanh toán", "Tổng thu theo tháng"], state="readonly")
    chart_choice.pack(side=TOP, padx=5, pady=5)

    # Mặc định chọn biểu đồ đầu tiên
    chart_choice.set("Số lượng sản phẩm theo nhóm")

    # Tạo khung chứa biểu đồ
    chart_frame = Frame(bottom_frame)
    chart_frame.pack(fill=BOTH, expand=True)

    # Vẽ biểu đồ ban đầu
    plot_product_count_by_category(products_df, chart_frame)

    # Hàm xử lý thay đổi lựa chọn trong Combobox
    def on_chart_choice_changed(event):
        # Xóa biểu đồ hiện tại trong chart_frame
        for widget in chart_frame.winfo_children():
            widget.destroy()
        
        # Vẽ biểu đồ tương ứng với lựa chọn trong Combobox
        choice = chart_choice.get()
        if choice == "Số lượng sản phẩm theo nhóm":
            plot_product_count_by_category(products_df, chart_frame)
        elif choice == "Tỉ lệ phương thức thanh toán":
            plot_payment_methods(orders_df, chart_frame)
        elif choice == "Tổng thu theo tháng":
            plot_revenue_by_month(orders_df, chart_frame)

    # Gắn sự kiện thay đổi lựa chọn của Combobox
    chart_choice.bind("<<ComboboxSelected>>", on_chart_choice_changed)

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
    if 'Nhóm Sản Phẩm' not in products_df.columns:
        print("Lỗi: Cột 'Nhóm Sản Phẩm' không có trong dữ liệu sản phẩm.")
        return

    product_counts = products_df['Nhóm Sản Phẩm'].value_counts()

    fig, ax = plt.subplots(figsize=(3, 2))
    product_counts.plot(kind='bar', ax=ax, color='#5bc0de')

    ax.set_title("Số lượng sản phẩm theo nhóm")
    ax.set_xlabel("Nhóm Sản Phẩm")
    ax.set_ylabel("Số lượng")
    ax.set_xticklabels(product_counts.index, rotation=0, ha='right', fontsize=10)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)

    plt.close(fig)

def plot_payment_methods(orders_df, frame):
    if 'Phương Thức Thanh Toán' not in orders_df.columns:
        print("Lỗi: Cột 'Phương Thức Thanh Toán' không có trong dữ liệu đơn hàng.")
        return

    payment_counts = orders_df['Phương Thức Thanh Toán'].value_counts()

    fig, ax = plt.subplots(figsize=(3, 2))
    payment_counts.plot(
        kind='pie', 
        autopct='%1.1f%%',  
        startangle=140,
        ax=ax, 
        colors=['#5bc0de', '#20c997', '#B1C6B4']
    )

    ax.set_ylabel('')
    ax.set_title("Tỉ lệ phương thức thanh toán")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)

    plt.close(fig)

def plot_revenue_by_month(orders_df, frame):
    if 'Ngày Đặt Hàng' not in orders_df.columns or 'Tổng Giá Trị Đơn Hàng' not in orders_df.columns:
        print("Lỗi: Dữ liệu không đầy đủ. Cần có 'Ngày Đặt Hàng' và 'Tổng Giá Trị Đơn Hàng' trong đơn hàng.")
        return
    
    # Đảm bảo cột 'Ngày Đặt Hàng' có dạng datetime
    orders_df['Ngày Đặt Hàng'] = pd.to_datetime(orders_df['Ngày Đặt Hàng'], errors='coerce')

    # Lọc bỏ các giá trị NaT (lỗi khi không chuyển được sang datetime)
    orders_df = orders_df.dropna(subset=['Ngày Đặt Hàng'])
    
    # Thêm cột 'Tháng' để lấy tháng từ ngày đặt hàng
    orders_df['Tháng'] = orders_df['Ngày Đặt Hàng'].dt.month
    
    # Tính tổng doanh thu theo từng tháng
    monthly_revenue = orders_df.groupby('Tháng')['Tổng Giá Trị Đơn Hàng'].sum()
    
    # Tính tổng doanh thu theo từng tháng
    monthly_revenue = orders_df.groupby('Tháng')['Tổng Giá Trị Đơn Hàng'].sum() / 1_000_000  # Chia cho 1 triệu VND

    # Vẽ biểu đồ cột
    fig, ax = plt.subplots(figsize=(3, 2))
    monthly_revenue.plot(kind='bar', ax=ax, color='#20c997')
    
    ax.set_title("Tổng thu theo tháng trong năm")
    ax.set_xlabel("Tháng")
    ax.set_ylabel("Tổng thu (triệu VND)")
    ax.set_xticklabels([f'Tháng {int(month)}' for month in monthly_revenue.index], rotation=0, ha='center', fontsize=10)
    
    # Thêm giá trị lên trên các cột
    for i, value in enumerate(monthly_revenue):
        ax.text(i, value + 0.1, f'{value:.2f}', ha='center', va='bottom', fontsize=10)

    # Hiển thị biểu đồ trong ứng dụng Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)
    
    plt.close(fig)


