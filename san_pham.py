import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def create_san_pham_tab(notebook):
    # Create frame for "Sản Phẩm" tab
    frame_san_pham = ttk.Frame(notebook)
    notebook.add(frame_san_pham, text="SẢN PHẨM")
    
    # You can add content to the "Sản Phẩm" tab here
    ttk.Label(frame_san_pham, text="Quản lý sản phẩm", bootstyle="primary").pack(pady=20)
