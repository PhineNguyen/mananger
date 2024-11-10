from tkinter import messagebox
import ttkbootstrap as ttk
from PIL import Image, ImageTk

DEFAULT_PIN = "1234"  # Đặt mã PIN mặc định 

def check_pin(entry_pin, app, login_frame, notebook, container_frame):
    """
    Hàm kiểm tra mã PIN khi nhấn nút "Đăng nhập". 
    Nếu đúng mã PIN, ẩn giao diện đăng nhập và hiển thị giao diện chính.
    """
    if entry_pin.get() == DEFAULT_PIN:
        login_frame.pack_forget()  # Ẩn giao diện đăng nhập
        container_frame.place_forget()  # Ẩn container_frame
        notebook.pack(fill="both", expand=True)  # Hiển thị giao diện chính
    else:
        messagebox.showerror("INCORRECT", "Mã PIN không đúng.")
        entry_pin.delete(0, 'end')  # Xóa mã PIN trong ô nhập

def create_login_frame(app, notebook):
    # Tạo khung bao ngoài container_frame
    container_frame = ttk.Frame(app, padding=20)
    container_frame.place(relx=0.5, rely=0.5, anchor="center")  # Căn giữa container_frame
    
    # Tạo khung đăng nhập bên trong container_frame
    login_frame = ttk.Frame(container_frame)
    login_frame.pack(padx=10, pady=10)

    # Tạo label với icon
    image = Image.open("icon/masterplan.png")
    image = image.resize((20, 20), Image.LANCZOS)
    masterplan_icon = ImageTk.PhotoImage(image)
    label = ttk.Label(login_frame, text="Management Application", image=masterplan_icon, compound="left", font=("Helvetica", 14))
    label.pack(pady=10)
    
    entry_pin = ttk.Entry(login_frame, show="*", font=("Helvetica", 14), width=15)
    entry_pin.pack(pady=10)

    login_button = ttk.Button(
        login_frame,
        text="Login",
        command=lambda: check_pin(entry_pin, app, login_frame, notebook, container_frame)
    )
    login_button.pack(pady=10)
