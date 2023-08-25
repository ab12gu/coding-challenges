class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

      p1 = len(s1)
      p2 = len(s2)
      pointers = [(0, 0)]

      if len(s3) != p1 + p2:
        return False

      for i in s3:
        curr = []
        
        while(1):
          a, b = pointers.pop()

          if a < p1 and i == s1[a]:
            curr.append((a + 1, b))
          if b < p2 and i == s2[b]:
            curr.append((a, b + 1))

          if not pointers:
            break

        if not curr:
          return False
        pointers = list(set(curr))

      return True

