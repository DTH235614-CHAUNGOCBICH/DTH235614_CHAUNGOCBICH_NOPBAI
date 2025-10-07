n = int(input("Nhập số phần tử: "))
lst = []

for i in range(n):
    while True:
        x = int(input(f"Nhập phần tử thứ {i}: "))
        if i == 0 or x >= lst[-1]:
            lst.append(x)
            break
        else:
            print("Sai quy tắc, nhập lại (phải >= phần tử trước đó).")

print("Dãy số sau khi nhập:", lst)