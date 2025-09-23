def LayTenFile(path):
    #Lấy phần tên file sau dấu "\" cuối cùng
    return path.split("\\")[-1]

def LayTenBaiHat(path):
    #Lấy tên bài hát (bỏ phần đuôi .mp3 nếu có)
    tenfile = LayTenFile(path)
    return tenfile.rsplit(".", 1)[0]

def main():
    duongdan = input("Nhập đường dẫn file nhạc: ")
    print("Tên file:", LayTenFile(duongdan))
    print("Tên bài hát:", LayTenBaiHat(duongdan))

main()