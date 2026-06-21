class Solution:
    def isValid(self, s: str) -> bool:

        #openset = set("{[(")
        reverse = {'{': "}", "[": "]", '(': ")"}
        d = []

        for i in list(s):
            if i in reverse:
                d.append(reverse[i])
            else:
                if not d:
                    return False
                if d.pop() != i:
                    return False

        if d:
            return False
        return True

