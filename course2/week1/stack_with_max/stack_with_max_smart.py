#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__otherstack=[]
        self.__max=-1
    def Push(self, a):
        self.__stack.append(a)
        if self.__otherstack==[]:
            self.__otherstack.append(a)
        elif a>=self.__otherstack[-1]:
            self.__otherstack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        popval=self.__stack.pop()
        if self.__otherstack:
            if self.__otherstack[-1]==popval:
                self.__otherstack.pop()

    def Max(self):
        assert(len(self.__stack))
        if self.__otherstack:
            return self.__otherstack[-1]
        else:
            return self.__stack[-1]

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
