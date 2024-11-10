import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from san_pham import create_san_pham_tab
from don_hang import create_don_hang_tab
from thong_ke import create_thong_ke_tab
from khach_hang import create_khach_hang_tab
from login import create_login_frame
from setting import create_setting_tab, load_settings, apply_settings  # Import thêm load_settings
from PIL import Image, ImageTk
from tkinter import PhotoImage
import time

click_count_san_pham = 0
last_click_time = 0

def change_window_icon(app, icon_path):
    try:
        icon = PhotoImage(file=icon_path)  # Ensure icon file exists
        app.iconphoto(False, icon)
    except Exception as e:
        print(f"Không thể thay đổi icon của cửa sổ: {e}")

# Double-click event handlers
def on_tab_double_click(event, notebook_bottom, app):
    global last_click_time
    current_time = time.time()
    time_diff = current_time - last_click_time
    if time_diff < 0.3:
        notebook = event.widget
        selected_tab_id = notebook.select()
        if not selected_tab_id:
            print("Không có tab nào được chọn.")
            return

        selected_tab = notebook.tab(selected_tab_id, "text")
        tab_index = notebook.index("current")

        if selected_tab == "SẢN PHẨM":
            notebook.forget(tab_index)
            create_san_pham_tab(notebook_bottom, app)
        elif selected_tab == "ĐƠN HÀNG":
            notebook.forget(tab_index)
            create_don_hang_tab(notebook_bottom, app)
        elif selected_tab == "KHÁCH HÀNG":
            notebook.forget(tab_index)
            create_khach_hang_tab(notebook_bottom, app)
        elif selected_tab == "THỐNG KÊ":
            notebook.forget(tab_index)
            create_thong_ke_tab(notebook_bottom, app)
        elif selected_tab == "CÀI ĐẶT":
            notebook.forget(tab_index)
            create_setting_tab(notebook_bottom, app)
    last_click_time = current_time

click_count_tabs = {"SẢN PHẨM": 0, "ĐƠN HÀNG": 0, "KHÁCH HÀNG": 0, "THỐNG KÊ": 0, "CÀI ĐẶT": 0}

def on_tab_changed(event):
    global click_count_tabs
    notebook = event.widget
    selected_tab = notebook.tab(notebook.select(), "text")
    if selected_tab in click_count_tabs:
        click_count_tabs[selected_tab] += 1
        print(f"Số lần nhấp vào tab {selected_tab}: {click_count_tabs[selected_tab]}")

def main():
    app = ttk.Window(themename="minty")
    app.geometry("800x500")
    app.title("Store Manager")
    change_window_icon(app, "store_icon.png")
    style = ttk.Style()
    style.configure("TNotebook.Tab", padding=[10, 5], font=("Arial", 10), background="#5bc0de")
    style.map("TNotebook.Tab", background=[('selected', '#ADD8E6'), ('!selected', '#B1C6B4')], foreground=[('selected', 'white'), ('!selected', 'black')])

    notebook = ttk.Notebook(app, style="TNotebook")
    notebook_bottom = ttk.Notebook(app)
    notebook_right = ttk.Notebook(app)
    notebook_top = ttk.Notebook(app)
    notebook_right1 = ttk.Notebook(app)

    notebook_top.grid(row=0, column=0, sticky="nsew")
    notebook.grid(row=1, column=0, sticky="nsew")
    notebook_right.grid(row=0, column=1, sticky="nsew")
    notebook_right1.grid(row=1, column=1, rowspan=2, sticky="nsew")
    notebook_bottom.grid(row=2, column=0, sticky="nsew")

    app.grid_rowconfigure(1, weight=1)
    app.grid_rowconfigure(2, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)

    create_san_pham_tab(notebook, app)
    create_don_hang_tab(notebook, app)
    create_khach_hang_tab(notebook, app)
    create_thong_ke_tab(notebook, app)
    create_setting_tab(notebook, app)

    create_login_frame(app, notebook)
    app.mainloop()

if __name__ == "__main__":
    main()
