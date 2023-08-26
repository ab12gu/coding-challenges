class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
      pairs = sorted(pairs, key=lambda pair: pair[1])

      chain_lengths = [1] * len(pairs)
      chain_end = [pairs[0]]
      for i in pairs[1:]:
        

        for c, j in enumerate(chain_end):
          if j[1] < i[0]:
            chain_lengths[c] += 1
            chain_end[c] = i
        
        chain_end.append(i)

      return max(chain_lengths)


