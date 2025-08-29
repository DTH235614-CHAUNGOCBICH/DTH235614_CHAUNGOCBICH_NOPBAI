#bai4
print("Chao cac ban")
#bai5
print("Châu ngọc Bích")
#bai6
print(" Mình về mình có nhớ ta?\n Mười lăm năm ấy thiết tha mặn nồng.\n Mình về mình có nhớ không?\n Nhìn cây nhớ núi, nhìn sông nhớ nguồn.")
#bai8
width = 6   # chiều ngang
height = 4  # chiều dọc

for i in range(height):
    for j in range(width):
        # nếu là dòng đầu, dòng cuối, hoặc cột đầu, cột cuối -> in '*'
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#bai9
    width = 9
    height = 4

    for _ in range(height):
        print('*' * width)
#bai10
h = [1, 3, 5, 3, 7, 9]
max_width = max(h)
for sao in h:
    space = (max_width - sao) // 2
    print(" " * space + "*" * sao)
for _ in range(2):
    space = (max_width - 3) // 2
    print(" " * space + "*" * 3)
