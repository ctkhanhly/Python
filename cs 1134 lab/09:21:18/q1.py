'''
Note that this must be done in-place and you are only
allowed Θ (1) additional space. In other words, you cannot use any collection of
elements of non-constant size.

= cannot make a new list
'''

# 1
'''
remove the first one => every other elements have to shift to the left

'''


def move_zeroes(nums):
    for i in range(len(nums)):
        if(nums[i] != 0):
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
    return nums


'''
    while i < (len(nums) - 1):
        if(nums[i] == 0):
            nums[i] = nums[i + 1]
            nums[i + 1] = 0
            zero_index = i + 1
            i += 1
            num_zero += 1
        if(nums[i] != 0 & i > zero_index):
            nums[zero_index] = nums[i]
            zero_index = i
'''


'''
2.
. Aim
for linear time complexity. That is if the first input list has n elements, and the second has m elements, the runtime should be θ(n + m)
'''


def inter(lst_A, lst_B):
    '''
    len_inter = len(lst_B)
    if(len(lst_A) > len(lst_B)):
        len_inter = len(lst_A)
    lst_inter = [0] * len_inter
    # why shouldnt we change the size of the list?
    index = 0
    for i in range(len_inter):
        if(lst_A[i] == lst_B[i]):
            lst_inter[index] = lst_A[i]
            index += 1
    '''


# return [n for n in lst1 if n in lst2], n in lst2 is linear, not constant
    p1 = 0
    p2 = 0
    while(p1 < len(lst1) & p2 < len(lst2)):
        if(lst1[p1] < lst2[p2]):
            p1 += 1
        elif (lst1[p1] > lst2[p2]):
            p2 += 1
        else:
            result.append(lst[p1])


nums = [0, 1, 2, 3, 0, 0, 2, 0, 4, 5, 0, 7]
print(move_zeroes(nums))
