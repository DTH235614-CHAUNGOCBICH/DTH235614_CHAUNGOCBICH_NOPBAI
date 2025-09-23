def XuLyChuoi(s):
    inhoa = sum(1 for c in s if c.isupper())
    inthuong = sum(1 for c in s if c.islower())
    chuso = sum(1 for c in s if c.isdigit())
    dacbiet = sum(1 for c in s if not c.isalnum() and not c.isspace())
    khoangtrang = sum(1 for c in s if c.isspace())

    nguyenam = sum(1 for c in s.lower() if c in "aeiouáàảãạăâêôơưíìĩịùúụủũ")
    phuam = sum(1 for c in s.lower() if c.isalpha() and c not in "aeiouáàảãạăâêôơưíìĩịùúụủũ")

    print("Chữ IN HOA:", inhoa)
    print("Chữ in thường:", inthuong)
    print("Chữ số:", chuso)
    print("Ký tự đặc biệt:", dacbiet)
    print("Khoảng trắng:", khoangtrang)
    print("Nguyên âm:", nguyenam)
    print("Phụ âm:", phuam)

s = input("Nhập chuỗi: ")
XuLyChuoi(s)