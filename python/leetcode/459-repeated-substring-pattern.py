# title: 459-repeated-substring-pattern.py
# by: Abhay Gupta
# date: 23-08-21
#
# desc: Given a string s, check if it can be constructed 
# by taking a substring of it and appending multiple 
# copies of the substring together.
#
# Leetcode || difficulty: Easy


class Solution:
  def repeatedSubstringPattern(self, s: str) -> bool:

    # super quick solution
    # the modulo was the trick bb


    total = len(s)

    if total == 1:
      return False

    for i in range(1,int(total/2+1)):
      if total % i == 0:
        if s[0:i] * int(total/i) == s:
          return True

    return False


######################
#####################

    # optimize 0

  total = len(s)

  if total == 1:
    return False

  for i in range(1,int((total+1)/2)+1):
    factor = total/i
    if factor.is_integer():
      repeat =  s[0:i] * int(factor)
      if repeat == s:
        return True

  return False


  # optimize 1

  total = len(s)
  factors = []

  if total == 1:
    return False

  for i in range(1,int((total+1)/2)+1):
    if (total/i).is_integer():
      factors.append(i)

  for i in factors:
    substring = s[0:i]
    repeat = []

    if (total/i).is_integer():
      for j in range(int(total/i)):
        repeat.append(substring)
      repeat = ''.join(repeat)

      if repeat == s:
        return True
  return False


  # iterate through string chronologically
  total = len(s)


  for i in range(1,total):
    substring = s[0:i]
    repeat = []

    if (total/i).is_integer():
      for j in range(int(total/i)):
        repeat.append(substring)
      repeat = ''.join(repeat)

      if repeat == s:
        return True
  return False


  # iterate through string chronologically
  total = len(s)

  for i in range(1,total):
    substring = s[0:i]
    repeat = ""
    if (total/i).is_integer():
      for j in range(int(total/i)):
        repeat += substring
    if repeat == s:
      return True
  return False


  # find factors of the length of string
  total = len(s)
  factors = []

  if total == 1:
    return False

  for i in range(1,int((total+1)/2)+1):
    if (total/i).is_integer():
      factors.append(i)

  for i in factors:
    substring = s[0:i]
    repeatsubstring = ""
    for i in range(int(total/i)):
      repeatsubstring += substring
    if repeatsubstring == s:
      return True
  return Fals



  ### Looked at all substrings within list rather than substring from start of string

  # find factors of the length of string
  total = len(s)
  factors = []

  # find factors of length of string
  for i in range(1, total+1):
    if (total/i).is_integer():
      factors.append(i)

  # loop through string & check if each substring is feasible
  for i in factors:
    for j in range(1,len(s)):
      clone = ""
      current = s[i:i+j] 
      if (len(s)/j).is_integer():
        for k in range(int(len(s)/j)):
          clone += current
        if clone == s:
          return True

  return False
                                            

