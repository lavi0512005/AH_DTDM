# -*- coding: utf-8 -*-
"""
Bài 1. Tạo một custom widget là CustomToggleButton dựa trên lớp tk.Button. Widget này
có thể chuyển đổi giữa hai trạng thái: bật và tắt. Xử lý sự kiện khi trạng thái thay đổi và gửi
ra thông báo tương ứng.ator
"""
import tkinter as tk
from tkinter import messagebox

class CustomToggleButton(tk.Button):
    def __init__(self, master=None, on_text="ON", off_text="OFF", **kwargs):
       
        super().__init__(master, **kwargs)
        self._on_text = on_text
        self._off_text = off_text
        self.state = False
       
        # Khởi tạo text và command
        self.config(text=self._off_text, command=self._toggle)
       
    def _toggle(self):
        self.state = not self.state
        new_text = self._on_text if self.state else self._off_text
        self.config(text=new_text)
       
        # Hiện thông báo lên màn hình
        message = f"Trạng thái hiện tại: {new_text}"
        messagebox.showinfo("CustomToggleButton", message)
       
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Demo CustomToggleButton")
    root.geometry("200x100")
   
    toggle_btn = CustomToggleButton(
        root,
        on_text="Tắt",
        off_text="Bật",
        width=10,
        height=2,
        bg="#4CAF50",
        fg="white",
        activebackground="#45A049"
        )
    toggle_btn.pack(pady=20)
   
    root.mainloop()