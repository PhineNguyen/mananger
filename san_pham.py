import sqlite3
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style, Window
from ttkbootstrap.constants import *

# Hàm tạo bảng trong CSDL
def create_table():
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('sanpham.db')
    cursor = conn.cursor()

    # Tạo bảng
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SanPham (
        Mã_sản_phẩm INTEGER PRIMARY KEY AUTOINCREMENT,
        Tên_sản_phẩm TEXT NOT NULL,
        Số_lượng INTEGER NOT NULL,
        Giá_Tiền REAL NOT NULL
    )
    ''')

    conn.commit()
    conn.close()
    print("Bảng sản phẩm đã được tạo.")

# Hàm thêm sản phẩm vào CSDL
def add_product(ten_san_pham, so_luong, gia_tien):
    # Lưu sản phẩm vào CSDL (bạn có thể bỏ qua nếu không cần)
    conn = sqlite3.connect('sanpham.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO SanPham (Tên_sản_phẩm, Số_lượng, Giá_Tiền) VALUES (?, ?, ?)
    ''', (ten_san_pham, so_luong, gia_tien))
    conn.commit()
    conn.close()

    # Cập nhật danh sách đơn hàng trên canvas
    update_order_list(ten_san_pham, so_luong, gia_tien)

# Hàm cập nhật danh sách đơn hàng
def update_order_list(ten_san_pham, so_luong, gia_tien):
    order_text = f"{ten_san_pham: <100} {so_luong: <110} {gia_tien: <110} \n"
    order_list.insert(tk.END, order_text)  # Thêm thông tin đơn hàng vào listbox

# Hàm để xử lý khi nhấn nút thêm sản phẩm trong giao diện
def submit_product():
    ten_san_pham = entry_product_name.get()
    so_luong = entry_quantity.get()
    gia_tien = entry_price.get()

    # Kiểm tra thông tin nhập vào
    if ten_san_pham and so_luong.isdigit() and gia_tien.replace('.', '', 1).isdigit():
        add_product(ten_san_pham, int(so_luong), float(gia_tien))
        # Xóa thông tin sau khi thêm
        entry_product_name.delete(0, tk.END)
        entry_quantity.delete(0, tk.END)
        entry_price.delete(0, tk.END)
    else:
        print("Vui lòng nhập đầy đủ thông tin hợp lệ.")


# Giao diện người dùng
window = Window(themename="flatly")
window.title("Quản lý sản phẩm")
window.geometry("400x300")

# Tạo bảng khi khởi động chương trình
create_table()
#tạo canvas
canvas1=tk.Canvas(window, bg="#B1C6B4", width=2000, height=200)
canvas1.config(bg="#B1C6B4")
canvas1.pack()


canvas2 = tk.Canvas(window, bg="#B1C6B4",width=515,height= 835)
canvas2.config(bg="#B1C6B4")
canvas2.place(x=1400, y=205)

canvas3 = tk.Canvas(window, bg="#B1C6B4",width=1390,height =835)
canvas3.config(bg="#B1C6B4")
canvas3.place(x=4,y=205)

label_product_name = tk.Label(canvas2, text="Tên sản phẩm", bg="#B1C6B4")
canvas2.create_window(220,50, window=label_product_name)

entry_product_name = tk.Entry(canvas2)
canvas2.create_window(220, 90, window=entry_product_name)  # Điều chỉnh vị trí

# Tạo Label và Entry cho số lượng
label_quantity = tk.Label(canvas2, text="Số lượng", bg="#B1C6B4")
canvas2.create_window(220, 150, window=label_quantity)  # Điều chỉnh vị trí

entry_quantity = tk.Entry(canvas2)
canvas2.create_window(220, 190, window=entry_quantity)  # Điều chỉnh vị trí

# Tạo Label và Entry cho giá tiền
label_price = tk.Label(canvas2, text="Giá tiền", bg="#B1C6B4")
canvas2.create_window(220, 250, window=label_price)  # Điều chỉnh vị trí

entry_price = tk.Entry(canvas2)
canvas2.create_window(220, 290, window=entry_price)  # Điều chỉnh vị trí

# Nút Thêm sản phẩm
btn_add_product = tk.Button(canvas2, text="Thêm sản phẩm", command=submit_product)
canvas2.create_window(220, 330, window=btn_add_product)  # Điều chỉnh vị trí

#creat Label

order_list = tk.Listbox(canvas3, width = 138, height= 34)
order_list.place(x=2,y=1)

#tiêu đề cho ListBox
header_text=f"{'Tên sản phẩm': <100} {'Số lượng': <90}  {'Giá tiền': <100}"
order_list.insert(tk.END, header_text)

order_list.insert(tk.END,'-'*1000) #Tạo dòng phân cách

i = 1
while True:
    print("\nNhập thông tin qua dòng lệnh hoặc bấm Enter để dừng")
    ten_san_pham = str(input("Nhập tên sản phẩm: "))
    
    if not ten_san_pham:
        break
    
    so_luong = int(input("Nhập số lượng: "))
    gia_tien = float(input("Nhập giá tiền: "))
    add_product(ten_san_pham, so_luong, gia_tien)
    i+=1

# Chạy vòng lặp chính của giao diện
    window.mainloop()