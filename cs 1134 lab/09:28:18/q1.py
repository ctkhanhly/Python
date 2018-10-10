import random


def roll_the_dice_str(n):
    s = ""
    for i in range(1, n + 1):
        curr_val = random.randint(1, 6)  # 0(1)
        s = s + str(curr_val) + " "  # 2i-2 + 2 = 2i, 0(n)
        # str.join()  -> 0(n)
    return s[:-1]  # 0(n)
    # 0(n*(n+1)) = 0(n^2)


def roll_the_dice_2(n):
    s = [0] * n
    for i in range(n):
        curr_val = random.randint(1, 6)
        s[i] = f'{curr_val}'
    return " ".join(s) #can only join list of strings
    #lst = [str(random.randint(1, 6)) for i in range(n)]


print(roll_the_dice_2(5))
