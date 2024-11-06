import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.messagebox as messagebox
import pandas as pd
from tkinter import PhotoImage
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import StringVar

search_value = []
sample_products = []

def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df.values.tolist()
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể đọc file: {e}")
        return []

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
    notebook.add(frame_product, text="SẢN PHẨM")

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
    product_search_entry.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    # Thêm sự kiện focus_in để xóa nội dung khi nhấn vào ô tìm kiếm
    product_search_entry.bind("<FocusIn>", lambda event: product_search_entry.delete(0, 'end') if product_search_entry.get() == "Tìm kiếm theo tên sản phẩm" else None)

    # Nút tìm kiếm
    search_button = ttk.Button(frame_product, text="Tìm kiếm", bootstyle="superhero", image=search_icon, compound=LEFT, command=lambda: button_click("Tìm kiếm", app), cursor="hand2")
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
    product_table.grid(row=2, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

    for col in columns:
        product_table.heading(col, text=col)
        if col == "Tên Sản Phẩm" or col == "Mô Tả":
            product_table.column(col, anchor='w')  # căn trái cho tên sản phẩm
        else:
            product_table.column(col, anchor='center')  # căn giữa cho các cột khác

    refresh_product_table()  # Initial load from sample_products

    frame_product.grid_rowconfigure(2, weight=1)
    frame_product.grid_columnconfigure(0, weight=1)

def refresh_product_table():
    for row in product_table.get_children():
        product_table.delete(row)  # Xóa tất cả các hàng trước khi làm mới
    for product in sample_products:
        product_table.insert("", "end", values=product)  # Thêm sản phẩm vào bảng
    update_row_colors()  # Cập nhật màu cho các hàng


def update_row_colors():
    for index, item in enumerate(product_table.get_children()):
        if index % 2 == 0:
            product_table.item(item, tags=('evenrow',))
        else:
            product_table.item(item, tags=('oddrow',))

    product_table.tag_configure('evenrow', background='#f0f0f0')
    product_table.tag_configure('oddrow', background='white')

def search_product():
    search_value = product_search_entry.get().lower()
    refresh_product_table()  # Làm mới bảng trước để đảm bảo không còn sản phẩm nào

    matched_products = [product for product in sample_products if search_value in product[1].lower()]
    
    for product in matched_products:
        product_table.insert("", "end", values=product)  # Thêm chỉ sản phẩm khớp vào bảng


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

        sample_products.append(new_product)
        refresh_product_table()
        add_window.destroy()

    add_button = ttk.Button(add_window, text="Thêm", bootstyle="superhero", command=submit_product)
    add_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

def edit_product(app):
    selected_item = product_table.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một sản phẩm để sửa.")
        return

    product_data = product_table.item(selected_item)["values"]
    edit_window = ttk.Toplevel(app)
    edit_window.title("Sửa Sản Phẩm")

    fields = ["ID Sản Phẩm", "Tên sản Phẩm", "Giá VND", "Số Lượng Tồn Kho", "Mô Tả", "Nhóm Sản Phẩm"]
    entries = {}

    for i, field in enumerate(fields):
        label = ttk.Label(edit_window, text=field)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = ttk.Entry(edit_window, bootstyle="superhero", width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, product_data[i])
        entries[field] = entry

    def submit_edit():
        updated_product = tuple(entries[field].get().strip() for field in fields)
        if any(not value for value in updated_product):
            messagebox.showerror("Lỗi", "Vui lòng không để trống các trường.")
            return

        product_table.item(selected_item, values=updated_product)

        product_id = updated_product[0]
        for index, existing_product in enumerate(sample_products):
            if existing_product[0] == product_id:
                sample_products[index] = updated_product
                break

        refresh_product_table()
        edit_window.destroy()

    update_button = ttk.Button(edit_window, text="Cập nhật", bootstyle="superhero", command=submit_edit)
    update_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

def delete_product():
    selected_item = product_table.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một sản phẩm để xóa.")
        return

    product_id = product_table.item(selected_item)["values"][0]
    confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc chắn muốn xóa sản phẩm ID {product_id}?")
    if confirm:
        product_table.delete(selected_item)
        global sample_products
        sample_products = [product for product in sample_products if product[0] != product_id]

sample_products.extend(read_csv('products.csv'))
if __name__ == "__main__":
    pass
    
   
