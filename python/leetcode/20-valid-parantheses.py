class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {"{": 0, "[": 0, "(": 0}
        reverse = {"}": "{", "]": "[", ")": "("}

        for i in list(s):
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[reverse[i]] -= 1

        for i in dictionary:
            if dictionary[i]:
                return False

        return True
       
