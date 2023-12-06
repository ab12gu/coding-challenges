class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        count = 0
        high = max(dist)
        n = len(dist)
    
        while(all(i > 0 for i in dist)):

            dist = [*map(lambda x, y: x - y, dist, speed)]
            index = dist.index(min(dist))

            dist[index] = high
            speed[index] = 0

            count += 1

            if count == n:
                return n

        return count

