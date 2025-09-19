# -*- coding: utf-8 -*-
"""
Bài 3. Tạo một custom widget là CustomListBox dựa trên lớp tk.Listbox. Widget này cho
phép người dùng chọn một hoặc nhiều mục từ danh sách. Xử lý sự kiện khi các mục được
chọn và hiển thị danh sách các mục đã được chọn.
"""
import tkinter as tk
from tkinter import messagebox

class CustomListBox(tk.Listbox):
    def __init__ (self, master=None, items=None, select_mode=tk.MULTIPLE, callback=None, **kwargs):
        super().__init__(master, selectmode=select_mode, exportselection=False, **kwargs)
        self.callback = callback
        #Thêm items vào listbox
        if items:
            for item in items:
                self.insert(tk.END, item)
        #bắt sự kiện chọn
        self.bind("<<ListboxSelect>>", self._on_select)
        
    def _on_select(self, event):
        #lấy chỉ số các mục đang được chọn
        indices = self.curselection()
        #lấy giá trị tương ứng
        selected = [self.get(1) for i in indices]
        #nếu có callback, gọi callback
        if callable(self.callback):
            self.callback(selected)
        else:
            #ngược lại thể hiện messagebox
            messagebox.showinfo("Đã chọn", "\n".join(selected))
            
if __name__ == "__main__":
    def on_items_selected(chosen):
        #ví dụ: cập nhật label và in ra console
        display_label.config(text="Đã chọn: "+", ".join(chosen))
        print("Đã chọn:", chosen)
    root = tk.Tk()
    root.title("Demo CustomListBox")
    root.geometry("300x250")
    sample_items = [
        "Python", "Java", "C++", "JavaScript", "Go", "Rust", "Kotlin", "Swift"
        ]
    #tạo customlistbox với nhiều lựa chọn (Multiple)
    listbox = CustomListBox(
        root,
        items=sample_items,
        select_mode=tk.MULTIPLE,
        callback=on_items_selected,
        width=20,
        height=8,
        bg="#f0f0f0"
        )
    listbox.pack(pady=(10,5))
    #Label để hiển thị lựa chọn
    display_label = tk.Label(root, text="Đã chọn: ")
    display_label.pack(pady=(0, 10))
    root.mainloop() 
                