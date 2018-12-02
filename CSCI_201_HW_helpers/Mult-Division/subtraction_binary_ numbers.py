import numpy as np
from bitstring import Bits

#allows for adding binary numbers
def add_binary_nums(x, y):
    max_len = max(len(x), len(y))

    x = x.zfill(max_len)
    y = y.zfill(max_len)

    # initialize the result
    result = ''

    # initialize the carry
    carry = 0

    # Traverse the string
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1  # Compute the carry.

    if carry != 0: result = '1' + result

    return result.zfill(max_len)

#get the 2's complement
def get2sComp(b):
    b_list = list(b)
    for i in range(len(b_list)):
        if b_list[i] == "0":
            b_list[i] = "1"
        else:
            b_list[i] = "0"

    return b_list

def subtract(bin_a, bin_b):


    return get2sComp(bin_b)

def run():
    a = "0110"
    b = "0100"

    print(subtract(a, b)) #a-b


    return 0
if __name__ == "__main__":
    run()