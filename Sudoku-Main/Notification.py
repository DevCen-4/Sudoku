import tkinter as tk
from tkinter import messagebox
import time

def center_window(window):
    window.update_idletasks()  # Necessary to get correct window size
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"+{x}+{y}")

def create_game_over_window():
    """Tạo cửa sổ thông báo kết thúc trò chơi"""
    window = tk.Tk()
    window.title("Kết thúc trò chơi")
    window.geometry("600x300")

    # Thông báo kết thúc
    label = tk.Label(window, text="Trò chơi Kết thúc", font=("Arial", 20, "bold"))
    label.pack(pady=10)

    # Thông báo kết quả
    result_text = "Bạn đã mắc 3 lỗi và thua trò chơi này"
    result_label = tk.Label(window, text=result_text, font=("Arial", 15))
    result_label.pack(pady=20)

    # Nút "Trò chơi Mới"
    new_game_button = tk.Button(window, text="Bạn đã Thua!", command=window.destroy, font=("Arial", 12), width=20, height=2)
    new_game_button.pack()

    center_window(window)
    window.mainloop()

def create_game_win_window():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Bạn đã chiến thắng")
    root.geometry("600x300")

    # Nút để hiển thị thông báo
    notify_button = tk.Button(root, text="Chúc mừng bạn đã thắng trò chơi", command=root.destroy, font=("Arial", 20, "bold"))
    notify_button.pack(pady=50)
    center_window(root)

    # Chạy ứng dụng
    root.mainloop()

def create_new_game_window():
    kt = None

    def yes():
        nonlocal kt
        kt = True
        root.destroy()

    def no():
        nonlocal kt
        kt = False
        root.destroy()

    root = tk.Tk()
    root.title("Xác nhận")
    root.geometry("600x300")

    label = tk.Label(root, text="Bạn có thật sự muốn tạo \n một trò chơi mới?", font=("Arial", 20, "bold"))
    label.pack(pady=20)

    button_yes = tk.Button(root, text="Yes", command=yes, font=("Arial", 12), width=20, height=2)
    button_yes.pack(side="left", padx=10)

    button_no = tk.Button(root, text="No", command=no, font=("Arial", 12), width=20, height=2)
    button_no.pack(side="right", padx=10)
    center_window(root)

    root.mainloop()
    return kt

