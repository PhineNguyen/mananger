import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from tkinter import ttk as tk
#<<<<<<< HEAD
#change2
#=======
#thuc hien commit
#>>>>>>> d2cc202325303808779addfcafd2a877f5fc0cb3
# Hàm để thêm đối tác mới
def add_partner():
    messagebox.showinfo("Thêm đối tác", "Chức năng thêm đối tác giao hàng")

# Hàm import danh sách đối tác từ file
def import_file():
    messagebox.showinfo("Import", "Chức năng import file")

# Hàm export danh sách đối tác ra file
def export_file():
    messagebox.showinfo("Xuất file", "Chức năng xuất file")

# Tạo cửa sổ chính của ứng dụng
app = ttk.Window(themename="solar")
app.title("Quản lý đối tác giao hàng")
app.geometry("1000x600")

# Thanh công cụ
toolbar = ttk.Frame(app)
toolbar.pack(fill=X, pady=5)

add_button = ttk.Button(toolbar, text="Đối tác giao hàng", bootstyle=SUCCESS, command=add_partner)
add_button.pack(side=LEFT, padx=5)

import_button = ttk.Button(toolbar, text="Import", bootstyle=PRIMARY, command=import_file)
import_button.pack(side=LEFT, padx=5)

export_button = ttk.Button(toolbar, text="Xuất file", bootstyle=PRIMARY, command=export_file)
export_button.pack(side=LEFT, padx=5)

# Khu vực bộ lọc tìm kiếm
filter_frame = ttk.Frame(app)
filter_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)

ttk.Label(filter_frame, text="Nhóm đối tác giao hàng").pack(anchor="w", pady=5)
ttk.Combobox(filter_frame, values=["Tất cả các nhóm"]).pack(fill=X)

ttk.Label(filter_frame, text="Tìm kiếm").pack(anchor="w", pady=5)
ttk.Entry(filter_frame).pack(fill=X)

ttk.Label(filter_frame, text="Tổng phí giao hàng").pack(anchor="w", pady=5)
ttk.Entry(filter_frame, width=10).pack(fill=X)
ttk.Entry(filter_frame, width=10).pack(fill=X)

ttk.Label(filter_frame, text="Nợ hiện tại").pack(anchor="w", pady=5)
ttk.Entry(filter_frame, width=10).pack(fill=X)
ttk.Entry(filter_frame, width=10).pack(fill=X)

# Bảng danh sách đối tác giao hàng
partner_list_frame = ttk.Frame(app)
partner_list_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

columns = ("ID", "Tên đối tác", "Điện thoại", "Tổng đơn hàng", "Nợ hiện tại", "Tổng phí giao hàng")
partner_list = ttk.Treeview(partner_list_frame, columns=columns, show="headings")
for col in columns:
    partner_list.heading(col, text=col)
partner_list.pack(fill=BOTH, expand=True)

# Khu vực chi tiết đối tác
detail_frame = ttk.LabelFrame(app, text="Thông tin chi tiết")
detail_frame.pack(fill=X, padx=10, pady=10)

ttk.Label(detail_frame, text="Mã đối tác:").grid(row=0, column=0, sticky=W, padx=5, pady=5)
entry_id = ttk.Entry(detail_frame, width=30)
entry_id.grid(row=0, column=1, sticky=W)

ttk.Label(detail_frame, text="Tên đối tác:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
entry_name = ttk.Entry(detail_frame, width=30)
entry_name.grid(row=1, column=1, sticky=W)

ttk.Label(detail_frame, text="Điện thoại:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
entry_phone = ttk.Entry(detail_frame, width=30)
entry_phone.grid(row=2, column=1, sticky=W)

ttk.Label(detail_frame, text="Địa chỉ:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
entry_address = ttk.Entry(detail_frame, width=30)
entry_address.grid(row=3, column=1, sticky=W)

ttk.Label(detail_frame, text="Khu vực:").grid(row=4, column=0, sticky=W, padx=5, pady=5)
entry_area = ttk.Entry(detail_frame, width=30)
entry_area.grid(row=4, column=1, sticky=W)

ttk.Label(detail_frame, text="Phường/xã:").grid(row=5, column=0, sticky=W, padx=5, pady=5)
entry_ward = ttk.Entry(detail_frame, width=30)
entry_ward.grid(row=5, column=1, sticky=W)

# Nút chức năng cập nhật, ngừng hoạt động, xóa
button_frame = ttk.Frame(detail_frame)
button_frame.grid(row=6, columnspan=2, pady=10)

update_button = ttk.Button(button_frame, text="Cập nhật", bootstyle=SUCCESS)
update_button.grid(row=0, column=0, padx=5)

deactivate_button = ttk.Button(button_frame, text="Ngừng hoạt động", bootstyle=DANGER)
deactivate_button.grid(row=0, column=1, padx=5)

delete_button = ttk.Button(button_frame, text="Xóa", bootstyle=DANGER)
delete_button.grid(row=0, column=2, padx=5)

# Chạy ứng dụng
app.mainloop()
