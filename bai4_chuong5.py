#cau 4:
s = "   Python Programming 123!   "

print("Chuỗi gốc:", repr(s))
print("strip() :", repr(s.strip()))          #Xóa khoảng trắng 2 đầu
print("lower() :", s.lower())                #Đổi thành chữ thường
print("upper() :", s.upper())                #Đổi thành chữ hoa
print("title() :", s.title())                #Viết hoa chữ cái đầu
print("split() :", s.split())                #Tách chuỗi thành list
print("replace:", s.replace("Python", "Java"))  #Thay thế
print("isdigit:", "123".isdigit())           #Kiểm tra toàn số
print("isalpha:", "abc".isalpha())           #Kiểm tra toàn chữ