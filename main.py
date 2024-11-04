import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from san_pham import create_san_pham_tab
from don_hang import create_don_hang_tab
from thong_ke import create_thong_ke_tab
from khach_hang import create_khach_hang_tab

# Khởi tạo cửa sổ chính
app = ttk.Window(themename="minty")
app.title("Quản Lý Cửa Hàng")
app.geometry("800x500")

# Tạo style cho tab
style = ttk.Style()
style.configure("TNotebook.Tab", padding=[101, 5], font=('Helvetica', 14), background="#5bc0de")#, foreground="white")  # Màu nền và chữ của tab
style.map("TNotebook.Tab",
          background=[('selected', '#20c997'), ('!selected', '#B1C6B4')],  # Màu nền khi tab được chọn và không được chọn
          foreground=[('selected', 'white'), ('!selected', 'black')])  # Màu chữ khi tab được chọn và không được chọn

# Tạo notebook với style tùy chỉnh
notebook = ttk.Notebook(app, style="TNotebook")  # Áp dụng style chuẩn TNotebook
notebook.pack(fill=BOTH, expand=TRUE)

# Add tabs to the notebook
create_san_pham_tab(notebook,app)
create_don_hang_tab(notebook,app)
create_khach_hang_tab(notebook, app)
create_thong_ke_tab(notebook)


# Start the application
app.mainloop()