#python3
import sys
class orderedList():
    def __init__(self):
        self.__data=[]
    def binarySearchExact(self,elem,left,right):
        #if left==right: return left
        if right-left<50:
            idx = left
            for val in self.__data[left:]:
                if val == elem:
                    return idx
                else: idx+=1


        mid = (left + right) // 2
        if elem ==self.__data[mid]:
            return mid
        if elem > self.__data[mid]:
            return self.binarySearchExact(elem,left,mid)
        else:
            return self.binarySearchExact(elem,mid,right)

    def binarySearch(self,elem,left,right):
        if right-left<500:
            idx = left
            for val in self.__data[left:]:
                if val < elem:
                    break
                else: idx+=1
            return idx
        mid = (left + right) // 2
        if elem ==self.__data[mid]:
            return mid
        if elem > self.__data[mid]:
            return self.binarySearch(elem,left,mid)
        else:
            return self.binarySearch(elem,mid,right)

    def add(self,val):
        insetLocation=self.binarySearch(val,0,len(self.__data))
        self.__data.insert(insetLocation,val)

    def pop(self,val):
        removeLocation=self.binarySearchExact(val,0,len(self.__data))
        del self.__data[removeLocation]

    def get_max(self):
        return self.__data[0]

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__orderedList=orderedList()

    def Push(self, a):
        self.__stack.append(a)
        self.__orderedList.add(a)

    def Pop(self):
        assert(len(self.__stack))
        popval=self.__stack.pop()
        self.__orderedList.pop(popval)

    def Max(self):
        assert(len(self.__stack))
        return self.__orderedList.get_max()


if __name__ == '__main__':
    stack = StackWithMax()
    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()
        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
