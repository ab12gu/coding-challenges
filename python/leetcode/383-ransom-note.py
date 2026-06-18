class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashtable = {}
        for i in magazine:
            if i in hashtable:
                hashtable[i] += 1
            else:
                hashtable[i] = 1

        for i in ransomNote:
            if i in hashtable:
                if hashtable[i] > 0:
                    hashtable[i] -= 1
                else:
                    return False
            else:
                return False
        return True
