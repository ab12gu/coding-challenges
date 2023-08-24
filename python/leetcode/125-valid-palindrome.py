class Solution:
    def isPalindrome(self, s: str) -> bool:

      s = s.lower()

      new_string = ""
      left = ord('a'); right = ord('z')

      for i in s:
        if ord(i) >= left and ord(i) <= right:
          new_string += i
        elif i.isdigit():
          new_string += i

      for i in range(len(new_string) // 2):
        if new_string[i] != new_string[-(i + 1)]:
          return False
      
      return True
        

