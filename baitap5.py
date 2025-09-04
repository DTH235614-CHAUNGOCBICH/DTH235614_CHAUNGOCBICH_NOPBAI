def doc_so_co_2_chu_so(n):
    """
    Đọc số có tối đa 2 chữ số thành chữ
    """
    # Danh sách cách đọc các số từ 0-9
    don_vi = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    # Danh sách cách đọc hàng chục
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi",
            "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    # Kiểm tra số hợp lệ
    if n < 0 or n > 99:
        return "Số không hợp lệ! Vui lòng nhập số từ 0 đến 99"

    # Xử lý số có 1 chữ số (0-9)
    if n < 10:
        return don_vi[n]

    # Xử lý số có 2 chữ số
    hang_chuc = n // 10
    hang_don_vi = n % 10

    # Các trường hợp đặc biệt
    if hang_chuc == 1:  # Số từ 10-19
        if hang_don_vi == 0:
            return "mười"
        elif hang_don_vi == 5:
            return "mười lăm"
        else:
            return f"mười {don_vi[hang_don_vi]}"

    elif hang_don_vi == 0:  # Số tròn chục (20, 30, ..., 90)
        return chuc[hang_chuc]

    elif hang_don_vi == 1:  # Số có đơn vị là 1 (21, 31, ..., 91)
        return f"{chuc[hang_chuc]} mốt"

    elif hang_don_vi == 5:  # Số có đơn vị là 5 (25, 35, ..., 95)
        return f"{chuc[hang_chuc]} lăm"

    else:  # Các trường hợp còn lại
        return f"{chuc[hang_chuc]} {don_vi[hang_don_vi]}"


def main():
    """
    Hàm chính của chương trình
    """
    print("CHƯƠNG TRÌNH ĐỌC SỐ CÓ TỐI ĐA 2 CHỮ SỐ")
    print("=" * 40)

    try:
        # Nhập số từ bàn phím
        n = int(input("Nhập một số (0-99): "))

        # Đọc số và in kết quả
        ket_qua = doc_so_co_2_chu_so(n)
        print(f"Số {n} đọc là: {ket_qua}")

    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")


# Chạy chương trình
if __name__ == "__main__":
    main()