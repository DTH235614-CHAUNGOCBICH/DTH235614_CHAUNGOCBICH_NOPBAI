def oscillate(a, b):
    for i in range(a, b + 1):
        yield i
        yield -i


# test
for n in oscillate(-3, 5):
    print(n, end=' ')
