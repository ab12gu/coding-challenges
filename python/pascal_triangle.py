##
#
# filename: pascal_triangle.py
# by: Abhay Gupta
# date: 04-03-2020
#
# desc: given height of pascal's triangle, return pascal's triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        soln = []
        
        for i in range(1,numRows+1):
            soln.append([1]*i)
            
            for j in range(0, len(soln[i-2])-1):
                temp = soln[i-2][j] + soln[i-2][j+1]
                soln[i-1][j+1] = temp
            
        print(soln)
        
        return(soln)