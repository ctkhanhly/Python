import time
import random


class PolyTimer:
    def __init__(self):
        self.start = time.time()

    def elapsed(self):
        return time.time() - self.start

    def reset(self):
        self.start = time.time()


'''
Linear maximum contiguous subsequence sum algorithm.
seqStart and seqEnd represent the actual best sequence.
'''


def maxSubsequenceSum3(vals):
    n = len(vals)
    thisSum = 0
    maxSum = 0

    i = 0
    seqStart = 0
    seqEnd = 0
    for j in range(n):
        thisSum += vals[j]
        if (thisSum > maxSum):
            maxSum = thisSum
            seqStart = i
            seqEnd = j
        elif (thisSum < 0):
            i = j + 1
            thisSum = 0

    return maxSum, seqStart, seqEnd


'''
Quadratic maximum contiguous subsequence sum algorithm.
seqStart and seqEnd represent the actual best sequence.
'''


def maxSubsequenceSum2(vals):
    n = len(vals)
    maxSum = 0
    seqStart = 0
    seqEnd = 0

    for i in range(n):
        thisSum = 0
        for j in range(i, n):
            thisSum += vals[j]
            if (thisSum > maxSum):
                maxSum = thisSum
                seqStart = i
                seqEnd = j

    return maxSum, seqStart, seqEnd


'''
Cubic maximum contiguous subsequence sum algorithm.
seqStart and seqEnd represent the actual best sequence.
'''


def maxSubsequenceSum1(vals):
    n = len(vals)
    maxSum = 0
    seqStart = 0
    seqEnd = 0

    for i in range(n):
        for j in range(i, n):
            thisSum = 0
            for k in range(i, j + 1):
                thisSum += vals[k]
            if (thisSum > maxSum):
                maxSum = thisSum
                seqStart = i
                seqEnd = j

    return maxSum, seqStart, seqEnd


if __name__ == '__main__':
    t = PolyTimer()
    t.reset()
    total_time1_1 = 0.0
    list1_1 = [random.randint(-1000, 1000) for i in range(128)]
    result1_1, start1_1, end1_1 = maxSubsequenceSum1(list1_1)
    total_time1_1 = t.elapsed()
    print(total_time1_1)

    t = PolyTimer()
    t.reset()
    total_time1_2 = 0.0
    list1_2 = [random.randint(-1000, 1000) for i in range(256)]
    result1_2, start1_2, end1_2 = maxSubsequenceSum1(list1_2)
    total_time1_2 = t.elapsed()
    print(total_time1_2)

    t = PolyTimer()
    t.reset()
    total_time1_3 = 0.0
    list1_3 = [random.randint(-1000, 1000) for i in range(512)]
    result1_3, start1_3, end1_3 = maxSubsequenceSum1(list1_3)
    total_time1_3 = t.elapsed()
    print(total_time1_3)

    t = PolyTimer()
    t.reset()
    total_time1_4 = 0.0
    list1_4 = [random.randint(-1000, 1000) for i in range(1024)]
    result1_4, start1_4, end1_4 = maxSubsequenceSum1(list1_4)
    total_time1_4 = t.elapsed()
    print(total_time1_4)

    t = PolyTimer()
    t.reset()
    total_time1_5 = 0.0
    list1_5 = [random.randint(-1000, 1000) for i in range(2048)]
    result1_5, start1_5, end1_5 = maxSubsequenceSum1(list1_5)
    total_time1_5 = t.elapsed()
    print(total_time1_5)

    t = PolyTimer()
    t.reset()
    total_time1_6 = 0.0
    list1_6 = [random.randint(-1000, 1000) for i in range(4096)]
    result1_6, start1_6, end1_6 = maxSubsequenceSum1(list1_6)
    total_time1_6 = t.elapsed()
    print(total_time1_6)
