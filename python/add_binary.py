##
# 
# filename: add_binary.py
# by: Abhay Gupta
# date: 03-28-20
#
# desc: given two binary strings, return their sum

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            large = a
            small = b
        else:
            large = b
            small = a

        d = ""
        small = small.zfill(len(large))


        carry = 0
        soln = ""
        for c, i in enumerate(large):
            temp = carry + int(large[-(c+1)]) + int(small[-(c+1)])
            if temp == 2:
                soln = "0" + soln
                carry = 1
            elif temp == 3:
                soln = "1" + soln
                carry = 1
            else:
                soln = str(temp) + soln
                carry = 0
        
        if carry == 1:
            soln = str(carry) + soln

        return(soln)
   

if __name__ == '__main__':
    a = '11'
    b = '1'

    total = Solution().addBinary(a, b)

    print(total)