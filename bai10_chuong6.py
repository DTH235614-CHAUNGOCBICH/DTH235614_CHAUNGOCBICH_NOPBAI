def nhap_matrix(m, n, name):
    A = []
    print(f"Nhập ma trận {name}:")
    for i in range(m):
        row = list(map(int, input(f"Hàng {i+1}: ").split()))
        while len(row) != n:
            print("Sai số cột, nhập lại!")
            row = list(map(int, input(f"Hàng {i+1}: ").split()))
        A.append(row)
    return A

def in_matrix(A):
    for row in A:
        print(row)

def cong_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

A = nhap_matrix(m, n, "A")
B = nhap_matrix(m, n, "B")

print("Ma trận A:")
in_matrix(A)
print("Ma trận B:")
in_matrix(B)

print("Tổng A + B:")
in_matrix(cong_matrix(A, B))

print("Hoán vị A:")
in_matrix(transpose(A))

print("Hoán vị B:")
in_matrix(transpose(B))