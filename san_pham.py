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
    print("Bảng sản phẩm đã được tạo.")

# Hàm thêm sản phẩm vào CSDL
def add_product(ten_san_pham, so_luong, gia_tien):
    conn = sqlite3.connect('sanpham.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO KhachHang (Tên_sản_phẩm, Số_lượng, Giá_Tiền)
    VALUES (?, ?, ?)
    ''', (ten_san_pham, so_luong, gia_tien))
    conn.commit()
    conn.close()
    print(f"Sản phẩm '{ten_san_pham}' đã được thêm.")

def on_add_product():
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

def create_san_pham_tab(notebook):
    frame_san_pham = ttk.Frame(notebook)
    notebook.add(frame_san_pham, text="SẢN PHẨM")

    # Tạo các thành phần giao diện
    label_product_name = tk.Label(frame_san_pham, text="Tên sản phẩm:")
    label_product_name.pack(pady=5)

    global entry_product_name
    entry_product_name = tk.Entry(frame_san_pham)
    entry_product_name.pack(pady=5)

    label_quantity = tk.Label(frame_san_pham, text="Số lượng:")
    label_quantity.pack(pady=5)

    global entry_quantity
    entry_quantity = tk.Entry(frame_san_pham)
    entry_quantity.pack(pady=5)

    label_price = tk.Label(frame_san_pham, text="Giá tiền:")
    label_price.pack(pady=5)

    global entry_price
    entry_price = tk.Entry(frame_san_pham)
    entry_price.pack(pady=5)

    btn_add_product = tk.Button(frame_san_pham, text="Thêm sản phẩm", command=on_add_product)
    btn_add_product.pack(pady=20)

def create_canvas():
    window = tk.Tk()
    window.title("Quản lý sản phẩm")
    window.geometry("1920x1080")
    window.configure(background="#EAE7D6")

    # Tạo canvas
    canvas1 = tk.Canvas(window, bg="#B1C6B4", width=2000, height=200)
    canvas1.config(bs="#B1C6B4")
    canvas1.pack()

    # Bảng ngoài bìa 
    canvas2 = tk.Canvas(window, bg="#B1C6B4", width=515, height=835)
    canvas2.config(bs="#B1C6B4")
    canvas2.place(x=1400, y=205)

    # Bảng ở trung tâm
    canvas3 = tk.Canvas(window, bg="#B1C6B4", width=1390, height=835)
    canvas3.config(bs="#B1C6B4")
    canvas3.place(x=4, y=205)

    # Tạo notebook và tab cho sản phẩm
    notebook = ttk.Notebook(window)
    notebook.place(x=10, y=10, width=1370, height=700)
    create_san_pham_tab(notebook)

    window.mainloop()

# Gọi hàm để tạo bảng khi chạy chương trình
create_table()
create_canvas()
