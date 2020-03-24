##
#
# filename: plus_one.py
# by: Abhay Gupta
# date: 03-23-20
#
# Desc: given an array of a integer, add one to array
##


import numpy as np
from typing import List
import math

class Solution:
    def __init__(self):
        pass

    def plusOne(self, digits: List[int]) -> List[int]:

        strings = [str(integer) for integer in digits]
        a_string = "".join(strings)
        an_integer = int(a_string)
        an_integer += 1
        print(an_integer)
        digits = []
        while an_integer > 0:
            temp = an_integer % 10
            digits.append(temp)
            an_integer = round((an_integer-temp)/10)

        digits.reverse()
        return digits






if __name__ == '__main__':

    input_arr = np.arange(4)
    print(input_arr)
    np.random.shuffle(input_arr)
    print(input_arr)
    input_arr = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]

    count = Solution().plusOne(input_arr)
    print(count)


