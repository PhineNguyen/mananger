# utils.py
import shared_state

def refresh_tabs():
    """
    Làm mới tất cả các tab sử dụng biến từ shared_state.
    """
    if not shared_state.notebook or not shared_state.create_tab_funcs:
        raise RuntimeError("shared_state chưa được khởi tạo.")

    # Xóa tất cả các tab hiện tại
    for tab in shared_state.notebook.winfo_children():
        tab.destroy()

    # Tạo lại các tab
    for func in shared_state.create_tab_funcs.values():
        func(shared_state.notebook, shared_state.app)

    print("Đã làm mới tất cả các tab.")
