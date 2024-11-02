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
style.configure("TNotebook.Tab", padding=[100, 5], font=('Helvetica', 20))

# Tạo notebook với style tùy chỉnh
notebook = ttk.Notebook(app, style="TNotebook")  # Áp dụng style chuẩn TNotebook
notebook.pack(fill=BOTH, expand=TRUE)

# Thêm các tab vào notebook
create_san_pham_tab(notebook)
create_don_hang_tab(notebook, app)
create_thong_ke_tab(notebook)
create_khach_hang_tab(notebook, app)

# Khởi chạy ứng dụng
app.mainloop()
