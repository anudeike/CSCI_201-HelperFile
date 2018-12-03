import numpy as np

diameter = float(input("Diameter of the wafer: "))
cost_wafer = float(input("Cost of the wafer: "))
len_die = float(input("Length of the wafer: "))
width_die = float(input("Width of the wafer: "))
defect_rate = float(input("Enter the raw defect rate: "))
cost_of_pkg = float(input("Enter the cost of packaging and texting: "))
final_test_yield = float(input("Enter the final test yield: "))
target_profit_margin = float(input("Enter the profit margin target: "))

"""
Main Functions
"""

#get area of the wafer
def getWaferArea(radius):
  return 3.1415 * (radius**2)

#get the area of the die
def getDieArea(length, width):
  return length * width

def run():
  return 0

if __name__ == "__main__":
  wafer_area = getWaferArea(diameter/2)
  die_area = getDieArea(len_die, width_die)

  #get the die per wafer
  die_per_wafer = wafer_area / die_area

  #temp
  temp = die_per_wafer * final_test_yield

  cost_per_die = cost_wafer / temp

  x_var = cost_of_pkg + cost_per_die

  y_var = x_var / (final_test_yield/100)

  answer = y_var + y_var * (target_profit_margin/100)

  print(answer)