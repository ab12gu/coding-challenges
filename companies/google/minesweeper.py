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

            row = [row, row, row+1, row-1]
            col = [col+1, col-1, col, col]

            for i,j in zip(row,col):
                #print("MAX", self.rows,self.cols)
                print("CURR", i, j)
                print(self.grid)
                if i >= 0 and i <= self.rows-1 and j >=0 and j <= self.cols-1:
                    print(len(self.grid))
                    print(len(self.grid[1]))
                    if self.grid[i][j] == False:
                        print("transform", i,j)
                        self.grid[i][j] = 1
                        self.click(i,j)
                    if self.grid[i][j] == True:
                        self.grid[i][j] = 2
                        self.click(i,j)
                    else:
                        return

    def print(self):
        print(self.grid)
                    

if __name__ == '__main__':

    matrix = Matrix();
    matrix.resize(2, 2)
    matrix.click(0, 0)
    matrix.print()




