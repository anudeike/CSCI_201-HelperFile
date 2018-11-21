
def IEEE_to_Decimal(exp_bit_num,bias,binary):
  sign_bit = int(binary[0]) #this is the sign portion
  exp_bits = binary[1:exp_bit_num + 1] #get the exp bits
  significand = binary[exp_bit_num + 1:] #put the rest in the fractional bits

  sign = (-1) ** sign_bit
  mantissa = fractional_bits_to_decimal(significand) #fractional bits
  exp = int(exp_bits,2) - bias


  return sign * (1 + mantissa) * 2 ** exp


def fractional_bits_to_decimal(bits):
  total = 0
  exp = -1

  for elem in bits:
    total += int(elem) * 2 ** exp
    exp -= 1

  return total




if __name__ == "__main__":
  #mantissa = fractional_bits_to_decimal("01010110100000000000000")

  #print(str((1 + mantissa) * 8))
  ex_bits = int(input("Enter the amount of exponent bits: "))
  bias = int(input("Enter the bias: "))
  target = input("Enter the IEEE formatted floating point number: ")

  #number of exponent bits, bias, actual binary
  result = IEEE_to_Decimal(ex_bits, bias, target)
  print(result)

