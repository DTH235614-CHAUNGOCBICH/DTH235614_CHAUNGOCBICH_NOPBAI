def tinh_tien_sau_18_thang():

    X = float(input("Nhập số tiền gửi tiết kiệm (X): "))
    lai_suat_thang = 0.6 / 100  # 0.6%
    so_thang = 18
    chu_ky = 6
    so_chu_ky_day_du = so_thang // chu_ky

    so_thang_con_lai = so_thang % chu_ky
    tien_hien_tai = X

    for i in range(so_chu_ky_day_du):
        lai_suat_6_thang = (1 + lai_suat_thang) ** chu_ky - 1
        tien_hien_tai = tien_hien_tai * (1 + lai_suat_6_thang)

    if so_thang_con_lai > 0:
        lai_suat_con_lai = (1 + lai_suat_thang) ** so_thang_con_lai - 1
        tien_hien_tai = tien_hien_tai * (1 + lai_suat_con_lai)

    print(f"\nSố tiền gốc: {X:,.0f} VNĐ")
    print(f"Lãi suất: 0.6% / tháng")
    print(f"Thời gian: 18 tháng")
    print(f"Cộng lãi vào gốc mỗi 6 tháng")
    print(f"Số tiền sau 18 tháng: {tien_hien_tai:,.0f} VNĐ")
    return tien_hien_tai
if __name__ == "__main__":
    tinh_tien_sau_18_thang()

