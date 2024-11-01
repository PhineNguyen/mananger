import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def create_thong_ke_tab(notebook):
    # Create frame for "Thống Kê" tab
    frame_thong_ke = ttk.Frame(notebook)
    notebook.add(frame_thong_ke, text="THỐNG KÊ")
    
    # Add content to "Thống Kê" tab
    ttk.Label(frame_thong_ke, text="Quản lý thống kê", bootstyle="primary").pack(pady=20)
