def find_singNum(lst):
    '''
    Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
    result = lst[0]
    for i in range(1, len(lst)):
        result = result ^ lst[i]
    return result


list1 = [1, 2, 3, 4, 5, 6, 7, 6, 1, 2, 4, 7, 3]
print(find_singNum(list1))
