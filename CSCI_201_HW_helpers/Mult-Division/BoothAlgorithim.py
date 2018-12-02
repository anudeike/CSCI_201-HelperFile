import numpy as np
from collections import deque

#helper to double the length of the multiplicand - could do it with numpy tho
def double_length(arr):
    toAdd = []
    for x in range(len(arr)):
        toAdd.append("0")

    #add them together.
    target = toAdd + arr
    return target

#fill array
def fillArray(length):
    target = []
    for x in range(length):
        target.append("0")
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
def multiplication(mp, mc, isSigned=False):
    #for testing purposes
    mp = list("0011")
    mc = list("0011")

    #double the length of the mc
    mc = double_length(mc)


    product = fillArray(len(mc))

    for x in range(10):
        final_bit = 0

        #print out the summary
        print("=== Step " + str(x) + " ===")
        print("The multiplier is: " + "".join(mp))
        print("The multiplicand is: " + "".join(mc))
        print("The Product is: " + "".join(product))
        print(" ")

        #check the last bit
        curr_last_bit = mp[len(mp)-1]
        choose_operation = checkLastBit(curr_last_bit,final_bit)

        if(choose_operation == 0):
            print("No Operation Needed \n")
            print("shifting...")
            mc = shiftLeft(mc)
            mp = shiftRight(mp)
        if(choose_operation == 1):
            print(0)


    return 0

def BoothAlgo():
    str_multiplier = input("Enter the Multiplier (the number on the right): ")
    str_multiplicand = input("Enter the multiplicand (the number on the left): ")
    str_isSigned = input("Signed (Y) or Unsigned (N)?")

    #convert to list (easier to use)
    mp_list = list(str_multiplier)
    mc_list = list(str_multiplicand)

    # if unsigned
    if (str_isSigned == "N"):
        multiplication(mp_list, mc_list)


if __name__ == "__main__":
    BoothAlgo()
