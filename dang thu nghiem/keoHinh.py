import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageTk
import random

# Biến lưu hình ảnh để tránh bị garbage collected
global_images = {}

def generate_captcha_image(width, height):
    """Tạo hình ảnh CAPTCHA động."""
    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Tạo các hình đơn giản (ví dụ: hình chữ nhật và hình tròn)
    for _ in range(5):
        x1, y1 = random.randint(0, width // 2), random.randint(0, height // 2)
        x2, y2 = x1 + random.randint(20, 100), y1 + random.randint(20, 100)
        color = tuple(random.randint(0, 255) for _ in range(3))
        draw.rectangle([x1, y1, x2, y2], fill=color, outline=(0, 0, 0))

    for _ in range(3):
        x, y = random.randint(0, width), random.randint(0, height)
        radius = random.randint(20, 50)
        color = tuple(random.randint(0, 255) for _ in range(3))
        draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=color, outline=(0, 0, 0))

    return image

def create_drag_captcha(app, verify_callback):
    def check_captcha():
        # Kiểm tra mảnh ghép với ngưỡng gần đúng
        threshold = 50  # Độ lệch tối đa cho phép
        if abs(piece_x - correct_x) <= threshold and abs(piece_y+correct_y - correct_y) <= threshold:
            messagebox.showinfo("Thành công", "CAPTCHA đã được xác minh!")
            verify_callback(True)
        else:
            messagebox.showerror("Thất bại", f"Mảnh ghép chưa đúng vị trí.\nHãy kéo gần vị trí chính xác hơn (±{threshold}px)!")
            verify_callback(False)

    def on_drag(event):
        global piece_x, piece_y
        piece_x, piece_y = event.x_root - frame.winfo_rootx(), event.y_root - frame.winfo_rooty()
        canvas.coords(piece_id, piece_x, piece_y)

    def on_release(event):
        check_captcha()

    # Tạo khung CAPTCHA
    frame = tk.Frame(app)
    frame.pack(pady=20)

    # Tạo hình CAPTCHA động và cắt thành hai phần
    width, height = 300, 150
    captcha_image = generate_captcha_image(width, height)
    split_x = random.randint(width // 3, 2 * width // 3)

    left_image = captcha_image.crop((0, 0, split_x, height))
    right_image = captcha_image.crop((split_x, 0, width, height))

    # Tọa độ mảnh ghép đúng
    global piece_x, piece_y, correct_x, correct_y
    piece_x, piece_y = width - 100, height // 2
    correct_x, correct_y = split_x, height // 2

    # Hiển thị hình nền (phần bên trái)
    left_photo = ImageTk.PhotoImage(left_image)
    global_images["left_photo"] = left_photo  # Lưu tham chiếu
    canvas = tk.Canvas(frame, width=width, height=height)
    canvas.pack()

    canvas.create_image(0, 0, image=left_photo, anchor="nw")

    # Hiển thị mảnh ghép (phần bên phải)
    right_photo = ImageTk.PhotoImage(right_image)
    global_images["right_photo"] = right_photo  # Lưu tham chiếu
    piece_id = canvas.create_image(piece_x, piece_y, image=right_photo, anchor="nw")

    # Kết nối sự kiện kéo thả
    canvas.tag_bind(piece_id, "<B1-Motion>", on_drag)
    canvas.tag_bind(piece_id, "<ButtonRelease-1>", on_release)

    return frame

# Hàm kiểm tra CAPTCHA được xác minh
def verify_callback(is_verified):
    if is_verified:
        print("CAPTCHA xác minh thành công!")
        print(f"Vị trí mảnh ghép: ({piece_x}, {piece_y}), Vị trí đúng: ({correct_x}, {correct_y})")

    else:
        print("CAPTCHA chưa đúng.")
        print(f"Vị trí mảnh ghép: ({piece_x}, {piece_y}), Vị trí đúng: ({correct_x}, {correct_y})")


# Tạo giao diện chính
if __name__ == "__main__":
    app = tk.Tk()
    app.title("CAPTCHA Kéo Ghép")
    app.geometry("400x300")

    # Tạo CAPTCHA
    create_drag_captcha(app, verify_callback)

    app.mainloop()
