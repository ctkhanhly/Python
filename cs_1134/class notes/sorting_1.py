'''
given a list, reorder them so that they are in increasing order.

selection sort
insertion sort
bubble sort
merge sort
quick sort
heap sort

selection sort:
1. find min
2. swap min with first element
3. deal with elements after index 0
4. Repeat step 1 and 2
"Take the smallest, put it first"

find min: scan the entire list
total = n + n-1 + n-2 +... + 1 = 0(n^2)

insertion sort: 0(n^2)

compare each index to the left elements and shift it to an order that matches an increasing order of the elements being considered

total = 1 + 2 + 3 + 4 + ... + n

def sort(lst):
    if(len(lst) ! = 1):
        return
    else:
        sort(lst[..:...])

change order to place last item in its sorted position

merge sort:
step 1: sort recursively the first half
step 2: sort recursively the second haldf
step 3: merge 2 halves

compare each element of in corresponding indexes of each half
'''


def merge_sort1(lst):
    if(len(lst) == 1):
        return
    else:
        first_half = merg_sort1(lst[:len(lst) // 2])
        second_half = merg_sort1(lst[len(lst) // 2:])

        new_list = [0] * len(lst)
        for i in range(len(lst) // 2):
            if(first_half[i] < second_half[i]):
                new_list.append(first_half[i])
                new_list.append(second_half[i])
            else:
                new_list.append(second_half[i])
                new_list.append(first_half[i])
        if(len(lst) % 2 != 0):
            new_list.append(second_half[len(second_half) - 1])
        list = new_list


def merge_sort(lst):
    pass


def merge_sort_helper(lst, low, high):
    if(low == high):
        return
    else:
        mid = (low + high) // 2
        merge_sort_helper(lst, low, mid)
        merge_sort_helper(lst, mid + 1, high)
        merge(lst, low, mid, high)


def merge(lst, low_left, high_left, high_right):
    pass
