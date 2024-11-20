import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from captcha.image import ImageCaptcha
import random
import string
from PIL import Image, ImageTk

# Dữ liệu giả lập (thay bằng cơ sở dữ liệu trong thực tế)
USER_DATA = {
    "admin": {"password": "admin123", "email": "admin@example.com", "security_question": "Tên con vật cưng của chủ tên gì?", "security_answer": "Peter"},
    "staff": {"password": "staff123", "email": "staff@example.com", "security_question": "Bạn tốt nghiệp trường Đại học nào?", "security_answer": "University of transport"},
}

def reset_password(username, answer=None, reset_window=None):
    """
    Hiển thị giao diện đặt lại mật khẩu.
    Nếu có câu trả lời bảo mật, kiểm tra và reset mật khẩu
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
        if reset_window:
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

        # Xác thực thành công, yêu cầu câu trả lời bảo mật
        security_question = USER_DATA[username]["security_question"]
        security_answer_window(security_question, username)
        forgot_window.destroy()
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

def security_answer_window(question, username):
    """
    Hiển thị giao diện câu trả lời bảo mật.
    """
    def verify_answer():
        answer = entry_answer.get().strip()

        if answer == USER_DATA[username]["security_answer"]:
            reset_password(username, answer, security_window)  # Thực hiện reset mật khẩu
            security_window.destroy()
        else:
            messagebox.showerror("Lỗi", "Câu trả lời không chính xác.")
              # Đóng cửa sổ nếu câu trả lời sai

    security_window = ttk.Toplevel()
    security_window.title("Câu hỏi bảo mật")
    security_window.geometry("400x250")

    ttk.Label(security_window, text=f"Câu hỏi: {question}").pack(pady=10, anchor="w", padx=20)

    ttk.Label(security_window, text="Câu trả lời:").pack(pady=10, anchor="w", padx=20)
    entry_answer = ttk.Entry(security_window)
    entry_answer.pack(fill="x", padx=20)

    ttk.Button(security_window, text="Xác nhận", command=verify_answer).pack(pady=20)

def generate_captcha_text(length=4):
    """
    Sinh chuỗi ngẫu nhiên gồm chữ cái cho Captcha (dễ đoán hơn).
    """
    return ''.join(random.choices(string.digits, k=length))  # Chỉ dùng chữ cái

def create_captcha_image(captcha_text):
    """
    Tạo hình ảnh Captcha từ chuỗi văn bản với font cụ thể.
    """
    font_path = "arial.ttf"  # Thay đường dẫn tới font của bạn
    image = ImageCaptcha(fonts=[font_path])
    data = image.generate(captcha_text)
    captcha_image = Image.open(data)
    return captcha_image

def create_login_frame(app, notebook, load_main_interface):
    # Khai báo user_role là một StringVar để lưu vai trò người dùng
    global user_role
    user_role = ttk.StringVar(value="guest")  # Giá trị mặc định là "guest"

    def authenticate():
        selected_role = combobox_role.get().strip()
        password = entry_password.get().strip()
        entered_captcha = entry_captcha.get().strip()

        if entered_captcha != current_captcha.get():
            messagebox.showerror("Xác minh thất bại", "Captcha không khớp. Vui lòng thử lại!")
            refresh_captcha()
            return

        username = "admin" if selected_role == "Quản Lý" else "staff"
        if USER_DATA[username]["password"] == password:
            user_role.set("owner" if selected_role == "Quản Lý" else "staff")  # Cập nhật user_role
            messagebox.showinfo("Đăng nhập", f"Đăng nhập thành công với vai trò: {user_role.get()}")
            login_frame.destroy()
            load_main_interface(app, notebook, user_role.get())  # Truyền vai trò vào hàm load_main_interface
        else:
            messagebox.showerror("Đăng nhập", "Sai mật khẩu! Vui lòng thử lại.")
            refresh_captcha()

    def refresh_captcha():
        new_captcha_text = generate_captcha_text()
        current_captcha.set(new_captcha_text)

        new_captcha_image = create_captcha_image(new_captcha_text)
        captcha_photo = ImageTk.PhotoImage(new_captcha_image)
        captcha_label.config(image=captcha_photo)
        captcha_label.image = captcha_photo

    current_captcha = ttk.StringVar(value=generate_captcha_text())
    login_frame = ttk.Frame(app)
    login_frame.grid(row=0, column=0, sticky="nsew")

    # Cấu hình để căn giữa
    app.grid_rowconfigure(0, weight=1, uniform="equal")
    app.grid_columnconfigure(0, weight=1, uniform="equal")
    login_frame.grid_rowconfigure(0, weight=1, minsize=20)
    login_frame.grid_rowconfigure(1, weight=1, minsize=20)
    login_frame.grid_rowconfigure(2, weight=1, minsize=20)
    login_frame.grid_rowconfigure(3, weight=1, minsize=20)
    login_frame.grid_rowconfigure(4, weight=1, minsize=20)
    login_frame.grid_rowconfigure(5, weight=1, minsize=20)
    login_frame.grid_rowconfigure(6, weight=1, minsize=20)
    login_frame.grid_columnconfigure(0, weight=1)
    login_frame.grid_columnconfigure(1, weight=1)

    ttk.Label(login_frame, text="Đăng nhập", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    ttk.Label(login_frame, text="Vai trò:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    combobox_role = ttk.Combobox(login_frame, state="readonly", width=25)
    combobox_role["values"] = ["Quản Lý", "Nhân Viên"]
    combobox_role.current(0)
    combobox_role.grid(row=1, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(login_frame, text="Mật khẩu:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entry_password = ttk.Entry(login_frame, show="*", width=25)
    entry_password.grid(row=2, column=1, sticky="w", padx=10, pady=5)

    captcha_image = create_captcha_image(current_captcha.get())
    captcha_photo = ImageTk.PhotoImage(captcha_image)
    captcha_label = ttk.Label(login_frame, image=captcha_photo)
    captcha_label.image = captcha_photo
    captcha_label.grid(row=4, column=0, columnspan=2, pady=10)

    captcha_frame = ttk.Frame(login_frame)
    captcha_frame.grid(row=5, column=0, columnspan=2, pady=5)

    entry_captcha = ttk.Entry(captcha_frame, width=15)
    entry_captcha.grid(row=0, column=0, padx=(0, 5))

    ttk.Button(captcha_frame, text="Làm mới", bootstyle="secondary", command=refresh_captcha).grid(row=0, column=1)

    ttk.Button(login_frame, text="Đăng nhập", bootstyle="primary", command=authenticate).grid(row=6, column=0, columnspan=2, pady=10)

    ttk.Button(login_frame, text="Quên mật khẩu", bootstyle="secondary", command=forgot_password).grid(row=7, column=0, columnspan=2, pady=(0, 20))

