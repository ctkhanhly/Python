import random
import os
'''
import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "2091/data.txt"
abs_file_path = os.path.join(script_dir, rel_path)
'''


def main():
    #os.listdir and os.path.join
    #os.getcwd
    # print(scramble_word('word'))
    # print(create_permutation(5))
    #script_dir = os.path.dirname(__file__)
    #print(script_dir)
    file_path = '/Users/lycao/Documents/file2.txt'

    file = open(file_path, 'r')
    words = file.read().split(' ')
    print(words)
    word = words[random.randint(0, len(words) - 1)]
    print(scramble_word(word))


def create_permutation(n, start=1):
    n = [k for k in range(start, n + start)]
    list = []
    while(len(n) > 0):
        index = random.randint(0, len(n) - 1)
        list.append(n[index])
        n.remove(n[index])
    return list


def scramble_word(word):
    list = create_permutation(len(word), 0)
    print(list)
    new_word = [word[list[k]] for k in range(len(list))]
    new_word = ''.join(new_word)
    return new_word


main()
