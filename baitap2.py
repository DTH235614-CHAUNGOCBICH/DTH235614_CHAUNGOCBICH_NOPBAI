# Nhập hai số a và b từ bàn phím
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

# Nhập ký tự ch từ bàn phím
ch = input("Nhập ký tự toán tử (+, -, *, /): ")

# Kiểm tra và thực hiện phép tính tương ứng
if ch == '+':
    ket_qua = a + b
    print(f"{a} + {b} = {ket_qua}")
elif ch == '-':
    ket_qua = a - b
    print(f"{a} - {b} = {ket_qua}")
elif ch == '*':
    ket_qua = a * b
    print(f"{a} * {b} = {ket_qua}")
elif ch == '/':
    if b != 0:  # Kiểm tra chia cho 0
        ket_qua = a / b
        print(f"{a} / {b} = {ket_qua}")
    else:
        print("Lỗi: Không thể chia cho 0!")
else:
    print(f"Ký tự '{ch}' không phải là một toán tử hợp lệ.")