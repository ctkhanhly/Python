def findMedianSortedArrays(num1, num2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    n1 = 0
    n2 = 0
    index = 0
    lst = [0] * ((len(num1) + len(num2)) // 2 + 1)
    while(n1 < len(num1) and n2 < len(num2) and index < len(lst)):
        if(num1[n1] < num2[n2]):
            lst[index] = num1[n1]
            n1 += 1
            index += 1
        elif(num1[n1] > num2[n2]):
            lst[index] = num2[n2]
            n2 += 1
            index += 1
        else:
            lst[index] = num1[n1]
            n1 += 1
            index += 1
            if(index < len(lst)):
                lst[index] = num2[n2]
                n2 += 1
                index += 1
    #compare = len(num1) > len(num2)
    if(n2 == len(num2) and index < len(lst)):
        for i in range(len(lst) - index):
            lst[index] = num1[n1]
            n1 += 1
            index += 1
    elif(n1 == len(num1) and index < len(lst)):
        for i in range(len(lst) - index):
            lst[index] = num2[n2]
            n2 += 1
            index += 1
    result = 0.0
    if((len(num1) + len(num2)) % 2 == 0):
        result = (float)(lst[len(lst) - 1] + lst[len(lst) - 2]) / 2
    else:
        result = (float)(lst[len(lst) - 1])
    return result


num1 = [3, 4]
num2 = [1, 2]
print(findMedianSortedArrays(num1, num2))
