"""
EXAMPLE QUESTION:

"Given a 10 bit binary sequence 0100111011,
show the decimal number it represents in unsigned integer,
sign-magnitude, one's complement, two's complement and execess-511.
Separate the answer with commma, such as "1,1,1,1,1,-126"
without the quotes. No spaces are allowed.
"""

#convert to int
def binaryToInt(binary_string):
    return int(binary_string, 2)

#main
def run():
    binary_input = input("Enter the binary number you would like to convert >>")
    
if __name__ == "__main__":
    run()