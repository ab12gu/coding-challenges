#
# filename: 645-set-mismatch.py
#
# by: Abhay Gupta
# date created: 24-01-22
#
# desc: Find the number that occurs twice and the number that is missing and return them in the form of an array.




class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        j = None
        output = [None, None]
        nums.sort()
        for i in nums:
            if j == i:
                output[0] = j
            if j is None:
                if i == 2:
                    output[1] = 1
            elif i - j == 2:
                output[1] = i - 1
            j = i

        if output[1] == None:
            output[1] = i + 1
        return output

