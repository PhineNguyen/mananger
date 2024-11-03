import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.messagebox as messagebox

# Dữ liệu mẫu sản phẩm
sample_products = [
    ("001", "Bút bi", "5.000", "5"),
    ("002", "Vở viết", "10.000", "25"),
    ("003", "Thước kẻ", "2.000", "30"),
]

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

    # Tạo frame sản phẩm
    frame_product = ttk.Frame(notebook)
    notebook.add(frame_product, text="SẢN PHẨM")

    # Tạo ô tìm kiếm và các nút chức năng
    product_search_entry = ttk.Entry(frame_product, bootstyle="secondary", width=30)
    product_search_entry.insert(0, "Tìm kiếm theo tên sản phẩm")
    product_search_entry.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    search_button = ttk.Button(frame_product, text="Tìm kiếm", bootstyle="secondary", command=search_product)
    search_button.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    add_product_button = ttk.Button(frame_product, text="Thêm sản phẩm", bootstyle="secondary", command=lambda: add_product(app))
    add_product_button.grid(row=0, column=2, padx=5, pady=5, sticky=W)

    edit_product_button = ttk.Button(frame_product, text="Sửa", bootstyle="secondary", command=lambda: edit_product(app))
    edit_product_button.grid(row=0, column=3, padx=5, pady=5, sticky=W)

    delete_product_button = ttk.Button(frame_product, text="Xóa", bootstyle="secondary", command=delete_product)
    delete_product_button.grid(row=0, column=4, padx=5, pady=5, sticky=W)

    # Cấu hình bảng hiển thị sản phẩm
    columns = ["Mã", "Tên sản phẩm", "Giá", "Số Lượng"]
    product_table = ttk.Treeview(frame_product, columns=columns, show="headings", bootstyle="secondary")
    product_table.grid(row=2, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

    product_table.column("Mã", width=80, anchor="center")
    product_table.column("Tên sản phẩm", width=150, anchor="center")
    product_table.column("Giá", width=80, anchor="center")
    product_table.column("Số Lượng", width=80, anchor="center")

    for col in columns:
        product_table.heading(col, text=col)

    # Thay đổi màu nền cho các hàng để tạo hiệu ứng ngăn cách
    for row in sample_products:
        product_table.insert("", "end", values=row)
    
    
    frame_product.grid_rowconfigure(2, weight=1)
    frame_product.grid_columnconfigure(0, weight=1)

    update_row_colors()

def update_row_colors():
    # Đổi màu nền cho các hàng
    for index, item in enumerate(product_table.get_children()):
        if index % 2 == 0:
            product_table.item(item, tags=('evenrow',))
        else:
            product_table.item(item, tags=('oddrow',))

    product_table.tag_configure('evenrow', background='#f0f0f0')
    product_table.tag_configure('oddrow', background='white')

def search_product():
    search_value = product_search_entry.get().lower()
    for row in product_table.get_children():
        product_table.delete(row)

    for product in sample_products:
        if search_value in product[1].lower():
            product_table.insert("", "end", values=product)

def add_product(app):
    add_window = ttk.Toplevel(app)
    add_window.title("Thêm Sản Phẩm")

    fields = ["Mã", "Tên sản phẩm", "Giá", "Số Lượng"]
    entries = {}

    for i, field in enumerate(fields):
        label = ttk.Label(add_window, text=field)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = ttk.Entry(add_window, bootstyle="secondary", width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[field] = entry

    def submit_product():
        new_product = tuple(entries[field].get().strip() for field in fields)

        if any(not value for value in new_product):
            messagebox.showerror("Lỗi", "Vui lòng không để trống các trường.")
            return

        product_table.insert("", "end", values=new_product)
        sample_products.append(new_product)
        update_row_colors()  # Cập nhật màu hàng
        add_window.destroy()

    add_button = ttk.Button(add_window, text="Thêm", bootstyle="secondary", command=submit_product)
    add_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

def edit_product(app):
    selected_item = product_table.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một sản phẩm để sửa.")
        return

    product_data = product_table.item(selected_item)["values"]
    edit_window = ttk.Toplevel(app)
    edit_window.title("Sửa Sản Phẩm")

    fields = ["Mã", "Tên sản phẩm", "Giá", "Số Lượng"]
    entries = {}

    for i, field in enumerate(fields):
        label = ttk.Label(edit_window, text=field)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = ttk.Entry(edit_window, bootstyle="secondary", width=30)
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

        update_row_colors()  # Cập nhật màu hàng
        edit_window.destroy()

    save_button = ttk.Button(edit_window, text="Lưu", bootstyle="secondary", command=submit_edit)
    save_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

def delete_product():
    selected_item = product_table.selection()
    if selected_item:
        product_table.delete(selected_item)
        update_row_colors()  # Cập nhật màu hàng
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn sản phẩm để xóa.")

def main():
    app = ttk.Window(themename="superhero")
    app.title("Quản Lý Sản Phẩm")

    notebook = ttk.Notebook(app)
    notebook.pack(expand=True, fill=BOTH)

    create_san_pham_tab(notebook, app)

    app.mainloop()

if __name__ == "__main__":
    main()
