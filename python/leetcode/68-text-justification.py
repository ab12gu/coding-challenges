lass Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
      
      output = []
      words_len = len(words)
      curr_width = len(words[0]) 
      curr_line = [words[0]]
      end = False

      if words_len == 1:
        return [words[0] + " " * (maxWidth - curr_width)]

      for c, i in enumerate(words[1:]):
        flag = True
        if (leftover := curr_width + len(i) + 1) <= maxWidth:
          curr_width = leftover
          curr_line.extend([" ", i])

          if c < words_len - 2:
            flag = False
          else:
            end = True

        if flag == True:

          if end == True:
            output.append(''.join(curr_line) + " " * (maxWidth - curr_width))
            return output

          if len(curr_line) > 1:
            spaces = (len(curr_line) - 1) // 2
            left_spaces = maxWidth - curr_width
            add_spaces = left_spaces // spaces 
            extra = left_spaces % spaces
  
            for j in range(1, len(curr_line), 2):
              curr_line[j] += " " * add_spaces
  
            for j in range(1, 2*extra, 2):
              curr_line[j] += " "
          else:
            curr_line += " " * (maxWidth - len(curr_line[-1]))

          output.append("".join(curr_line))
          curr_line = [i]
          curr_width = len(i)

          if c == words_len - 2:
            last = i + " " * (maxWidth - len(i))
            output.append(last)

      return output


