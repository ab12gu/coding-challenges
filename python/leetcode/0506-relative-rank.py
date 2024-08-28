class Solution:
    def findRelativeRanks(self, score):
        arr = []
        for e, i in enumerate(score):
            arr.append([i, e])
        arr.sort()
        arr.reverse()

        output = []
        for e,i in enumerate(arr):
            print(e, i)
            if e == 0:
                score[i[1]] = "Gold Medal"
            elif e == 1:
                score[i[1]] = "Silver Medal"
            elif e == 2:
                score[i[1]] = "Bronze Medal"
            else:
                score[i[1]] = str(e+1)

        return scoree

if __name__ == "__main__":
    score = [5,4,3,2,1]
    myClass = Solution()
    print(myClass.findRelativeRanks(score))