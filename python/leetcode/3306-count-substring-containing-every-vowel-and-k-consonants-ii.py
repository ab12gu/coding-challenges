class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        arr = []
        self.vowels = ["a", "e", "i", "o", "u"]
        self.total = 0
        self.constants = k

        for e, i in enumerate(word):
            self.substring(word[e:])

        return self.total

    def substring(self, word):
        vowels = self.vowels[:]
        constant = 0
        for i in word:                
            if i in self.vowels:
                if i in vowels:
                    vowels.pop(vowels.index(i))
            else:
                constant += 1
                if constant > self.constants:
                    return
            
            if not vowels:
                if constant == self.constants:
                    self.total += 1
