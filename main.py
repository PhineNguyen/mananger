import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from san_pham import create_san_pham_tab
from don_hang import create_don_hang_tab
from thong_ke import create_thong_ke_tab
from khach_hang import create_khach_hang_tab
from login import create_login_frame
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
    # Khởi tạo cửa sổ chính
    app = ttk.Window(themename="minty")
    app.geometry("800x500")
    app.title("Store Manager")  # Đặt tên ban đầu cho cửa sổ

    change_window_icon(app, "store_icon.png")  # Đảm bảo file store_icon.png có trong thư mục


    # Create a frame for the title area at the top
    title_frame = ttk.Frame(app)
    title_frame.pack(side=TOP, fill=X, padx=10, pady=10)

    # Tạo style cho tab
    style = ttk.Style()
    style.configure("TNotebook.Tab", padding=[101, 5], font=('Helvetica', 14), background="#5bc0de")
    style.map("TNotebook.Tab",
              background=[('selected', '#ADD8E6'), ('!selected', '#B1C6B4')],
              foreground=[('selected', 'white'), ('!selected', 'black')])

    # Tạo notebook với style tùy chỉnh
    notebook = ttk.Notebook(app, style="TNotebook")
    #notebook.pack(fill=BOTH, expand=TRUE)

    # Thêm các tab vào notebook
    create_san_pham_tab(notebook, app)
    create_don_hang_tab(notebook, app)
    create_khach_hang_tab(notebook, app)
    create_thong_ke_tab(notebook, app)

    create_login_frame(app, notebook)

    # Chạy ứng dụng
    app.mainloop()

if __name__ == "__main__":
    main()
