import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.messagebox as messagebox  # Import messagebox từ tkinter

# Dữ liệu mẫu
sample_customers = [
    ("001", "Túy", "1/1/1995", "Nam", "123 Đường A", "0123"),
    ("002", "Minh", "5/6/1990", "Nữ", "456 Đường B", "0456"),
    ("003", "Hùng", "12/12/1985", "Nam", "789 Đường C", "0789"),
]

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

def search_customer(app):
    search_value = search_entry.get().lower()
    for row in customer_table.get_children():
        customer_table.delete(row)

    for row in sample_customers:
        if search_value in row[1].lower():
            customer_table.insert("", "end", values=row)

def add_customer(app):
    add_window = ttk.Toplevel(app)
    add_window.title("Thêm Khách Hàng")

    fields = ["Mã khách hàng", "Tên khách hàng", "Ngày sinh", "Giới tính", "Địa chỉ", "SDT"]
    entries = {}

    for i, field in enumerate(fields):
        label = ttk.Label(add_window, text=field)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = ttk.Entry(add_window, bootstyle="secondary", width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[field] = entry

    def submit_customer():
        new_customer = tuple(entries[field].get().strip() for field in fields)
        try:
            if any(not value for value in new_customer):
                raise ValueError("Vui lòng không để trống các trường.")

            customer_table.insert("", "end", values=new_customer)
            sample_customers.append(new_customer)
            add_window.destroy()
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))

    add_button = ttk.Button(add_window, text="Thêm", bootstyle="secondary", command=submit_customer)
    add_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

def edit_customer(app):
    selected_item = customer_table.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một khách hàng để sửa.")
        return

    customer_data = customer_table.item(selected_item)["values"]
    edit_window = ttk.Toplevel(app)
    edit_window.title("Sửa Khách Hàng")

    fields = ["Mã khách hàng", "Tên khách hàng", "Ngày sinh", "Giới tính", "Địa chỉ", "SDT"]
    entries = {}

    for i, field in enumerate(fields):
        label = ttk.Label(edit_window, text=field)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = ttk.Entry(edit_window, bootstyle="secondary", width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, customer_data[i])
        entries[field] = entry

    def submit_edit():
        updated_customer = tuple(entries[field].get().strip() for field in fields)
        try:
            if any(not value for value in updated_customer):
                raise ValueError("Vui lòng không để trống các trường.")

            customer_table.item(selected_item, values=updated_customer)
            customer_id = updated_customer[0]
            for index, existing_customer in enumerate(sample_customers):
                if existing_customer[0] == customer_id:
                    sample_customers[index] = updated_customer
                    break

            edit_window.destroy()
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))

    save_button = ttk.Button(edit_window, text="Lưu", bootstyle="secondary", command=submit_edit)
    save_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

def delete_customer():
    selected_item = customer_table.selection()
    if selected_item:
        customer_table.delete(selected_item)
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn khách hàng để xóa.")

def create_khach_hang_tab(notebook, app):
    global search_entry, customer_table

    frame_khach_hang = ttk.Frame(notebook)
    notebook.add(frame_khach_hang, text="KHÁCH HÀNG")
    

    search_entry = ttk.Entry(frame_khach_hang, bootstyle="secondary", width=30)
    search_entry.insert(0, "tìm kiếm theo tên khách hàng")
    search_entry.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    search_button = ttk.Button(frame_khach_hang, text="Tìm kiếm", bootstyle="secondary",
                               command=lambda: button_click("Tìm kiếm", app))
    search_button.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    add_customer_button = ttk.Button(frame_khach_hang, text="Thêm khách hàng", bootstyle="secondary",
                                     command=lambda: button_click("Thêm khách hàng", app))
    add_customer_button.grid(row=0, column=2, padx=5, pady=5, sticky=W)

    edit_button = ttk.Button(frame_khach_hang, text="Sửa", bootstyle="secondary",
                             command=lambda: button_click("Sửa", app))
    edit_button.grid(row=0, column=3, padx=5, pady=5, sticky=W)

    delete_button = ttk.Button(frame_khach_hang, text="Xóa", bootstyle="secondary",
                               command=delete_customer)
    delete_button.grid(row=0, column=4, padx=5, pady=5, sticky=W)

    latest_button = ttk.Button(frame_khach_hang, text="Mới nhất", bootstyle="secondary",
                               command=lambda: button_click("Mới nhất", app))
    latest_button.grid(row=0, column=5, padx=5, pady=5, sticky=W)

    columns = ["Mã khách hàng", "Tên khách hàng", "Ngày sinh", "Giới tính", "Địa chỉ", "SDT"]

    customer_table = ttk.Treeview(frame_khach_hang, columns=columns, show="headings", bootstyle="secondary")
    customer_table.grid(row=2, column=0, columnspan=len(columns), padx=5, pady=5, sticky="nsew")

    for col in columns:
        customer_table.heading(col, text=col)
        customer_table.column(col, width=100)

    for row in sample_customers:
        customer_table.insert("", "end", values=row)

    frame_khach_hang.grid_rowconfigure(2, weight=1)
    frame_khach_hang.grid_columnconfigure(0, weight=1)
