class Solution:

    def boarder_search(self, indices):
        indices = [indices]

        while(indices):
        
            i, j = indices.pop()
            
            if i - 1 >= 0:
                if self.grid[i-1][j] == "1":
                    indices.append((i-1,j))
                    self.grid[i-1][j] = "0"
            
            if i + 1 < self.row:
                if self.grid[i+1][j] == "1":
                    indices.append((i+1,j))
                    self.grid[i+1][j] = "0"
            
            if j - 1 >= 0:
                if self.grid[i][j-1] == "1":
                    indices.append((i,j-1))
                    self.grid[i][j-1] = "0"
            
            if j + 1 < self.coln:
                if self.grid[i][j+1] == "1":
                    indices.append((i,j+1))
                    self.grid[i][j+1] = "0"
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.row = len(grid)
        self.coln = len(grid[0])
        self.grid = grid
        
        number_of_islands = 0
        
        for i in range(self.row):
            for j in range(self.coln):
            
                # check if island
                if grid[i][j] == "1":
                    self.grid[i][j] = "0"
                    self.boarder_search((i,j))
                    number_of_islands += 1

        return number_of_islands
