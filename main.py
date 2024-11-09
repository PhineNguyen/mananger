import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from san_pham import create_san_pham_tab
from don_hang import create_don_hang_tab
from thong_ke import create_thong_ke_tab
from khach_hang import create_khach_hang_tab
from login import create_login_frame
from setting import create_setting_tab, load_settings  # Import thêm load_settings
from PIL import Image, ImageTk
from tkinter import PhotoImage



def change_window_icon(app, icon_path):
    #Hàm thay đổi icon của cửa sổ
    try:
        icon = PhotoImage(file="masterplan.png")  # Đảm bảo file icon tồn tại
        app.iconphoto(False, icon)
    except Exception as e:
        print(f"Không thể thay đổi icon của cửa sổ: {e}")

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
    style.configure("TNotebook.Tab", padding=[101, 5], font=(current_settings["font"], current_settings["font_size"]), background="#5bc0de")
    style.map("TNotebook.Tab",
              background=[('selected', '#ADD8E6'), ('!selected', '#B1C6B4')],
              foreground=[('selected', 'white'), ('!selected', 'black')])

    # Tạo notebook
    notebook = ttk.Notebook(app, style="TNotebook")
    #notebook.pack(fill=BOTH, expand=TRUE)

    # Thêm các tab vào notebook
    create_san_pham_tab(notebook, app)
    create_don_hang_tab(notebook, app)
    create_khach_hang_tab(notebook, app)
    create_thong_ke_tab(notebook, app)
    create_setting_tab(notebook, app)  # Thêm tab Setting

    create_login_frame(app, notebook)

    # Chạy ứng dụng
    app.mainloop()

if __name__ == "__main__":
    main()