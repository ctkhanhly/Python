import random


def main():
    print(add_binary('10', '110'))
    print(can_construct('haha', 'ahihihi'))


def add_binary(num1_str, num2_str):
    '''
    if(len(num1_str) < 8):
        while(len(num1_str) < 8):
            num1_str = '0' + num1_str
        print(num1_str)

    if(len(num2_str) < 8):
        while(len(num2_str) < 8):
            num2_str = '0' + num2_str
        print(num2_str)
    '''

    num1_str = int(num1_str, 2)
    # print(num1_str)
    num2_str = int(num2_str, 2)
    # print(num2_str)
    sum = num1_str + num2_str

    return(bin(sum))


'''
    remember = 0;
    sum = '';
    for (int i = 7; i>=0; i--):
        if(num1_str[i] and num2_str[i] == 1)
            if remember:

            else:
                sum = sum + '0'
                remember = 1


'''


def can_construct(ransom_note, magazine):
    ransom_copy = set(ransom_note)
    magazine_copy = set(magazine)
    # contain = True
    for i in ransom_copy:
        if(i not in magazine_copy):
            return False
    return True


def create_permutation(n):
    return lst = [randint(k, n - 1) for k in range(n)]


def scramble_word(word):
    i = len(word)
    new_word = ''
    while(i >= 0):
        k = randint(len(word))
        new _word += word[k]
        word.remove(k)
    return new_word


main()
