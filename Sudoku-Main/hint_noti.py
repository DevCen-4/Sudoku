import tkinter as tk
import time

def show_notification(text, duration=1):
    """
    Hiển thị thông báo ở một bên của cửa sổ trong khoảng thời gian đã cho.
    """
    root = tk.Tk()
    root.overrideredirect(True)
    root.geometry("+40+40")  # Vị trí của thông báo (ở góc trên bên trái)
    root.wm_attributes("-topmost", True)  # Đặt thông báo ở trên cùng

    label = tk.Label(root, text=text, bg="lightblue", fg="black", padx=40, pady=40, font=("Arial", 20, "bold"))
    label.pack()

    root.after(duration * 1000, root.destroy)  # Hủy thông báo sau duration giây
    root.mainloop()