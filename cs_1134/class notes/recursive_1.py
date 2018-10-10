

'''
def count_appearances(lst, val):
    if(len(lst) == 0):
        return 0
    else:
        count_rest = count_appearances(lst[1:],val)
        if(lst[0] == val):
            return count_rest +1
        else:
            return count_rest
'''


def count_appearances(lst, val): #not recursive
    # count_appearances_helper alone is bad for user experience
    #definition of any function has run-time O(n)
    def count_appearances_helper(lst, low, high, val): #recursive
        if(low == high):
            if(lst[low] == val):
                return 1
            else:
                return 0
        else:
            count_rest = count_appearances(lst, low + 1, high, val)
            if(lst[low] == val):
                return count_rest + 1
            else:
                return count_rest
    if(len(lst) == 0):
        return 0 #O(1)
    else:
        return count_appearances_helper(lst, 0, len(lst) - 1, val) #O(n)

def power(x,n):
    if(n==1):
        return x
    else:
        rest = power(x, n-1)
        return x*rest
        #x^n = x^(n/2) * x^(n/2) if n is even
        #x^n = x^(n/2) * x^(n/2) if n is even
