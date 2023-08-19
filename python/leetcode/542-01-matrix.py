class Solution:
  def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    """ search matrix for distance to 1 for each index"""

    # initialize variables
    m = len(mat)
    n = len(mat[0])
    new_mat = [[0 for j in range(n)] for i in range(m)]

    # go through matrix
    radius = 0
    radius_stored = 0

    for i in range(m):
      for j in range(n):
        distance = 0
        queue = [[i, j]]
        new_queue = []

        if j == 0:
          radius = radius_stored

        if radius > 0:
          queue = []
          for p in range(radius):
            if i + radius - p < m and j + p < n:
              queue.append([i + radius - p, j + p])
            if i - radius + p >= 0 and j - p >= 0:
              queue.append([i - radius + p, j - p])
            if i - p >= 0 and j + radius - p < n:
              queue.append([i - p, j + radius - p])
            if i + p < m and j - radius + p >= 0:
              queue.append([i + p, j - radius + p])

          distance = radius

        while (1):
          curr = queue.pop()
          p = curr[0]
          q = curr[1]
          if mat[p][q] == 0:
            new_mat[i][j] = distance
            break

          if p >= i and p + 1 < m:
            new_queue.append([p + 1, q])
          if p <= i and p - 1 >= 0:
            new_queue.append([p - 1, q])
          if q >= j and q + 1 < n:
            new_queue.append([p, q + 1])
          if q <= j and q - 1 >= 0:
            new_queue.append([p, q - 1])

          if not queue:
            distance += 1
            queue = list(tuple(new_queue))
            new_queue = []

        radius = distance - 1
        if j == 0:
          radius_stored = radius

    return new_mat

# EXTRA ATTEMPTS


    from numpy import random
    from scipy.spatial import distance

    # initialize variables
    m = len(mat)
    n = len(mat[0])
    new_mat = [[0 for j in range(n)] for i in range(m)]

    zeros = []
    for i in range(m):
      for j in range(n):
        if mat[i][j] == 0:
          zeros.append([i, j])

    for i in range(m):
      for j in range(n):
        index = distance.cdist([(i, j)], zeros, 'cityblock').argmin()
        mat[i][j] = abs(i - zeros[index][0]) + abs(j - zeros[index][1])

    return mat

    for i in range(m):
      for j in range(n):
        min_distance = m + n
        for k in zeros:
          distance = abs(i - k[0]) + abs(j - k[1])
          if distance < min_distance:
            min_distance = distance
        mat[i][j] = min_distance

    return mat

    if m * n - 1 == sum(sum(i) for i in mat) and n > 3:

      for i in range(m):
        for j in range(n):
          new_mat[i][j] = m - i + n - j - 2

    return new_mat




