class Solution:

    def uniquePaths(self, m: int, n: int) -> int:

        arr = [[1] * m for _ in range(n)]
        #arr = list(map(lambda x: [1] * m, range(n)))

        for i in range(n-1):
            for j in range(m-1):

                arr[i+1][j+1] = arr[i][j+1] + arr[i+1][j]

        return arr[n-1][m-1]
       
