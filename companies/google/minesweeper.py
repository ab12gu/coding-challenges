# Minesweeper
#
# Correctly identify the location of all mines in a given grid
# 0 if empty, 9 if mine
# Adjencent spaces specify mines next to it

class Matrix:

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.grid = []

    def resize(self, rows, cols):

        # Alternate method
        #self.grid = [False] * rows
        #self.grid = [self.grid] * cols

        self.grid = [[False for i in range(rows)] for i in range(cols)]
        
        self.rows = rows
        self.cols = cols
        print(self.grid)

    def setmatrix(self, row, col):
        if len(grid) <= row and len(grid[0]) <= col:
            grid[row,col] = True
   

if __name__ == '__main__':

    matrix = Matrix();
    matrix.resize(2, 3)



