##
#
# filename: sqrt.py
# by: Abhay Gupta
# date: 03-23-20
#
# Desc: find the square root of a number
##


class Solution:
    def mySqrt(self, x: int) -> int:

        i = 1
        while i*i <= x:
            i += 1
        return i-1


if __name__ == '__main__':
    val = 8

    s = Solution().mySqrt(val)

    print(val, s)
