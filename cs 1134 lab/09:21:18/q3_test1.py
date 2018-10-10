import random
import q3

if __name__ == '__main__':
    t = PolyTimer()
    t.reset()
    total_time1_1 = 0.0
    list1_1 = [random.randint(-1000, 1000) for i in range(128)]
    result1_1, start1_1, end1_1 = maxSubsequenceSum1(list1_1)
    total_time1_1 = t.elapsed()

    t = PolyTimer()
    t.reset()
    total_time1_2 = 0.0
    list1_2 = [random.randint(-1000, 1000) for i in range(256)]
    result1_2, start1_2, end1_2 = maxSubsequenceSum1(list1_2)
    total_time1_2 = t.elapsed()

    t = PolyTimer()
    t.reset()
    total_time1_3 = 0.0
    list1_3 = [random.randint(-1000, 1000) for i in range(512)]
    result1_3, start1_3, end1_3 = maxSubsequenceSum1(list1_3)
    total_time1_3 = t.elapsed()

    t = PolyTimer()
    t.reset()
    total_time1_4 = 0.0
    list1_4 = [random.randint(-1000, 1000) for i in range(1024)]
    result1_4, start1_4, end1_4 = maxSubsequenceSum1(list1_4)
    total_time1_4 = t.elapsed()

    t = PolyTimer()
    t.reset()
    total_time1_5 = 0.0
    list1_5 = [random.randint(-1000, 1000) for i in range(2048)]
    result1_5, start1_5, end1_5 = maxSubsequenceSum1(list1_5)
    total_time1_5 = t.elapsed()

    t = PolyTimer()
    t.reset()
    total_time1_6 = 0.0
    list1_1 = [random.randint(-1000, 1000) for i in range(4096)]
    result1_6, start1_6, end1_6 = maxSubsequenceSum1(list1_6)
    total_time1_6 = t.elapsed()
