import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.messagebox as messagebox
import pandas as pd
from PIL import Image, ImageTk
from tkinter import StringVar
import csv
from setting import load_settings  # Import thêm load_settings
import tkinter as tk
from tkinter import messagebox

sample_data = []

# Lưu lại dữ liệu đơn hàng đã tính tổng giá trị vào file orders.csv
def save_orders_to_csv(filename, orders):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            header = ["ID Đơn Hàng", "ID Khách Hàng", "Ngày Đặt Hàng", "Danh Sách Sản Phẩm","Số Lượng Sản Phẩm", "Tổng Giá Trị Đơn Hàng", "Trạng Thái Đơn Hàng", "Phương Thức Thanh Toán"]
            writer.writerow(header)
            for order in orders:
                writer.writerow(order)
    except Exception as e:
        print(f"Lỗi khi lưu file đơn hàng: {e}")
def read_customers_csv(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Bỏ qua dòng tiêu đề
            return [row for row in reader]
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể đọc file customers.csv: {e}")
        return []
def load_product_data(filename):
    product_data = {}
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Bỏ qua header
            for row in reader:
                product_id = row[0]  # ID Sản Phẩm
                price = int(row[2])  # Giá
                product_data[product_id] = price  # Lưu vào dictionary
        return product_data
    except Exception as e:
        print(f"Lỗi khi đọc file sản phẩm: {e}")
        return {}

# Tính tổng giá trị đơn hàng từ dữ liệu đơn hàng, có tính đến số lượng sản phẩm
def calculate_order_total(order, product_data):
    total = 0
    product_ids = order[3].split(',')  # Danh sách ID Sản Phẩm trong đơn hàng (giả sử là chuỗi ngăn cách bằng dấu phẩy)
    quantities = order[4].split(',')  # Danh sách Số Lượng sản phẩm trong đơn hàng
    for product_id, quantity in zip(product_ids, quantities):
        quantity = int(quantity)  # Chuyển số lượng thành kiểu số nguyên
        if product_id in product_data:
            total += product_data[product_id] * quantity  # Nhân giá với số lượng
    return total

# Đọc dữ liệu từ file orders.csv và tính tổng giá trị đơn hàng
def process_orders(order_filename, product_data_filename):
    product_data = load_product_data(product_data_filename)  # Lấy dữ liệu sản phẩm
    orders = []
    try:
        with open(order_filename, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # Bỏ qua header
            for row in reader:
                order_id = row[0]  # ID Đơn Hàng
                customer_id = row[1]  # ID Khách Hàng
                order_date = row[2]  # Ngày Đặt Hàng
                product_list = row[3]  # Danh sách sản phẩm (ID sản phẩm)
                quantity_list = row[4]  # Danh sách số lượng sản phẩm
                total_value = calculate_order_total(row, product_data)  # Tính tổng giá trị đơn hàng
                status = row[7]  # Trạng thái đơn hàng
                payment_method = row[6]  # Phương thức thanh toán
                orders.append([order_id, customer_id, order_date, product_list,quantity_list ,total_value, status, payment_method])
    except Exception as e:
        print(f"Lỗi khi đọc file đơn hàng: {e}")
    return orders
order_filename = 'orders.csv'  # Đường dẫn tới file orders.csv
product_filename = 'products.csv'  # Đường dẫn tới file products.csv

# Xử lý các đơn hàng và tính tổng giá trị
orders = process_orders(order_filename, product_filename)


save_orders_to_csv(order_filename, orders)
# Hàm để chọn khách hàng
def choose_customer(entries):
    customers = read_customers_csv('customers.csv')
    customer_window = ttk.Toplevel()
    customer_window.title("Chọn Khách Hàng")
    
    # Tạo bảng hiển thị danh sách khách hàng
    customer_table = ttk.Treeview(customer_window, columns=("ID Khách Hàng", "Tên Khách Hàng", "Email"), show="headings")
    customer_table.heading("ID Khách Hàng", text="ID Khách Hàng")
    customer_table.heading("Tên Khách Hàng", text="Tên Khách Hàng")
    customer_table.heading("Email", text="Email")
    
    # Thêm dữ liệu vào bảng
    for customer in customers:
        customer_table.insert("", "end", values=customer)
    
    customer_table.pack(fill="both", expand=True)

    # Hàm điền ID Khách Hàng vào ô nhập liệu
    def select_customer(event):
        selected_item = customer_table.selection()
        if selected_item:
            customer_id = customer_table.item(selected_item)["values"][0]
            entries["ID Khách Hàng"].delete(0, "end")
            entries["ID Khách Hàng"].insert(0, customer_id)
            customer_window.destroy()
    
    customer_table.bind("<Double-1>", select_customer)  # Chọn khách hàng bằng double-click

def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df.values.tolist()
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể đọc file: {e}")
        return []

def save_to_csv(filename):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Define header
            header = ["ID Đơn Hàng", "ID Khách Hàng", "Ngày Đặt Hàng", "Danh Sách Sản Phẩm", "Số Lượng Sản Phẩm", "Tổng Giá Trị Đơn Hàng", "Trạng Thái Đơn Hàng", "Phương Thức Thanh Toán"]
            writer.writerow(header)
            
            # Write the order data
            for order in sample_data:
                writer.writerow(order)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu file: {e}")

def button_click(button_name, app):
    if button_name == "Tìm kiếm":
        search_order()
    elif button_name == "Thêm đơn":
        add_order(app)
    elif button_name == "Sửa":
        edit_order(app)
    elif button_name == "Xóa":
        delete_order()

def create_don_hang_tab(notebook, app):
    # Khai báo biến toàn cục để sử dụng trong các phần khác của chương trình
    global order_table, search_entry

    # Tạo một frame cho tab ĐƠN HÀNG và thêm vào notebook
    frame_order = ttk.Frame(notebook)
    notebook.add(frame_order, text="ĐƠN HÀNG", padding=(10,10))

    # Tải các hình ảnh icon và thay đổi kích thước thành 20x20 pixels
    image = Image.open("icon/search.png").resize((20, 20), Image.LANCZOS)
    search_icon = ImageTk.PhotoImage(image)

    image2 = Image.open("icon/multiple.png").resize((20, 20), Image.LANCZOS)
    multiple_icon = ImageTk.PhotoImage(image2)

    image3 = Image.open("icon/wrenchalt.png").resize((20, 20), Image.LANCZOS)
    wrenchalt_icon = ImageTk.PhotoImage(image3)

    image4 = Image.open("icon/trash.png").resize((20, 20), Image.LANCZOS)
    trash_icon = ImageTk.PhotoImage(image4)
    
    # Tạo biến StringVar để lưu giá trị nhập vào của ô tìm kiếm
    search_value = StringVar()
    
    # Tạo ô nhập (Entry) để tìm kiếm đơn hàng
    search_entry = ttk.Entry(frame_order, bootstyle="superhero", width=30, textvariable=search_value)
    search_entry.insert(0, "Tìm kiếm theo id khách hàng")  # Văn bản mặc định trong ô tìm kiếm
    search_entry.config(foreground="grey")
    search_entry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Hàm xử lý khi nhấp vào entry tìm kiếm (FocusIn)
    def on_focus_in(event):
        if search_entry.get() == "Tìm kiếm theo tên sản phẩm":
            search_entry.delete(0, "end")
            search_entry.config(foreground="black")

# Hàm xử lý khi rời khỏi entry tìm kiếm (FocusOut)
    def on_focus_out(event):
        if search_entry.get() == "":
            search_entry.insert(0, "Tìm kiếm theo tên sản phẩm")
            search_entry.config(foreground="grey")

# Gán sự kiện FocusIn và FocusOut cho entry tìm kiếm
    search_entry.bind("<FocusIn>", on_focus_in)
    search_entry.bind("<FocusOut>", on_focus_out)

    search_entry.bind("<Return>", lambda event: button_click("Tìm kiếm", app))  # Kích hoạt tìm kiếm khi nhấn Enter

    # Tạo nút Tìm kiếm với icon và liên kết hàm button_click khi nhấn
    search_button = ttk.Button(frame_order, text="Tìm kiếm", bootstyle="superhero", image=search_icon, compound=LEFT, cursor="hand2", command=lambda: button_click("Tìm kiếm",app))
    search_button.grid(row=0, column=1, padx=5, pady=5, sticky=W)
    frame_order.search_icon = search_icon  # Để giữ tham chiếu đến icon, tránh bị thu hồi bộ nhớ

    # Tạo nút Thêm đơn với icon và liên kết hàm button_click khi nhấn
    add_order_button = ttk.Button(frame_order, text="Thêm đơn", bootstyle="superhero", image=multiple_icon, compound=LEFT, command=lambda: button_click("Thêm đơn", app), cursor="hand2")
    add_order_button.grid(row=0, column=2, padx=5, pady=5, sticky=W)
    frame_order.multiple_icon = multiple_icon

    # Tạo nút Sửa với icon và liên kết hàm button_click khi nhấn
    edit_order_button = ttk.Button(frame_order, text="Sửa", bootstyle="superhero", image=wrenchalt_icon, compound=LEFT, command=lambda: button_click("Sửa", app), cursor="hand2")
    edit_order_button.grid(row=0, column=3, padx=5, pady=5, sticky=W)
    frame_order.wrenchalt_icon = wrenchalt_icon

    # Tạo nút Xóa với icon và liên kết hàm delete_order khi nhấn
    delete_order_button = ttk.Button(frame_order, text="Xóa", bootstyle="superhero", image=trash_icon, compound=LEFT, command=delete_order, cursor="hand2")
    delete_order_button.grid(row=0, column=4, padx=5, pady=5, sticky=W)
    frame_order.trash_icon = trash_icon

    create_filter_controls_order(frame_order)

    # Định nghĩa các cột cho bảng order_table
    columns = ["ID Đơn Hàng", "ID Khách Hàng", "Ngày Đặt Hàng", "Danh Sách Sản Phẩm","Số Lượng Sản Phẩm", "Tổng Giá Trị Đơn Hàng", "Trạng Thái Đơn Hàng", "Phương Thức Thanh Toán"]
    order_table = ttk.Treeview(frame_order, columns=columns, show="headings", bootstyle="superhero")
    order_table.grid(row=2, column=0, columnspan=5, padx=5, pady=5, sticky="ns")

    # Thiết lập tiêu đề và căn chỉnh cho các cột trong bảng
    for col in columns:
        order_table.heading(col, text=col)
        if col in ["Trạng Thái Đơn Hàng", "Phương Thức Thanh Toán", "Danh Sách Sản Phẩm"]:
            order_table.column(col, anchor='w')  # Căn trái cho các cột này 
        else:
            order_table.column(col, anchor='center')  # Căn giữa cho các cột còn lại

    # Thêm Scrollbar dọc
    y_scrollbar = ttk.Scrollbar(frame_order, orient=VERTICAL, command=order_table.yview)
    y_scrollbar.grid(row=2, column=5, sticky="ns")
    order_table.configure(yscrollcommand=y_scrollbar.set)

    # Thêm Scrollbar ngang
    x_scrollbar = ttk.Scrollbar(frame_order, orient=HORIZONTAL, command=order_table.xview)
    x_scrollbar.grid(row=3, column=0, columnspan=5, sticky="ew")
    order_table.configure(xscrollcommand=x_scrollbar.set)


    # Hàm cập nhật bố cục khi thay đổi kích thước cửa sổ
    def update_layout(event=None):
        window_width = frame_order.winfo_width()
        window_height = frame_order.winfo_height()
        
        if window_width >= 1000 and window_height >= 600:  # Kích thước tùy ý cho chế độ toàn màn hình
            order_table.grid(sticky="nsew")  # Mở rộng cả chiều dọc và chiều ngang
            frame_order.grid_rowconfigure(2, weight=1)  # Mở rộng chiều dọc
            frame_order.grid_columnconfigure(0, weight=1)  # Mở rộng chiều ngang
        else:
            order_table.grid(sticky="ns")  # Mở rộng chỉ theo chiều dọc
            frame_order.grid_rowconfigure(2, weight=1)  # Mở rộng chiều dọc, không thay đổi chiều ngang
            frame_order.grid_columnconfigure(0, weight=1)  # Không mở rộng chiều ngang


    # Ràng buộc sự kiện cấu hình kích thước cửa sổ
    frame_order.bind("<Configure>", update_layout)

    #dbclick để xem chi tiết
    def show_product_details(event):
        """
        Hàm hiển thị cửa sổ chi tiết sản phẩm khi người dùng nhấp đúp vào một hàng trong bảng.
        """
        # Lấy ID của hàng đang được chọn
        selected_item = order_table.selection()
        if not selected_item:
            return

        # Lấy thông tin của hàng được chọn
        item_data = order_table.item(selected_item, "values")

        # Tạo cửa sổ Toplevel để hiển thị thông tin
        detail_window = ttk.Toplevel()
        detail_window.title("Thông tin chi tiết sản phẩm")
        #detail_window.geometry("600x300")  # Kích thước cửa sổ tùy ý

        # Hiển thị thông tin chi tiết của sản phẩm
        labels = ["ID Đơn Hàng", "ID Khách Hàng", "Ngày Đặt Hàng", "Danh Sách Sản Phẩm","Số Lượng Sản Phẩm", "Tổng Giá Trị Đơn Hàng", "Trạng Thái Đơn Hàng", "Phương Thức Thanh Toán"]
        for i, label_text in enumerate(labels):
            label = tk.Label(detail_window, text=f"{label_text}: {item_data[i]}", font=("Helvetica", 12))
            label.pack(anchor="w", padx=10, pady=5)

        # Đặt button đóng cửa sổ
        close_button = tk.Button(detail_window, text=" Xong ", command=detail_window.destroy)
        close_button.pack(pady=10)
        
        # Cập nhật kích thước của cửa sổ theo nội dung
        detail_window.update_idletasks()
        detail_window.geometry(f"{detail_window.winfo_width()}x{detail_window.winfo_height()}")

    # Gán sự kiện double-click vào bảng
    order_table.bind("<Double-1>", show_product_details)

    # Gọi hàm để tải dữ liệu ban đầu vào bảng
    refresh_order_table()
    
    # Thiết lập khung chứa bảng để tự động thay đổi kích thước khi giao diện mở rộng
    frame_order.grid_rowconfigure(2, weight=1)
    frame_order.grid_columnconfigure(0, weight=1)


def load_image(image_path):
    try:
        image = Image.open(image_path)
        image = image.resize((20, 20), Image.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tải hình ảnh: {e}")
        return None

def get_customer_ids(file_path):
    """
    Đọc file CSV và trả về danh sách ID khách hàng từ file.
    """
    customer_ids = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                customer_ids.append(row['ID Khách Hàng'])  # Sử dụng tên cột trong file CSV
    except FileNotFoundError:
        print(f"Không tìm thấy file {file_path}")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
    
    return customer_ids

def create_filter_controls_order(frame_order, file_path="orders.csv"):
    """
    Hàm tạo bộ lọc dữ liệu cho bảng Đơn Hàng.
    """
    # Tạo frame chứa các bộ lọc
    filter_frame = ttk.Frame(frame_order)
    filter_frame.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky="w")

    # Bộ lọc theo trạng thái đơn hàng
    order_status_label = ttk.Label(filter_frame, text="Trạng Thái Đơn Hàng:")
    order_status_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
    order_status_var = StringVar()
    order_status_filter = ttk.Combobox(filter_frame, textvariable=order_status_var, state="readonly", width=15)
    order_status_filter["values"] = ["Tất cả", "Chờ xử lý", "Đang giao", "Đã hoàn thành", "Đã hủy"]
    order_status_filter.current(0)
    order_status_filter.grid(row=0, column=3, padx=5, pady=5, sticky="w")

    # Bộ lọc theo phương thức thanh toán
    payment_method_label = ttk.Label(filter_frame, text="Phương Thức Thanh Toán:")
    payment_method_label.grid(row=0, column=4, padx=5, pady=5, sticky="w")
    payment_method_var = StringVar()
    payment_method_filter = ttk.Combobox(filter_frame, textvariable=payment_method_var, state="readonly", width=15)
    payment_method_filter["values"] = ["Tất cả", "Thanh toán khi nhận hàng", "Chuyển khoản", "Thanh toán qua ví điện tử"]
    payment_method_filter.current(0)
    payment_method_filter.grid(row=0, column=5, padx=5, pady=5, sticky="w")

    # Bộ lọc theo khoảng ngày
    date_label = ttk.Label(filter_frame, text="Khoảng Ngày:")
    date_label.grid(row=0, column=6, padx=5, pady=5, sticky="w")
    
    start_date_var = StringVar()
    start_date_entry = ttk.Entry(filter_frame, textvariable=start_date_var, width=10)
    start_date_entry.grid(row=0, column=7, padx=5, pady=5, sticky="w")

    end_date_var = StringVar()
    end_date_entry = ttk.Entry(filter_frame, textvariable=end_date_var, width=10)
    end_date_entry.grid(row=0, column=8, padx=5, pady=5, sticky="w")

    # Nút áp dụng bộ lọc
    def apply_filters_order():
        """
        Hàm áp dụng bộ lọc lên bảng Đơn Hàng.
        """
        order_status = order_status_var.get()
        payment_method = payment_method_var.get()
        start_date = start_date_var.get()
        end_date = end_date_var.get()

        # Lọc dữ liệu từ `sample_orders`
        filtered_orders = []
        for order in sample_data:  # sample_orders là danh sách dữ liệu gốc
            order_id, customer_id_order, order_date, product_list, quantity_list, total_price, status, payment_method_order = order
            order_date = str(order_date)  # Chuyển ngày thành chuỗi để so sánh

            # Kiểm tra điều kiện lọc
            if order_status != "Tất cả" and order_status != status:
                continue
            if payment_method != "Tất cả" and payment_method != payment_method_order:
                continue
            if start_date and order_date < start_date:
                continue
            if end_date and order_date > end_date:
                continue

            filtered_orders.append(order)

        # Cập nhật bảng với dữ liệu đã lọc
        refresh_order_table(filtered_orders)

    # Nút "Áp dụng" để áp dụng bộ lọc
    apply_button_order = ttk.Button(filter_frame, text="Áp dụng", bootstyle="superhero", command=apply_filters_order, cursor="hand2")
    apply_button_order.grid(row=0, column=9, padx=5, pady=5, sticky="w")

    # Nút "Xóa Lọc"
    def clear_filters_order():
        """
        Hàm xóa bộ lọc và trả bảng về trạng thái ban đầu (không lọc).
        """
        # Reset các giá trị của bộ lọc
        order_status_var.set("Tất cả")
        payment_method_var.set("Tất cả")
        start_date_var.set("")
        end_date_var.set("")

        # Cập nhật bảng với dữ liệu gốc
        refresh_order_table(sample_data)

    clear_button_order = ttk.Button(filter_frame, text="Xóa Lọc", bootstyle="danger", command=clear_filters_order, cursor="hand2")
    clear_button_order.grid(row=0, column=10, padx=5, pady=5, sticky="w")

    # Tạo frame riêng để chứa nút thu gọn bộ lọc
    toggle_frame = ttk.Frame(frame_order)
    toggle_frame.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    # Biến trạng thái thu gọn bộ lọc
    filter_expanded = True

    # Hàm thu gọn và mở rộng bộ lọc
    def toggle_filter():
        nonlocal filter_expanded

        if filter_expanded:
            # Thu gọn bộ lọc: Ẩn toàn bộ dòng chứa bộ lọc
            filter_frame.grid_forget()  # Ẩn toàn bộ frame chứa bộ lọc
            toggle_button.config(text="Mở rộng bộ lọc")  # Đổi tên nút
            filter_expanded = False
        else:
            # Mở rộng bộ lọc: Hiển thị lại toàn bộ frame chứa bộ lọc
            filter_frame.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky="w")
            toggle_button.config(text="Thu gọn bộ lọc")  # Đổi tên nút
            filter_expanded = True

    # Nút thu gọn bộ lọc sẽ được thêm vào frame riêng biệt
    toggle_button = ttk.Button(toggle_frame, text="Thu gọn bộ lọc", bootstyle="info", command=toggle_filter, cursor="hand2")
    toggle_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    filter_frame.grid_forget()  # Ẩn toàn bộ frame chứa bộ lọc
    toggle_button.config(text="Mở rộng bộ lọc")  # Đổi tên nút
    filter_expanded = False

# Cập nhật hàm refresh_product_table để hỗ trợ dữ liệu lọc
def refresh_order_table(filtered_products=None):
    """
    Hàm làm mới bảng sản phẩm với dữ liệu gốc hoặc đã lọc.
    """
    # Xóa dữ liệu cũ trong bảng
    for row in order_table.get_children():
        order_table.delete(row)

    # Dữ liệu để hiển thị
    data = filtered_products if filtered_products is not None else sample_data

    # Thêm dữ liệu vào bảng
    for product in data:
        order_table.insert("", "end", values=product)
    update_row_colors()



# def refresh_order_table():
#     for row in order_table.get_children():
#         order_table.delete(row)
#     for order in sample_data:
#         order_table.insert("", "end", values=order)
#     update_row_colors()

def update_row_colors():
    # Tải cài đặt từ file
    current_settings = load_settings()
    theme = current_settings.get('theme', 'minty')  # Mặc định là 'minty' nếu không có theme nào
    font_name = current_settings.get('font', 'Helvetica')  # Mặc định là 'Helvetica' nếu không có trong config
    font_size = current_settings.get('font_size', 14)     # Mặc định là 14 nếu không có trong config

    # Cấu hình màu sắc dựa trên theme
    theme_colors = {
        "minty": {"foreground": "#000000", "background_even": "#e8f5e9", "background_odd": "#ffffff"},
        "flatly": {"foreground": "#2c3e50", "background_even": "#f8f9fa", "background_odd": "#ffffff"},
        "darkly": {"foreground": "#ffffff", "background_even": "#343a40", "background_odd": "#23272b"},
        "pulse": {"foreground": "#495057", "background_even": "#e1e8f0", "background_odd": "#ffffff"},
        "solar": {"foreground": "#657b83", "background_even": "#fdf6e3", "background_odd": "#ffffff"},
    }

    # Lấy màu chữ và nền theo theme
    colors = theme_colors.get(theme, theme_colors["minty"])
    font_color = colors["foreground"]
    background_even = colors["background_even"]
    background_odd = colors["background_odd"]

    # Tạo tag cho font với font cố định là 'superhero' và màu chữ thay đổi theo theme
    order_table.tag_configure("custom_font1", font=(font_name, font_size), background=background_even, foreground=font_color)
    order_table.tag_configure("custom_font2", font=(font_name, font_size), background=background_odd, foreground=font_color)

    # Áp dụng các tag xen kẽ để tạo màu nền cho các dòng
    for index, item in enumerate(order_table.get_children()):
        if index % 2 == 0:
            order_table.item(item, tags=('custom_font1',))
        else:
            order_table.item(item, tags=('custom_font2',))
    update_row_height(font_size)

def update_row_height(font_size):
    # Tạo kiểu tùy chỉnh cho bảng Treeview
    style = ttk.Style()

    # Cài đặt chiều cao của các hàng (row height) cho Treeview
    row_height = font_size*2  # Tính toán chiều cao hàng dựa trên cỡ chữ

    # Áp dụng kiểu cho bảng Treeview
    style.configure("Custom.Treeview", rowheight=row_height)

    # Cập nhật style của product_table
    order_table.configure(style="Custom.Treeview")

def search_order():
    search_value = search_entry.get().strip().lower()  # Lấy giá trị tìm kiếm và chuyển về chữ thường
    
    # Xóa toàn bộ các hàng trong bảng trước khi hiển thị kết quả tìm kiếm
    for row in order_table.get_children():
        order_table.delete(row)

    # Tìm các đơn hàng khớp với ID đơn hàng trong cột đầu tiên (ID Đơn Hàng)
    # chuyển qua tìm bằng id khách hàng
    matched_orders = [order for order in sample_data if search_value in str(order[1]).lower()]

    # Hiển thị các đơn hàng khớp trong bảng
    for order in matched_orders:
        order_table.insert("", "end", values=order)

    # Cập nhật màu sắc hàng (nếu có) để đảm bảo giao diện đồng nhất
    update_row_colors()


####################################################################################
def add_order(app):
    # Tạo cửa sổ "Thêm Đơn Hàng" mới
    add_window = ttk.Toplevel(app)
    add_window.title("Thêm Đơn Hàng")

    # Danh sách các trường thông tin cần nhập cho đơn hàng
    fields = ["ID Đơn Hàng", "ID Khách Hàng", "Ngày Đặt Hàng", "Danh Sách Sản Phẩm","Số Lượng Sản Phẩm","Tổng Giá Trị Đơn Hàng", "Trạng Thái Đơn Hàng", "Phương Thức Thanh Toán"]
    entries = {}  # Tạo dictionary để lưu các entry widget

    def calculate_total():
        try:
            # Lấy giá trị từ trường "Số Lượng Sản Phẩm"
            quantity_str = entries["Số Lượng Sản Phẩm"].get().strip()

            quantity_str = int(quantity_str)

            # # Kiểm tra nếu ô trống hoặc không phải số nguyên dương
            # if not quantity_str.isdigit() or int(quantity_str) <= 0:
            #     raise ValueError("Số lượng phải là số nguyên dương lớn hơn 0.")

            quantity = int(quantity_str)  # Chuyển thành số nguyên

            # Lấy giá trị từ trường "Danh Sách Sản Phẩm"
            product_id = entries["Danh Sách Sản Phẩm"].get().strip()

            # Đọc danh sách sản phẩm từ file CSV
            products = read_csv("products.csv")
            price = 0

            # Tìm giá sản phẩm dựa trên ID
            for product in products:
                if str(product[0]) == str(product_id):  # So khớp ID sản phẩm
                    price = int(product[2])  # Giá sản phẩm
                    break

            # Tính tổng giá trị
            total_value = price * quantity
            

            # Hiển thị vào ô "Tổng Giá Trị Đơn Hàng"
            entries["Tổng Giá Trị Đơn Hàng"].delete(0, 'end')
            entries["Tổng Giá Trị Đơn Hàng"].insert(0, str(total_value))

        except ValueError as ve:
            messagebox.showerror("Lỗi", f"Hãy nhập số lượng dcm")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

    # Tạo các nhãn và entry widget cho mỗi trường thông tin
    for i, field in enumerate(fields):
        label = ttk.Label(add_window, text=field)  # Tạo nhãn cho trường
        label.grid(row=i, column=0, padx=10, pady=5)  # Đặt nhãn vào lưới
        # entry = ttk.Entry(add_window, bootstyle="superhero", width=30)  # Tạo entry cho trường
        # entry.grid(row=i, column=1, padx=10, pady=5)  # Đặt entry vào lưới
        # entries[field] = entry  # Lưu entry vào dictionary với khóa là tên trường


        # Sử dụng Combobox cho "Phương Thức Thanh Toán" với ba tùy chọn
        if field == "Trạng Thái Đơn Hàng":
            payment_method = ttk.Combobox(add_window, values=["Đang Xử Lý", "Đã Giao", "Đã Hủy"], state="readonly",width=28)
            payment_method.grid(row=i, column=1, padx=10, pady=5)
            entries[field] = payment_method  # Lưu combobox vào dictionary với khóa là tên trường
        elif field == "Phương Thức Thanh Toán":
            payment_method = ttk.Combobox(add_window, values=["Tiền mặt", "Thẻ tín dụng", "Chuyển khoản"], state="readonly",width=28)
            payment_method.grid(row=i, column=1, padx=10, pady=5)
            entries[field] = payment_method  # Lưu combobox vào dictionary với khóa là tên trường
        elif field == "Số Lượng Sản Phẩm":
            quantity_spinbox = ttk.Spinbox(add_window, from_=1, to=100, width=26, command=calculate_total, increment=1)  # Spinbox cho số lượng sản phẩm
            quantity_spinbox.set(1)  # Thiết lập giá trị ban đầu là 1
            quantity_spinbox.grid(row=i, column=1, padx=10, pady=5)
            entries[field] = quantity_spinbox
        else:
            entry = ttk.Entry(add_window, bootstyle="superhero", width=30)  # Tạo entry cho các trường khác
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[field] = entry  # Lưu entry vào dictionary với khóa là tên trường

        # Thêm nút chọn khách hàng bên cạnh ô "ID Khách Hàng"
        if field == "ID Khách Hàng":
            choose_button = ttk.Button(add_window, text="Chọn", command=lambda: choose_customer(entries))
            choose_button.grid(row=i, column=2, padx=5)

    # Hàm để mở cửa sổ chọn sản phẩm
    def select_products():
        product_window = ttk.Toplevel(add_window)  # Tạo cửa sổ "Chọn Sản Phẩm" mới
        product_window.title("Chọn Sản Phẩm")

        # Tải danh sách sản phẩm từ file CSV
        products = read_csv("products.csv")

        # Tạo bảng hiển thị danh sách sản phẩm với các cột ID, Tên và Giá
        product_table = ttk.Treeview(
            product_window, columns=("ID", "Tên", "Giá", "Tồn Kho"), show="headings", selectmode="browse"
        )
        product_table.heading("ID", text="ID")  # Cột ID
        product_table.heading("Tên", text="Tên Sản Phẩm")  # Cột tên sản phẩm
        product_table.heading("Giá", text="Giá VND")  # Cột giá sản phẩm
        product_table.heading("Tồn Kho", text="Số Lượng Tồn Kho")  # Cột tồn kho
        product_table.pack(fill="both", expand=True)  # Đặt bảng vào cửa sổ, mở rộng đầy đủ

        # Thêm các sản phẩm vào bảng
        for product in products:
            product_table.insert("", "end", values=(product[0], product[1], product[2], product[3]))

        # Hàm để thêm sản phẩm được chọn vào đơn hàng
        def add_selected_product():
            selected_item = product_table.selection()
            if not selected_item:
                messagebox.showwarning("Cảnh báo", "Vui lòng chọn một sản phẩm.")
                return

            selected_product = product_table.item(selected_item[0])["values"]

            # Cập nhật trường "Danh Sách Sản Phẩm" với ID sản phẩm
            entries["Danh Sách Sản Phẩm"].delete(0, 'end')
            entries["Danh Sách Sản Phẩm"].insert(0, str(selected_product[0]))

            # Cập nhật trường "Tổng Giá Trị Đơn Hàng" với giá sản phẩm
            entries["Tổng Giá Trị Đơn Hàng"].delete(0, 'end')
            entries["Tổng Giá Trị Đơn Hàng"].insert(0, str(selected_product[2]))

            # Cập nhật giới hạn cho Spinbox
            max_quantity = int(selected_product[3])  # Lấy số lượng tồn kho
            entries["Số Lượng Sản Phẩm"].config(to=max_quantity)  # Cập nhật giới hạn Spinbox

            # Tính tổng giá trị đơn hàng ngay sau khi chọn sản phẩm
            calculate_total()

            product_window.destroy()  # Đóng cửa sổ chọn sản phẩm

        # Nút để xác nhận chọn sản phẩm
        select_button = ttk.Button(product_window, text="Chọn Sản Phẩm", command=add_selected_product)
        select_button.pack(pady=10)


        

    # Nút "Chọn Sản Phẩm" trong cửa sổ "Thêm Đơn Hàng", mở cửa sổ chọn sản phẩm
    product_select_button = ttk.Button(add_window, text="Chọn Sản Phẩm",  bootstyle="superhero", command=select_products)
    product_select_button.grid(row=fields.index("Danh Sách Sản Phẩm"), column=2, padx=10, pady=5)

    # Hàm để lưu đơn hàng mới vào danh sách và file CSV

    def submit_order():
        # Lấy thông tin từ các trường và kiểm tra xem có trường nào bỏ trống không
        try:
            new_order = tuple(entries[field].get().strip() for field in fields)
        except AttributeError as e:
            print(f"Lỗi khi lấy giá trị từ trường: {e}")
            return

        if any(not value for value in new_order):
            messagebox.showerror("Lỗi", "Vui lòng không để trống các trường.")  # Hiển thị lỗi nếu bỏ trống
            return
        
        # Kiểm tra xem ID đơn hàng đã tồn tại chưa
        new_order_id = new_order[0]  # ID đơn hàng là phần tử đầu tiên
        for order in sample_data:
            order_id = str(order[0])  # ID đơn hàng nằm ở vị trí đầu tiên của mỗi danh sách con
            if order_id == new_order_id:  # Nếu ID đã tồn tại
                messagebox.showerror("Lỗi", "ID Đơn Hàng đã tồn tại. Vui lòng nhập ID khác.")
                entries["ID Đơn Hàng"].delete(0, 'end')
                return

        # Tải danh sách sản phẩm từ file
        products = read_csv("products.csv")
        product_id = new_order[3]  # ID sản phẩm
        quantity_ordered = int(new_order[4])  # Số lượng sản phẩm đã đặt
        updated_products = []  # Danh sách sản phẩm sau khi cập nhật tồn kho

        # Cập nhật tồn kho
        for product in products:
            if str(product[0]) == product_id:  # Nếu đúng sản phẩm được đặt
                current_stock = int(product[3])  # Số lượng tồn kho hiện tại
                if quantity_ordered > current_stock:  # Nếu số lượng đặt lớn hơn tồn kho
                    messagebox.showerror("Lỗi", f"Số lượng đặt ({quantity_ordered}) vượt quá số lượng tồn kho ({current_stock}).")
                    return
                product[3] = str(current_stock - quantity_ordered)  # Cập nhật số lượng tồn kho
            updated_products.append(product)

        # Lưu danh sách sản phẩm đã cập nhật vào file CSV
        with open("products.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            header = ["ID Sản Phẩm", "Tên Sản Phẩm", "Giá VND", "Số Lượng Tồn Kho", "Mô Tả", "Nhóm Sản Phẩm"]  # Thay đổi theo các cột của bạn
            writer.writerow(header)
            writer.writerows(updated_products)

        # Thêm đơn hàng vào danh sách tạm thời và lưu vào file CSV
        sample_data.append(new_order)
        save_to_csv("orders.csv")  # Lưu đơn hàng vào file CSV

        # Cập nhật biến tạm
        sample_data.clear()
        sample_data.extend(read_csv("orders.csv"))

        refresh_order_table()  # Cập nhật bảng đơn hàng

        # Cập nhật lịch sử mua hàng cho khách hàng
        order_id = new_order[0]
        customer_id = new_order[1]
        update_customer_purchase_history(customer_id, order_id)

        # Đóng cửa sổ thêm đơn hàng
        add_window.destroy()


    def update_customer_purchase_history(customer_id, order_id):
        # Đọc dữ liệu từ file customers.csv
        customers = []
        with open("customers.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)  # Đọc dòng tiêu đề
            for row in reader:
                if row[0] == customer_id:
                    # Cập nhật lịch sử mua hàng bằng cách thêm ID đơn hàng mới
                    if row[5]:  # Nếu đã có lịch sử, nối thêm ID đơn hàng
                        row[5] += f", {order_id}"
                    else:  # Nếu chưa có lịch sử, gán ID đơn hàng mới
                        row[5] = order_id
                customers.append(row)

        # Ghi lại dữ liệu đã cập nhật vào file customers.csv
        with open("customers.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)  # Ghi dòng tiêu đề
            writer.writerows(customers)  # Ghi dữ liệu khách hàng đã cập nhật
    
    


    # Nút "Thêm" để xác nhận thêm đơn hàng mới
    add_button = ttk.Button(add_window, text="Thêm", bootstyle="superhero", command=submit_order)
    add_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

def edit_order(app):
    selected_item = order_table.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một đơn hàng để sửa.")
        return

    order_data = order_table.item(selected_item)["values"]
    edit_window = ttk.Toplevel(app)
    edit_window.title("Sửa Đơn Hàng")

    fields = ["ID Đơn Hàng", "ID Khách Hàng", "Ngày Đặt Hàng", "Danh Sách Sản Phẩm","Số Lượng Sản Phẩm", "Tổng Giá Trị Đơn Hàng", "Trạng Thái Đơn Hàng", "Phương Thức Thanh Toán"]
    entries = {}

    for i, field in enumerate(fields):
        label = ttk.Label(edit_window, text=field)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = ttk.Entry(edit_window, bootstyle="superhero", width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, order_data[i])
        entries[field] = entry

    def submit_edit():
        edited_order = tuple(entries[field].get().strip() for field in fields)
        for i, value in enumerate(edited_order):
            if value != order_data[i]:
                # Update the order data
                sample_data[sample_data.index(order_data)] = edited_order
                break
        
        save_to_csv('orders.csv')
        refresh_order_table()
        edit_window.destroy()

    edit_button = ttk.Button(edit_window, text="Sửa", bootstyle="superhero", command=submit_edit)
    edit_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

def delete_order():
    selected_item = order_table.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn đơn hàng cần xóa.")
        return

    confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa đơn hàng này?")
    if confirm:
        selected_indices = sorted([order_table.index(item)for item in selected_item], reverse=True)
        for index in selected_indices:
            del sample_data[index]
        
        for item in selected_item:
            order_table.delete(item)

        refresh_order_table()
        save_to_csv('orders.csv')
sample_data.extend(read_csv('orders.csv'))
