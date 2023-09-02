class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        index = []
        free = []
        dictionary = set(dictionary)
        right = len(s)

        min_char = len(s)
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):   
                if s[i:j] in dictionary:
                    for k in range(len(index)):
                        if i >= index[k]:

                            if min_char > free[k] + i - index[k]:
                                free.append(free[k] + i - index[k])
                                index.append(j)
    
                                curr = free[k] + i - index[k] + right - j
                                if min_char > curr:
                                    min_char = curr
    
                    if min_char > i:
                        index.append(j)
                        free.append(i)

                        curr = i + right - j
                        if min_char > curr:
                            min_char = curr

        return min_char

       
