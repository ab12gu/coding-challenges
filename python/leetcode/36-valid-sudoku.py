class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

      for i in range(9):
        for j in range(9):
          if not board[i][j].isdigit():
            board[i][j] = ""
          else:
            board[i][j] = int(board[i][j])

      for i in range(9):
        table = {i: 0 for i in range(1,10)}
        atable = {i: 0 for i in range(1,10)}
        for j in range(9):

          # check row
          current = board[i][j]
          if current:
            if table[current] > 0:
              return False
            table[current] += 1

          # check column
          current = board[j][i]
          if current:
            if atable[current] > 0:
              return False
            atable[current] += 1

      init = 0
      cube = []
      size = 3
      for i in range(size):
        cube.append([])
        for j in range(size):
          init = i*size+j
          cube[i].append(init)
      print(cube) 

      # check 3x3 square
      for i in cube:
        for j in cube:
          table = {i: 0 for i in range(1,10)}
          for p in i:
            for q in j:
              current = board[p][q]
              if current:
                if table[current] > 0:
                  return False
                table[current] += 1

      return True 

