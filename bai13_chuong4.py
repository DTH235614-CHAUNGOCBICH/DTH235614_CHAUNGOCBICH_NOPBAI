def tong_uoc(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s

def la_so_hoan_thien(n):
    return tong_uoc(n) == n

def la_so_thinh_vuong(n):
    return tong_uoc(n) > n

#test
n = int(input("Nhập số nguyên dương n: "))
if la_so_hoan_thien(n):
    print(n, "là số hoàn thiện")
elif la_so_thinh_vuong(n):
    print(n, "là số thịnh vượng")
else:
    print(n, "không phải số hoàn thiện/thịnh vượng")