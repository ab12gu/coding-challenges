class OrderedStream:

    def __init__(self, n: int):
      self.n = n
      self.xlist = []
      self.point = 0

      for i in range(n):
        self.xlist.append([])
        
    def insert(self, idKey: int, value: str) -> List[str]:
      # self.xlist = xlist(self.point)
      curr = []
      
      self.xlist[idKey-1].append(value)

      while(1):
        if len(self.xlist) == self.point or self.xlist[self.point] == []:
          break
        else:
          curr = curr + self.xlist[self.point]
          self.point += 1

      return curr


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
