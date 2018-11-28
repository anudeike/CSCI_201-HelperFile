#Example Question
"""

"""
num_in_base10 = int(input("Enter the number in base ten: "))
desired_base = int(input("Enter the base you want to convert to: "))

remainders = []
running = True
x = 0

while(num_in_base10 != 0):
  #calc the modulus
  remain = num_in_base10 % desired_base
  quotient = int(num_in_base10 / desired_base)
  remainders.append(remain)
  print(" ")
  print("Quotient " + str(len(remainders)) + " = " + str(quotient))
  print("Remainder " + str(len(remainders)) + " = " + str(remainders[x]))
  print(" ")
  num_in_base10 = quotient
  x += 1
  running = False