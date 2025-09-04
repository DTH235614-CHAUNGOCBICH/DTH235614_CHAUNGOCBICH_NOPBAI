import math


def tinh_S(x, n):
    """Tính S(x, n) = x + x²/2! + x³/3! + ... + xⁿ/n!"""
    tong = 0.0
    for i in range(1, n + 1):
        # Tính tử số: x^i
        tu_so = x ** i
        # Tính mẫu số: i! (giai thừa của i)
        mau_so = math.factorial(i)
        # Cộng vào tổng
        tong += tu_so / mau_so
    return tong


# Chương trình chính đơn giản
print("TÍNH DÃY SỐ S(x, n) = x + x²/2! + x³/3! + ... + xⁿ/n!")
print("=" * 50)

try:
    x = float(input("Nhập giá trị x: "))
    n = int(input("Nhập giá trị n: "))

    if n <= 0:
        print("n phải là số nguyên dương!")
    else:
        ket_qua = tinh_S(x, n)
        print(f"S({x}, {n}) = {ket_qua}")
        print(f"S({x}, {n}) ≈ {ket_qua:.6f}")

except ValueError:
    print("Vui lòng nhập số hợp lệ!")