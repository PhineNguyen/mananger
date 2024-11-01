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
canvas1 = tk.Canvas(window, bg="#B1C6B4", width=2000, height=200)
canvas1.config(bg="#B1C6B4")
canvas1.pack()

#Bảng ngoài bìa 
canvas2 = tk.Canvas(window, bg="#B1C6B4",width=515,height= 835)
canvas2.config(bg="#B1C6B4")

canvas2.place(x=1400, y=205)

#Bảng ở trung tâm
canvas3 = tk.Canvas(window, bg="#B1C6B4",width=1390,height =835)
canvas3.config(bg="#B1C6B4")
canvas3.place(x=4,y=205)

#Các ô chức năng
#Sản phẩm
frame1=tk.Frame(canvas1, bg="#EAE7D6",width=200, height=100)
frame1_label=tk.Label(frame1,text="Frame1",bg="#EAE7D6")
frame1_label.pack(pady=10)
#thêm frame 1 vào canvas
canvas1.create_window(50,50,window=frame1)

#Đơn hàng
frame2=tk.Frame(canvas1, bg="#EAE7D6",width=200, height=100)
frame2_label=tk.Label(frame2,text="Frame2",bg="#EAE7D6")
frame2_label.pack(pady=10)
#thêm frame 1 vào canvas
canvas1.create_window(300,50,window=frame2)


#Thống kê
frame3=tk.Frame(canvas1, bg="#EAE7D6",width=200, height=100)
frame3_label=tk.Label(frame3,text="Frame3",bg="#EAE7D6")
frame3_label.pack(pady=10)
#thêm frame 1 vào canvas
canvas1.create_window(500,50,window=frame3)

#Khách hàng
frame4=tk.Frame(canvas1, bg="#EAE7D6",width=200, height=100)
frame4_label=tk.Label(frame4,text="Frame4",bg="#EAE7D6")
frame4_label.pack(pady=10)
#thêm frame 1 vào canvas
canvas1.create_window(800,50,window=frame4)

#Các frame nhập thông tin của bảng bìa bên phải 
frame6 =tk.Frame(canvas2, bg="#EAE7D6", padx=10, pady=10)
label_frame6 =tk.Label(frame6, text="Frame6",bg="#EAE7D6")
label_frame6.pack(padx=20, pady=20)
canvas2.create_window(50,50, window=frame6)

frame7 =tk.Frame(canvas2, bg="#EAE7D6", padx=10, pady=10)
label_frame7 =tk.Label(frame7, text="Frame7",bg="#EAE7D6")
label_frame7.pack(padx=20, pady=20)
canvas2.create_window(50,200, window=frame7)

frame8 =tk.Frame(canvas2, bg="#EAE7D6", padx=10, pady=10)
label_frame8 =tk.Label(frame8, text="Frame8",bg="#EAE7D6")
label_frame8.pack(padx=20, pady=20)
canvas2.create_window(50,400, window=frame8)

frame9 =tk.Frame(canvas2, bg="#EAE7D6", padx=10, pady=10)
label_frame9 =tk.Label(frame9, text="Frame9",bg="#EAE7D6")
label_frame9.pack(padx=20, pady=20)
canvas2.create_window(50,600, window=frame9)




#Câu lệnh hiển thị cửa sổ
window.mainloop()