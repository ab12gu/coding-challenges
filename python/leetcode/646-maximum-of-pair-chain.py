class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
      pairs = sorted(pairs, key=lambda pair: pair[1])

      chain_lengths = [1] * len(pairs)
      chain_end = [pairs[0]]

      # iterate through pairs
      for i in pairs[1:]:
       
        # find length of pair chains prior to current pair
        for c, j in enumerate(chain_end):
          if j[1] < i[0]:
            chain_lengths[c] += 1
            chain_end[c] = i
        
        # add new pair to prior pairs
        chain_end.append(i)
    
      # return longest chain  
      return max(chain_lengths)

  # alternative solutions

      size = len(pairs)
      chain_lengths = [1] * size

      for i in range(1,size):
        for j in range(i):
          if pairs[j][1] < pairs[i][0]:
            chain_lengths[j] += 1
            pairs[j] = pairs[i]

      return max(chain_lengths)

      #for c, i in enumerate(pairs[1:]):
      #  for d, j in enumerate(pairs[:c+1]):
      #    if j[1] < i[0]:
      #      chain_lengths[d] += 1
      #      pairs[d] = i



       
