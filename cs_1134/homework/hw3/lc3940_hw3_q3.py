def find_duplicates(lst):
    count = [0] * (len(lst) - 1)
    # index 0- (n-1): values 1 ->n-1: n-1 elements
    num_of_duplicates = 0
    for i in range(len(lst)):
        count[lst[i] - 1] += 1
    for i in range(len(count)):
        if(count[i] > 1):
            num_of_duplicates += 1
    new_list = [0] * num_of_duplicates
    index = 0
    for i in range(len(count)):
        if(count[i] > 1):
            new_list[index] = i + 1
            index += 1
    return new_list


'''
list1 = [3, 4, 1, 2, 2, 3, 5, 1, 7, 9]
print(find_duplicates(list1))
'''
