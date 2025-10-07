import math

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

M = list(map(int, input("Nhập mảng số tự nhiên (cách nhau bằng dấu cách): ").split()))

#dòng 1: số lẻ
odd = [x for x in M if x % 2 != 0]
print("Dòng 1:", odd, "-> có", len(odd), "số lẻ")

#dòng 2: số chẵn
even = [x for x in M if x % 2 == 0]
print("Dòng 2:", even, "-> có", len(even), "số chẵn")

#dòng 3: số nguyên tố
prime = [x for x in M if is_prime(x)]
print("Dòng 3:", prime, "-> có", len(prime), "số nguyên tố")

#dòng 4: không phải số nguyên tố
not_prime = [x for x in M if not is_prime(x)]
print("Dòng 4:", not_prime, "-> có", len(not_prime), "số không nguyên tố")