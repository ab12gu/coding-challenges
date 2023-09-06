class Solution:

    def boarder_search(self, indices):
        indices = [indices]

        while(indices):
        
            index = indices.pop()
            
            i = index[0]
            j = index[1]
            
            if i - 1 >= 0:
                if self.grid[i-1][j] == "1" and (i-1, j) not in self.land:
                    indices.append((i-1,j))
                    self.land.add((i-1,j))
            
            if i + 1 < self.row:
                if self.grid[i+1][j] == "1" and (i+1, j) not in self.land:
                    indices.append((i+1,j))
                    self.land.add((i+1,j))
            
            if j - 1 >= 0:
                if self.grid[i][j-1] == "1" and (i, j-1) not in self.land:
                    indices.append((i,j-1))
                    self.land.add((i,j-1))
            
            if j + 1 < self.coln:
                if self.grid[i][j+1] == "1" and (i, j+1) not in self.land:
                    indices.append((i,j+1))
                    self.land.add((i,j+1))
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.row = len(grid)
        self.coln = len(grid[0])
        self.grid = grid
        
        self.land = set()
        number_of_islands = 0
        
        for i in range(self.row):
            for j in range(self.coln):
            
                # check if island
                if grid[i][j] == "1":

                    if (i, j) not in self.land:
                        self.land.add((i,j))
                        self.boarder_search((i,j))
                        number_of_islands += 1

        return number_of_islands



