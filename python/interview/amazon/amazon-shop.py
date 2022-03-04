# filename: amazon-shop.py
# by: abhay gupta
# date: 22-03-03
#
# desc: amazon demo qn: 
#       given two groups, determine if cart contains both groups in order

def recurse(cart, group):
  for item in cart:
    if item == group[0]:
      if len(group) == 1:
        return 1
      return recurse(cart[1:], group[1:])
  return 0

def isWinner(group1, group2, cart):
  group = group1 + group2
  
  print(group)
  return (recurse(cart, group))

if __name__ == "__main__":
  group1 = ["pear", "peach", "apple"]
  group2 = ["kiwi", "tangerine"]
  cart = ["pear", "peach", "orange", "apple","kiwi"]
  
  print(isWinner(group1, group2, cart))
  
  