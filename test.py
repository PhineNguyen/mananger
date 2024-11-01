from ttkbootstrap import Style, Window
from ttkbootstrap.constants import*
import ttkbootstrap as ttk
import tkinter as tk

#tạo cửa xổ
window = Window(themename ="flatly")
window.title("management application")
window.geometry("2000x1000")

#Đặt màu nền \
window.configure(background="#EAE7D6")

#Thành phần giao diện 
#bảng trên cùng
canvas = tk.Canvas(window, width=2000, height=200)
canvas.config(bg="#B1C6B4")
canvas.pack()


#Bảng ngoài bìa 
canvas = tk.Canvas(window, bg="#B1C6B4",width=515,height= 835)
canvas.config(bg="#B1C6B4")

canvas.place(x=1400, y=205)

#Bảng ở trung tâm
canvas = tk.Canvas(window, bg="#B1C6B4",width=1390,height =835)
canvas.config(bg="#B1C6B4")

canvas.place(x=4,y=205)

#tạo các hàng và cột cho bảng 

# tree = ttk.Treeview(window, columns=("test"),show="headings")
# tree.heading("test", text="Test")
# tree.column("test", width=100)



#Câu lệnh hiển thị cửa sổ
window.mainloop()