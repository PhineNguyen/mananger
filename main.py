import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from san_pham import create_san_pham_tab
from don_hang import create_don_hang_tab
from thong_ke import create_thong_ke_tab
from khach_hang import create_khach_hang_tab
from PIL import Image, ImageTk

def main():
    # Khởi tạo cửa sổ chính
    app = ttk.Window(themename="minty")
    app.geometry("800x500")

    # Load the icon image
    masterplan_icon = Image.open("D:/mananger/icon/masterplan.png")
    masterplan_icon = masterplan_icon.resize((30, 30), Image.LANCZOS)
    masterplan_icon = ImageTk.PhotoImage(masterplan_icon)

    # Create a frame for the title area at the top
    title_frame = ttk.Frame(app)
    title_frame.pack(side=TOP, fill=X, padx=10, pady=10)

    # Create a label for the icon
    icon_label = ttk.Label(title_frame, image=masterplan_icon)
    icon_label.image = masterplan_icon  # Keep a reference to avoid garbage collection
    icon_label.pack(side=LEFT)

    # Create a label for the title text
    title_label = ttk.Label(title_frame, text="Store Manager", font=('Helvetica', 16))
    title_label.pack(side=LEFT, padx=(10, 0))

    # Tạo style cho tab
    style = ttk.Style()
    style.configure("TNotebook.Tab", padding=[101, 5], font=('Helvetica', 14), background="#5bc0de")
    style.map("TNotebook.Tab",
              background=[('selected', '#ADD8E6'), ('!selected', '#B1C6B4')],
              foreground=[('selected', 'white'), ('!selected', 'black')])

    # Tạo notebook với style tùy chỉnh
    notebook = ttk.Notebook(app, style="TNotebook")
    notebook.pack(fill=BOTH, expand=TRUE)

    # Thêm các tab vào notebook
    create_san_pham_tab(notebook, app)
    create_don_hang_tab(notebook, app)
    create_khach_hang_tab(notebook, app)
    create_thong_ke_tab(notebook, app)

    # Chạy ứng dụng
    app.mainloop()

if __name__ == "__main__":
    main()
