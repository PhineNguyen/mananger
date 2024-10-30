import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.constants import *

class OrderManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản Lý Đơn Hàng")
        
        # Thiết lập style
        style = Style(theme="minty")  # Chọn theme phù hợp với màu sắc
        root.geometry("600x350")
        
        # Tạo frame bên trái
        left_frame = tk.Frame(root, bg="#b3d9b3", width=150, height=350)
        left_frame.pack(side=LEFT, fill=Y)
        
        # Tiêu đề
        title_label = tk.Label(left_frame, text="ĐƠN HÀNG", font=("Arial", 12, "bold"), bg="#b3d9b3", fg="white")
        title_label.pack(pady=10)
        
        # Nhãn và ô nhập cho Tên Hàng
        tk.Label(left_frame, text="TÊN HÀNG", bg="#b3d9b3", fg="white", font=("Arial", 10)).pack(pady=(20, 5))
        self.ten_hang_entry = tk.Entry(left_frame, width=20)
        self.ten_hang_entry.pack(pady=5)
        
        # Nhãn và ô nhập cho Giá
        tk.Label(left_frame, text="GIÁ", bg="#b3d9b3", fg="white", font=("Arial", 10)).pack(pady=(20, 5))
        self.gia_entry = tk.Entry(left_frame, width=20)
        self.gia_entry.pack(pady=5)
        
        # Nút Thêm
        add_button = tk.Button(left_frame, text="THÊM", command=self.add_item, bg="#6bb36b", fg="white", font=("Arial", 10, "bold"))
        add_button.pack(pady=20)
        
        # Tạo frame bên phải
        right_frame = tk.Frame(root, bg="#e6e6e6", width=450, height=350)
        right_frame.pack(side=RIGHT, fill=BOTH, expand=True)
        
        # Tạo bảng đơn hàng
        self.tree = tk.ttk.Treeview(right_frame, columns=("stt", "ten_hang", "gia"), show="headings", height=10)
        self.tree.heading("stt", text="STT")
        self.tree.heading("ten_hang", text="TÊN HÀNG")
        self.tree.heading("gia", text="GIÁ")
        self.tree.column("stt", width=50, anchor=CENTER)
        self.tree.column("ten_hang", width=200)
        self.tree.column("gia", width=100, anchor=CENTER)
        self.tree.pack(fill=BOTH, padx=10, pady=10)
        
        # Khởi tạo STT
        self.stt = 1

    def add_item(self):
        ten_hang = self.ten_hang_entry.get()
        gia = self.gia_entry.get()
        
        if ten_hang and gia:
            self.tree.insert("", "end", values=(self.stt, ten_hang, gia))
            self.stt += 1
            self.ten_hang_entry.delete(0, tk.END)
            self.gia_entry.delete(0, tk.END)

# Khởi chạy ứng dụng
root = tk.Tk()
app = OrderManagerApp(root)
root.mainloop()
