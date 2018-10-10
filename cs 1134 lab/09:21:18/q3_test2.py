import random

if __name__ == '__main__':
    t = Polytimer()
    t.reset()
    total_time2_1 = 0.0
    list2_1 = [i random.randint(-1000, 1000) for i in range(128)]
    result2_1, start2_1, end2_1 = t.maxSubsequenceSum2(list)
    total_time2_1 = t.elapsed()

    t = Polytimer()
    t.reset()
    total_time2_2 = 0.0
    list2_2 = [i random.randint(-1000, 1000) for i in range(256)]
    result2_2, start2_2, end2_2 = t.maxSubsequenceSum2(list)
    total_time2_2 = t.elapsed()

    t = Polytimer()
    t.reset()
    total_time2_3 = 0.0
    list2_3 = [i random.randint(-1000, 1000) for i in range(512)]
    result2_3, start2_3, end2_3 = t.maxSubsequenceSum2(list)
    total_time1_3 = t.elapsed()

    t = Polytimer()
    t.reset()
    total_time2_4 = 0.0
    list2_4 = [i random.randint(-1000, 1000) for i in range(1024)]
    result2_4, start2_4, end2_4 = t.maxSubsequenceSum2(list)
    total_time2_4 = t.elapsed()

    t = Polytimer()
    t.reset()
    total_time2_5 = 0.0
    list2_5 = [i random.randint(-1000, 1000) for i in range(2048)]
    result2_5, start2_5, end2_5 = t.maxSubsequenceSum2(list)
    total_time2_5 = t.elapsed()

    t = Polytimer()
    t.reset()
    total_time2_6 = 0.0
    list2_6 = [i random.randint(-1000, 1000) for i in range(4096)]
    result2_6, start2_6, end2_6 = t.maxSubsequenceSum2(list)
    total_time2_6 = t.elapsed()
