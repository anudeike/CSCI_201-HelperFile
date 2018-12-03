import numpy as np
from bitstring import Bits

#allows for adding binary numbers (takes in two strings)
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

    result = result.zfill(max_len)

    #just a little clean up for booth's removes the first number if it is long
    if (len(result) > max_len and result[0] == "1"):
        result = result[1:]  # remove the first part

    return result

#get the 2's complement
def get2sComp(b):
    b_list = list(b)

    #this part gets the ones complement
    for i in range(len(b_list)):
        if b_list[i] == "0":
            b_list[i] = "1"
        else:
            b_list[i] = "0"

    #add one to make it a 2s comp
    b = "".join(b_list)
    comp = add_binary_nums(b,'1')

    return comp

def subtract(bin_a, bin_b):

    #set the given length of the result
    if len(bin_a) > len(bin_b):
        result_length = len(bin_a)
    else:
        result_length = len(bin_b)

    comp_b = get2sComp(bin_b)
    result = add_binary_nums(bin_a,comp_b)

    #check if the result was longer than the longest incoming
    #and if the result[0] == 1
    if(len(result) > result_length and result[0] == "1"):
        result = result[1:] #remove the first part

    return result

def run():
    a = "00000000"
    b = "00001010"
    print(add_binary_nums("11110110","00101000"))
    print(subtract(a, b)) #a-b


    return 0
