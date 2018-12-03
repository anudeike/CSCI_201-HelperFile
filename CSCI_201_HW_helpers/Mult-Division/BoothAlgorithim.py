import numpy as np
from collections import deque
import sys
sys.path.append("CSCI_201_HW_helpers/Mult-Division/subtraction_binary_ numbers.py")

"""
HELPER FUNCTIONS
"""
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

#helper to double the length of the multiplicand - could do it with numpy tho
def double_length(arr, filling_element):
    toAdd = []
    for x in range(len(arr)):
        toAdd.append(filling_element)

    #add them together.
    target = toAdd + arr
    return target

#fill array
def fillArray(length, filling_element):
    target = []
    for x in range(length):
        target.append(filling_element)
    return target

#shifting functions
def shiftLeft(arr):
    a = deque(arr)
    a.rotate(1) #shift left
    toReturn = list(a)
    toReturn[0] = "0" #replace whatever is at the front with a 0
    return toReturn

def shiftRight(arr):
    a = deque(arr)
    a.rotate(-1)  # shift left
    toReturn = list(a)
    toReturn[len(toReturn)-1] = "0"  # replace whatever is at the back with a 0
    return toReturn

def checkLastBit(curr_last_bit, past_last_bit):
    """
    :param curr_last_bit:
    :param past_last_bit:
    :return: 0 if the bits are the same, 1 if 1->0, and 0 if 0->1
    """

    if curr_last_bit == past_last_bit:
        return 0
    elif curr_last_bit > past_last_bit:
        return 1
    elif curr_last_bit < past_last_bit:
        return -1

#takes in the multiplier and the multiplicand
def multiplicationBooth(mp, mc, isSigned=False):

    #for testing purposes
    mp = list(mp)
    mc = list(mc)

    #check if signed
    if (isSigned):
        filling_element = "1"
    else:
        filling_element = "0"

    #double the length of the mc
    mc = double_length(mc, filling_element)

    final_bit = 0


    product = fillArray(len(mc), "0")

    for x in range(10):


        #print out the summary
        print("\n=== Step " + str(x) + " ===")
        print("The multiplier is: " + "".join(mp))
        print("The multiplicand is: " + "".join(mc))
        print("The Product is: " + "".join(product))
        print(" ")

        #check the last bit
        curr_last_bit = mp[len(mp)-1]
        choose_operation = checkLastBit(int(curr_last_bit),int(final_bit))

        if(choose_operation == 0):
            print("No Operation Needed \n")
            print("shifting...")
            mc = shiftRight(mc)
            mp = shiftLeft(mp)
        if(choose_operation == 1):
            print("0 -> 1: Product = Product - Mcand")
            new_product = subtract("".join(product), "".join(mc))
            print("shifting...")
            mc = shiftRight(mc)
            mp = shiftLeft(mp)
            product = list(new_product)
        if(choose_operation == -1):
            print("1 -> 0: Product = Product + Mcand")
            new_product = add_binary_nums("".join(product), "".join(mc))
            print("shifting...")
            mc = shiftRight(mc)
            mp = shiftLeft(mp)
            product = list(new_product)

        final_bit = int(curr_last_bit)

    return 0

#takes in the multiplier and the multiplicand
def multiplication_nonOp(mp, mc, isSigned=False):

    #for testing purposes
    mp = list(mp)
    mc = list(mc)

    #check if signed
    if (isSigned):
        filling_element = "1"
    else:
        filling_element = "0"

    #double the length of the mc
    mc = double_length(mc, filling_element)

    final_bit = 0


    product = fillArray(len(mc), "0")

    for x in range(10):


        #print out the summary
        print("\n=== Step " + str(x) + " ===")
        print("The multiplier is: " + "".join(mp))
        print("The multiplicand is: " + "".join(mc))
        print("The Product is: " + "".join(product))
        print(" ")

        #check the last bit
        curr_last_bit = mp[len(mp)-1]
        #choose_operation = checkLastBit(int(curr_last_bit),int(final_bit))

        #choose the operation (for the non optimized)
        if int(curr_last_bit) == 1:
            choose_operation = -1
        else:
            choose_operation = 0

        if(choose_operation == 0):
            print("Last bit of multiplier is 0: No Operation Needed \n")
            print("shifting...")
            mc = shiftRight(mc)
            mp = shiftLeft(mp)
        if(choose_operation == -1):
            print("Last bit of multiplier is 1: Product = Product + Mcand")
            new_product = add_binary_nums("".join(product), "".join(mc))
            print("shifting...")
            mc = shiftRight(mc)
            mp = shiftLeft(mp)
            product = list(new_product)

        #final_bit = int(curr_last_bit)

    return 0

def BoothAlgo():
    mc = input("Enter the multiplicand: ")
    mp = input("Enter the multiplier: ")
    int_signed = int(input("Signed [0] or Unsigned [1]: "))

    if int_signed == 0:
        multiplicationBooth(mp, mc, True)
    else:
        multiplicationBooth(mp, mc)

def NonOptimizedMultiplication():
    mc = input("Enter the multiplicand: ")
    mp = input("Enter the multiplier: ")
    int_signed = int(input("Signed [0] or Unsigned [1]: "))

    if int_signed == 0:
        multiplication_nonOp(mp, mc, True)
    else:
        multiplication_nonOp(mp, mc)




if __name__ == "__main__":
    #BoothAlgo()
    NonOptimizedMultiplication()
