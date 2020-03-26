##
#
# filename: climbing_stairs.py
# by: Abhay Gupta
# date: 03-23-20
#
# Desc: how many distinct ways can you climb n stairs, given you can take 1 or 2 steps at a time
##


def fibonacci(n: int) -> int:
    fibo = [0, 1]

    for i in range(2, n+1):
        new_elem = fibo[i-1] + fibo[i-2]
        fibo.append(new_elem)

    return fibo[n]


class Solution:

    def climbStairs(self, n: int) -> int:
        return fibonacci(n+1)


if __name__ == '__main__':
    stairs = 10

    combos = Solution().climbStairs(stairs)
    print(combos)


