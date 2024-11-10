import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from san_pham import create_san_pham_tab
from don_hang import create_don_hang_tab
from thong_ke import create_thong_ke_tab
from khach_hang import create_khach_hang_tab
from login import create_login_frame
from setting import create_setting_tab, load_settings,apply_settings  # Import thêm load_settings
from PIL import Image, ImageTk
from tkinter import PhotoImage
import time


click_count_san_pham = 0
last_click_time = 0


def change_window_icon(app, icon_path):
    #Hàm thay đổi icon của cửa sổ
    try:
        icon = PhotoImage(file="masterplan.png")  # Đảm bảo file icon tồn tại
        app.iconphoto(False, icon)
    except Exception as e:
        print(f"Không thể thay đổi icon của cửa sổ: {e}")

def on_tab_double_click(event):
    global last_click_time
    current_time = time.time()
    time_diff = current_time - last_click_time

    # Kiểm tra nếu double-click trong vòng 300ms
    if time_diff < 0.3:
        notebook = event.widget  # Lấy notebook từ sự kiện
        selected_tab = notebook.tab(notebook.select(), "text")  # Lấy tên của tab đang chọn

        # Kiểm tra nếu tab hiện tại là "SẢN PHẨM"
        if selected_tab == "SẢN PHẨM":
            print("Double-click vào tab SẢN PHẨM")

    # Cập nhật lại thời gian lần click trước
    last_click_time = current_time

def on_tab_changed(event):
    global click_count_san_pham
    notebook = event.widget  # Lấy notebook từ sự kiện
    selected_tab = notebook.tab(notebook.select(), "text")  # Lấy tên của tab đang chọn
    
    # Kiểm tra nếu tab hiện tại là "SẢN PHẨM"
    if selected_tab == "SẢN PHẨM":
        click_count_san_pham += 1
        print(f"Số lần nhấp vào tab SẢN PHẨM: {click_count_san_pham}")

def main():
    # Tải cài đặt từ file
    current_settings = load_settings()

    # Khởi tạo cửa sổ chính với theme từ cài đặt
    app = ttk.Window(themename=current_settings["theme"])
    app.geometry("800x500")
    app.title("Store Manager")

    # Áp dụng icon cho cửa sổ
    change_window_icon(app, "store_icon.png")

    # Tạo style cho tab với font từ cài đặt
    style = ttk.Style()
    style.configure("TNotebook.Tab", padding=[10, 5], font=(current_settings["font"], current_settings["font_size"]), background="#5bc0de")
    style.map("TNotebook.Tab",
              background=[('selected', '#ADD8E6'), ('!selected', '#B1C6B4')],
              foreground=[('selected', 'white'), ('!selected', 'black')])
    #style.configure("TNotebook", tabposition='n')  # 'n' cho trên, 's' cho dưới, 'e' cho phải, 'w' cho trái

    notebook_right = ttk.Notebook(app)
    notebook_right.pack(side="right", fill="both", expand=True)

    # Tạo notebook
    notebook = ttk.Notebook(app, style="TNotebook")
    notebook.pack(fill=BOTH, expand=TRUE)

    # Thêm các tab vào notebook
    create_san_pham_tab(notebook, app)
    create_don_hang_tab(notebook, app)
    create_khach_hang_tab(notebook, app)
    create_thong_ke_tab(notebook, app)
    create_setting_tab(notebook_right, app,create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab,create_setting_tab)  # Thêm tab Setting

    #create_login_frame(app, notebook)

    # Liên kết sự kiện <<NotebookTabChanged>> với hàm on_tab_changed
    notebook.bind("<Button-1>", on_tab_double_click)

    notebook.bind("<<NotebookTabChanged>>", on_tab_changed)
    notebook_right.bind("<<NotebookTabChanged>>", on_tab_changed)

    # Chạy ứng dụng
    app.mainloop()

if __name__ == "__main__":
    main()