def kiem_tra_nam_nhuan(nam):
    """
    Kiểm tra xem một năm có phải là năm nhuận không
    """
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    return False


def so_ngay_trong_thang():
    """
    Hàm chính để xác định số ngày trong tháng
    """
    try:
        # Nhập tháng từ bàn phím
        thang = int(input("Nhập tháng (1-12): "))

        # Kiểm tra tháng hợp lệ
        if thang < 1 or thang > 12:
            print("Lỗi: Tháng phải từ 1 đến 12!")
            return

        # Xác định số ngày cho các tháng
        if thang in [1, 3, 5, 7, 8, 10, 12]:
            print(f"Tháng {thang} có 31 ngày")
        elif thang in [4, 6, 9, 11]:
            print(f"Tháng {thang} có 30 ngày")
        else:  # Tháng 2
            # Yêu cầu nhập năm để kiểm tra năm nhuận
            nam = int(input("Nhập năm: "))

            if kiem_tra_nam_nhuan(nam):
                print(f"Tháng 2 năm {nam} có 29 ngày (năm nhuận)")
            else:
                print(f"Tháng 2 năm {nam} có 28 ngày (không nhuận)")

    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")


# Chạy chương trình
if __name__ == "__main__":
    so_ngay_trong_thang()