import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.messagebox as messagebox
import pandas as pd
from PIL import Image, ImageTk
from tkinter import StringVar, Scrollbar
import csv
from setting import load_settings  # Import thêm load_settings
import tkinter as tk


search_value = []
sample_products = []

def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df.values.tolist()
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể đọc file: {e}")
        return []
import csv

def save_to_csv(filename):
    # Mở file ở chế độ ghi (write mode)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Ghi tiêu đề cột nếu cần
        header = ["ID Sản Phẩm", "Tên Sản Phẩm", "Giá VND", "Số Lượng Tồn Kho", "Mô Tả", "Nhóm Sản Phẩm"]  # Thay đổi theo các cột của bạn
        writer.writerow(header)
        
        # Ghi từng dòng dữ liệu từ sample_products
        for product in sample_products:
            writer.writerow(product)

def button_click(button_name, app):
    if button_name == "Tìm kiếm":
        search_product()
    elif button_name == "Thêm":
        add_product(app)
    elif button_name == "Sửa":
        edit_product(app)
    elif button_name == "Xóa":
        delete_product()

def create_san_pham_tab(notebook, app):
    global product_table, product_search_entry

    frame_product = ttk.Frame(notebook)
    notebook.add(frame_product, text=" SẢN PHẨM ", padding=(10,10))

    # Tải icon
    image = Image.open("icon/search.png").resize((20, 20), Image.LANCZOS)
    search_icon = ImageTk.PhotoImage(image)

    image2 = Image.open("icon/multiple.png").resize((20, 20), Image.LANCZOS)
    multiple_icon = ImageTk.PhotoImage(image2)

    image3 = Image.open("icon/wrenchalt.png").resize((20, 20), Image.LANCZOS)
    wrenchalt_icon = ImageTk.PhotoImage(image3)

    image4 = Image.open("icon/trash.png").resize((20, 20), Image.LANCZOS)
    trash_icon = ImageTk.PhotoImage(image4)

    search_value = StringVar()

    product_search_entry = ttk.Entry(frame_product, bootstyle="superhero", width=30, textvariable=search_value)
    product_search_entry.insert(0, "Tìm kiếm theo tên sản phẩm")
    product_search_entry.config(foreground="grey")
    product_search_entry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Hàm xử lý khi nhấp vào entry tìm kiếm (FocusIn)
    def on_focus_in(event):
        if product_search_entry.get() == "Tìm kiếm theo tên sản phẩm":
            product_search_entry.delete(0, "end")
            product_search_entry.config(foreground="black")

# Hàm xử lý khi rời khỏi entry tìm kiếm (FocusOut)
    def on_focus_out(event):
        if product_search_entry.get() == "":
            product_search_entry.insert(0, "Tìm kiếm theo tên sản phẩm")
            product_search_entry.config(foreground="grey")

# Gán sự kiện FocusIn và FocusOut cho entry tìm kiếm
    product_search_entry.bind("<FocusIn>", on_focus_in)
    product_search_entry.bind("<FocusOut>", on_focus_out)

# Đặt focus vào entry tìm kiếm sau một khoảng thời gian ngắn
    notebook.after(100, lambda: product_search_entry.focus_set())

    search_button = ttk.Button(frame_product, text="Tìm kiếm", bootstyle="superhero",image=search_icon,compound= LEFT ,command=search_product, cursor="hand2")
    search_button.grid(row=0, column=1, padx=5, pady=5, sticky=W)
    frame_product.search_icon = search_icon
    

    # Gán chức năng cho phím Enter
    product_search_entry.bind("<Return>", lambda event: button_click("Tìm kiếm", app))

    # Nút thêm sản phẩm
    add_product_button = ttk.Button(frame_product, text="Thêm sản phẩm", bootstyle="superhero", image=multiple_icon, compound=LEFT, command=lambda: add_product(app), cursor="hand2")
    add_product_button.grid(row=0, column=2, padx=5, pady=5, sticky=W)
    frame_product.multiple_icon = multiple_icon

    # Nút sửa sản phẩm
    edit_product_button = ttk.Button(frame_product, text="Sửa", bootstyle="superhero", image=wrenchalt_icon, compound=LEFT, command=lambda: edit_product(app), cursor="hand2")
    edit_product_button.grid(row=0, column=3, padx=5, pady=5, sticky=W)
    frame_product.wrenchalt_icon = wrenchalt_icon

    # Nút xóa sản phẩm
    delete_product_button = ttk.Button(frame_product, text="Xóa", bootstyle="superhero", image=trash_icon, compound=LEFT, command=delete_product, cursor="hand2")
    delete_product_button.grid(row=0, column=4, padx=5, pady=5, sticky=W)
    frame_product.trash_icon = trash_icon

    columns = ["ID Sản Phẩm", "Tên Sản Phẩm", "Giá VND", "Số Lượng Tồn Kho", "Mô Tả", "Nhóm Sản Phẩm"]
    product_table = ttk.Treeview(frame_product, columns=columns, show="headings", bootstyle="superhero")
    product_table.grid(row=2, column=0, columnspan=5, padx=5, pady=5, sticky="ns")

    for col in columns:
        product_table.heading(col, text=col)
        if col == "Tên Sản Phẩm" or col == "Mô Tả":
            product_table.column(col, anchor='w')  # căn trái cho tên sản phẩm
        else:
            product_table.column(col, anchor='center')  # căn giữa cho các cột khác

    # Thêm Scrollbar dọc
    y_scrollbar = Scrollbar(frame_product, orient=VERTICAL, command=product_table.yview)
    y_scrollbar.grid(row=2, column=5, sticky="ns")
    product_table.configure(yscrollcommand=y_scrollbar.set)

    # Thêm Scrollbar ngang
    x_scrollbar = Scrollbar(frame_product, orient=HORIZONTAL, command=product_table.xview)
    x_scrollbar.grid(row=3, column=0, columnspan=5, sticky="ew")
    product_table.configure(xscrollcommand=x_scrollbar.set)

    # Hàm cập nhật bố cục khi thay đổi kích thước cửa sổ
    def update_layout(event=None):
        window_width = frame_product.winfo_width()
        window_height = frame_product.winfo_height()
        
        if window_width >= 1000 and window_height >= 600:  # Kích thước tùy ý cho chế độ toàn màn hình
            product_table.grid(sticky="nsew")  # Mở rộng cả chiều dọc và chiều ngang
            frame_product.grid_rowconfigure(2, weight=1)  # Mở rộng chiều dọc
            frame_product.grid_columnconfigure(0, weight=1)  # Mở rộng chiều ngang
        else:
            product_table.grid(sticky="ns")  # Mở rộng chỉ theo chiều dọc
            frame_product.grid_rowconfigure(2, weight=1)  # Mở rộng chiều dọc, không thay đổi chiều ngang
            frame_product.grid_columnconfigure(0, weight=1)  # Không mở rộng chiều ngang

    # Ràng buộc sự kiện cấu hình kích thước cửa sổ
    frame_product.bind("<Configure>", update_layout)


    #dbclick để xem chi tiết
    def show_product_details(event):
        """
        Hàm hiển thị cửa sổ chi tiết sản phẩm khi người dùng nhấp đúp vào một hàng trong bảng.
        """
        # Lấy ID của hàng đang được chọn
        selected_item = product_table.selection()
        if not selected_item:
            return

        # Lấy thông tin của hàng được chọn
        item_data = product_table.item(selected_item, "values")

        # Tạo cửa sổ Toplevel để hiển thị thông tin
        detail_window = ttk.Toplevel()
        detail_window.title("Thông tin chi tiết sản phẩm")
        #detail_window.geometry("600x300")  # Kích thước cửa sổ tùy ý

        # Hiển thị thông tin chi tiết của sản phẩm
        labels = ["ID Sản Phẩm", "Tên Sản Phẩm", "Giá VND", "Số Lượng Tồn Kho", "Mô Tả", "Nhóm Sản Phẩm"]
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
    product_table.bind("<Double-1>", show_product_details)

    #tải dữ liệu vào bảng
    refresh_product_table()  # Initial load from sample_products

    # Đặt tỷ lệ khung cho các hàng và cột
    frame_product.grid_rowconfigure(2, weight=1)
    frame_product.grid_columnconfigure(0, weight=1)

def refresh_product_table():
    for row in product_table.get_children():
        product_table.delete(row)  # Xóa tất cả các hàng trước khi làm mới
    for product in sample_products:
        product_table.insert("", "end", values=product)  # Thêm sản phẩm vào bảng
    update_row_colors()  # Cập nhật màu cho các hàng


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
    product_table.tag_configure("custom_font1", font=(font_name, font_size), background=background_even, foreground=font_color)
    product_table.tag_configure("custom_font2", font=(font_name, font_size), background=background_odd, foreground=font_color)

    # Áp dụng các tag xen kẽ để tạo màu nền cho các dòng
    for index, item in enumerate(product_table.get_children()):
        if index % 2 == 0:
            product_table.item(item, tags=('custom_font1',))
        else:
            product_table.item(item, tags=('custom_font2',))
    #product_table.configure(height=font_size+5)
    update_row_height(font_size)

def update_row_height(font_size):
    # Tạo kiểu tùy chỉnh cho bảng Treeview
    style = ttk.Style()

    # Cài đặt chiều cao của các hàng (row height) cho Treeview
    row_height = font_size*2  # Tính toán chiều cao hàng dựa trên cỡ chữ

    # Áp dụng kiểu cho bảng Treeview
    style.configure("Custom.Treeview", rowheight=row_height)

    # Cập nhật style của product_table
    product_table.configure(style="Custom.Treeview")



def search_product():
    search_value = product_search_entry.get().lower()
    for row in product_table.get_children():  # Làm mới bảng trước để đảm bảo không còn sản phẩm nào
        product_table.delete(row)
        
    matched_products = [product for product in sample_products if search_value in product[1].lower()]
    
    for product in matched_products:
        product_table.insert("", "end", values=product)  # Thêm chỉ sản phẩm khớp vào bảng

    update_row_colors()
    
def add_product(app):
    add_window = ttk.Toplevel(app)
    add_window.title("Thêm Sản Phẩm")

    
    fields = ["ID Sản Phẩm", "Tên sản Phẩm", "Giá VND", "Số Lượng Tồn Kho", "Mô Tả", "Nhóm Sản Phẩm"]
    entries = {}

    for i, field in enumerate(fields):
        label = ttk.Label(add_window, text=field)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = ttk.Entry(add_window, bootstyle="superhero", width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[field] = entry

    
    def submit_product():
        new_product = tuple(entries[field].get().strip() for field in fields)

        if any(not value for value in new_product):
            messagebox.showerror("Lỗi", "Vui lòng không để trống các trường.")
            return
        
        # Kiểm tra xem ID sản phẩm đã tồn tại chưa
        new_product_id = new_product[0]  # ID sản phẩm là phần tử đầu tiên trong tuple
        for product in sample_products:
            if product[0] == new_product_id:  # Nếu ID đã tồn tại
                messagebox.showerror("Lỗi", "ID sản phẩm đã tồn tại. Vui lòng nhập lại ID khác.")
                entries["ID Sản Phẩm"].delete(0, 'end')  # Xóa ID hiện tại để người dùng nhập lại
                return

        sample_products.append(new_product)
       
        refresh_product_table()
        save_to_csv('products.csv')
        add_window.destroy()

    add_button = ttk.Button(add_window, text="Thêm", bootstyle="superhero", command=submit_product)
    add_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

def edit_product(app):
    # Lấy sản phẩm được chọn từ bảng
    selected_item = product_table.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một sản phẩm để sửa.")
        return

    product_data = product_table.item(selected_item)["values"]
    edit_window = ttk.Toplevel(app)
    edit_window.title("Sửa Sản Phẩm")

    fields = ["ID Sản Phẩm", "Tên sản Phẩm", "Giá VND", "Số Lượng Tồn Kho", "Mô Tả", "Nhóm Sản Phẩm"]
    entries = {}

    # Tạo các trường nhập liệu cho mỗi thuộc tính sản phẩm
    for i, field in enumerate(fields):
        label = ttk.Label(edit_window, text=field)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = ttk.Entry(edit_window,bootstyle="superhero", width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, product_data[i])
        entries[field] = entry

    def submit_edit():
        # Lấy dữ liệu mới từ các trường nhập liệu
        updated_product = tuple(entries[field].get().strip() for field in fields)
        
        # Kiểm tra dữ liệu có trống không
        if any(not value for value in updated_product):
            messagebox.showerror("Lỗi", "Vui lòng không để trống các trường.")
            return

        sample_products[product_table.index(selected_item)] = updated_product
        product_table.item(selected_item, values=updated_product)
        
        # Cập nhật dữ liệu trong `sample_products` để đồng bộ với CSV
        product_id = updated_product[0]
        for index, existing_product in enumerate(sample_products):
            if existing_product[0] == product_id:
                sample_products[index] = updated_product
                break

        # Làm mới bảng và lưu thay đổi vào CSV
        
        edit_window.destroy()
        save_to_csv('products.csv')
        refresh_product_table()
    # Nút cập nhật để lưu thay đổi
    update_button = ttk.Button(edit_window, text="Cập nhật", bootstyle="superhero", command=submit_edit)
    update_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

def delete_product():
    selected_item = product_table.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn sản phẩm cần xóa.")
        return

    confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa sản phẩm này?")
    if confirm:
        selected_index = product_table.index(selected_item)
        del sample_products[selected_index]

        refresh_product_table()
        save_to_csv('products.csv')
sample_products.extend(read_csv('products.csv'))
if __name__ == "__main__":
    pass
    
   
