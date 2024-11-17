import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from captcha.image import ImageCaptcha
import random
import string
from PIL import Image, ImageTk

# Dữ liệu giả lập (thay bằng cơ sở dữ liệu trong thực tế)
USER_DATA = {
    "admin": {"password": "admin123", "email": "admin@example.com"},
    "staff": {"password": "staff123", "email": "staff@example.com"},
}

def reset_password(username):
    """
    Hiển thị giao diện đặt lại mật khẩu.
    """
    def confirm_reset():
        new_password = entry_new_password.get().strip()
        confirm_password = entry_confirm_password.get().strip()

        if new_password != confirm_password:
            messagebox.showerror("Lỗi", "Mật khẩu không khớp. Vui lòng thử lại.")
            return

        if len(new_password) < 6:
            messagebox.showerror("Lỗi", "Mật khẩu phải có ít nhất 6 ký tự.")
            return

        # Cập nhật mật khẩu mới
        USER_DATA[username]["password"] = new_password
        messagebox.showinfo("Thành công", "Mật khẩu đã được đặt lại.")
        reset_window.destroy()

    # Giao diện đặt lại mật khẩu
    reset_window = ttk.Toplevel()
    reset_window.title("Đặt lại mật khẩu")
    reset_window.geometry("400x250")

    ttk.Label(reset_window, text="Mật khẩu mới:").pack(pady=10, anchor="w", padx=20)
    entry_new_password = ttk.Entry(reset_window, show="*")
    entry_new_password.pack(fill="x", padx=20)

    ttk.Label(reset_window, text="Xác nhận mật khẩu:").pack(pady=10, anchor="w", padx=20)
    entry_confirm_password = ttk.Entry(reset_window, show="*")
    entry_confirm_password.pack(fill="x", padx=20)

    ttk.Button(reset_window, text="Xác nhận", command=confirm_reset).pack(pady=20)

def forgot_password():
    """
    Xử lý quên mật khẩu.
    """
    def verify_email():
        username = entry_username.get().strip()
        email = entry_email.get().strip()

        if username not in USER_DATA:
            messagebox.showerror("Lỗi", "Tên đăng nhập không tồn tại.")
            return

        if USER_DATA[username]["email"] != email:
            messagebox.showerror("Lỗi", "Email không khớp với tài khoản.")
            return

        # Xác thực thành công, chuyển sang đặt lại mật khẩu
        messagebox.showinfo("Thành công", "Xác thực thành công. Vui lòng đặt lại mật khẩu.")
        forgot_window.destroy()
        reset_password(username)

    # Giao diện quên mật khẩu
    forgot_window = ttk.Toplevel()
    forgot_window.title("Quên mật khẩu")
    forgot_window.geometry("400x250")

    ttk.Label(forgot_window, text="Tên đăng nhập:").pack(pady=10, anchor="w", padx=20)
    entry_username = ttk.Entry(forgot_window)
    entry_username.pack(fill="x", padx=20)

    ttk.Label(forgot_window, text="Email:").pack(pady=10, anchor="w", padx=20)
    entry_email = ttk.Entry(forgot_window)
    entry_email.pack(fill="x", padx=20)

    ttk.Button(forgot_window, text="Xác nhận", command=verify_email).pack(pady=20)

def generate_captcha_text(length=4):
    """
    Sinh chuỗi ngẫu nhiên gồm chữ cái cho Captcha (dễ đoán hơn).
    """
    return ''.join(random.choices(string.ascii_lowercase, k=length))  # Chỉ dùng chữ cái

def create_captcha_image(captcha_text):
    """
    Tạo hình ảnh Captcha từ chuỗi văn bản với font mặc định.
    """
    image = ImageCaptcha()  # Sử dụng font mặc định của PIL
    data = image.generate(captcha_text)
    captcha_image = Image.open(data)
    return captcha_image



def create_login_frame(app, notebook, load_main_interface):
    def authenticate():
        username = entry_username.get().strip()
        password = entry_password.get().strip()
        entered_captcha = entry_captcha.get().strip()

        if entered_captcha != current_captcha.get():
            messagebox.showerror("Xác minh thất bại", "Captcha không khớp. Vui lòng thử lại!")
            refresh_captcha()
            return

        if username in USER_DATA and USER_DATA[username]["password"] == password:
            user_role.set("owner" if username == "admin" else "staff")
            messagebox.showinfo("Đăng nhập", f"Đăng nhập thành công với vai trò: {user_role.get()}")
            login_frame.destroy()
            load_main_interface(app, notebook, user_role.get())
        else:
            messagebox.showerror("Đăng nhập", "Sai tên đăng nhập hoặc mật khẩu!")
            refresh_captcha()

    def refresh_captcha():
        new_captcha_text = generate_captcha_text()
        current_captcha.set(new_captcha_text)

        new_captcha_image = create_captcha_image(new_captcha_text)
        captcha_photo = ImageTk.PhotoImage(new_captcha_image)
        captcha_label.config(image=captcha_photo)
        captcha_label.image = captcha_photo

    # Biến Captcha hiện tại
    current_captcha = ttk.StringVar(value=generate_captcha_text())

    # Khung đăng nhập chính
    login_frame = ttk.Frame(app)
    login_frame.pack(fill="both", expand=True)

    ttk.Label(login_frame, text="Đăng nhập", font=("Arial", 16, "bold")).pack(pady=20)

    # Khung trung tâm
    center_frame = ttk.Frame(login_frame)
    center_frame.pack(anchor="center", pady=10)

    ttk.Label(center_frame, text="Tên đăng nhập:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
    entry_username = ttk.Entry(center_frame, width=25)
    entry_username.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(center_frame, text="Mật khẩu:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entry_password = ttk.Entry(center_frame, show="*", width=25)
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    # Captcha
    ttk.Label(center_frame, text="Xác minh: Tôi không phải là robot").grid(row=2, column=0, columnspan=2, pady=10)

    captcha_image = create_captcha_image(current_captcha.get())
    captcha_photo = ImageTk.PhotoImage(captcha_image)
    captcha_label = ttk.Label(center_frame, image=captcha_photo)
    captcha_label.image = captcha_photo
    captcha_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Khung chứa nhập Captcha và nút Làm mới
    captcha_frame = ttk.Frame(center_frame)
    captcha_frame.grid(row=4, column=0, columnspan=2, pady=5)

    entry_captcha = ttk.Entry(captcha_frame, width=15)
    entry_captcha.pack(side="left", padx=(0, 5))

    ttk.Button(captcha_frame, text="Làm mới", bootstyle="secondary", command=refresh_captcha).pack(side="right")

    ttk.Button(login_frame, text="Đăng nhập", bootstyle="primary", command=authenticate).pack(pady=20)
    ttk.Button(login_frame, text="Quên mật khẩu", bootstyle="secondary", command=forgot_password).pack(pady=(0, 20))

    global user_role
    user_role = ttk.StringVar(value="guest")

