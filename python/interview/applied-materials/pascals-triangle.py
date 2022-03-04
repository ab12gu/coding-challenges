##
# filename: pascals-triangle.py
# by: Abhay Gupta
#
# desc: Given an integer numRows, return the first numRows of Pascal's triangle. 
#       Pascal's triangle: each number is the sum of the two numbers directly above
#       it as shown
##

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        temp = []
        pascal_list = []
        for i in range(0, numRows):
            print("hello")
            if i == 0:
                prev = [0, 0]
            else:
                prev = 0 + pascal_list[i-1] + 0

                for j in range(0, len(pascal_list)):
                    print(1)
                    #pascal_list.append(j)
                
        return pascal_list



if __name__ == "__main__":
    numRows = 1
    pascal_list = Solution.generate(None, numRows)
    print(pascal_list)