import tkinter as tk
from tkinter import messagebox

def create_login_window():
    # Tạo cửa sổ đăng nhập
    login_window = tk.Toplevel()
    login_window.geometry("400x300")
    login_window.title("Đăng nhập")
    
    # Label và Entry cho mã PIN
    pin_label = tk.Label(login_window, text="Nhập mã PIN:")
    pin_label.pack(pady=20)
    
    pin_entry = tk.Entry(login_window, show="*")
    pin_entry.pack(pady=10)
    
    # Hàm kiểm tra mã PIN
    def check_pin():
        pin = pin_entry.get()
        if pin == "1234":  # Mã PIN đúng
            login_window.destroy()  # Đóng cửa sổ đăng nhập
            return True  # Trả về True để mở cửa sổ chính
        else:
            messagebox.showerror("Sai mã PIN", "Mã PIN không đúng!")
            return False

    # Button để kiểm tra mã PIN
    login_button = tk.Button(login_window, text="Đăng nhập", command=check_pin)
    login_button.pack(pady=10)
    
    return login_window
