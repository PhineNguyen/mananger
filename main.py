import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from san_pham import create_san_pham_tab
from don_hang import create_don_hang_tab
from thong_ke import create_thong_ke_tab
from khach_hang import create_khach_hang_tab
from staff_san_pham import staff_create_san_pham_tab
from staff_don_hang import staff_create_don_hang_tab
from staff_khach_hang import staff_create_khach_hang_tab
from login import create_login_frame
from setting import create_setting_tab, load_settings, apply_settings,refresh_tabs  # Import thêm load_settings
from tkinter import PhotoImage
from tkinter import messagebox
from bao_cao import create_bao_cao_tab




def load_main_interface(app, notebook, role):
    app.resizable(True, True)
    app.geometry("1200x800")

    # Thêm các tab cơ bản
    # create_san_pham_tab(notebook, app)
    # create_don_hang_tab(notebook, app)
    # create_khach_hang_tab(notebook, app)

    if role=="staff":
        staff_create_san_pham_tab(notebook, app)
        staff_create_don_hang_tab(notebook, app)
        staff_create_khach_hang_tab(notebook, app)

    # Chỉ thêm các tab đặc quyền nếu người dùng là chủ cửa hàng
    if role == "owner":
        create_san_pham_tab(notebook, app)
        create_don_hang_tab(notebook, app)
        create_khach_hang_tab(notebook, app)
        create_thong_ke_tab(notebook, app)
        create_setting_tab(notebook, app,create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab,create_setting_tab)  # Thêm tab Setting
        create_bao_cao_tab(notebook, app)  # Thêm tab Báo Cáo vào đây


    notebook.pack(fill="both", expand=True)

def change_window_icon(app):
    #Hàm thay đổi icon của cửa sổ
    try:
        icon = PhotoImage(file="masterplan.png")  # Đảm bảo file icon tồn tại
        app.iconphoto(False, icon)
    except Exception as e:
        print(f"Không thể thay đổi icon của cửa sổ: {e}")

def on_window_state_change(event, app, notebook, create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab, create_setting_tab):
    global dem, prev_state
    state = app.wm_state()
    
    if state == "zoomed" and prev_state != "zoomed":
        dem += 1
        #print("Cửa sổ đã được maximize.")
        prev_state = "zoomed"
    
    elif state == "normal" and prev_state == "zoomed" and dem > 0:
        window_width = app.winfo_width()
        window_height = app.winfo_height()
        
        if window_width < 1000 and window_height < 600:
            refresh_tabs(notebook, app, create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab, create_setting_tab)
        
        #print("Cửa sổ đã được restore.")
        dem -= 1
        prev_state = "normal"


def main():
    # Tải cài đặt từ file
    current_settings = load_settings()

    # Khởi tạo cửa sổ chính với theme từ cài đặt
    app = ttk.Window(themename=current_settings["theme"])
    app.geometry("600x400")
    app.title("Store Manager")
    app.resizable(False, False)


    # Áp dụng icon cho cửa sổ
    change_window_icon(app)

    # Tạo style cho tab với font từ cài đặt
    # style = ttk.Style()
    # style.configure("TNotebook.Tab", padding=[10, 5], font=(current_settings["font"], current_settings["font_size"]), background="#5bc0de")
    # style.map("TNotebook.Tab",
    #           background=[('selected', '#ADD8E6'), ('!selected', '#B1C6B4')],
    #           foreground=[('selected', 'white'), ('!selected', 'black')])
    # style.configure("TNotebook", tabposition='n')  # 'n' cho trên, 's' cho dưới, 'e' cho phải, 'w' cho trái

    #Tạo notebook
    notebook = ttk.Notebook(app, style="TNotebook")
    #notebook.pack(fill="both", expand=True)

    # Thêm các tab vào notebook
    # create_san_pham_tab(notebook, app)
    # create_don_hang_tab(notebook, app)
    # create_khach_hang_tab(notebook, app)
    # create_thong_ke_tab(notebook, app)
    # create_setting_tab(notebook, app,create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab,create_setting_tab)  # Thêm tab Setting
    # #login here
    #create_login_frame(app, notebook)

    # Hiển thị giao diện đăng nhập
    create_login_frame(app, notebook, load_main_interface)


    app.mainloop()

if __name__ == "__main__":
    main()

