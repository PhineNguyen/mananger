import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.messagebox as messagebox
import sqlite3

# Kết nối tới cơ sở dữ liệu
def connect_db():
    return sqlite3.connect('sanpham.db')

# Tạo bảng donhang
def create_don_hang_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS donhang (
        ma TEXT PRIMARY KEY,
        ten_san_pham TEXT NOT NULL,
        ngay TEXT NOT NULL,
        ten_khach_hang TEXT NOT NULL,
        sdt TEXT NOT NULL,
        so_luong INTEGER NOT NULL,
        thanh_tien REAL NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Gọi hàm tạo bảng
create_don_hang_table()  # Đảm bảo bảng được tạo trước khi truy vấn

# Lấy danh sách đơn hàng từ cơ sở dữ liệu
def fetch_orders():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM donhang")
    orders = cursor.fetchall()
    conn.close()
    return orders

# Khởi tạo sample_data từ cơ sở dữ liệu
sample_data = fetch_orders()

# Thêm đơn hàng vào cơ sở dữ liệu
def insert_order(order):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO donhang (ma, ten_san_pham, ngay, ten_khach_hang, sdt, so_luong, thanh_tien) VALUES (?, ?, ?, ?, ?, ?, ?)", order)
    conn.commit()
    conn.close()

# Cập nhật thông tin đơn hàng trong cơ sở dữ liệu
def update_order(order):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE donhang SET ten_san_pham = ?, ngay = ?, ten_khach_hang = ?, sdt = ?, so_luong = ?, thanh_tien = ? WHERE ma = ?", order[1:] + (order[0],))
    conn.commit()
    conn.close()

# Khởi tạo sample_data từ cơ sở dữ liệu
sample_data = fetch_orders()

def button_click(button_name, app):
    if button_name == "Tìm kiếm":
        search_order(app)
    elif button_name == "Thêm đơn":
        add_order(app)
    elif button_name == "Mới nhất":
        latest()
    elif button_name == "Sửa":
        edit_order(app)

def latest():
    for row in order_table.get_children():
        order_table.delete(row)

    for row in sample_data:
        order_table.insert("", "end", values=row)

def search_order(app):
    search_value = search_entry.get().lower()
    for row in order_table.get_children():
        order_table.delete(row)

    for row in sample_data:
        if search_value in row[1].lower():
            order_table.insert("", "end", values=row)

def add_order(app):
    add_window = ttk.Toplevel(app)
    add_window.title("Thêm Đơn Hàng")

    fields = ["Mã", "Tên sản phẩm", "Ngày", "Tên khách hàng", "SDT", "Số lượng", "Thành tiền"]
    entries = {}

    for i, field in enumerate(fields):
        label = ttk.Label(add_window, text=field)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = ttk.Entry(add_window, bootstyle="secondary", width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[field] = entry

    def submit_order():
        new_order = tuple(entries[field].get().strip() for field in fields)

        try:
            quantity = int(entries["Số lượng"].get())
            total = entries["Thành tiền"].get().replace('.', '').replace(',', '')
            total = int(total)

            if any(not value for value in new_order):
                raise ValueError("Vui lòng không để trống các trường.")

            order_table.insert("", "end", values=new_order)
            sample_data.append(new_order)
            insert_order(new_order)  # Lưu vào cơ sở dữ liệu

            add_window.destroy()
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))

    add_button = ttk.Button(add_window, text="Thêm", bootstyle="secondary", command=submit_order)
    add_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

def edit_order(app):
    selected_item = order_table.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một đơn hàng để sửa.")
        return

    order_data = order_table.item(selected_item)["values"]

    edit_window = ttk.Toplevel(app)
    edit_window.title("Sửa Đơn Hàng")

    fields = ["Mã", "Tên sản phẩm", "Ngày", "Tên khách hàng", "SDT", "Số lượng", "Thành tiền"]
    entries = {}

    for i, field in enumerate(fields):
        label = ttk.Label(edit_window, text=field)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = ttk.Entry(edit_window, bootstyle="secondary", width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, order_data[i])
        entries[field] = entry

    def submit_edit():
        updated_order = tuple(entries[field].get().strip() for field in fields)

        try:
            quantity = int(entries["Số lượng"].get())
            total = entries["Thành tiền"].get().replace('.', '').replace(',', '')
            total = int(total)

            if any(not value for value in updated_order):
                raise ValueError("Vui lòng không để trống các trường.")

            order_table.item(selected_item, values=updated_order)
            update_order(updated_order)  # Cập nhật vào cơ sở dữ liệu

            # Cập nhật thông tin trong sample_data
            order_id = updated_order[0]
            for index, existing_order in enumerate(sample_data):
                if existing_order[0] == order_id:
                    sample_data[index] = updated_order
                    break

            edit_window.destroy()
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))

    save_button = ttk.Button(edit_window, text="Lưu", bootstyle="secondary", command=submit_edit)
    save_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

def delete_order():
    selected_item = order_table.selection()
    if selected_item:
        order_table.delete(selected_item)
        # Cần thêm mã xóa từ cơ sở dữ liệu
        order_id = order_table.item(selected_item)["values"][0]
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM donhang WHERE ma = ?", (order_id,))
        conn.commit()
        conn.close()
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn đơn hàng để xóa.")

def create_don_hang_tab(notebook, app):
    global search_entry, order_table

    frame_don_hang = ttk.Frame(notebook)
    notebook.add(frame_don_hang, text="ĐƠN HÀNG")

    search_entry = ttk.Entry(frame_don_hang, bootstyle="secondary", width=30)
    search_entry.insert(0, "tìm kiếm theo sản phẩm")
    search_entry.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    search_button = ttk.Button(frame_don_hang, text="Tìm kiếm", bootstyle="secondary",
                               command=lambda: button_click("Tìm kiếm", app))
    search_button.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    add_order_button = ttk.Button(frame_don_hang, text="Thêm đơn", bootstyle="secondary",
                                   command=lambda: button_click("Thêm đơn", app))
    add_order_button.grid(row=0, column=2, padx=5, pady=5, sticky=W)

    edit_order_button = ttk.Button(frame_don_hang, text="Sửa", bootstyle="secondary",
                                    command=lambda: button_click("Sửa", app))
    edit_order_button.grid(row=0, column=3, padx=5, pady=5, sticky=W)

    delete_button = ttk.Button(frame_don_hang, text="Xóa", bootstyle="secondary",
                               command=delete_order)
    delete_button.grid(row=0, column=4, padx=5, pady=5, sticky=W)

    latest_button = ttk.Button(frame_don_hang, text="Mới nhất", bootstyle="secondary",
                               command=lambda: button_click("Mới nhất", app))
    latest_button.grid(row=0, column=5, padx=5, pady=5, sticky=W)

    columns = ["Mã", "Tên sản phẩm", "Ngày", "Tên khách hàng", "SDT", "Số lượng", "Thành tiền"]

    order_table = ttk.Treeview(frame_don_hang, columns=columns, show="headings", bootstyle="secondary")
    order_table.grid(row=2, column=0, columnspan=len(columns), padx=10, pady=10)

    for col in columns:
        order_table.heading(col, text=col)
        order_table.column(col, anchor=CENTER)

    latest()
    create_don_hang_table()  # Tạo bảng khi khởi động ứng dụng
