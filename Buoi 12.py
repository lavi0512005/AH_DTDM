# -*- coding: utf-8 -*-
"""
35 Nguyễn Hoàng Thanh Thanh
BUỔI 12. Regular Expression và Web Crawling & Scraping
"""

import re

def is_valid_email(email: str) -> bool:
    """
    Email phải:
    - Bắt đầu bằng chữ cái hoặc số, cho phép ., _, %, +, -
    - Có kí tự @
    - Tên miền gồm chữ/số/-, sau đó, và phần mở rộng 2-4 chữ thường
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,4}$'
    return bool(re.match(pattern, email))

def is_valid_phone(phone: str) -> bool:
    """
    Số điện thoại phải:
    - Bắt đầu từ 0
    - Có từ 9-10 số (tổng là 10-11 số)
    - Không có kí tự khác
    """
    pattern = r'^0\d{9,10}$'
    return bool(re.match(pattern, phone))

def is_valid_password(pw: str) -> (bool, str):
    """
    Password phải:
    - Có cả chữ thường và chữ hoa, chữ số, kí tự đặc biệt
    - Độ dài 8 - 16 kí tự
    - Không chứa khoảng trắng
    Trả về (True, "") nếu hợp lệ, (False, lí do) nếu không hợp lệ
    """
    if len(pw) < 8 or len(pw) > 16:
        return False, "Mật khẩu phải có độ dài từ 8 đến 16 ký tự."
    if re.search(r'\s', pw):
        return False, "Mật khẩu không được chứa khoảng trắng."
    if not re.search(r'[a-z]', pw):
        return False, "Mật khẩu phải chứa ít nhất một chữ cái thường."
    if not re.search(r'[A-Z]', pw):
        return False, "Mật khẩu phải chứa ít nhất một chữ cái hoa."
    if not re.search(r'\d', pw):
        return False, "Mật khẩu phải chứa ít nhất một chữ số."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=]', pw):
        return False, "Mật khẩu phải chứa ít nhất một ký tự đặc biệt."
    return True, ""

def tutrongcau():
    n = input("Nhập câu :")
    text = r'\w+'
    lable = re.findall(text, n)
    print(lable)

def atrongcau():
    n = input("Nhập câu: ")
    text = r'\w*[aA]\w*'
    lable = re.findall(text, n)
    print(lable)
    
def thaythe():
    n = input("Nhập câu: ")
    m = input("Nhập từ muốn thay thế: ")
    i = input("Nhập từ thế: ")
    text = re.sub(m,i,n)
    print(text)
    
def inhoa():
    n = input("Nhập câu: ")
    text = r'\b[A-Z]\w*'
    lable = re.findall(text, n)
    print(lable)



def main():
    while True:
        print("---------------------MENU--------------------")
        print("1. Kiểm tra Email.")
        print("2. Kiểm tra số điện thoại.")
        print("3. Kiểm tra mật khẩu.")
        print("4. Danh sách từ trong câu.")
        print("5. Danh sách từ có a trong câu.")
        print("6. Thay thế từ trong câu.")
        print("7. Danh sách từ in hoa trong câu.")
        print("0. Thoát.")
        choice = input("Chọn chức năng (0-7): ").strip()

        if choice == '0':
            print("Kết thúc chương trình.")
            break
        elif choice == '1':
            email = input("Nhập địa chỉ email: ").strip()
            if is_valid_email(email):
                print(f"{email} là một địa chỉ email hợp lệ.")
            else:
                print(f"{email} không phải là một địa chỉ email hợp lệ.")
        elif choice == '2':
            sdt = input("Nhập số điện thoại: ").strip()
            if is_valid_phone(sdt):
                print(f"{sdt} là một số điện thoại hợp lệ.")
            else:
                print(f"{sdt} không phải là một số điện thoại hợp lệ.")
        elif choice == '3':
            pw = input("Nhập mật khẩu: ").strip()
            valid, reason = is_valid_password(pw)
            if valid:
                print("Mật khẩu hợp lệ.")
            else:
                print(f"Mật khẩu không hợp lệ: {reason}")
        elif choice == '4':
            tutrongcau()
        elif choice == '5':
            atrongcau()
        elif choice == '6':
            thaythe()
        elif choice == '7':
            inhoa()
        elif 
            else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
