class Solution:
    def countBits(self, n: int) -> List[int]:

        arr = []
        exp = 0
        for i in range(n+1):
            if i == 2**(exp + 1):
                exp += 1

            curr = exp 
            count = 0
            while(1):
                if curr < 0:
                    break

                if i >= 2**curr:
                    i = i - 2**curr
                    count += 1
                
                curr = curr - 1
                
            arr.append(count)
            
        return arr
