import math

# goal is to convert a decimal to floating point

"""
[ISSUES]
1. Something weird and annoyingly recursive happens when you input anything with "0.3" [FIXED]
2. Right now, it rounds to 10 in the separate function. Be careful.
"""


def run():
    decimal = input("Enter the base-10 decimal number: >>")
    mantissa_limit = int(input("Enter the mantissa limit: >> "))
    bias = int(input("Enter the bias: "))

    # decide whether the number is negative or positive
    if decimal[0] == "-":
        sign = 1
    else:
        sign = 0

    # get the decimal and whole numbers
    left, right = separate(str(abs(float(decimal))))

    # gets the number in binary using the multiplication method
    binFrac = fractionToBinary(right, mantissa_limit)
    binWhole = intToBinary(left)



    # display in raw binary
    bin_raw = str(binWhole) + "." + str(binFrac)

    print("Straight Binary is: " + bin_raw)

    # MoveTheDecimalPlace
    moved, exp, sig = moveDecimal(bin_raw)


    # add the bias to the exp and convert it to binary
    decimal_bias_exponent = (bias-1) + exp
    binBiasExp = intToBinary(decimal_bias_exponent)

    print("This is the moved: " + str(moved))



    #lets join the whole thing! sign + binBiasExp + the significand
    IEEE_format = str(sign) + " " + str(binBiasExp) + " " + str(sig)
    print("Sign bit: " + str(sign))
    print("Exponent Bias bits: " + str(binBiasExp))
    print("Significand bits: " + str(sig))
    print("COMPLETE IEEE Format: " + IEEE_format)



"""
Move the decimal place to the right place
RETURNS: Exponent, 
"""

def moveDecimal(rawBin):
    rawBin_float = float(rawBin)
    rawBin_list = list(rawBin)
    exp = 0  # holds the exponent
    moved = ""

    # if greater than 0, just move the point to the front
    if (rawBin_float > 0):

        # calculate the amount of spaces to move

        for i in range(len(rawBin)):
            if (rawBin[i] == "."):
                break

        exp = i  # this is the 2^x (the x part)

        rawBin_list.remove(".")
        rawBin_list.insert(1, ".")
        moved = "".join(rawBin_list)

    # if less than 0 ->
    if (rawBin_float < 0):
        afterOne = False
        for w in range(len(rawBin_list)):
            if (afterOne):
                break

            if (rawBin_list[w] == "1"):
                afterOne = True

        # save the exponent
        exp = -(w - 2)

        # move the decimal point to where it needs to be
        rawBin_list.remove(".")
        rawBin_list.insert(w - 1, ".")
        moved = "".join(rawBin_list)

    #get the relevant portion
    rel = moved.split(".")

    return moved, exp, rel[1]


# returns a tuple (left, right)
def separate(num):
    print("Separation...")
    # get the numbers to the right and left of the decimal point
    # if 5.672, then a = 5 and b = 0.672
    left = math.floor(float(num))
    right = round(float(num) - left, 10)

    return left, right


# uses the multiplication method
def fractionToBinary(frac, limit):
    running = True
    frac_binary = []
    k = 0
    while (running):
        frac = frac * 2

        whole, new_frac = separate(str(frac))  # get the whole and fractional part of result
        frac_binary.append(str(whole))
        print("")

        # check whether the new fraction is 0 -> if it is stop
        if (int(new_frac == 0)):
            running = False

        frac = new_frac

        # fail safe
        if (len(frac_binary) > limit):
            #print("[Warning] Binary is too long. Losing Precision...")
            running = False

        k += 1

    # join the list to make it a string
    binFracString = "".join(frac_binary)
    return binFracString


# int to binary -- helluva lot easier
def intToBinary(integer):
    a = bin(integer)
    return a[2:]


if __name__ == "__main__":
    run()
