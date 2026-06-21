# Longest Word

class LongestWord:
    def __init__(self):
        pass

    def subsequence(self, S, D):
        subsequence = ""

        for i in D:
            reset_word = list(i[::-1])
            word = reset_word[:]
            print(word)
            letter = word.pop()
            length = len(word)
            count = 0
            for j in list(S):
                if letter == j:
                    count += 1
                    if count == length:
                        subsequence = i
                        break
                else:
                    count = 0
                    print("Base", reset_word)
                    word = reset_word[:]

                letter = word.pop()

        return subsequence


if __name__ == '__main__':

    S = 'helloworld'
    D = ['ello', 'world']

    longestword = LongestWord()
    subsequence = longestword.subsequence(S,D)
    print(subsequence)


