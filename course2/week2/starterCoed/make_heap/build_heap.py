# python3
import math
class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []
    self.n=0
    self.numLevels=0
  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    # n=6
    # self._data=[6,5,4,3,2,1]
    self.n=n-1
    self.numLevels=self.getHeight(n)
    assert n == len(self._data)

  def getHeight(self,idx):
    return math.ceil(math.log(idx+1,2))

  def swap(self,idx1,idx2):
    tmp=self._data[idx1]
    self._data[idx1]=self._data[idx2]
    self._data[idx2]=tmp
  def upsweep(self,idx):
      if idx==0:
          return
      if self._data[idx]<self._data[(idx-1) // 2]:
              self._swaps.append((idx,((idx-1) // 2)))
              self.swap(self._swaps[-1][0],self._swaps[-1][1])
  def downsweep(self,idx):
      if (self.n)<(idx*2+1):
         return
      smallestIdx=idx
      if self._data[smallestIdx] > self._data[2*idx+1]:
         smallestIdx=2*idx+1
      if self.n>idx*2+1:
         if self._data[smallestIdx] > self._data[2*idx+2]:
            smallestIdx=2*idx+2
      if smallestIdx!=idx:
          self.swap(idx,smallestIdx)
          self._swaps.append((idx,smallestIdx))
          self.downsweep(smallestIdx)
  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])
    # print(str(self._data))

  def GenerateSwaps(self):
    if self.n<2:
        return
    if self.n==(self.n//2)*2:
        lastElement=self.n
    else:
        lastElement=self.n-1
        self.upsweep(self.n)
    for idx in range(lastElement,0,-1):
        self.upsweep(idx)
        self.downsweep(idx)
    self.downsweep(0)
    # for idx in range(self.n,-1,-1):
    #     self.upsweep(idx)
    #     self.downsweep(idx)

  def outcomeCorrect(self):
      #print(str(self._data))
      assert(len(self._swaps)<=4*self.n)
      for idx in range(0,(self.n-1)//2):
           try:
               assert self._data[idx]<=self._data[2*idx+1]
               assert self._data[idx]<=self._data[2*idx+2]
           except:
               print(idx)
               break



  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    #self.outcomeCorrect()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
