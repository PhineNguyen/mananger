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

def save_settings(theme, font, font_size):
    # Hàm lưu cài đặt vào file config.json
    settings = {"theme": theme, "font": font, "font_size": font_size}
    with open(CONFIG_FILE, "w") as file:
        json.dump(settings, file)

def apply_settings(app, notebook, theme_var, font_var, font_size_var):
    # Thay đổi theme và font
    theme = theme_var.get()
    font = font_var.get()
    font_size = font_size_var.get()

    app.style.theme_use(theme)
    notebook.option_add("*TNotebook.Tab*Font", (font, font_size))

    # Lưu cài đặt mới
    save_settings(theme, font, font_size)

def create_setting_tab(notebook, app):
    # Tải cài đặt từ file
    current_settings = load_settings()

    # Tạo frame cho tab Setting
    setting_frame = ttk.Frame(notebook)
    notebook.add(setting_frame, text="Cài Đặt")

    # Theme selection
    theme_label = ttk.Label(setting_frame, text="Chọn Giao Diện")
    theme_label.pack(pady=10)

    theme_var = StringVar(value=current_settings["theme"])
    for theme in THEMES:
        theme_radio = ttk.Radiobutton(setting_frame, text=theme, variable=theme_var, value=theme)
        theme_radio.pack(anchor="w")

    # Font selection
    font_label = ttk.Label(setting_frame, text="Chọn Font Chữ")
    font_label.pack(pady=10)

    font_var = StringVar(value=current_settings["font"])
    font_dropdown = ttk.Combobox(setting_frame, textvariable=font_var, values=FONTS, state="readonly")
    font_dropdown.pack()

    # Font size selection
    font_size_label = ttk.Label(setting_frame, text="Chọn Cỡ Chữ")
    font_size_label.pack(pady=10)

    font_size_var = IntVar(value=current_settings["font_size"])
    font_size_spinbox = ttk.Spinbox(setting_frame, from_=8, to=32, textvariable=font_size_var)
    font_size_spinbox.pack()

    # Apply button
    apply_button = ttk.Button(
        setting_frame, 
        text="Áp Dụng", 
        command=lambda: apply_settings(app, notebook, theme_var, font_var, font_size_var)
    )
    apply_button.pack(pady=20)
