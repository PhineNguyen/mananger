import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkcalendar import Calendar
from datetime import datetime

def open_toplevel():
    # Tạo cửa sổ Toplevel
    toplevel_window = ttk.Toplevel(root)
    toplevel_window.title("Lịch Tháng Này")
    toplevel_window.geometry("300x300")

    # Lấy ngày hiện tại
    today = datetime.today()
    current_year = today.year
    current_month = today.month

    # Thêm lịch hiển thị tháng hiện tại
    cal = Calendar(toplevel_window, selectmode="day", year=current_year, month=current_month)
    cal.pack(pady=20)

    # Thêm nút đóng cửa sổ
    close_button = ttk.Button(toplevel_window, text="Đóng", command=toplevel_window.destroy, bootstyle=DANGER)
    close_button.pack(pady=10)

# Tạo cửa sổ chính sử dụng ttkbootstrap
root = ttk.Window(themename="superhero")
root.title("Cửa sổ chính")
root.geometry("300x200")

# Nút mở Toplevel
open_button = ttk.Button(root, text="Mở Lịch Tháng Này", command=open_toplevel, bootstyle=SUCCESS)
open_button.pack(pady=50)

# Chạy vòng lặp chính
root.mainloop()
