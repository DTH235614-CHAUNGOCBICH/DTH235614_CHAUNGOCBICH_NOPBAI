import random

n = int(input("Nhập số phần tử: "))
lst = random.sample(range(0, 100), n)  #sample đảm bảo không trùng
print("List ngẫu nhiên không trùng:", lst)