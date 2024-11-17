import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from captcha.image import ImageCaptcha
import random
import string
from PIL import Image, ImageTk
import json
import hashlib
import os

PASSWORD_FILE = "password.json"

# --- Utility Functions ---
def hash_password(password):
    """Mã hóa mật khẩu bằng SHA256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def load_user_credentials():
    """Tải thông tin người dùng từ file JSON."""
    if os.path.exists(PASSWORD_FILE):
        try:
            with open(PASSWORD_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            messagebox.showerror("Lỗi", "Dữ liệu người dùng không hợp lệ. Tạo lại tệp dữ liệu.")
    return {}

def save_user_credentials(username, password, email=None):
    """Lưu thông tin người dùng vào file JSON."""
    credentials = load_user_credentials()
    credentials[username] = {
        "hashed_password": hash_password(password),
        "email": email
    }
    with open(PASSWORD_FILE, "w") as file:
        json.dump(credentials, file, indent=4)

def verify_user_credentials(username, password):
    """Xác minh thông tin đăng nhập."""
    credentials = load_user_credentials()
    return (
        username in credentials and
        credentials[username]["hashed_password"] == hash_password(password)
    )

def initialize_default_users():
    """Khởi tạo người dùng mặc định nếu chưa tồn tại."""
    credentials = load_user_credentials()
    if "admin" not in credentials:
        save_user_credentials("admin", "admin123", "admin@example.com")
    if "staff" not in credentials:
        save_user_credentials("staff", "staff123", "staff@example.com")

# --- Captcha Functions ---
def generate_captcha(length=5):
    """Sinh chuỗi và hình ảnh Captcha."""
    text = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    image = ImageCaptcha()
    captcha_image = Image.open(image.generate(text))
    return text, captcha_image

# --- Password Reset ---
def reset_password(username):
    """Giao diện đặt lại mật khẩu."""
    def confirm_reset():
        new_password = entry_new_password.get().strip()
        confirm_password = entry_confirm_password.get().strip()
        if new_password != confirm_password:
            messagebox.showerror("Lỗi", "Mật khẩu không khớp.")
            return
        if len(new_password) < 6 or not any(c.isdigit() for c in new_password):
            messagebox.showerror("Lỗi", "Mật khẩu phải có ít nhất 6 ký tự và 1 số.")
            return
        save_user_credentials(username, new_password)
        messagebox.showinfo("Thành công", "Mật khẩu đã được đặt lại.")
        reset_window.destroy()

    reset_window = ttk.Toplevel()
    reset_window.title("Đặt lại mật khẩu")
    reset_window.geometry("400x200")

    ttk.Label(reset_window, text="Mật khẩu mới:").pack(pady=10, anchor="w", padx=20)
    entry_new_password = ttk.Entry(reset_window, show="*")
    entry_new_password.pack(fill="x", padx=20)

    ttk.Label(reset_window, text="Xác nhận mật khẩu:").pack(pady=10, anchor="w", padx=20)
    entry_confirm_password = ttk.Entry(reset_window, show="*")
    entry_confirm_password.pack(fill="x", padx=20)

    ttk.Button(reset_window, text="Xác nhận", command=confirm_reset).pack(pady=20)

# --- Forgot Password ---
def forgot_password():
    """Xử lý quên mật khẩu."""
    def verify_email():
        username = entry_username.get().strip()
        email = entry_email.get().strip()
        credentials = load_user_credentials()

        if username not in credentials or credentials[username].get("email") != email:
            messagebox.showerror("Lỗi", "Tên đăng nhập hoặc email không chính xác.")
            return

        messagebox.showinfo("Thành công", "Xác thực thành công. Vui lòng đặt lại mật khẩu.")
        forgot_window.destroy()
        reset_password(username)

    forgot_window = ttk.Toplevel()
    forgot_window.title("Quên mật khẩu")
    forgot_window.geometry("400x200")

    ttk.Label(forgot_window, text="Tên đăng nhập:").pack(pady=10, anchor="w", padx=20)
    entry_username = ttk.Entry(forgot_window)
    entry_username.pack(fill="x", padx=20)

    ttk.Label(forgot_window, text="Email:").pack(pady=10, anchor="w", padx=20)
    entry_email = ttk.Entry(forgot_window)
    entry_email.pack(fill="x", padx=20)

    ttk.Button(forgot_window, text="Xác nhận", command=verify_email).pack(pady=20)

# --- Login Frame ---
def create_login_frame(app, notebook, load_main_interface):
    initialize_default_users()

    def authenticate():
        username = entry_username.get().strip()
        password = entry_password.get().strip()
        entered_captcha = entry_captcha.get().strip()

        if entered_captcha != current_captcha.get():
            messagebox.showerror("Xác minh thất bại", "Captcha không khớp. Vui lòng thử lại!")
            refresh_captcha()
            return

        if verify_user_credentials(username, password):
            user_role.set("owner" if username == "admin" else "staff")
            messagebox.showinfo("Đăng nhập", f"Đăng nhập thành công với vai trò: {user_role.get()}")
            login_frame.destroy()
            load_main_interface(app, notebook, user_role.get())
        else:
            messagebox.showerror("Đăng nhập", "Sai tên đăng nhập hoặc mật khẩu!")
            refresh_captcha()

    def refresh_captcha():
        captcha_text, captcha_image = generate_captcha()
        current_captcha.set(captcha_text)
        captcha_photo = ImageTk.PhotoImage(captcha_image)
        captcha_label.config(image=captcha_photo)
        captcha_label.image = captcha_photo  # Gắn ảnh vào biến để tránh bị xóa bộ nhớ

    current_captcha = ttk.StringVar()

    # Tạo giao diện đăng nhập
    login_frame = ttk.Frame(app)
    login_frame.pack(fill="both", expand=True)

    ttk.Label(login_frame, text="Đăng nhập", font=("Arial", 16, "bold")).pack(pady=20)

    center_frame = ttk.Frame(login_frame)
    center_frame.pack(anchor="center", pady=10)

    ttk.Label(center_frame, text="Tên đăng nhập:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
    entry_username = ttk.Entry(center_frame, width=25)
    entry_username.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(center_frame, text="Mật khẩu:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entry_password = ttk.Entry(center_frame, show="*", width=25)
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(center_frame, text="Captcha:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entry_captcha = ttk.Entry(center_frame, width=15)
    entry_captcha.grid(row=2, column=1, padx=10, pady=5)

    # Tạo `captcha_label` trước khi gọi hàm `refresh_captcha`
    captcha_label = ttk.Label(center_frame)
    captcha_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Làm mới captcha ngay khi khởi tạo
    refresh_captcha()

    ttk.Button(login_frame, text="Đăng nhập", bootstyle="primary", command=authenticate).pack(pady=20)
    ttk.Button(login_frame, text="Quên mật khẩu", bootstyle="secondary", command=forgot_password).pack()

    global user_role
    user_role = ttk.StringVar(value="guest")
