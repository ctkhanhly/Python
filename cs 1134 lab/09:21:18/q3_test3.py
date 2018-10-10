import random

if __name__ == '__main__':
    t = Polytimer()
    t.reset()
    total_time3_1 = 0.0
    list3_1 = [i random.randint(-1000, 1000) for i in range(128)]
    result3_1, start3_1, end3_1 = t.maxSubsequenceSum3(list)
    total_time3_1 = t.elapsed()

    t = Polytimer()
    t.reset()
    total_time3_2 = 0.0
    list3_2 = [i random.randint(-1000, 1000) for i in range(256)]
    result2_2, start3_2, end3_2 = t.maxSubsequenceSum3(list)
    total_time3_2 = t.elapsed()

    t = Polytimer()
    t.reset()
    total_time3_3 = 0.0
    list3_3 = [i random.randint(-1000, 1000) for i in range(512)]
    result3_3, start3_3, end3_3 = t.maxSubsequenceSum3(list)
    total_time3_3 = t.elapsed()

    t = Polytimer()
    t.reset()
    total_time3_4 = 0.0
    list3_4 = [i random.randint(-1000, 1000) for i in range(1024)]
    result3_4, start3_4, end3_4 = t.maxSubsequenceSum3(list)
    total_time3_4 = t.elapsed()

    t = Polytimer()
    t.reset()
    total_time3_5 = 0.0
    list3_5 = [i random.randint(-1000, 1000) for i in range(2048)]
    result3_5, start3_5, end3_5 = t.maxSubsequenceSum3(list)
    total_time3_5 = t.elapsed()

    t = Polytimer()
    t.reset()
    total_time3_6 = 0.0
    list3_6 = [i random.randint(-1000, 1000) for i in range(4096)]
    result3_6, start3_6, end3_6 = t.maxSubsequenceSum3(list)
    total_time3_6 = t.elapsed()
