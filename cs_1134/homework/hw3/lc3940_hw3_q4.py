def remove_all(lst, val):
    count = 0
    i = 0
    while(i < len(lst)):
        if(lst[i] == val):
            i = i + 1
            count += 1
            # shift every element to the left and shift them on top of the duplicates
            while (i < len(lst) and not(lst[i] == val)):
                lst[i - count] = lst[i]
                i += 1  # this increase makes the outer loop only runs n times
        else:
            i += 1
    while(count > 0):
        lst.pop()
        count -= 1
    return lst


'''
list1 = [2, 1, 3, 8, 1, 0, 2, 33, 11, 2, 4, 2]
print(remove_all(list1, 2))
'''
