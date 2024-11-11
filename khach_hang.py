import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.messagebox as messagebox  # Import messagebox từ tkinter
import pandas as pd 
from PIL import Image, ImageTk
from tkinter import StringVar
import csv
from setting import load_settings  # Import thêm load_settings
from tkinter import Scrollbar, VERTICAL, HORIZONTAL


sample_customers = []
def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df.values.tolist()
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể đọc file: {e}")
        return []
def save_to_csv(filename):
    # Mở file ở chế độ ghi (write mode)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Ghi tiêu đề cột nếu cần
        header = ["ID Khách Hàng", "Tên Khách Hàng", "Địa Chỉ", "Số Điện Thoại", "Email", "Lịch Sử Mua Hàng"]  # Thay đổi theo các cột của bạn
        writer.writerow(header)
        
        # Ghi từng dòng dữ liệu từ sample_products
        for customer in sample_customers:
            writer.writerow(customer)

def button_click(button_name, app):
    if button_name == "Tìm kiếm":
        search_customer(app)
    elif button_name == "Thêm khách hàng":
        add_customer(app)
    elif button_name == "Mới nhất":
        latest_customers()
    elif button_name == "Sửa":
        edit_customer(app)

def latest_customers():
    for row in customer_table.get_children():
        customer_table.delete(row)

    for row in sample_customers:
        customer_table.insert("", "end", values=row)
    update_row_colors()
def search_customer(app):
    search_value = search_entry.get().lower()
    for row in customer_table.get_children():
        customer_table.delete(row)

    for row in sample_customers:
        if search_value in row[1].lower():
            customer_table.insert("", "end", values=row)

        update_row_colors()
def add_customer(app):
    add_window = ttk.Toplevel(app)
    add_window.title("Thêm Khách Hàng")

    fields = ["ID Khách Hàng", "Tên Khách Hàng", "Địa Chỉ", "Số Điện Thoại", "Email", "Lịch Sử Mua Hàng"]
    entries = {}

    for i, field in enumerate(fields):
        label = ttk.Label(add_window, text=field)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = ttk.Entry(add_window, bootstyle="superhero", width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[field] = entry
        

    def submit_customer():
        new_customer = tuple(entries[field].get().strip() for field in fields)
        try:
            if any(not value for value in new_customer):
                raise ValueError("Vui lòng không để trống các trường.")

            customer_table.insert("", "end", values=new_customer)
            sample_customers.append(new_customer)
            save_to_csv('customers.csv')
            add_window.destroy()
            
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))

    add_button = ttk.Button(add_window, text="Thêm", bootstyle="superhero", command=submit_customer)
    add_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

def refresh_customers_table():
    for row in customer_table.get_children():
        customer_table.delete(row)
    for product in sample_customers:
        customer_table.insert("", "end", values=product)
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
    customer_table.tag_configure("custom_font1", font=(font_name, font_size), background=background_even, foreground=font_color)
    customer_table.tag_configure("custom_font2", font=(font_name, font_size), background=background_odd, foreground=font_color)

    # Áp dụng các tag xen kẽ để tạo màu nền cho các dòng
    for index, item in enumerate(customer_table.get_children()):
        if index % 2 == 0:
            customer_table.item(item, tags=('custom_font1',))
        else:
            customer_table.item(item, tags=('custom_font2',))
    update_row_height(font_size)

def update_row_height(font_size):
    # Tạo kiểu tùy chỉnh cho bảng Treeview
    style = ttk.Style()

    # Cài đặt chiều cao của các hàng (row height) cho Treeview
    row_height = font_size*2  # Tính toán chiều cao hàng dựa trên cỡ chữ

    # Áp dụng kiểu cho bảng Treeview
    style.configure("Custom.Treeview", rowheight=row_height)

    # Cập nhật style của product_table
    customer_table.configure(style="Custom.Treeview")

def edit_customer(app):
    selected_item = customer_table.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một khách hàng để sửa.")
        return

    customer_data = customer_table.item(selected_item)["values"]
    edit_window = ttk.Toplevel(app)
    edit_window.title("Sửa Thông Tin Khách Hàng")

    fields = ["ID Khách Hàng", "Tên Khách Hàng", "Địa Chỉ", "Số Điện Thoại", "Email", "Lịch Sử Mua Hàng"]
    entries = {}

    for i, field in enumerate(fields):
        label = ttk.Label(edit_window, text=field)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = ttk.Entry(edit_window, bootstyle="superhero", width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, customer_data[i])
        entries[field] = entry

    def submit_edit():
        # Cập nhật dữ liệu trong `sample_products` để đồng bộ với CSV
        edited_order = tuple(entries[field].get().strip() for field in fields)
        for i, value in enumerate(edited_order):
            if value != customer_data[i]:
                # Update the order data
                sample_customers[sample_customers.index(customer_data)] = edited_order
                break

        # Làm mới bảng và lưu thay đổi vào CSV
        
       
        save_to_csv('customers.csv')
        refresh_customers_table() 
        edit_window.destroy()
    # Nút cập nhật để lưu thay đổi
    update_button = ttk.Button(edit_window, text="Cập nhật", bootstyle="superhero", command=submit_edit)
    update_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

def delete_customer():
    selected_item = customer_table.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn sản phẩm cần xóa.")
        return

    confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa sản phẩm này?")
    if confirm:
        selected_index = customer_table.index(selected_item)
        del sample_customers[selected_index]

        refresh_customers_table()
        save_to_csv('customers.csv')
def create_khach_hang_tab(notebook, app):
    global search_entry, customer_table

    frame_khach_hang = ttk.Frame(notebook)
    notebook.add(frame_khach_hang, text="KHÁCH HÀNG", padding=(10,10))
    
    image = Image.open("icon/search.png")
    image = image.resize((20, 20), Image.LANCZOS)
    search_icon = ImageTk.PhotoImage(image)

    image2 = Image.open("icon/multiple.png")
    image2 = image2.resize((20, 20), Image.LANCZOS)
    multiple_icon = ImageTk.PhotoImage(image2)

    image3 = Image.open("icon/wrenchalt.png")
    image3 = image3.resize((20, 20), Image.LANCZOS)
    wrenchalt_icon = ImageTk.PhotoImage(image3)

    image4 = Image.open("icon/trash.png")
    image4 = image4.resize((20,20), Image.LANCZOS)
    trash_icon = ImageTk.PhotoImage(image4)
    
    image5 = Image.open("icon/arrowup.png")
    image5 = image5.resize((20,20), Image.LANCZOS)
    arrowup_icon = ImageTk.PhotoImage(image5)
    
    

    search_value = StringVar()

    search_entry = ttk.Entry(frame_khach_hang, bootstyle="superhero", width=30, textvariable=search_value)
    search_entry.insert(0, "Tìm kiếm theo tên khách hàng")
    search_entry.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    # Clear the placeholder text on focus
    search_entry.bind("<FocusIn>", lambda event: search_entry.delete(0, 'end') if search_entry.get() == "Tìm kiếm theo tên khách hàng" else None)

    # Bind Enter key to perform the search
    search_entry.bind("<Return>", lambda event: button_click("Tìm kiếm", app))

    search_button = ttk.Button(frame_khach_hang, text="Tìm kiếm", bootstyle="superhero", image=search_icon, compound=LEFT, cursor="hand2", command=lambda: button_click("Tìm kiếm", app))
    search_button.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    frame_khach_hang.search_icon = search_icon  # Keep reference to avoid garbage collection

    add_customer_button = ttk.Button(frame_khach_hang, text="Thêm khách hàng", bootstyle="superhero",image=multiple_icon,compound=LEFT,cursor="hand2",command=lambda: button_click("Thêm khách hàng", app))
    add_customer_button.grid(row=0, column=2, padx=5, pady=5, sticky=W)
    frame_khach_hang.multiple_icon = multiple_icon
 
    edit_button = ttk.Button(frame_khach_hang, text="Sửa", bootstyle="superhero",image= wrenchalt_icon,compound=LEFT,cursor="hand2",command=lambda: button_click("Sửa", app))
    edit_button.grid(row=0, column=3, padx=5, pady=5, sticky=W)
    frame_khach_hang.wrenchalt_icon = wrenchalt_icon

    delete_button = ttk.Button(frame_khach_hang, text="Xóa", bootstyle="superhero",image=trash_icon ,compound=LEFT,cursor="hand2", command=delete_customer)
    delete_button.grid(row=0, column=4, padx=5, pady=5, sticky=W)
    frame_khach_hang.trash_icon = trash_icon
    
    # latest_button = ttk.Button(frame_khach_hang, text="Mới nhất", bootstyle="superhero",image=arrowup_icon ,compound=LEFT,cursor ="hand2",command=lambda: button_click("Mới nhất", app))
    # latest_button.grid(row=0, column=5, padx=5, pady=5, sticky=W)
    # frame_khach_hang.arrowup_icon = arrowup_icon
    
    columns = ["ID Khách Hàng", "Tên Khách Hàng", "Địa Chỉ", "Số Điện Thoại", "Email", "Lịch Sử Mua Hàng"]

    customer_table = ttk.Treeview(frame_khach_hang, columns=columns, show="headings", bootstyle="superhero")
    customer_table.grid(row=2, column=0, columnspan=5, padx=5, pady=5, sticky="ns")

    for col in columns:
        customer_table.heading(col, text=col)
        #customer_table.column(col, width=100)
        if col == "ID Khách Hàng":
            customer_table.column(col,anchor='center') 
        else:
            customer_table.column(col, anchor='w')
    for row in sample_customers:
        customer_table.insert("", "end", values=row)

    

    # Thêm Scrollbar dọc
    y_scrollbar = Scrollbar(frame_khach_hang, orient=VERTICAL, command=customer_table.yview)
    y_scrollbar.grid(row=2, column=5, sticky="ns")
    customer_table.configure(yscrollcommand=y_scrollbar.set)

    # Thêm Scrollbar ngang
    x_scrollbar = Scrollbar(frame_khach_hang, orient=HORIZONTAL, command=customer_table.xview)
    x_scrollbar.grid(row=3, column=0, columnspan=5, sticky="ew")
    customer_table.configure(xscrollcommand=x_scrollbar.set)

   # Hàm cập nhật bố cục khi thay đổi kích thước cửa sổ
    def update_layout(event=None):
        window_width = frame_khach_hang.winfo_width()
        window_height = frame_khach_hang.winfo_height()
        
        if window_width >= 1000 and window_height >= 600:  # Kích thước tùy ý cho chế độ toàn màn hình
            customer_table.grid(sticky="nsew")  # Mở rộng cả chiều dọc và chiều ngang
            frame_khach_hang.grid_rowconfigure(2, weight=1)  # Mở rộng chiều dọc
            frame_khach_hang.grid_columnconfigure(0, weight=1)  # Mở rộng chiều ngang
        else:
            customer_table.grid(sticky="ns")  # Mở rộng chỉ theo chiều dọc
            frame_khach_hang.grid_rowconfigure(2, weight=1)  # Mở rộng chiều dọc, không thay đổi chiều ngang
            frame_khach_hang.grid_columnconfigure(0, weight=1)  # Không mở rộng chiều ngang


    # Ràng buộc sự kiện cấu hình kích thước cửa sổ
    frame_khach_hang.bind("<Map>", update_layout)
    frame_khach_hang.bind("<Unmap>", update_layout)  # Khi cửa sổ bị thu nhỏ

    refresh_customers_table()

    frame_khach_hang.grid_rowconfigure(2, weight=1)
    frame_khach_hang.grid_columnconfigure(0, weight=1)
    
sample_customers.extend(read_csv('customers.csv'))

