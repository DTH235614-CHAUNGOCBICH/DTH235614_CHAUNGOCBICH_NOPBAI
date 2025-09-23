def ToiUuDanhTu(s):
    #Xóa khoảng trắng dư thừa
    words = s.strip().split()
    #Viết hoa chữ cái đầu, các ký tự sau chuyển về thường
    words = [w.capitalize() for w in words if w.strip() != ""]
    return " ".join(words)

def main():
    chuoi = input("Nhập vào một chuỗi họ tên: ")
    ketqua = ToiUuDanhTu(chuoi)
    print("Chuỗi đã tối ưu:", ketqua)

main()