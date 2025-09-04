def tinh_S(n):
    """Tính S = 1 + 2 + ... + n"""
    return n * (n + 1) // 2


def tinh_S1(n):
    """Tính S1 = 1 + 3 + ... + (2n - 1)"""
    return n * n  # Tổng n số lẻ đầu tiên


def tinh_S2(n):
    """Tính S2 = 2 + 4 + ... + 2n"""
    return n * (n + 1)  # 2*(1+2+...+n) = 2*(n(n+1)/2)


def tinh_S3(n):
    """Tính S3 = 1² + 2² + ... + n²"""
    return n * (n + 1) * (2 * n + 1) // 6


def tinh_S4(n):
    """Tính S4 = 1/1 + 1/2 + ... + 1/n"""
    tong = 0.0
    for i in range(1, n + 1):
        tong += 1.0 / i
    return tong


def main():
    try:
        # Nhập số n từ người dùng
        n = int(input("Nhập số nguyên dương n: "))

        # Kiểm tra điều kiện
        if n <= 0:
            print("Lỗi: n phải là số nguyên dương!")
            return

        # Tính các tổng
        S = tinh_S(n)
        S1 = tinh_S1(n)
        S2 = tinh_S2(n)
        S3 = tinh_S3(n)
        S4 = tinh_S4(n)

        # In kết quả
        print(f"\nVới n = {n}:")
        print(f"S  = 1 + 2 + ... + {n} = {S}")
        print(f"S1 = 1 + 3 + ... + {2 * n - 1} = {S1}")
        print(f"S2 = 2 + 4 + ... + {2 * n} = {S2}")
        print(f"S3 = 1² + 2² + ... + {n}² = {S3}")
        print(f"S4 = 1/1 + 1/2 + ... + 1/{n} = {S4:.6f}")

        # In chi tiết cách tính (tùy chọn)
        print(f"\nChi tiết cách tính:")
        print(f"S:  công thức n(n+1)/2 = {n}*{n + 1}/2 = {S}")
        print(f"S1: công thức n² = {n}² = {S1}")
        print(f"S2: công thức n(n+1) = {n}*{n + 1} = {S2}")
        print(f"S3: công thức n(n+1)(2n+1)/6 = {n}*{n + 1}*{2 * n + 1}/6 = {S3}")

    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")


# Chạy chương trình
if __name__ == "__main__":
    main()