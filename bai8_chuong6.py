n = int(input("Nhập số phần tử: "))
M = []

for i in range(n):
    M.append(float(input(f"Nhập M[{i}]: ")))

print("Dãy số ban đầu:", M)
M.sort(reverse=True)
print("Dãy số sau khi sắp xếp giảm dần:", M)