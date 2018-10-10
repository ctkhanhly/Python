def square_root(num):
    i = 1
    while(i * i <= num):
        i *= 2
    i = i / 2
    if((i + 1) * (i + 1) <= num):
        i += 1
    root_approx = i
    print(root_approx)
    for x in range(10):
        intermediate = num / root_approx
        root_approx = intermediate / 2 + root_approx / 2

    return round(root_approx, 2)


def sqrt(num):
    if num == 1 or num == 0:
        return num
    low = 0.0
    factor = 1.0
    if(num < 1):
        high = 1
    else:
        high = num * factor


print(square_root(5))
