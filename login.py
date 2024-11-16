import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

def create_login_frame(app, notebook, load_main_interface):
    """
    Tạo giao diện đăng nhập và xử lý xác thực người dùng.

    Args:
        app: Cửa sổ chính của ứng dụng.
        notebook: Notebook sẽ chứa các tab sau khi đăng nhập.
        load_main_interface: Hàm để tải giao diện chính sau khi đăng nhập thành công.
    """
    def authenticate():
        """
        Xác thực người dùng dựa trên tên đăng nhập và mật khẩu.
        """
        username = entry_username.get().strip()
        password = entry_password.get().strip()

        # Xác định vai trò tài khoản dựa trên thông tin nhập
        if username == "admin" and password == "admin123":
            user_role.set("owner")  # Chủ cửa hàng
            messagebox.showinfo("Đăng nhập", "Đăng nhập thành công với vai trò: Chủ cửa hàng")
            login_frame.destroy()
            load_main_interface(app, notebook, user_role.get())
        elif username == "staff" and password == "staff123":
            user_role.set("staff")  # Nhân viên
            messagebox.showinfo("Đăng nhập", "Đăng nhập thành công với vai trò: Nhân viên")
            login_frame.destroy()
            load_main_interface(app, notebook, user_role.get())
        else:
            messagebox.showerror("Đăng nhập", "Sai tên đăng nhập hoặc mật khẩu!")

    # Tạo giao diện đăng nhập
    login_frame = ttk.Frame(app)
    login_frame.pack(fill="both", expand=True)

    # Tiêu đề đăng nhập
    ttk.Label(login_frame, text="Đăng nhập", font=("Arial", 16, "bold")).pack(pady=20)

    # Nhãn và ô nhập tên đăng nhập
    ttk.Label(login_frame, text="Tên đăng nhập:").pack(anchor="w", padx=20)
    entry_username = ttk.Entry(login_frame)
    entry_username.pack(fill="x", padx=20)

    # Nhãn và ô nhập mật khẩu
    ttk.Label(login_frame, text="Mật khẩu:").pack(anchor="w", padx=20, pady=(10, 0))
    entry_password = ttk.Entry(login_frame, show="*")
    entry_password.pack(fill="x", padx=20)

    # Nút đăng nhập
    ttk.Button(login_frame, text="Đăng nhập", bootstyle="primary", command=authenticate).pack(pady=20)

    # Biến lưu vai trò người dùng
    global user_role
    user_role = ttk.StringVar(value="guest")  # Mặc định là khách
