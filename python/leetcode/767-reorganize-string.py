class Solution:
    def reorganizeString(self, s: str) -> str:

      # find maximum  character count
      size = len(s)
      max_elem = (size + 1) // 2
      max_duplicates = list(range(1, max_elem+1))

      # there are 2 maximum if even
      if not size % 2:
        max_duplicates.append(max_elem)

      # add up the duplicates for each char
      duplicates = {}
      for i in s:
        duplicates[i] = duplicates.get(i, 0) + 1

      # check if duplicate characters are lower than maximums 
      repeats = []
      for i in duplicates:
        repeats.append([i, duplicates[i]])

      repeats.sort(key=lambda x: x[1])
      a, b = len(repeats), len(max_duplicates)

      for i in range(min(a,b)):
        if repeats[-(i+1)][1] > max_duplicates[-(i+1)]:
          return ""

      # find the output string with no adjacent duplicates
      # start with lowest duplicate
      output = []
      for char, freq in repeats:
        curr = []

        for d in range(freq):
          curr.append(char)

          if d != freq-1:
            if output:
              o_char = output.pop()
              if o_char:
                curr.append(o_char)
              else:
                curr.append(output.pop())
            else:
              curr.append("")

        # add leftover output      
        output = curr + output

      return "".join(output)
     
