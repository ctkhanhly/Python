def find_duplicates(lst):
    for i in range(len(lst)):
        if(lst[i] < lst[0]):
            lst[0], lst[i] = lst[i], lst[0]
    return lst


lst = [4, 1, 5, 2, 3, 24, 10, 3]
print(find_duplicates(lst))
