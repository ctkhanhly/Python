def square_root(num):
    n = 0.01
    while round(n * n, 1) != num:
        n += 0.01
    return n
    # 0(100n)


def square_root(num):
    i = 1
    while(i * i <= num):
        i += 1
    root_approx = i - 1
    print(root_approx)
    for x in range(10):
        intermediate = num / root_approx
        root_approx = intermediate / 2 + root_approx / 2

    return round(root_approx, 2)


print(square_root(5))
