import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.messagebox as messagebox  # Import messagebox từ tkinter

# Dữ liệu mẫu
sample_data = [
    ("123", "Dép lào", "1/11/2024", "Túy", "0123", "2", "100.000"),
    ("124", "Áo thun", "2/11/2024", "Minh", "0456", "1", "150.000"),
    ("125", "Nón bảo hiểm", "3/11/2024", "Hùng", "0789", "3", "300.000"),
]

def button_click(button_name, app):
    if button_name == "Tìm kiếm":
        search_order(app)  # Truyền app vào search_order
    elif button_name == "Thêm đơn":
        add_order(app)
    elif button_name == "Mới nhất":
        latest()

def latest():
    for row in order_table.get_children():
        order_table.delete(row)

    for row in sample_data:
        order_table.insert("", "end", values=row)

def search_order(app):  # Đảm bảo app được truyền vào
    search_value = search_entry.get().lower()
    for row in order_table.get_children():
        order_table.delete(row)

    for row in sample_data:
        if search_value in row[1].lower():
            order_table.insert("", "end", values=row)

def add_order(app):
    # Tạo cửa sổ mới cho việc nhập đơn hàng
    add_window = ttk.Toplevel(app)  # Sử dụng app từ tham số truyền vào
    add_window.title("Thêm Đơn Hàng")

    # Các trường nhập liệu
    fields = ["Mã", "Tên sản phẩm", "Ngày", "Tên khách hàng", "SDT", "Số lượng", "Thành tiền"]
    entries = {}

    for i, field in enumerate(fields):
        label = ttk.Label(add_window, text=field)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = ttk.Entry(add_window, bootstyle="secondary", width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[field] = entry

    # Hàm để thêm đơn hàng vào bảng
    def submit_order():
        new_order = tuple(entries[field].get().strip() for field in fields)

        # Kiểm tra dữ liệu đầu vào
        try:
            # Kiểm tra nếu số lượng và thành tiền là số
            quantity = int(entries["Số lượng"].get())
            total = entries["Thành tiền"].get().replace('.', '').replace(',', '')
            total = int(total)

            # Kiểm tra xem các trường không trống
            if any(not value for value in new_order):
                raise ValueError("Vui lòng không để trống các trường.")

            # Thêm đơn hàng vào bảng
            order_table.insert("", "end", values=new_order)
            add_window.destroy()  # Đóng cửa sổ sau khi thêm
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))  # Sử dụng messagebox từ tkinter

    # Nút Thêm
    add_button = ttk.Button(add_window, text="Thêm", bootstyle="secondary", command=submit_order)
    add_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

def delete_order():
    selected_item = order_table.selection()
    if selected_item:
        order_table.delete(selected_item)
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn đơn hàng để xóa.")  # Sử dụng messagebox từ tkinter

def create_don_hang_tab(notebook, app):  # Thêm app vào tham số
    global search_entry, order_table

    frame_don_hang = ttk.Frame(notebook)
    notebook.add(frame_don_hang, text="ĐƠN HÀNG")

    search_entry = ttk.Entry(frame_don_hang, bootstyle="secondary", width=30)
    search_entry.insert(0, "tìm kiếm theo sản phẩm")
    search_entry.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    search_button = ttk.Button(frame_don_hang, text="Tìm kiếm", bootstyle="secondary",
                               command=lambda: button_click("Tìm kiếm", app))  # Truyền app vào
    search_button.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    add_order_button = ttk.Button(frame_don_hang, text="Thêm đơn", bootstyle="secondary",
                                   command=lambda: button_click("Thêm đơn", app))
    add_order_button.grid(row=0, column=2, padx=5, pady=5, sticky=W)

    delete_button = ttk.Button(frame_don_hang, text="Xóa", bootstyle="secondary",
                               command=delete_order)
    delete_button.grid(row=0, column=3, padx=5, pady=5, sticky=W)

    latest_button = ttk.Button(frame_don_hang, text="Mới nhất", bootstyle="secondary",
                               command=lambda: button_click("Mới nhất", app))
    latest_button.grid(row=0, column=4, padx=5, pady=5, sticky=W)

    columns = ["Mã", "Tên sản phẩm", "Ngày", "Tên khách hàng", "SDT", "Số lượng", "Thành tiền"]

    order_table = ttk.Treeview(frame_don_hang, columns=columns, show="headings", bootstyle="secondary")
    order_table.grid(row=2, column=0, columnspan=len(columns), padx=5, pady=5, sticky="nsew")

    for col in columns:
        order_table.heading(col, text=col)
        order_table.column(col, width=100)

    for row in sample_data:
        order_table.insert("", "end", values=row)

    frame_don_hang.grid_rowconfigure(2, weight=1)
    frame_don_hang.grid_columnconfigure(0, weight=1)

if __name__ == "__main__":
    # Không cần khởi tạo lại app ở đây
    pass
