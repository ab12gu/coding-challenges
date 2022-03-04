##
#
# filename: pascal_triangle2.py
# by: Abhay Gupta
# date: 04-03-2020
#
# desc: given row of pascal's triangle, return row (row index begins at 0)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        soln = []
        
        for i in range(1,rowIndex+2):
            soln.append([1]*i)
            
            for j in range(0, len(soln[i-2])-1):
                temp = soln[i-2][j] + soln[i-2][j+1]
                soln[i-1][j+1] = temp
            
        print(soln)
        
        return(soln[-1])