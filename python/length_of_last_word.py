##
#
# filename: length_of_last_word.py
# by: Abhay Gupta
# date: 03-23-20
#
# Desc: find the length of the last word of a string
##


class Solution:
    def __init__(self):
        pass

    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        prev = 0
        for c in s:
            if c != ' ':
                count += 1
            else:
                if count != 0:
                    prev = count
                count = 0

        if count == 0:
            count = prev

        return count


if __name__ == '__main__':
    input_str = "Hello World"

    print(input_str)

    count = Solution().lengthOfLastWord(input_str)
    print(count)



