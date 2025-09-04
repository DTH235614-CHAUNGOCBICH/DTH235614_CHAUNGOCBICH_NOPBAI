def in_bang_cuu_chuong_don_gian():
    """
    In bảng cửu chương đơn giản
    """
    print("BẢNG CỬU CHƯƠNG TỪ 2 ĐẾN 9")
    print("=" * 50)

    for i in range(2, 10):
        print(f"\nBảng nhân {i}:")
        print("-" * 15)
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")

    print("\n" + "=" * 50)


def in_bang_cuu_chuong_khoi():
    """
    In bảng cửu chương theo khối 3x3
    """
    print("\nBẢNG CỬU CHƯƠNG THEO KHỐI")
    print("=" * 75)

    # Chia thành 3 cột: 2-4, 5-7, 8-9
    for row in range(0, 3):
        start = 2 + row * 3
        end = start + 3

        # In tiêu đề các cột
        for i in range(start, min(end, 10)):
            print(f"Bảng {i}".center(25), end="")
        print()
        print("-" * 75)

        # In nội dung
        for j in range(1, 11):
            for i in range(start, min(end, 10)):
                result = i * j
                print(f"{i} x {j:2} = {result:2}".ljust(25), end="")
            print()
        print()


# Chạy chương trình đơn giản
in_bang_cuu_chuong_don_gian()
in_bang_cuu_chuong_khoi()