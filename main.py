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

# Create Notebook for tabs
notebook = ttk.Notebook(app)
notebook.pack(fill=BOTH, expand=TRUE)

# Add tabs to the notebook
create_san_pham_tab(notebook,app)
create_don_hang_tab(notebook,app)
create_thong_ke_tab(notebook)
create_khach_hang_tab(notebook, app)
create_thong_ke_tab(notebook)


# Khởi chạy ứng dụng
app.mainloop()