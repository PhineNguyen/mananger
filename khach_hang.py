import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def create_khach_hang_tab(notebook):
    # Create frame for "Khách Hàng" tab
    frame_khach_hang = ttk.Frame(notebook)
    notebook.add(frame_khach_hang, text="KHÁCH HÀNG")
    
    # Add content to "Khách Hàng" tab
    ttk.Label(frame_khach_hang, text="Quản lý khách hàng", bootstyle="primary").pack(pady=20)
