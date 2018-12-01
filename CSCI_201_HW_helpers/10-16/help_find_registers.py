import numpy as np

register_lookup = {}
def hexToBinary(hex):
    int_rep = int(hex,16) #convert the hex to int
    bin_val = bin(int_rep)
    print("\nThe Binary Value of " + hex + "is ")
    return bin_val

def run():

    hex_values = input("Enter the rest of the mips instruction code in hex: ")

    format = input("Enter the format: ")

    return 0

if __name__ == "__main__":
    run()