from random import randrange

while True:
    somay = randrange(1, 101)
    solandoan = 0
    win = False

    while solandoan < 7:
        solandoan += 1
        songuoi = int(input("Máy đã chọn [1..100], mời bạn đoán: "))
        print("Bạn đoán lần thứ", solandoan)

        if somay == songuoi:
            print("Chúc mừng bạn đoán đúng! Số máy là =", somay)
            win = True
            break
        elif somay > songuoi:
            print("Bạn đoán sai, số máy > số bạn đoán")
        else:
            print("Bạn đoán sai, số máy < số bạn đoán")

    if win == False:
        print("GAME OVER! Số máy =", somay)

    hoi = input("Tiếp không? (nhấn k để dừng): ")
    if hoi.lower() == "k":
        break

print("Cám ơn bạn đã chơi Game!")