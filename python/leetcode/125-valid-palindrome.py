class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = []

        for i in s:
            if ord('a') <= ord(i) and ord(i) <= ord('z'):
                string.append(i)
        for i in range(int(len(string)/2)):
            if string[i] != string[-i-1]:
                return False

        return True

        string = ''.join([s for s in string if s.isalnum()])
        return string == string[::-1]

if __name__ == '__main__':

    string = "A man, a plan, a canal: Panama"

    new_class = Solution()
    boolean = new_class.isPalindrome(string)

    print(boolean)
