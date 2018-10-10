

def add_binary(num1, num2):
    if (len(num1) < len(num2)):
        num1 = '0' * (len(num2) - len(num1)) + num1
    elif (len(num2) < len(num1)):
        num2 = '0' * (len(num1) - len(num2)) + num2
    i = len(num1) - 1
    carry = 0
    result = ''
    sum_str = ''
    while i > 0:
        e1 = int(num1[i])
        e2 = int(num2[i])
        res = e1 + e2 + carry
        if res == 2:
            carry = 1
            res = 0
        elif res == 3:
            carry = 1
            res = 1
        sum_str = str(res) + sum_str
        i -= 1

    if carry == 1:
        sum_str = '1' + sum_str
    return sum_str


def add_binary2(num1_str, num2_str):
    if (len(num1_str) < len(num2_str)):
        num1_str = '0' * (len(num2_str) - len(num1_str)) + num1_str
    elif (len(num2_str) < len(num1_str)):
        num1_str = '0' * (len(num1_str) - len(num2_str)) + num2_str

    i = len(num1_str) - 1
    carry = 0
    result = ''

    while(i >= 0):
        if carry:
            if num1_str[i] != num2_str:
                result = '0' + result
            elif num1_str == 0:
                result = '1' + result
                carry -= 1  # -=1, carry--
            else:
                result = '0' + result
                carry += 1  # carry++

        elif num1_str != num2_str:
            result = result + '1'
        elif num1_str[i] == '0':
            result = '0' + result
        else:
            result = '0' + result
            carry += 1
    if(result[0] == '0'):
        result = '1' + result
    return result


print(add_binary2('110', '10'))
