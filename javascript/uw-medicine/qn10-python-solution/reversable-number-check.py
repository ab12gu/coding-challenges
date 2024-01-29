# 
# filename: reversable-number-check.py
# by: Abhay Gupta
# date created: 24-01-24
#
# desc: check if a number and it's reverse add to a number w/ all odd values


def is_reversible(n):
  """Checks if a number is reversible."""
  # Reverse the digits of n
  reversed_n = int(str(n)[::-1]) 
  sum_n_reversed = str(n + reversed_n)
  
  # Check if all digits are odd
  return all(int(digit) % 2 != 0 for digit in sum_n_reversed)  

reversible_numbers = []
# Check numbers between 1001 and 10001 (inclusive)
for n in range(1001, 10002):  
  if is_reversible(n):
    reversible_numbers.append(n)

print("Reversible numbers:", reversible_numbers)