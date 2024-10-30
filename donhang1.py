import tkinter as tk
from ttkbootstrap import ttk

# Tạo cửa sổ chính
app = tk.Tk()
app.title("Ứng dụng Quản Lý")

# Tạo notebook (tab control)
notebook = ttk.Notebook(app)
notebook.pack(fill="both", expand=True)

# Tạo các tab
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)

notebook.add(tab1, text="Sản phẩm")
notebook.add(tab2, text="Đơn hàng")
notebook.add(tab3, text="Thanh toán")
notebook.add(tab4, text="Thống kê")
notebook.add(tab5, text="Khách hàng")

# Tab 1: Sản phẩm
label1 = ttk.Label(tab1, text="Thông tin sản phẩm", font=("Helvetica", 16))
label1.pack(pady=10)

# Entry cho tên sản phẩm và giá
ttk.Label(tab1, text="Tên sản phẩm:").pack(pady=5)
product_name = ttk.Entry(tab1)
product_name.pack(pady=5)

ttk.Label(tab1, text="Giá sản phẩm:").pack(pady=5)
product_price = ttk.Entry(tab1)
product_price.pack(pady=5)

# Nút thêm sản phẩm
add_product_button = ttk.Button(tab1, text="Thêm sản phẩm")
add_product_button.pack(pady=10)

# Tab 2: Đơn hàng
label2 = ttk.Label(tab2, text="Danh sách đơn hàng", font=("Helvetica", 16))
label2.pack(pady=10)

# Treeview để hiển thị danh sách đơn hàng
order_tree = ttk.Treeview(tab2, columns=("Mã đơn", "Khách hàng", "Sản phẩm", "Giá"), show="headings")
order_tree.heading("Mã đơn", text="Mã đơn")
order_tree.heading("Khách hàng", text="Khách hàng")
order_tree.heading("Sản phẩm", text="Sản phẩm")
order_tree.heading("Giá", text="Giá")

order_tree.pack(fill="both", expand=True, pady=10)

# Tab 3: Thanh toán
label3 = ttk.Label(tab3, text="Thanh toán", font=("Helvetica", 16))
label3.pack(pady=10)

# Tab 4: Thống kê
label4 = ttk.Label(tab4, text="Thống kê", font=("Helvetica", 16))
label4.pack(pady=10)

# Tab 5: Khách hàng
label5 = ttk.Label(tab5, text="Thông tin khách hàng", font=("Helvetica", 16))
label5.pack(pady=10)

# Entry cho tên khách hàng
ttk.Label(tab5, text="Tên khách hàng:").pack(pady=5)
customer_name = ttk.Entry(tab5)
customer_name.pack(pady=5)

# Nút thêm khách hàng
add_customer_button = ttk.Button(tab5, text="Thêm khách hàng")
add_customer_button.pack(pady=10)

# Khởi chạy ứng dụng
app.mainloop()
