from tkinter import messagebox
import ttkbootstrap as ttk

DEFAULT_PIN = "1234"  # Đặt mã PIN mặc định để đăng nhập

def check_pin(entry_pin, app, login_frame, notebook, notebook_right, notebook_right1):
    """
    Hàm kiểm tra mã PIN khi nhấn nút "Đăng nhập".
    Nếu đúng mã PIN, ẩn giao diện đăng nhập và hiển thị giao diện chính.
    """
    if entry_pin.get() == DEFAULT_PIN:
        # Ẩn giao diện đăng nhập
        login_frame.grid_forget()

        # Hiển thị giao diện chính
        notebook.grid(row=1, column=0, sticky="nsew")
        notebook_right.grid(row=0, column=1, sticky="nsew")
        notebook_right1.grid(row=1, column=1, rowspan=2, sticky="nsew")
        
        # Hiển thị lại các tab "Cài đặt" và "Thống kê" sau khi đăng nhập
        notebook_right.grid(row=0, column=1, sticky="nsew")
        notebook_right1.grid(row=1, column=1, rowspan=2, sticky="nsew")
    else:
        messagebox.showerror("Lỗi", "Mã PIN không đúng. Vui lòng thử lại.")
        entry_pin.delete(0, 'end')  # Xóa mã PIN trong ô nhập

def create_login_frame(app, notebook, notebook_right, notebook_right1):
    """
    Tạo giao diện đăng nhập trong cửa sổ chính và yêu cầu nhập mã PIN.
    """
    # Tạo login_frame và sử dụng grid để căn giữa
    login_frame = ttk.Frame(app)
    login_frame.grid(row=0, column=0, sticky="nsew")  # Đặt login_frame vào vị trí (0, 0)

    # Cấu hình các hàng và cột để cho phép co giãn và căn giữa
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    # Thêm một frame con trong login_frame để căn giữa nội dung
    inner_frame = ttk.Frame(login_frame)
    inner_frame.grid(row=0, column=0, padx=20, pady=20)  # Thêm khoảng cách với biên của cửa sổ

    # Cấu hình cho phép co giãn cho các hàng và cột của inner_frame
    inner_frame.grid_rowconfigure(0, weight=1)
    inner_frame.grid_rowconfigure(1, weight=1)
    inner_frame.grid_rowconfigure(2, weight=1)
    inner_frame.grid_columnconfigure(0, weight=1)

    # Thiết lập label, entry, và button vào inner_frame, với căn giữa
    label = ttk.Label(inner_frame, text="Nhập mã PIN để đăng nhập", font=("Helvetica", 14))
    label.grid(row=0, column=0, pady=20, sticky="nsew")  # Căn giữa với sticky="nsew"

    entry_pin = ttk.Entry(inner_frame, show="*", font=("Helvetica", 14), width=15)
    entry_pin.grid(row=1, column=0, pady=10, sticky="nsew")  # Căn giữa với sticky="nsew"

    login_button = ttk.Button(
        inner_frame,
        text="Đăng nhập",
        command=lambda: check_pin(entry_pin, app, login_frame, notebook, notebook_right, notebook_right1)
    )
    login_button.grid(row=2, column=0, pady=10, sticky="nsew")  # Căn giữa với sticky="nsew"

    # Ẩn các tab trong lúc login
    notebook.grid_forget()
    notebook_right.grid_forget()
    notebook_right1.grid_forget()

