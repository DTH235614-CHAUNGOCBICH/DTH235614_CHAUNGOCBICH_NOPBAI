def in_bang_cuu_chuong(n):
    """
    In bảng cửu chương của số n
    """
    print(f"Bảng cửu chương {n}:")
    print("-" * 20)

    for i in range(1, 11):
        ket_qua = n * i
        print(f"{n} x {i:2} = {ket_qua:2}")
    print()


def main():
    try:
        # Nhập số n từ người dùng
        n = int(input("Nhập số n (1 < n < 9): "))

        # Kiểm tra điều kiện
        if n <= 1 or n >= 9:
            print("Lỗi: n phải lớn hơn 1 và nhỏ hơn 9!")
            return

        # In bảng cửu chương
        in_bang_cuu_chuong(n)

    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")


# Chạy chương trình
if __name__ == "__main__":
    main()