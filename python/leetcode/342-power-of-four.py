class Solution:
    def __init__(self):
        self.powers = set()
        self.curr = 0

    def isPowerOfFour(self, n: int) -> bool:
        
        if n in self.powers:
            return false

        curr = 0 
        while(curr < n):
            curr = 4 ** self.curr
            self.powers.add(curr)

            if curr == n:
                return 1

            self.curr += 1

