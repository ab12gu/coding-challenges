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

    def click(self, row, col):
        if row <= self.rows and col <= self.cols:
            i,j = row + 1, col
            print(self.rows,i)
            if i <= self.rows:
                if self.grid[i][j] == False:
                    self.grid[i][j] = 0
                    self.click(i,j)
                if self.grid[i][j] == True:
                    self.grid[i][j] = 1
                    self.click(i,j)

    def print(self):
        print(self.grid)
                    

if __name__ == '__main__':

    matrix = Matrix();
    matrix.resize(2, 3)
    matrix.click(0, 0)
    matrix.print()




