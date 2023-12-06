class Solution:
    def numberOfMatches(self, n: int) -> int:
        output = 0

        while(n > 1):
            if n % 2 == 1:
                output += 1
                n -= 1
            n = n/2
            output += n
        
        return int(output)
