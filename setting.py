import json
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar, IntVar


# Danh sách các theme và font
THEMES = ["minty", "flatly", "darkly", "pulse", "solar"]
FONTS = ["Helvetica", "Arial", "Times New Roman", "Courier New"]
CONFIG_FILE = "config.json"

def load_settings():
    # Hàm tải cài đặt từ file config.json
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Trả về cài đặt mặc định nếu file không tồn tại hoặc bị lỗi
        return {"theme": "minty", "font": "Helvetica", "font_size": 14}
    
def reset_to_default_settings(app, notebook_right, theme_var, font_var, font_size_var, create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab, create_setting_tab):
    # Đặt giá trị mặc định
    default_settings = {"theme": "minty", "font": "Helvetica", "font_size": 14}
    
    # Cập nhật biến giao diện
    theme_var.set(default_settings["theme"])
    font_var.set(default_settings["font"])
    font_size_var.set(default_settings["font_size"])

    # Lưu cài đặt mặc định vào file
    save_settings(default_settings["theme"], default_settings["font"], default_settings["font_size"])

    # Áp dụng cài đặt mặc định
    apply_settings(app, notebook_right, theme_var, font_var, font_size_var, create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab, create_setting_tab)


def save_settings(theme, font, font_size):
    # Hàm lưu cài đặt vào file config.json
    settings = {"theme": theme, "font": font, "font_size": font_size}
    with open(CONFIG_FILE, "w") as file:
        json.dump(settings, file)

def refresh_tabs(notebook, app,create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab,create_setting_tab):
    # Xóa tất cả các tab hiện tại
    for tab in notebook.tabs():
        notebook.forget(tab)

    current_settings = load_settings()

    style = ttk.Style()
    style.configure("TNotebook.Tab", padding=[10, 5], font=(current_settings["font"], current_settings["font_size"]), background="#5bc0de")
    style.map("TNotebook.Tab",
              background=[('selected', '#ADD8E6'), ('!selected', '#B1C6B4')],
              foreground=[('selected', 'white'), ('!selected', 'black')])
    style.configure("TNotebook", tabposition='n')  # 'n' cho trên, 's' cho dưới, 'e' cho phải, 'w' cho trái


    # Tạo notebook
    #notebook = ttk.Notebook(app, style="TNotebook")
    notebook.configure(style="CustomNotebook.TNotebook")

    notebook.pack(fill=BOTH, expand=TRUE)

    # Thêm lại các tab sau khi cập nhật theme và font
    create_san_pham_tab(notebook, app)
    create_don_hang_tab(notebook, app)
    create_khach_hang_tab(notebook, app)
    create_thong_ke_tab(notebook, app)
    create_setting_tab(notebook, app,create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab,create_setting_tab)  # Thêm tab Setting

def apply_settings(app, notebook_right, theme_var, font_var, font_size_var,create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab,create_setting_tab):
    # Thay đổi theme và font
    theme = theme_var.get()
    font = font_var.get()
    font_size = font_size_var.get()

    # Thay đổi theme và font trong app và notebook
    app.style.theme_use(theme)
    notebook_right.option_add("*TNotebook.Tab*Font", (font, font_size))

    # Lưu cài đặt mới
    save_settings(theme, font, font_size)

    # Gọi hàm refresh_tabs để cập nhật lại các tab
    refresh_tabs(notebook_right, app,create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab,create_setting_tab)
    #refresh_tabs(notebook, app)


def create_setting_tab(notebook_right, app,create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab,create_setting_tab):
    # Tải cài đặt từ file
    current_settings = load_settings()

    # Tạo frame cho tab Setting
    setting_frame = ttk.Frame(notebook_right)
    notebook_right.add(setting_frame, text="CÀI ĐẶT", padding=(20,20))

    # Theme selection
    theme_label = ttk.Label(setting_frame, text="Chọn Giao Diện", font = (current_settings["font"],current_settings["font_size"],"bold"))
    theme_label.pack(pady=10)

    theme_var = StringVar(value=current_settings["theme"])
    for theme in THEMES:
        theme_radio = ttk.Radiobutton(setting_frame, text=theme, variable=theme_var, value=theme)
        theme_radio.pack(anchor="center")

    # Font selection
    font_label = ttk.Label(setting_frame, text="Chọn Font Chữ", font=(current_settings["font"], current_settings["font_size"],"bold"))
    font_label.pack(pady=10)

    font_var = StringVar(value=current_settings["font"])
    font_dropdown = ttk.Combobox(setting_frame, textvariable=font_var, values=FONTS, state="readonly")
    font_dropdown.pack()

    # Font size selection
    font_size_label = ttk.Label(setting_frame, text="Chọn Cỡ Chữ", font=(current_settings["font"], current_settings["font_size"],"bold"))
    font_size_label.pack(pady=10)

    font_size_var = IntVar(value=current_settings["font_size"])
    font_size_spinbox = ttk.Spinbox(setting_frame, from_=8, to=32, textvariable=font_size_var)
    font_size_spinbox.pack()

    # Hàm kiểm tra và giới hạn cỡ chữ trước khi áp dụng
    def limited_apply_settings():
        font_size = font_size_var.get()
        # Giới hạn giá trị cỡ chữ
        if font_size < 8:
            font_size_var.set(8)
        elif font_size > 32:
            font_size_var.set(32)
        apply_settings(app, notebook_right, theme_var, font_var, font_size_var, create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab, create_setting_tab)


    # Apply button
    apply_button = ttk.Button(
        setting_frame, 
        text="Áp Dụng", 
        #command=lambda: apply_settings(app, notebook_right, theme_var, font_var, font_size_var,create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab,create_setting_tab)
        command=limited_apply_settings
    )
    apply_button.pack(pady=20)

    # Default button
    default_button = ttk.Button(
        setting_frame,
        text="Mặc Định",
        command=lambda: reset_to_default_settings(app, notebook_right, theme_var, font_var, font_size_var, create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab, create_setting_tab)
    )
    default_button.pack(pady=10)
