import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.messagebox as messagebox
import pandas as pd
from PIL import Image, ImageTk
from tkinter import StringVar
import csv
from setting import load_settings  # Import thêm load_settings
from tkinter import Scrollbar, VERTICAL, HORIZONTAL



# Sample data
sample_data = []

# Hàm đọc dữ liệu từ customers.csv
def read_customers_csv(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Bỏ qua dòng tiêu đề
            return [row for row in reader]
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể đọc file customers.csv: {e}")
        return []
    
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
            header = ["ID Đơn Hàng", "ID Khách Hàng", "Ngày Đặt Hàng", "Danh Sách Sản Phẩm", "Tổng Giá Trị Đơn Hàng", "Trạng Thái Đơn Hàng", "Phương Thức Thanh Toán"]
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
    search_entry.insert(0, "Tìm kiếm theo id đơn hàng")  # Văn bản mặc định trong ô tìm kiếm
    search_entry.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    
    
    # Xóa gợi ý khi nhấn vào ô tìm kiếm
    def on_entry_click(event):
        if search_entry.get() == "Tìm kiếm theo id đơn hàng":
            search_entry.delete(0, 'end')  # Xóa gợi ý
            search_entry.config(foreground='black')  # Đổi màu chữ để nhập nội dung mới

    # Hiển thị lại gợi ý nếu ô trống khi bỏ chọn
    def on_focus_out(event):
        if search_entry.get() == "":
            search_entry.insert(0, "Tìm kiếm theo id đơn hàng")  # Đặt lại gợi ý
            search_entry.config(foreground='gray')  # Đổi màu chữ cho gợi ý

    # Gắn sự kiện focus
    search_entry.bind("<FocusIn>", on_entry_click)
    search_entry.bind("<FocusOut>", on_focus_out)
    # Gắn sự kiện Enter cho ô tìm kiếm
    search_entry.bind("<Return>", lambda event: search_order())

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

    # Định nghĩa các cột cho bảng order_table
    columns = ["ID Đơn Hàng", "ID Khách Hàng", "Ngày Đặt Hàng", "Danh Sách Sản Phẩm", "Tổng Giá Trị Đơn Hàng", "Trạng Thái Đơn Hàng", "Phương Thức Thanh Toán"]
    order_table = ttk.Treeview(frame_order, columns=columns, show="headings", bootstyle="superhero")
    order_table.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky="ns")

    # Thiết lập tiêu đề và căn chỉnh cho các cột trong bảng
    for col in columns:
        order_table.heading(col, text=col)
        if col in ["Trạng Thái Đơn Hàng", "Phương Thức Thanh Toán", "Danh Sách Sản Phẩm"]:
            order_table.column(col, anchor='w')  # Căn trái cho các cột này
        else:
            order_table.column(col, anchor='center')  # Căn giữa cho các cột còn lại

    # Thêm Scrollbar dọc
    y_scrollbar = ttk.Scrollbar(frame_order, orient=VERTICAL, command=order_table.yview)
    y_scrollbar.grid(row=1, column=5, sticky="ns")
    order_table.configure(yscrollcommand=y_scrollbar.set)

    # Thêm Scrollbar ngang
    x_scrollbar = ttk.Scrollbar(frame_order, orient=HORIZONTAL, command=order_table.xview)
    x_scrollbar.grid(row=2, column=0, columnspan=5, sticky="ew")
    order_table.configure(xscrollcommand=x_scrollbar.set)

    order_table.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)

    # Hàm cập nhật bố cục khi thay đổi kích thước cửa sổ
    def update_layout(event=None):
        window_width = frame_order.winfo_width()
        window_height = frame_order.winfo_height()
        
        if window_width >= 1000 and window_height >= 600:  # Kích thước tùy ý cho chế độ toàn màn hình
            order_table.grid(sticky="nsew")  # Mở rộng cả chiều dọc và chiều ngang
            frame_order.grid_rowconfigure(1, weight=1)  # Mở rộng chiều dọc
            frame_order.grid_columnconfigure(0, weight=1)  # Mở rộng chiều ngang
        else:
            order_table.grid(sticky="ns")  # Mở rộng chỉ theo chiều dọc
            frame_order.grid_rowconfigure(1, weight=1)  # Mở rộng chiều dọc, không thay đổi chiều ngang
            frame_order.grid_columnconfigure(0, weight=1)  # Không mở rộng chiều ngang


    # Ràng buộc sự kiện cấu hình kích thước cửa sổ
    frame_order.bind("<Configure>", update_layout)


    # Gọi hàm để tải dữ liệu ban đầu vào bảng
    refresh_order_table()
    
    # Thiết lập khung chứa bảng để tự động thay đổi kích thước khi giao diện mở rộng
    frame_order.grid_rowconfigure(1, weight=1)
    frame_order.grid_columnconfigure(0, weight=1)


def load_image(image_path):
    try:
        image = Image.open(image_path)
        image = image.resize((20, 20), Image.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tải hình ảnh: {e}")
        return None

def refresh_order_table():
    for row in order_table.get_children():
        order_table.delete(row)
    for order in sample_data:
        order_table.insert("", "end", values=order)
    update_row_colors()

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
    matched_orders = [order for order in sample_data if search_value in str(order[0]).lower()]

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
    fields = ["ID Đơn Hàng", "ID Khách Hàng", "Ngày Đặt Hàng", "Danh Sách Sản Phẩm", 
              "Tổng Giá Trị Đơn Hàng", "Trạng Thái Đơn Hàng", "Phương Thức Thanh Toán"]
    entries = {}  # Tạo dictionary để lưu các entry widget

    # Tạo các nhãn và entry widget cho mỗi trường thông tin
    for i, field in enumerate(fields):
        label = ttk.Label(add_window, text=field)  # Tạo nhãn cho trường
        label.grid(row=i, column=0, padx=10, pady=5)  # Đặt nhãn vào lưới
        entry = ttk.Entry(add_window, bootstyle="superhero", width=30)  # Tạo entry cho trường
        entry.grid(row=i, column=1, padx=10, pady=5)  # Đặt entry vào lưới
        entries[field] = entry  # Lưu entry vào dictionary với khóa là tên trường

        # Thêm nút chọn khách hàng bên cạnh ô "ID Khách Hàng"
        if field == "ID Khách Hàng":
            choose_button = ttk.Button(add_window, text="Chọn", command=lambda: choose_customer(entries))
            choose_button.grid(row=i, column=2, padx=5)

    # Hàm để mở cửa sổ chọn sản phẩm
    def select_products():
        product_window = ttk.Toplevel(add_window)  # Tạo cửa sổ "Chọn Sản Phẩm" mới
        product_window.title("Chọn")

        # Tải danh sách sản phẩm từ file CSV
        products = read_csv("products.csv")

        # Tạo bảng hiển thị danh sách sản phẩm với các cột ID, Tên và Giá
        product_table = ttk.Treeview(product_window, columns=("ID", "Tên", "Giá"), 
                                     show="headings", selectmode="extended")
        product_table.heading("ID", text="ID")  # Cột ID
        product_table.heading("Tên", text="Tên Sản Phẩm")  # Cột tên sản phẩm
        product_table.heading("Giá", text="Giá VND")  # Cột giá sản phẩm
        product_table.pack(fill="both", expand=True)  # Đặt bảng vào cửa sổ, mở rộng đầy đủ

        # Thêm các sản phẩm vào bảng
        for product in products:
            product_table.insert("", "end", values=(product[0], product[1], product[2]))

        # Hàm để thêm các sản phẩm đã chọn vào đơn hàng
        def add_selected_products():
            selected_products = [product_table.item(item)["values"] for item in product_table.selection()]
            entries["Danh Sách Sản Phẩm"].delete(0, 'end')  # Xóa nội dung cũ trong trường danh sách sản phẩm
            selected_product_names = [f"{prod[1]} ({prod[2]} VND)" for prod in selected_products]
            # Ghép tên và giá của các sản phẩm được chọn thành chuỗi và thêm vào trường danh sách sản phẩm
            entries["Danh Sách Sản Phẩm"].insert(0, ", ".join(selected_product_names))
            product_window.destroy()  # Đóng cửa sổ chọn sản phẩm

        # Nút để xác nhận chọn các sản phẩm
        select_button = ttk.Button(product_window, text="Chọn Sản Phẩm", command=add_selected_products)
        select_button.pack(pady=10)

        

    # Nút "Chọn Sản Phẩm" trong cửa sổ "Thêm Đơn Hàng", mở cửa sổ chọn sản phẩm
    product_select_button = ttk.Button(add_window, text="Chọn Sản Phẩm", 
                                       bootstyle="superhero", command=select_products)
    product_select_button.grid(row=fields.index("Danh Sách Sản Phẩm"), column=2, padx=10, pady=5)

    # Hàm để lưu đơn hàng mới vào danh sách và file CSV

    def submit_order():
        # Lấy thông tin từ các trường và kiểm tra xem có trường nào bỏ trống không
        new_order = tuple(entries[field].get().strip() for field in fields)
        if any(not value for value in new_order):
            messagebox.showerror("Lỗi", "Vui lòng không để trống các trường.")  # Hiển thị lỗi nếu bỏ trống
            return

        # Thêm đơn hàng vào danh sách tạm thời và lưu vào file CSV
        sample_data.append(new_order)
        save_to_csv("orders.csv")  # Lưu đơn hàng vào file CSV
        refresh_order_table()  # Cập nhật bảng đơn hàng

        # Lấy ID đơn hàng và ID khách hàng
        order_id = new_order[0]
        customer_id = new_order[1]

        # Cập nhật lịch sử mua hàng cho khách hàng trong file customers.csv
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

    fields = ["ID Đơn Hàng", "ID Khách Hàng", "Ngày Đặt Hàng", "Danh Sách Sản Phẩm", "Tổng Giá Trị Đơn Hàng", "Trạng Thái Đơn Hàng", "Phương Thức Thanh Toán"]
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
        selected_index = order_table.index(selected_item)
        del sample_data[selected_index]

        refresh_order_table()
        save_to_csv('orders.csv')
sample_data.extend(read_csv('orders.csv'))
