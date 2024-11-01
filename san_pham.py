import sqlite3 
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style, Window
from ttkbootstrap.constants import *
from tkinter import PhotoImage

def create_table():
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('sanpham.db')
    cursor = conn.cursor()

    # Tạo bảng
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS KhachHang (
        Mã_sản_phẩm INTEGER PRIMARY KEY AUTOINCREMENT,
        Tên_sản_phẩm TEXT NOT NULL,
        Số_lượng INTEGER NOT NULL,
        Giá_Tiền REAL NOT NULL
    )
    ''')

    conn.commit()
    conn.close()
    print("Bảng khách hàng đã được tạo.")

def add_product(ten_san_pham, so_luong, gia_tien):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('sanpham.db')
    cursor = conn.cursor()
    
    # Thêm sản phẩm vào bảng
    cursor.execute('''
    INSERT INTO KhachHang (Tên_sản_phẩm, Số_lượng, Giá_Tiền)
    VALUES (?, ?, ?)
    ''', (ten_san_pham, so_luong, gia_tien))

    conn.commit()
    conn.close()
    print(f"Sản phẩm '{ten_san_pham}' đã được thêm.")

# Hàm để xử lý sự kiện khi nhấn nút
def on_add_product():
    ten_san_pham = entry_product_name.get()
    so_luong = entry_quantity.get()
    gia_tien = entry_price.get()

    if ten_san_pham and so_luong.isdigit() and gia_tien.replace('.', '', 1).isdigit():
        add_product(ten_san_pham, int(so_luong), float(gia_tien))
        entry_product_name.delete(0, tk.END)
        entry_quantity.delete(0, tk.END)
        entry_price.delete(0, tk.END)
    else:
        print("Vui lòng nhập đầy đủ thông tin hợp lệ.")

def delete_product(ma_san_pham):
    conn = sqlite3.connect('sanpham.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM KhachHang WHERE Mã_sản_phẩm=?", (ma_san_pham,))
    conn.commit()
    conn.close()
    print(f"Sản phẩm với mã {ma_san_pham} đã bị xóa.")
    
# Tạo cửa sổ chính
window = Window(themename ="flatly")
window.title("management application")
window.geometry("800x800")

# Gọi hàm để tạo bảng khi chạy chương trình
create_table()

# Tạo các thành phần giao diện
label_product_name = tk.Label(window, text="Tên sản phẩm:")
label_product_name.pack(pady=5)

entry_product_name = tk.Entry(window)
entry_product_name.pack(pady=5)

label_quantity = tk.Label(window, text="Số lượng:")
label_quantity.pack(pady=5)

entry_quantity = tk.Entry(window)
entry_quantity.pack(pady=5)

label_price = tk.Label(window, text="Giá tiền:")
label_price.pack(pady=5)

entry_price = tk.Entry(window)
entry_price.pack(pady=5)

btn_add_product = tk.Button(window, text="Thêm sản phẩm", command=on_add_product)
btn_add_product.pack(pady=20)

# Chạy vòng lặp chính
window.mainloop()
