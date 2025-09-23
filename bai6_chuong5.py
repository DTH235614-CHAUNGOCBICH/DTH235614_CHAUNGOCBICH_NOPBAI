import re

def NegativeNumberInStrings(s):
    # tìm tất cả số nguyên âm trong chuỗi
    numbers = re.findall(r'-\d+', s)
    return [int(num) for num in numbers]

def main():
    chuoi = input("Nhập vào 1 chuỗi bất kỳ: ")
    so_am = NegativeNumberInStrings(chuoi)
    if so_am:
        print("Các số nguyên âm trong chuỗi là:", so_am)
    else:
        print("Không có số nguyên âm nào trong chuỗi.")

main()