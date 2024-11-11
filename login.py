from tkinter import messagebox
import ttkbootstrap as ttk

DEFAULT_PIN = "1234"  # Đặt mã PIN mặc định để đăng nhập

def check_pin(entry_pin, app, login_frame, notebook):
    """
    Hàm kiểm tra mã PIN khi nhấn nút "Đăng nhập".
    Nếu đúng mã PIN, ẩn giao diện đăng nhập và hiển thị giao diện chính.
    """
    if entry_pin.get() == DEFAULT_PIN:
        login_frame.pack_forget()  # Ẩn giao diện đăng nhập
        notebook.pack(fill="both", expand=True)  # Hiển thị giao diện chính
    else:
        messagebox.showerror("Lỗi", "Mã PIN không đúng. Vui lòng thử lại.")
        entry_pin.delete(0, 'end')  # Xóa mã PIN trong ô nhập

def create_login_frame(app, notebook):
    """
    Tạo giao diện đăng nhập trong cửa sổ chính và yêu cầu nhập mã PIN.
    """
    login_frame = ttk.Frame(app)
    login_frame.pack(fill="both", expand=True)

    label = ttk.Label(login_frame, text="Nhập mã PIN để đăng nhập", font=("Helvetica", 14))
    label.pack(pady=20)

    entry_pin = ttk.Entry(login_frame, show="*", font=("Helvetica", 14), width=15)
    entry_pin.pack(pady=10)

    login_button = ttk.Button(
        login_frame,
        text="Đăng nhập",
        command=lambda: check_pin(entry_pin, app, login_frame, notebook)
    )
    login_button.pack(pady=10)
