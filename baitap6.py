import math


def giai_phuong_trinh_bac_2(a, b, c):
    """
    Giải phương trình bậc 2: ax² + bx + c = 0
    """
    if a == 0:
        # Trở thành phương trình bậc 1: bx + c = 0
        if b == 0:
            if c == 0:
                return "Phương trình có vô số nghiệm"
            else:
                return "Phương trình vô nghiệm"
        else:
            x = -c / b
            return f"Phương trình có 1 nghiệm: x = {x:.2f}"

    # Tính delta
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b / (2 * a)
        return f"Phương trình có nghiệm kép: x = {x:.2f}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Phương trình có 2 nghiệm phân biệt:\nx1 = {x1:.2f}\nx2 = {x2:.2f}"


# Nhập hệ số từ bàn phím
try:
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))

    ket_qua = giai_phuong_trinh_bac_2(a, b, c)
    print(f"\nKết quả: {ket_qua}")

except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ!")