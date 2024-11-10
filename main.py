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

def on_tab_double_click(event, notebook_bottom, app):
    global last_click_time
    current_time = time.time()
    time_diff = current_time - last_click_time

    # Kiểm tra nếu double-click trong vòng 300ms
    if time_diff < 0.3:
        notebook = event.widget  # Lấy notebook từ sự kiện
        selected_tab_id = notebook.select()  # Lấy ID của tab hiện tại

        # Kiểm tra nếu không có tab nào được chọn
        if not selected_tab_id:
            print("Không có tab nào được chọn.")
            return  # Dừng nếu không có tab được chọn

        selected_tab = notebook.tab(selected_tab_id, "text")  # Lấy tên của tab đang chọn
        tab_index = notebook.index("current")
        tab_frame = notebook.nametowidget(notebook.tabs()[tab_index])  # Lấy widget của tab

        # Kiểm tra nếu tab hiện tại là "SẢN PHẨM"
        if selected_tab == "SẢN PHẨM":
            print("Double-click vào tab SẢN PHẨM")
            notebook.forget(tab_index)  # Xóa tab khỏi notebook_top
            #notebook_bottom.add(tab_frame, text="SẢN PHẨM")  # Thêm tab vào notebook_bottom

            # Nếu cần tái tạo lại nội dung tab, sử dụng hàm tạo lại tab
            create_san_pham_tab(notebook_bottom, app)

        elif selected_tab == "ĐƠN HÀNG":
            print("Double-click vào tab ĐƠN HÀNG")
            notebook.forget(tab_index)  # Xóa tab khỏi notebook_top
            #notebook_bottom.add(tab_frame, text="ĐƠN HÀNG")  # Thêm tab vào notebook_bottom

            # Tái tạo lại nội dung của tab ĐƠN HÀNG
            create_don_hang_tab(notebook_bottom, app)

        elif selected_tab == "KHÁCH HÀNG":
            print("Double-click vào tab KHÁCH HÀNG")
            notebook.forget(tab_index)  # Xóa tab khỏi notebook_top
            #notebook_bottom.add(tab_frame, text="KHÁCH HÀNG")  # Thêm tab vào notebook_bottom

            # Tái tạo lại nội dung của tab KHÁCH HÀNG
            create_khach_hang_tab(notebook_bottom, app)

        elif selected_tab == "THỐNG KÊ":
            print("Double-click vào tab THỐNG KÊ")
            notebook.forget(tab_index)  # Xóa tab khỏi notebook_top
            # notebook_bottom.add(tab_frame, text="THỐNG KÊ")  # Thêm tab vào notebook_bottom
            create_thong_ke_tab(notebook_bottom, app)  # Tái tạo lại nội dung tab THỐNG KÊ

        elif selected_tab == "CÀI ĐẶT":
            print("Double-click vào tab CÀI ĐẶT")
            notebook.forget(tab_index)  # Xóa tab khỏi notebook_top
            # notebook_bottom.add(tab_frame, text="CÀI ĐẶT")  # Thêm tab vào notebook_bottom
            create_setting_tab(notebook_bottom, app)  # Tái tạo lại nội dung tab CÀI ĐẶT

    # Cập nhật lại thời gian lần click trước
    last_click_time = current_time

def on_tab_double_click2(event, notebook_top, app):
    global last_click_time
    current_time = time.time()
    time_diff = current_time - last_click_time

    # Kiểm tra nếu double-click trong vòng 300ms
    if time_diff < 0.3:
        notebook = event.widget  # Lấy notebook từ sự kiện
        selected_tab_id = notebook.select()  # Lấy ID của tab hiện tại

        # Kiểm tra nếu không có tab nào được chọn
        if not selected_tab_id:
            print("Không có tab nào được chọn.")
            return  # Dừng nếu không có tab được chọn

        selected_tab = notebook.tab(selected_tab_id, "text")  # Lấy tên của tab đang chọn
        tab_index = notebook.index("current")
        tab_frame = notebook.nametowidget(notebook.tabs()[tab_index])  # Lấy widget của tab

        # Kiểm tra nếu tab hiện tại là "SẢN PHẨM"
        if selected_tab == "SẢN PHẨM":
            print("Double-click vào tab SẢN PHẨM")
            notebook.forget(tab_index)  # Xóa tab khỏi notebook_top
            #notebook_bottom.add(tab_frame, text="SẢN PHẨM")  # Thêm tab vào notebook_bottom

            # Nếu cần tái tạo lại nội dung tab, sử dụng hàm tạo lại tab
            create_san_pham_tab(notebook_top, app)

        elif selected_tab == "ĐƠN HÀNG":
            print("Double-click vào tab ĐƠN HÀNG")
            notebook.forget(tab_index)  # Xóa tab khỏi notebook_top
            #notebook_bottom.add(tab_frame, text="ĐƠN HÀNG")  # Thêm tab vào notebook_bottom

            # Tái tạo lại nội dung của tab ĐƠN HÀNG
            create_don_hang_tab(notebook_top, app)

        elif selected_tab == "KHÁCH HÀNG":
            print("Double-click vào tab KHÁCH HÀNG")
            notebook.forget(tab_index)  # Xóa tab khỏi notebook_top
            #notebook_bottom.add(tab_frame, text="KHÁCH HÀNG")  # Thêm tab vào notebook_bottom

            # Tái tạo lại nội dung của tab KHÁCH HÀNG
            create_khach_hang_tab(notebook_top, app)

        elif selected_tab == "THỐNG KÊ":
            print("Double-click vào tab THỐNG KÊ")
            notebook.forget(tab_index)  # Xóa tab khỏi notebook_top
            # notebook_bottom.add(tab_frame, text="THỐNG KÊ")  # Thêm tab vào notebook_bottom
            create_thong_ke_tab(notebook_top, app)  # Tái tạo lại nội dung tab THỐNG KÊ

        elif selected_tab == "CÀI ĐẶT":
            print("Double-click vào tab CÀI ĐẶT")
            notebook.forget(tab_index)  # Xóa tab khỏi notebook_top
            # notebook_bottom.add(tab_frame, text="CÀI ĐẶT")  # Thêm tab vào notebook_bottom
            create_setting_tab(notebook_top, app)  # Tái tạo lại nội dung tab CÀI ĐẶT

    # Cập nhật lại thời gian lần click trước
    last_click_time = current_time


click_count_tabs = {
    "SẢN PHẨM": 0,
    "ĐƠN HÀNG": 0,
    "KHÁCH HÀNG": 0,
    "THỐNG KÊ": 0,
    "CÀI ĐẶT": 0
}

def on_tab_changed(event):
    global click_count_tabs
    notebook = event.widget  # Lấy notebook từ sự kiện
    selected_tab = notebook.tab(notebook.select(), "text")  # Lấy tên của tab đang chọn

    # Đếm số lần nhấp vào tab
    if selected_tab in click_count_tabs:
        click_count_tabs[selected_tab] += 1
        print(f"Số lần nhấp vào tab {selected_tab}: {click_count_tabs[selected_tab]}")

        # Thực hiện hành động cụ thể khi tab được chọn
        if selected_tab == "SẢN PHẨM":
            print("Tab 'SẢN PHẨM' đã được chọn.")
            # Thực hiện hành động đặc biệt cho tab SẢN PHẨM
        elif selected_tab == "ĐƠN HÀNG":
            print("Tab 'ĐƠN HÀNG' đã được chọn.")
            # Thực hiện hành động đặc biệt cho tab ĐƠN HÀNG
        elif selected_tab == "KHÁCH HÀNG":
            print("Tab 'KHÁCH HÀNG' đã được chọn.")
            # Thực hiện hành động đặc biệt cho tab KHÁCH HÀNG
        elif selected_tab == "THỐNG KÊ":
            print("Tab 'THỐNG KÊ' đã được chọn.")
            # Thực hiện hành động đặc biệt cho tab THỐNG KÊ
        elif selected_tab == "CÀI ĐẶT":
            print("Tab 'CÀI ĐẶT' đã được chọn.")
            # Thực hiện hành động đặc biệt cho tab CÀI ĐẶT




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

    #Tạo notebook
    notebook = ttk.Notebook(app, style="TNotebook")
    notebook_bottom = ttk.Notebook(app)
    notebook_right = ttk.Notebook(app)
    notebook_top = ttk.Notebook(app)
    notebook_right1 = ttk.Notebook(app)

    # notebook_right.pack(side="right", fill="both", expand=True)
    

    # notebook_bottom.pack(side="bottom", fill="both", expand=True)

    # notebook_top.pack(side="top", fill="both", expand=True)

    # notebook.pack(side="left", fill=BOTH, expand=TRUE)

    # Đặt các Notebook trong lưới
    notebook_top.grid(row=0, column=0, sticky="nsew")
    notebook.grid(row=1, column=0, sticky="nsew")
    
    # Cài đặt notebook_right ở hàng trên của cột bên phải (để làm tab Cài đặt)
    notebook_right.grid(row=0, column=1, sticky="nsew")

    # Cài đặt notebook_right1 ở hàng dưới của cột bên phải (để làm tab Thống kê)
    notebook_right1.grid(row=1, column=1, rowspan=2, sticky="nsew")
    notebook_bottom.grid(row=2, column=0, sticky="nsew")

    # Cấu hình hàng và cột để cho phép co giãn
    app.grid_rowconfigure(1, weight=1)  # Tab giữa (sản phẩm)
    app.grid_rowconfigure(2, weight=1)  # Tab dưới (khách hàng)
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)


    # Thêm các tab vào notebook
    create_san_pham_tab(notebook_top, app)
    create_don_hang_tab(notebook_top, app)
    create_khach_hang_tab(notebook_top, app)
    create_thong_ke_tab(notebook_right1, app)
    create_setting_tab(notebook_right, app,create_san_pham_tab, create_don_hang_tab, create_khach_hang_tab, create_thong_ke_tab,create_setting_tab)  # Thêm tab Setting

    #create_login_frame(app, notebook)

    # Liên kết sự kiện <<NotebookTabChanged>> với hàm on_tab_changed
    notebook.bind("<Button-1>", on_tab_double_click)
    # notebook_top.bind("<Button-1>", on_tab_double_click)
    # notebook_bottom.bind("<Button-1>", on_tab_double_click)
    notebook_right.bind("<Button-1>", on_tab_double_click)
    notebook_right1.bind("<Button-1>", on_tab_double_click)

    notebook.bind("<<NotebookTabChanged>>", on_tab_changed)
    notebook_top.bind("<<NotebookTabChanged>>", on_tab_changed)
    notebook_bottom.bind("<<NotebookTabChanged>>", on_tab_changed)
    notebook_right.bind("<<NotebookTabChanged>>", on_tab_changed)
    notebook_right1.bind("<<NotebookTabChanged>>", on_tab_changed)

    # Liên kết sự kiện double-click với các notebook
    notebook_top.bind("<Button-1>", lambda event: on_tab_double_click(event, notebook_bottom,app))
    notebook_bottom.bind("<Button-1>", lambda event: on_tab_double_click2(event, notebook_top,app))

    notebook.pack_forget

    # Chạy ứng dụng
    app.mainloop()

if __name__ == "__main__":
    main()